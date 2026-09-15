/**
 * 萬能科技大學 - 創意行銷企劃實務 ✕ Agentic AI 互動教學平台
 * 授課教師：邱俊維 博士 ｜ 開課班級：進企管四系3甲 (F401 普通教室)
 */

// Firebase 雲端服務設定 (vnu-marketing-planning-11501)
const firebaseConfig = {
  apiKey: "AIzaSyDEHKEIs9Z5tlyw6kXB1909HtSLnicZQoQ",
  authDomain: "vnu-marketing-planning-11501.firebaseapp.com",
  projectId: "vnu-marketing-planning-11501",
  storageBucket: "vnu-marketing-planning-11501.firebasestorage.app",
  messagingSenderId: "167838302248",
  appId: "1:167838302248:web:8788ef9c778b4238cf351d",
  measurementId: "G-QY89CC9YTK"
};

let firebaseApp = null;
let firebaseAuth = null;
let firestoreDb = null;
let firebaseAnalytics = null;
let isFirebaseAvailable = false;
let currentFirebaseUser = null;
let isTeacherUser = false;

// 全域狀態管理
let curriculumData = null;
let questionsData = [];
let agentTemplates = [];
let isOfflineMode = false;
let systemInfo = {
  local_ip: '127.0.0.1',
  port: 5000,
  classroom_url: window.location.origin
};

// 使用者狀態
let currentUser = {
  studentId: localStorage.getItem('vnu_student_id') || '',
  studentName: localStorage.getItem('vnu_student_name') || '',
  email: '',
  photoURL: '',
  isGoogleAuth: false
};

// 錯題筆記本與解鎖徽章
let wrongQuestionsSet = new Set(JSON.parse(localStorage.getItem('vnu_wrong_questions') || '[]'));
let unlockedBadges = new Set(JSON.parse(localStorage.getItem('vnu_unlocked_badges') || '["badge_first_login"]'));

// 測驗狀態
let activeQuiz = {
  questions: [],
  currentIndex: 0,
  userAnswers: {}, // {qid: optIndex}
  timerSeconds: 0,
  timerInterval: null,
  examModeTitle: '隨堂練習'
};

// 大轉盤狀態 (個人隨機點名抽籤，可自訂座號或姓名)
let wheelNames = ['01 號', '02 號', '03 號', '04 號', '05 號', '06 號', '07 號', '08 號', '09 號', '10 號', '11 號', '12 號'];
let wheelAngle = 0;
let isSpinning = false;

// 課堂討論計時器狀態
let workshopTimer = {
  duration: 300,
  remaining: 300,
  interval: null,
  isRunning: false
};

// 初始化
document.addEventListener('DOMContentLoaded', async () => {
  // 0. 優先初始化 Firebase 雲端服務與 Google 驗證監聽
  try { initFirebase(); } catch(e) { console.warn('initFirebase error', e); }

  initUserModal();
  await loadSystemData();
  renderHeaderInfo();
  renderCurriculum();
  renderAgentTemplates();
  initClassroomTools();
  initQuizSystem();
  renderBadges();
  loadStudentWorks();
  loadVibeManual();
});

/* ==========================================================================
   0. Firebase 初始化與 Google 登入驗證
   ========================================================================== */
function initFirebase() {
  if (isFirebaseAvailable && firebaseAuth) return;
  if (typeof firebase !== 'undefined' && firebase.initializeApp) {
    try {
      if (!firebase.apps || !firebase.apps.length) {
        firebaseApp = firebase.initializeApp(firebaseConfig);
      } else {
        firebaseApp = firebase.app();
      }
      firebaseAuth = firebase.auth();
      firestoreDb = firebase.firestore();
      if (typeof firebase.analytics === 'function') {
        try { firebaseAnalytics = firebase.analytics(); } catch(e) {}
      }
      isFirebaseAvailable = true;
      console.log('✅ Firebase 初始化成功 (專案: vnu-marketing-planning-11501)');

      // 監聽 Redirect 登入結果
      if (firebaseAuth.getRedirectResult) {
        firebaseAuth.getRedirectResult().then((result) => {
          if (result && result.user) {
            console.log('Google 重定向登入成功:', result.user.email);
          }
        }).catch((err) => {
          console.warn('Redirect sign-in notice:', err);
        });
      }

      // 監聽 Auth 狀態
      firebaseAuth.onAuthStateChanged(async (user) => {
        currentFirebaseUser = user;
        if (user) {
          console.log('👤 Google 使用者已登入:', user.email, user.uid);
          
          // 判定授課教師身分 (邱俊維 博士)
          const userEmail = (user.email || (user.providerData && user.providerData[0] && user.providerData[0].email) || '').toLowerCase().trim();
          const teacherEmails = ['kevin87332000', 'kevin87332000@gmail.com', 'jimchiu', 'jimchiu@mail.vnu.edu.tw', 'vnuemba@gmail.com', 'h12s12bs', 'h12s12bs@gmail.com'];
          isTeacherUser = teacherEmails.some(em => userEmail.includes(em.toLowerCase()));
          console.log('👑 教師身分判定結果:', isTeacherUser ? '是授課教師 (邱俊維 博士)' : '一般學生/訪客');
          
          await loadUserProfileFromFirestore(user);
          renderHeaderInfo();
          listenToFirestoreWorks();
        } else {
          console.log('👤 使用者已登出 (訪客模式)');
          isTeacherUser = false;
          currentUser.isGoogleAuth = false;
          renderHeaderInfo();
        }
      });
    } catch (e) {
      console.warn('⚠️ Firebase 初始化警告:', e);
      isFirebaseAvailable = false;
    }
  } else {
    console.log('離線或未載入 Firebase SDK，使用本機 localStorage 模式');
  }
}

// 立即嘗試一次初始化
try { initFirebase(); } catch(e) {}

function loginWithGoogle() {
  console.log('🔘 Google 登入按鈕被點擊');
  if (!isFirebaseAvailable || !firebaseAuth) {
    if (typeof firebase !== 'undefined' && firebase.initializeApp) {
      initFirebase();
    }
  }

  if (!isFirebaseAvailable || !firebaseAuth) {
    alert('Firebase 雲端驗證服務載入中或處於離線狀態，系統已為您直接開啟學籍登記視窗！');
    openProfileModal(false);
    return;
  }

  try {
    const provider = new firebase.auth.GoogleAuthProvider();
    provider.setCustomParameters({ prompt: 'select_account' });
    firebaseAuth.signInWithPopup(provider).then((result) => {
      console.log('Google 登入成功:', result.user.email);
    }).catch((error) => {
      console.error('Google 登入失敗:', error);
      if (error.code === 'auth/popup-closed-by-user') return;
      if (error.code === 'auth/popup-blocked') {
        const tryRedirect = confirm('⚠️ 您的瀏覽器封鎖了 Google 登入彈跳視窗！\n\n是否改用直接頁面跳轉 (Redirect) 方式進行 Google 登入？');
        if (tryRedirect) {
          firebaseAuth.signInWithRedirect(provider);
        }
        return;
      }
      if (error.code === 'auth/unauthorized-domain') {
        alert(`⚠️ Firebase 網域尚未授權提示：\n\n目前網站網域為：【${window.location.hostname}】\n\n請至 Firebase Console (專案：vnu-marketing-planning-11501)\n-> Authentication\n-> Settings (設定)\n-> Authorized domains (已授權的網域)\n將【${window.location.hostname}】加入授權網域清單即可順利登入！`);
        return;
      }
      alert('Google 登入提示：' + (error.message || error));
    });
  } catch (err) {
    console.error('啟動登入程序錯誤:', err);
    alert('啟動登入視窗失敗：' + err.message);
  }
}

function logoutUser() {
  if (firebaseAuth) {
    firebaseAuth.signOut().then(() => {
      alert('您已安全登出 Google 帳號。');
    });
  } else {
    alert('已清除登入狀態。');
  }
}

async function loadUserProfileFromFirestore(user) {
  if (!firestoreDb) return;
  try {
    if (isTeacherUser) {
      currentUser.studentId = 'TEACHER';
      currentUser.studentName = '邱俊維 博士';
      currentUser.email = user.email || '';
      currentUser.photoURL = user.photoURL || '';
      currentUser.isGoogleAuth = true;
      localStorage.setItem('vnu_student_id', 'TEACHER');
      localStorage.setItem('vnu_student_name', '邱俊維 博士');
      
      try {
        firestoreDb.collection('users').doc(user.uid).set({
          uid: user.uid,
          email: user.email || '',
          studentId: 'TEACHER',
          studentName: '邱俊維 博士',
          className: '進企管四系3甲 (授課教師)',
          role: 'teacher',
          photoURL: user.photoURL || '',
          updatedAt: firebase.firestore.FieldValue.serverTimestamp()
        }, { merge: true }).catch(() => {});
      } catch(e) {}
      return;
    }

    const doc = await firestoreDb.collection('users').doc(user.uid).get();
    if (doc.exists) {
      const data = doc.data();
      currentUser.studentId = data.studentId || '';
      currentUser.studentName = data.studentName || user.displayName || '';
      currentUser.email = user.email || '';
      currentUser.photoURL = user.photoURL || '';
      currentUser.isGoogleAuth = true;

      // 若學號或姓名未完整填寫，彈窗提醒補填
      if (!currentUser.studentId || !currentUser.studentName) {
        initUserModal();
        openProfileModal(true);
      } else {
        localStorage.setItem('vnu_student_id', currentUser.studentId);
        localStorage.setItem('vnu_student_name', currentUser.studentName);
      }
    } else {
      // 首次學生登入 -> 彈窗登記學號與姓名
      currentUser.studentId = '';
      currentUser.studentName = user.displayName || '';
      currentUser.email = user.email || '';
      currentUser.photoURL = user.photoURL || '';
      currentUser.isGoogleAuth = true;
      initUserModal();
      openProfileModal(true);
    }
  } catch (e) {
    console.warn('載入 Firestore 使用者學籍失敗:', e);
  }
}

let unsubscribeFirestoreWorks = null;
function listenToFirestoreWorks() {
  if (!firestoreDb) return;
  if (unsubscribeFirestoreWorks) unsubscribeFirestoreWorks();

  try {
    unsubscribeFirestoreWorks = firestoreDb.collection('works')
      .onSnapshot((snapshot) => {
        const firestoreWorks = [];
        snapshot.forEach(doc => {
          firestoreWorks.push(doc.data());
        });
        if (firestoreWorks.length > 0) {
          // 依提交時間由新到舊排序
          firestoreWorks.sort((a, b) => (b.submitted_at || '').localeCompare(a.submitted_at || ''));
          
          const existingIds = new Set(firestoreWorks.map(w => w.id));
          const nonDuplicateSamples = (window.OFFLINE_SAMPLE_WORKS || []).filter(w => !existingIds.has(w.id));
          allStudentWorks = [...firestoreWorks, ...nonDuplicateSamples];
        } else {
          allStudentWorks = window.OFFLINE_SAMPLE_WORKS || [];
        }
        filteredStudentWorks = [...allStudentWorks];
        renderStudentWorksGallery(filteredStudentWorks);
      }, (err) => {
        console.warn('Firestore works listener notice:', err);
      });
  } catch (e) {
    console.warn('建立 Firestore 作品即時監聽失敗:', e);
  }
}

function openProfileModal(isForced = false) {
  initUserModal();
  const modalEl = document.getElementById('userProfileModal');
  if (modalEl) {
    const forceNotice = document.getElementById('force-profile-notice');
    if (forceNotice) forceNotice.style.display = isForced ? 'block' : 'none';
    if (window.bootstrap) {
      const modal = bootstrap.Modal.getOrCreateInstance(modalEl);
      modal.show();
    }
  }
}

async function exportGradesToCSV() {
  if (!isTeacherUser) {
    alert('此功能僅限授課教師使用！');
    return;
  }
  
  let worksList = [];
  if (firestoreDb) {
    try {
      const snap = await firestoreDb.collection('works').get();
      snap.forEach(doc => worksList.push(doc.data()));
    } catch (e) {
      console.warn('Export Firestore error:', e);
    }
  }
  if (worksList.length === 0) {
    worksList = allStudentWorks || [];
  }
  
  // Build CSV
  const headers = ['學號', '姓名', '班級', '專案模式', '專案名稱', '成果類型', '週次', '協同特工', 'GitHub Pages 成果網址', 'GitHub Repo 網址', '繳交時間'];
  const rows = worksList.map(w => [
    `"${w.student_id || ''}"`,
    `"${w.student_name || w.author || ''}"`,
    `"進企管四系3甲"`,
    `"個人獨立企劃"`,
    `"${(w.title || '').replace(/"/g, '""')}"`,
    `"${w.category || ''}"`,
    `"${w.week || ''}"`,
    `"${w.agent_used || ''}"`,
    `"${w.github_page_url || w.live_url || ''}"`,
    `"${w.github_repo_url || ''}"`,
    `"${w.submitted_at || ''}"`
  ]);
  
  const csvContent = '\uFEFF' + [headers.join(','), ...rows.map(r => r.join(','))].join('\n');
  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `創意行銷企劃實務_全班個人企劃作品名冊_${new Date().toISOString().slice(0,10)}.csv`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

/* ==========================================================================
   1. 資料載入與離線容錯機制
   ========================================================================== */
async function loadSystemData() {
  try {
    const res = await fetch('/api/system_info');
    if (res.ok) {
      systemInfo = await res.json();
    }
  } catch (e) {
    console.warn('Backend API unavailable, using offline defaults.');
    isOfflineMode = true;
  }

  // 1. 課綱資料
  try {
    const res = await fetch('/api/curriculum');
    if (res.ok) curriculumData = await res.json();
  } catch (e) {
    curriculumData = window.OFFLINE_CURRICULUM || null;
  }
  if (!curriculumData && window.OFFLINE_CURRICULUM) {
    curriculumData = window.OFFLINE_CURRICULUM;
  }

  // 2. 題庫資料
  try {
    const res = await fetch('/api/questions?count=200&shuffle=false');
    if (res.ok) {
      const data = await res.json();
      questionsData = data.questions || [];
    }
  } catch (e) {
    questionsData = window.OFFLINE_QUESTIONS || [];
  }
  if ((!questionsData || questionsData.length === 0) && window.OFFLINE_QUESTIONS) {
    questionsData = window.OFFLINE_QUESTIONS;
  }

  // 3. Agent 範本
  try {
    const res = await fetch('/api/agent_templates');
    if (res.ok) agentTemplates = await res.json();
  } catch (e) {
    agentTemplates = window.OFFLINE_TEMPLATES || [];
  }
  if ((!agentTemplates || agentTemplates.length === 0) && window.OFFLINE_TEMPLATES) {
    agentTemplates = window.OFFLINE_TEMPLATES;
  }
}

function renderHeaderInfo() {
  const btnGoogleLogin = document.getElementById('btn-google-login');
  const userAuthBox = document.getElementById('user-auth-box');
  const studentBadge = document.getElementById('student-info-badge');
  const userAvatarImg = document.getElementById('user-avatar-img');
  const userAvatarIcon = document.getElementById('user-avatar-icon');
  const dropdownEmail = document.getElementById('dropdown-user-email');
  const teacherMenuItem = document.getElementById('teacher-export-menu-item');

  if (currentFirebaseUser) {
    const userEmail = (currentFirebaseUser.email || (currentFirebaseUser.providerData && currentFirebaseUser.providerData[0] && currentFirebaseUser.providerData[0].email) || '').toLowerCase().trim();
    const teacherEmails = ['kevin87332000', 'kevin87332000@gmail.com', 'jimchiu', 'jimchiu@mail.vnu.edu.tw', 'vnuemba@gmail.com', 'h12s12bs', 'h12s12bs@gmail.com'];
    if (teacherEmails.some(em => userEmail.includes(em.toLowerCase()))) {
      isTeacherUser = true;
      currentUser.studentName = '邱俊維 博士';
      currentUser.studentId = 'TEACHER';
    }

    if (btnGoogleLogin) {
      btnGoogleLogin.classList.add('d-none');
      btnGoogleLogin.style.setProperty('display', 'none', 'important');
    }
    if (userAuthBox) {
      userAuthBox.classList.remove('d-none');
      userAuthBox.style.setProperty('display', 'block', 'important');
    }

    if (currentFirebaseUser.photoURL && userAvatarImg) {
      userAvatarImg.src = currentFirebaseUser.photoURL;
      userAvatarImg.style.display = 'inline-block';
      if (userAvatarIcon) userAvatarIcon.style.display = 'none';
    } else {
      if (userAvatarImg) userAvatarImg.style.display = 'none';
      if (userAvatarIcon) userAvatarIcon.style.display = 'inline-block';
    }

    if (dropdownEmail) {
      dropdownEmail.textContent = isTeacherUser ? `👑 授課教師 (${currentFirebaseUser.email})` : currentFirebaseUser.email;
    }

    if (studentBadge) {
      if (isTeacherUser) {
        studentBadge.innerHTML = `<span class="badge bg-warning text-dark me-1">教師</span>邱俊維 博士`;
      } else {
        studentBadge.textContent = currentUser.studentId 
          ? `進企管四系3甲 ${currentUser.studentName}` 
          : `${currentUser.studentName || '同學 (請登記學號)'}`;
      }
    }

    if (teacherMenuItem) teacherMenuItem.style.display = isTeacherUser ? 'block' : 'none';
  } else {
    if (btnGoogleLogin) {
      btnGoogleLogin.classList.remove('d-none');
      btnGoogleLogin.style.setProperty('display', 'inline-flex', 'important');
    }
    if (userAuthBox) {
      userAuthBox.classList.add('d-none');
      userAuthBox.style.setProperty('display', 'none', 'important');
    }
    if (studentBadge) {
      studentBadge.textContent = currentUser.studentId 
        ? `${currentUser.studentName} (${currentUser.studentId})` 
        : '學號登記';
    }
    if (teacherMenuItem) teacherMenuItem.style.display = 'none';
  }
}

/* ==========================================================================
   2. 使用者學號與成就管理
   ========================================================================== */
function initUserModal() {
  const inputId = document.getElementById('input-student-id');
  const inputName = document.getElementById('input-student-name');
  if (inputId) inputId.value = currentUser.studentId || '';
  if (inputName) inputName.value = currentUser.studentName || '';

  const googleBox = document.getElementById('google-account-info-box');
  const googleEmail = document.getElementById('input-google-email');
  if (googleBox && googleEmail) {
    if (currentFirebaseUser && currentFirebaseUser.email) {
      googleBox.style.display = 'block';
      googleEmail.value = currentFirebaseUser.email;
    } else {
      googleBox.style.display = 'none';
    }
  }
}

function saveUserProfile() {
  const inputId = (document.getElementById('input-student-id')?.value || '').trim();
  const inputName = (document.getElementById('input-student-name')?.value || '').trim();
  if (!inputId || !inputName) {
    alert('請輸入學號與姓名以完成學籍綁定！');
    return;
  }
  currentUser.studentId = inputId;
  currentUser.studentName = inputName;
  localStorage.setItem('vnu_student_id', inputId);
  localStorage.setItem('vnu_student_name', inputName);

  // 若已登入 Google，同步至 Firestore
  if (currentFirebaseUser && firestoreDb) {
    try {
      firestoreDb.collection('users').doc(currentFirebaseUser.uid).set({
        uid: currentFirebaseUser.uid,
        email: currentFirebaseUser.email || '',
        studentId: inputId,
        studentName: inputName,
        className: '進企管四系3甲',
        projectMode: '個人實務獨立企劃',
        photoURL: currentFirebaseUser.photoURL || '',
        updatedAt: firebase.firestore.FieldValue.serverTimestamp()
      }, { merge: true }).then(() => {
        console.log('✅ 學籍資料已同步至 Firebase Firestore');
      }).catch(err => console.warn('Firestore sync user error:', err));
    } catch (e) {
      console.warn('Sync profile to Firestore failed:', e);
    }
  }

  renderHeaderInfo();
  unlockBadge('badge_profile_set');
  alert(`歡迎【進企管四系3甲】${currentUser.studentName} 同學！個人學習歷程已成功綁定。`);
  const modalEl = document.getElementById('userProfileModal');
  if (modalEl && window.bootstrap) {
    const modal = bootstrap.Modal.getInstance(modalEl);
    if (modal) modal.hide();
  }
}

function unlockBadge(badgeId) {
  if (!unlockedBadges.has(badgeId)) {
    unlockedBadges.add(badgeId);
    localStorage.setItem('vnu_unlocked_badges', JSON.stringify([...unlockedBadges]));
    renderBadges();
  }
}

function renderBadges() {
  const container = document.getElementById('badges-container');
  if (!container) return;

  const allBadges = [
    { id: 'badge_first_login', name: '破冰啟航', icon: 'fa-compass', desc: '首次登入創意行銷企劃平台' },
    { id: 'badge_profile_set', name: '正式名冊', icon: 'fa-id-card', desc: '完成進修部個人學號與姓名登記' },
    { id: 'badge_idea_deck', name: '靈感捕手', icon: 'fa-lightbulb', desc: '課堂操作靈感抽卡機完成創意發想' },
    { id: 'badge_agent_react', name: 'AI 指揮官', icon: 'fa-robot', desc: '完成一次 Agentic AI 思考推理模擬' },
    { id: 'badge_weekly_quiz', name: '隨堂精兵', icon: 'fa-check-double', desc: '完成一次手機隨堂 5 題觀念快測' },
    { id: 'badge_score_90', name: '企劃大師', icon: 'fa-award', desc: '在 IPAS 模擬檢定測驗中取得 90 分以上高分' },
    { id: 'badge_proposal_draft', name: '提案先鋒', icon: 'fa-file-signature', desc: '一鍵產出完整一頁式行銷企劃草案' },
    { id: 'badge_wrong_review', name: '精益求精', icon: 'fa-book-open', desc: '複習並清空個人錯題筆記本' }
  ];

  container.innerHTML = allBadges.map(b => {
    const isUnlocked = unlockedBadges.has(b.id);
    return `
      <div class="col-6 col-md-3 mb-3">
        <div class="badge-card ${isUnlocked ? 'unlocked' : ''}">
          <i class="fas ${b.icon} badge-icon"></i>
          <h6 class="fw-bold mb-1">${b.name}</h6>
          <p class="small text-muted mb-0">${b.desc}</p>
          <span class="badge ${isUnlocked ? 'bg-warning text-dark' : 'bg-light text-secondary'} mt-2">
            ${isUnlocked ? '已解鎖' : '未解鎖'}
          </span>
        </div>
      </div>
    `;
  }).join('');
}

/* ==========================================================================
   第一週破冰與 18 週教學地圖
   ========================================================================== */
function renderCurriculum(filterPhase = 'all') {
  if (!curriculumData) return;

  // 1. 渲染第一週教師資訊與評分標準
  const info = curriculumData.course_info;
  const teacherEl = document.getElementById('teacher-profile-box');
  if (teacherEl && info) {
    teacherEl.innerHTML = `
      <div class="d-flex align-items-center mb-3">
        <div class="teacher-avatar-box me-3">
          <i class="fas fa-chalkboard-teacher"></i>
        </div>
        <div>
          <h4 class="fw-bold mb-0 text-dark">${info.instructor.name}</h4>
          <p class="text-primary fw-semibold mb-1">${info.instructor.title}</p>
          <div class="d-flex flex-wrap gap-2">
            <span class="info-badge"><i class="fas fa-envelope me-1"></i>${info.instructor.email}</span>
            <span class="info-badge"><i class="fas fa-clock me-1"></i>Office Hour: ${info.instructor.office_hours}</span>
            <span class="info-badge bg-light text-dark border"><i class="fas fa-book-open text-primary me-1"></i><strong>參考用書：</strong>${info.reference_book || '曾光華《行銷企劃：邏輯、創意、執行力》(2026 第五版)'}</span>
          </div>
        </div>
      </div>
      <p class="text-secondary small mb-2"><i class="fas fa-quote-left text-muted me-1"></i>${info.instructor.philosophy}</p>
      <div class="alert alert-light border small mb-0 py-2">
        <strong><i class="fas fa-bullhorn text-warning me-1"></i>給進修部同學的一句話：</strong>
        ${info.instructor.welcome_message}
      </div>
    `;
  }

  // 評分標準卡片 (極簡計算：期中考 30% ✕ 期末考 30% ✕ 平時出席 40%)
  const gradingEl = document.getElementById('grading-policy-box');
  if (gradingEl && info && info.grading_policy) {
    const gp = info.grading_policy;
    const midterm = gp.midterm_exam || gp.midterm_assessment || { title: '期中考試 (30%)', percentage: 30, description: '第 9 週筆試/實務測驗，檢定前半學期觀念與企劃邏輯。' };
    const finalEx = gp.final_exam || gp.final_project || { title: '期末考試 (30%)', percentage: 30, description: '第 18 週筆試/實務測驗，綜合檢驗全學期企劃整合能力。' };
    const attendance = gp.attendance || gp.learning_attitude || { title: '平時出席 (40%)', percentage: 40, description: '每週課堂出勤與常態點名紀錄，到課即有分，計分客觀透明。' };

    gradingEl.innerHTML = `
      <div class="row g-3 mb-3">
        <div class="col-md-4">
          <div class="grading-card h-100 p-3 rounded bg-white border-start border-4 shadow-sm" style="border-left-color: #F59E0B !important;">
            <div class="d-flex justify-content-between align-items-center mb-2">
              <h6 class="fw-bold mb-0 text-dark"><i class="fas fa-file-signature text-warning me-2"></i>${midterm.title}</h6>
              <span class="percentage-badge" style="color: #D97706; background: #FEF3C7; font-weight: 700; padding: 4px 10px; border-radius: 20px;">${midterm.percentage}%</span>
            </div>
            <p class="small text-muted mb-2">${midterm.description}</p>
            <div class="small text-secondary bg-light p-2 rounded">
              <i class="fas fa-check-circle text-warning me-1"></i><strong>評分形式</strong>：第 9 週筆試 / 實務測驗題型
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="grading-card h-100 p-3 rounded bg-white border-start border-4 shadow-sm" style="border-left-color: #2563EB !important;">
            <div class="d-flex justify-content-between align-items-center mb-2">
              <h6 class="fw-bold mb-0 text-dark"><i class="fas fa-graduation-cap text-primary me-2"></i>${finalEx.title}</h6>
              <span class="percentage-badge" style="color: #2563EB; background: #EFF6FF; font-weight: 700; padding: 4px 10px; border-radius: 20px;">${finalEx.percentage}%</span>
            </div>
            <p class="small text-muted mb-2">${finalEx.description}</p>
            <div class="small text-secondary bg-light p-2 rounded">
              <i class="fas fa-check-circle text-primary me-1"></i><strong>評分形式</strong>：第 18 週筆試 / 企劃實務整合測驗
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="grading-card h-100 p-3 rounded bg-white border-start border-4 shadow-sm" style="border-left-color: #10B981 !important;">
            <div class="d-flex justify-content-between align-items-center mb-2">
              <h6 class="fw-bold mb-0 text-dark"><i class="fas fa-user-check text-success me-2"></i>${attendance.title}</h6>
              <span class="percentage-badge" style="color: #059669; background: #ECFDF5; font-weight: 700; padding: 4px 10px; border-radius: 20px;">${attendance.percentage}%</span>
            </div>
            <p class="small text-muted mb-2">${attendance.description}</p>
            <div class="small text-secondary bg-light p-2 rounded">
              <i class="fas fa-check-circle text-success me-1"></i><strong>評分形式</strong>：每週課堂常態點名與到課記錄
            </div>
          </div>
        </div>
      </div>
      <div class="alert alert-light border d-flex align-items-center justify-content-between py-2 px-3 mb-0 rounded-3">
        <div class="small text-secondary">
          <i class="fas fa-calculator text-primary me-2"></i><strong>學期總成績計算公式</strong>：<code>總成績 ＝ (期中考 × 30%) ＋ (期末考 × 30%) ＋ (平時出席 × 40%)</code>
        </div>
        <span class="badge bg-success text-white">通過及格標準：60 分</span>
      </div>
    `;
  }

  // 2. 渲染 18 週清單
  const weeksContainer = document.getElementById('curriculum-weeks-list');
  if (!weeksContainer) return;

  let weeks = curriculumData.weeks || [];
  if (filterPhase === 'phase1') {
    weeks = weeks.filter(w => w.week <= 6);
  } else if (filterPhase === 'phase2') {
    weeks = weeks.filter(w => w.week >= 7 && w.week <= 12);
  } else if (filterPhase === 'phase3') {
    weeks = weeks.filter(w => w.week >= 13);
  }

  weeksContainer.innerHTML = weeks.map(w => `
    <div class="week-card p-3">
      <div class="d-flex flex-wrap align-items-center justify-content-between mb-2">
        <div class="d-flex align-items-center gap-2 mb-1 mb-md-0">
          <span class="week-badge">第 ${w.week} 週</span>
          <h5 class="fw-bold mb-0 text-dark">${w.title}</h5>
        </div>
        <div class="d-flex flex-wrap gap-1">
          <span class="tag-textbook"><i class="fas fa-book me-1"></i>${w.textbook_ref}</span>
          <span class="tag-martech"><i class="fas fa-microchip me-1"></i>${w.martech_domain}</span>
        </div>
      </div>

      <div class="alert alert-light border py-2 px-3 my-2 small">
        <strong class="text-danger"><i class="fas fa-fire me-1"></i>課堂破冰思辨：</strong>${w.break_ice}
      </div>

      <div class="row g-2 small my-1">
        <div class="col-md-6">
          <div class="p-2 bg-light rounded border h-100">
            <span class="fw-bold text-primary"><i class="fas fa-user-check me-1"></i>課堂實務演練活動：</span>
            <p class="mb-0 text-secondary">${w.classroom_activity}</p>
          </div>
        </div>
        <div class="col-md-6">
          <div class="p-2 bg-light rounded border h-100">
            <span class="fw-bold text-success"><i class="fas fa-house-laptop me-1"></i>課後延伸實作任務 (AI 協同)：</span>
            <p class="mb-0 text-secondary">${w.homework_task}</p>
          </div>
        </div>
      </div>

      <div class="d-flex flex-wrap justify-content-between align-items-center mt-2 pt-2 border-top">
        <div class="small text-muted">
          <i class="fas fa-tags me-1"></i>重點觀念：${w.key_concepts.join(' ｜ ')}
        </div>
        <button class="btn btn-sm btn-outline-primary mt-1 mt-md-0" onclick="startWeeklyQuickQuiz(${w.week})">
          <i class="fas fa-mobile-screen me-1"></i>本週 5 題快測
        </button>
      </div>
    </div>
  `).join('');
}

function filterCurriculum(phase, btn) {
  document.querySelectorAll('.filter-curriculum-btn').forEach(b => b.classList.remove('active', 'btn-primary'));
  document.querySelectorAll('.filter-curriculum-btn').forEach(b => b.classList.add('btn-outline-primary'));
  btn.classList.add('active', 'btn-primary');
  btn.classList.remove('btn-outline-primary');
  renderCurriculum(phase);
}

/* ==========================================================================
   課堂即時互動工具箱
   ========================================================================== */
function initClassroomTools() {
  // 1. 初始化大轉盤
  drawWheel();

  // 2. 初始化靈感抽卡機預設值
  refreshIdeaCards();
}

// 靈感抽卡機
async function refreshIdeaCards() {
  try {
    const res = await fetch('/api/random_cards');
    if (res.ok) {
      const card = await res.json();
      document.getElementById('card-target-text').textContent = card.target;
      document.getElementById('card-pain-text').textContent = card.pain;
      document.getElementById('card-tech-text').textContent = card.tech;
      document.getElementById('card-scene-text').textContent = card.scene;
      unlockBadge('badge_idea_deck');
      return;
    }
  } catch (e) {}

  // 離線備援資料庫
  const offlineCards = [
    { t: '白天上班、晚上讀企管進修部的大三同學', p: '下班趕著上課常常沒時間吃晚餐，希望有健康快速飽足點心', tech: 'LINE 預約點餐 ✕ 到教室 1 分鐘自取櫃', s: '週一傍晚 16:15 課堂鐘響前 10 分鐘' },
    { t: '追求體態但每天開會精神崩潰的粉領族', p: '下午 3 點極度想吃甜食犒賞自己，但怕糖分超標脂肪囤積', tech: 'AI 體態測驗推薦減糖 40% 燕麥生乳捲', s: '週三小週末辦公室厭世午茶時光' },
    { t: '重視天然無添加的雙薪家庭新手媽媽', p: '市售伴手禮添加物太多，送長輩或小孩吃都不放心', tech: '包裝數位產地透明溯源履歷 ✕ 零方數據問卷', s: '中秋與春節返鄉送禮關鍵時刻' }
  ];
  const item = offlineCards[Math.floor(Math.random() * offlineCards.length)];
  document.getElementById('card-target-text').textContent = item.t;
  document.getElementById('card-pain-text').textContent = item.p;
  document.getElementById('card-tech-text').textContent = item.tech;
  document.getElementById('card-scene-text').textContent = item.s;
  unlockBadge('badge_idea_deck');
}

// 創意大轉盤
function drawWheel() {
  const canvas = document.getElementById('wheel-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const numSegments = wheelNames.length;
  const anglePerSegment = (2 * Math.PI) / numSegments;
  const colors = ['#FF5E3A', '#3B82F6', '#10B981', '#F59E0B', '#8B5CF6', '#EC4899', '#06B6D4', '#64748B'];

  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const centerX = canvas.width / 2;
  const centerY = canvas.height / 2;
  const radius = centerX - 10;

  for (let i = 0; i < numSegments; i++) {
    const angle = wheelAngle + i * anglePerSegment;
    ctx.beginPath();
    ctx.moveTo(centerX, centerY);
    ctx.arc(centerX, centerY, radius, angle, angle + anglePerSegment);
    ctx.closePath();
    ctx.fillStyle = colors[i % colors.length];
    ctx.fill();
    ctx.stroke();

    // 繪製文字
    ctx.save();
    ctx.translate(centerX, centerY);
    ctx.rotate(angle + anglePerSegment / 2);
    ctx.textAlign = 'right';
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 15px Noto Sans TC, sans-serif';
    ctx.fillText(wheelNames[i], radius - 20, 5);
    ctx.restore();
  }

  // 中心圓圈
  ctx.beginPath();
  ctx.arc(centerX, centerY, 24, 0, 2 * Math.PI);
  ctx.fillStyle = '#FFFFFF';
  ctx.fill();
  ctx.lineWidth = 3;
  ctx.strokeStyle = '#0F172A';
  ctx.stroke();
}

function spinWheel() {
  if (isSpinning) return;
  isSpinning = true;
  const resultDisplay = document.getElementById('wheel-result-text');
  resultDisplay.textContent = '轉盤旋轉中...';

  const totalRounds = 5 + Math.random() * 4;
  const spinAngle = totalRounds * 2 * Math.PI + Math.random() * 2 * Math.PI;
  const duration = 3500;
  const startTime = performance.now();
  const startAngle = wheelAngle;

  function animate(now) {
    const elapsed = now - startTime;
    const progress = Math.min(elapsed / duration, 1);
    // Ease-out cubic
    const easeOut = 1 - Math.pow(1 - progress, 3);
    wheelAngle = startAngle + spinAngle * easeOut;
    drawWheel();

    if (progress < 1) {
      requestAnimationFrame(animate);
    } else {
      isSpinning = false;
      // 計算指針指向的扇形 (頂部指針位於 3*PI/2)
      const numSegments = wheelNames.length;
      const anglePerSegment = (2 * Math.PI) / numSegments;
      const normalizedAngle = (wheelAngle % (2 * Math.PI) + 2 * Math.PI) % (2 * Math.PI);
      const pointerAngle = (3 * Math.PI / 2);
      let hitIndex = Math.floor((pointerAngle - normalizedAngle + 2 * Math.PI) % (2 * Math.PI) / anglePerSegment);
      hitIndex = (hitIndex % numSegments + numSegments) % numSegments;
      
      const winner = wheelNames[hitIndex];
      resultDisplay.innerHTML = `🎉 抽中：<strong class="text-danger fs-4">${winner}</strong> 發表！`;
    }
  }
  requestAnimationFrame(animate);
}

function updateWheelNames() {
  const input = prompt('請輸入轉盤抽籤名單 (用逗號分隔)：', wheelNames.join(', '));
  if (input) {
    wheelNames = input.split(',').map(s => s.trim()).filter(s => s.length > 0);
    if (wheelNames.length === 0) wheelNames = ['01 號', '02 號', '03 號'];
    drawWheel();
  }
}

// SCAMPER 課堂計時器
function setWorkshopTimer(seconds) {
  stopWorkshopTimer();
  workshopTimer.duration = seconds;
  workshopTimer.remaining = seconds;
  updateTimerDisplay();
}

function updateTimerDisplay() {
  const mins = Math.floor(workshopTimer.remaining / 60);
  const secs = workshopTimer.remaining % 60;
  const display = document.getElementById('workshop-timer-text');
  if (display) {
    display.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  }
}

function startWorkshopTimer() {
  if (workshopTimer.isRunning) return;
  workshopTimer.isRunning = true;
  document.getElementById('timer-start-btn').classList.add('disabled');
  
  const hints = [
    'S (Substitute 替代)：有什麼原料、通路或形式可以被替代？',
    'C (Combine 結合)：能否與另一個完全不相干的產業跨界聯名？',
    'A (Adapt 調整)：能否借鑑其他成功產品的哪一個機制？',
    'M (Modify 修改)：能否把份量變超大、或是切成一口單人份？',
    'P (Put to other uses)：除了原本用途，還能解決什麼非預期痛點？',
    'E (Eliminate 消除)：拿掉最繁瑣、最讓人討厭的哪一個步驟？',
    'R (Reverse 顛倒)：如果把時間、收費或規則完全倒過來會怎樣？'
  ];
  let hintIdx = 0;

  workshopTimer.interval = setInterval(() => {
    workshopTimer.remaining--;
    updateTimerDisplay();

    // 每 30 秒輪播 SCAMPER 思考提示
    if (workshopTimer.remaining % 30 === 0 && workshopTimer.remaining > 0) {
      document.getElementById('scamper-hint-box').textContent = hints[hintIdx % hints.length];
      hintIdx++;
    }

    if (workshopTimer.remaining <= 0) {
      stopWorkshopTimer();
      alert('⏰ 時間到！請各組停止討論，將便利貼貼上白板準備發表！');
      document.getElementById('scamper-hint-box').textContent = '🎉 討論結束！請推派代表進行 60 秒極速提案！';
    }
  }, 1000);
}

function stopWorkshopTimer() {
  if (workshopTimer.interval) {
    clearInterval(workshopTimer.interval);
    workshopTimer.interval = null;
  }
  workshopTimer.isRunning = false;
  const startBtn = document.getElementById('timer-start-btn');
  if (startBtn) startBtn.classList.remove('disabled');
}

function resetWorkshopTimer() {
  stopWorkshopTimer();
  workshopTimer.remaining = workshopTimer.duration;
  updateTimerDisplay();
  document.getElementById('scamper-hint-box').textContent = '準備就緒：點擊開始計時，展開便利貼個人創意發想！';
}

/* ==========================================================================
   回家練習：Agentic AI 企劃工作坊 (Take-Home AI Studio)
   ========================================================================== */
function renderAgentTemplates() {
  const container = document.getElementById('agent-template-selector');
  if (!container || !agentTemplates.length) return;

  container.innerHTML = agentTemplates.map((a, idx) => `
    <button class="btn btn-outline-dark text-start p-2 mb-2 w-100 ${idx === 0 ? 'active' : ''}" 
            id="agent-btn-${a.id}" onclick="selectAgent('${a.id}')">
      <div class="d-flex align-items-center justify-content-between">
        <div>
          <i class="fas ${a.icon} me-2 text-primary"></i>
          <strong>${a.name}</strong>
        </div>
        <span class="badge ${a.badge_color || 'bg-secondary'}">${a.role.split(' ')[0]}</span>
      </div>
      <div class="small text-muted text-truncate mt-1">${a.mission}</div>
    </button>
  `).join('');

  selectAgent(agentTemplates[0].id);
}

function selectAgent(agentId) {
  const agent = agentTemplates.find(a => a.id === agentId);
  if (!agent) return;

  // 標記選中按鈕
  document.querySelectorAll('#agent-template-selector button').forEach(b => b.classList.remove('active', 'border-primary'));
  const activeBtn = document.getElementById(`agent-btn-${agentId}`);
  if (activeBtn) activeBtn.classList.add('active', 'border-primary');

  // 渲染表單與說明
  document.getElementById('current-agent-title').innerHTML = `<i class="fas ${agent.icon} text-primary me-2"></i>${agent.name}`;
  document.getElementById('current-agent-role').textContent = `角色定位：${agent.role}`;
  document.getElementById('current-agent-mission').textContent = agent.mission;

  // 動態渲染輸入欄位
  const fieldsContainer = document.getElementById('agent-dynamic-fields');
  fieldsContainer.innerHTML = agent.fields.map(f => {
    if (f.type === 'select') {
      return `
        <div class="mb-3">
          <label class="form-label fw-semibold small">${f.label}</label>
          <select class="form-select form-select-sm agent-field-input" data-field-id="${f.id}">
            ${f.options.map(opt => `<option value="${opt}" ${opt === f.default ? 'selected' : ''}>${opt}</option>`).join('')}
          </select>
        </div>
      `;
    } else {
      return `
        <div class="mb-3">
          <label class="form-label fw-semibold small">${f.label}</label>
          <input type="${f.type}" class="form-control form-control-sm agent-field-input" 
                 data-field-id="${f.id}" value="${f.default || ''}">
        </div>
      `;
    }
  }).join('');

  // 渲染模擬工具
  const toolsContainer = document.getElementById('agent-simulated-tools');
  toolsContainer.innerHTML = agent.simulated_tools.map(t => `
    <span class="badge bg-light text-dark border me-1 mb-1">
      <i class="fas fa-wrench text-secondary me-1"></i>${t.name}
    </span>
  `).join('');

  // 準備黃金 Prompt
  window.currentSelectedAgent = agent;
  updateGoldenPromptDisplay();
}

function updateGoldenPromptDisplay() {
  const agent = window.currentSelectedAgent;
  if (!agent) return;

  let promptText = agent.golden_prompt;
  document.querySelectorAll('.agent-field-input').forEach(input => {
    const fid = input.getAttribute('data-field-id');
    const val = input.value;
    promptText = promptText.replaceAll(`{${fid}}`, val);
  });

  const displayEl = document.getElementById('agent-golden-prompt-text');
  if (displayEl) displayEl.value = promptText;
}

// 模擬 ReAct 執行
async function runAgentReActSimulation() {
  const agent = window.currentSelectedAgent;
  if (!agent) return;

  const terminalBody = document.getElementById('react-terminal-output');
  terminalBody.innerHTML = '';
  document.getElementById('proposal-draft-output').style.display = 'none';

  const runBtn = document.getElementById('run-agent-btn');
  runBtn.classList.add('disabled');
  runBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-1"></i>Agent 推理運算中...';

  function appendLog(html) {
    terminalBody.innerHTML += `<div class="mb-2">${html}</div>`;
    terminalBody.scrollTop = terminalBody.scrollHeight;
  }

  appendLog(`<span class="text-muted">[系統初始化]</span> 正在掛載行銷代理人環境：<strong>${agent.name}</strong>...`);
  await sleep(600);

  for (const step of agent.react_steps) {
    let badge = '';
    let contentColor = '#C9D1D9';
    if (step.type === 'Thought') {
      badge = `<span class="react-badge badge-thought">THOUGHT 思考</span>`;
      contentColor = '#93C5FD';
    } else if (step.type === 'Action') {
      badge = `<span class="react-badge badge-action">ACTION 調用</span>`;
      contentColor = '#FDE68A';
    } else if (step.type === 'Observation') {
      badge = `<span class="react-badge badge-observation">OBSERVATION 觀察</span>`;
      contentColor = '#A7F3D0';
    } else if (step.type === 'Decision') {
      badge = `<span class="react-badge badge-decision">DECISION 決策</span>`;
      contentColor = '#F5D0FE';
    }

    let detail = step.content;
    if (step.tool) {
      detail = `調用工具 <code>${step.tool}</code>, 參數: <code>${JSON.stringify(step.params || {})}</code>`;
    }

    appendLog(`${badge} <span style="color: ${contentColor};">${detail}</span>`);
    await sleep(750);
  }

  appendLog(`<span class="text-success"><i class="fas fa-check-circle me-1"></i>[執行完成]</span> 行銷企劃產出已準備就緒！`);
  runBtn.classList.remove('disabled');
  runBtn.innerHTML = '<i class="fas fa-play me-1"></i>啟動 ReAct 思考推理';

  // 展現企劃書草案
  renderProposalDraft(agent);
  unlockBadge('badge_agent_react');
}

function renderProposalDraft(agent) {
  const container = document.getElementById('proposal-draft-output');
  const contentEl = document.getElementById('proposal-draft-content');
  if (!container || !contentEl) return;

  // 取得使用者填入的產品名
  const brandInput = document.querySelector('.agent-field-input[data-field-id="brand_product"]') 
                  || document.querySelector('.agent-field-input');
  const subjectName = brandInput ? brandInput.value : '本案專案品牌';

  contentEl.innerHTML = `
    <div class="p-3 bg-white border rounded">
      <div class="d-flex justify-content-between align-items-center border-bottom pb-2 mb-3">
        <h5 class="fw-bold mb-0 text-primary"><i class="fas fa-file-contract me-2"></i>【一頁式行銷企劃書草案】：${subjectName}</h5>
        <span class="badge bg-secondary">產出時間：${new Date().toLocaleDateString()}</span>
      </div>
      <div class="markdown-preview small text-dark" style="white-space: pre-line; line-height: 1.8;">
        ${agent.proposal_snippet}
      </div>
      <div class="mt-3 pt-3 border-top d-flex justify-content-between">
        <button class="btn btn-sm btn-outline-secondary" onclick="window.print()">
          <i class="fas fa-print me-1"></i>列印 / 匯出 PDF
        </button>
        <button class="btn btn-sm btn-primary" onclick="copyGoldenPrompt()">
          <i class="fas fa-copy me-1"></i>複製黃金 Prompt 至 ChatGPT / Gemini
        </button>
      </div>
    </div>
  `;
  container.style.display = 'block';
  container.scrollIntoView({ behavior: 'smooth' });
  unlockBadge('badge_proposal_draft');
}

function copyGoldenPrompt() {
  const textarea = document.getElementById('agent-golden-prompt-text');
  if (!textarea) return;
  textarea.select();
  navigator.clipboard.writeText(textarea.value).then(() => {
    alert('✅ 黃金 Prompt 已成功複製至剪貼簿！\n\n您可直接貼入 ChatGPT、Google Gemini、Claude 或本平台繼續深入對話！');
  }).catch(() => {
    alert('請手動選取文字框並複製。');
  });
}

/* ==========================================================================
   IPAS 證照模擬題庫與檢定系統
   ========================================================================== */
function initQuizSystem() {
  const countSpan = document.getElementById('total-questions-stat');
  if (countSpan) countSpan.textContent = questionsData.length;
}

// 啟動每週隨堂 5 題快測
function startWeeklyQuickQuiz(weekNum) {
  const weekQs = questionsData.filter(q => q.weeks && q.weeks.includes(weekNum));
  const pool = weekQs.length > 0 ? weekQs : questionsData;
  const shuffled = [...pool].sort(() => 0.5 - Math.random()).slice(0, 5);
  
  startQuizWithQuestions(shuffled, `第 ${weekNum} 週隨堂 5 題觀念快測`);
  // 切換至測驗分頁
  const quizTabBtn = document.getElementById('tab-quiz-btn');
  if (quizTabBtn) quizTabBtn.click();
}

// 依題型模式啟動
function startExamMode(mode) {
  let pool = [...questionsData];
  let count = 5;
  let title = '隨堂測驗';

  if (mode === 'weekly_5') {
    pool.sort(() => 0.5 - Math.random());
    count = 5;
    title = '隨堂 5 題隨機快測';
  } else if (mode === 'midterm_40') {
    pool = pool.filter(q => q.chapter <= 6 || q.module.includes('內容') || q.module.includes('社群'));
    pool.sort(() => 0.5 - Math.random());
    count = Math.min(40, pool.length);
    title = '期中 40 題鑑定模擬測驗 (限時40分鐘)';
  } else if (mode === 'final_60') {
    pool.sort(() => 0.5 - Math.random());
    count = Math.min(60, pool.length);
    title = '期末 60 題綜合能力檢定 (限時60分鐘)';
  } else if (mode === 'ipas_brand') {
    pool = pool.filter(q => q.ipas_cert === 'IPAS 品牌規劃師');
    pool.sort(() => 0.5 - Math.random());
    count = Math.min(25, pool.length);
    title = '【IPAS 品牌規劃師】專項能力模擬測驗 (25題)';
  } else if (mode === 'ipas_ai') {
    pool = pool.filter(q => q.ipas_cert === 'IPAS AI 應用規劃師');
    pool.sort(() => 0.5 - Math.random());
    count = Math.min(25, pool.length);
    title = '【IPAS AI 應用規劃師】專項能力模擬測驗 (25題)';
  } else if (mode === 'wrong_notebook') {
    if (wrongQuestionsSet.size === 0) {
      alert('太棒了！目前錯題筆記本空空如也，沒有任何錯題需要重練！');
      return;
    }
    pool = pool.filter(q => wrongQuestionsSet.has(q.id));
    count = pool.length;
    title = `錯題筆記本重練專區 (${count} 題)`;
  }

  const selected = pool.slice(0, count);
  startQuizWithQuestions(selected, title);
}

function startQuizWithQuestions(qs, title) {
  if (!qs || qs.length === 0) {
    alert('目前暫無符合條件之測驗題目。');
    return;
  }
  activeQuiz.questions = qs;
  activeQuiz.currentIndex = 0;
  activeQuiz.userAnswers = {};
  activeQuiz.examModeTitle = title;
  activeQuiz.timerSeconds = 0;

  if (activeQuiz.timerInterval) clearInterval(activeQuiz.timerInterval);
  activeQuiz.timerInterval = setInterval(() => {
    activeQuiz.timerSeconds++;
    const m = Math.floor(activeQuiz.timerSeconds / 60);
    const s = activeQuiz.timerSeconds % 60;
    const timerDisplay = document.getElementById('quiz-live-timer');
    if (timerDisplay) timerDisplay.textContent = `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
  }, 1000);

  document.getElementById('quiz-setup-panel').style.display = 'none';
  document.getElementById('quiz-result-panel').style.display = 'none';
  document.getElementById('quiz-active-panel').style.display = 'block';

  document.getElementById('quiz-mode-title').textContent = title;
  renderCurrentQuestion();
}

function renderCurrentQuestion() {
  const q = activeQuiz.questions[activeQuiz.currentIndex];
  if (!q) return;

  const total = activeQuiz.questions.length;
  const currentIdx1 = activeQuiz.currentIndex + 1;

  document.getElementById('quiz-progress-text').textContent = `第 ${currentIdx1} / ${total} 題`;
  document.getElementById('quiz-progress-bar').style.width = `${(currentIdx1 / total) * 100}%`;

  const certBadge = q.ipas_cert ? `<span class="badge bg-dark me-1"><i class="fas fa-award text-warning me-1"></i>${q.ipas_cert}</span>` : '';
  const subjBadge = q.ipas_subject ? `<span class="badge bg-info text-dark me-1">${q.ipas_subject}</span>` : '';

  document.getElementById('quiz-question-meta').innerHTML = `
    ${certBadge}
    ${subjBadge}
    <span class="badge bg-primary me-1">${q.chapter_title || '行銷企劃'}</span>
    <span class="badge bg-secondary">${q.module || '專業考點'}</span>
  `;
  document.getElementById('quiz-question-stem').textContent = q.question;

  const optionsContainer = document.getElementById('quiz-options-container');
  const userSelected = activeQuiz.userAnswers[q.id];
  const prefixes = ['A', 'B', 'C', 'D'];

  optionsContainer.innerHTML = q.options.map((opt, idx) => `
    <div class="quiz-option ${userSelected === idx ? 'selected' : ''}" onclick="selectQuizAnswer('${q.id}', ${idx})">
      <div class="option-prefix">${prefixes[idx]}</div>
      <div class="option-text">${opt}</div>
    </div>
  `).join('');

  // 上一題 / 下一題 按鈕狀態
  document.getElementById('quiz-prev-btn').disabled = (activeQuiz.currentIndex === 0);
  const nextBtn = document.getElementById('quiz-next-btn');
  if (activeQuiz.currentIndex === total - 1) {
    nextBtn.innerHTML = '<i class="fas fa-paper-plane me-1"></i>完成交卷';
    nextBtn.className = 'btn btn-danger';
  } else {
    nextBtn.innerHTML = '下一題<i class="fas fa-arrow-right ms-1"></i>';
    nextBtn.className = 'btn btn-primary';
  }
}

function selectQuizAnswer(qid, optIndex) {
  activeQuiz.userAnswers[qid] = optIndex;
  renderCurrentQuestion();
}

function prevQuizQuestion() {
  if (activeQuiz.currentIndex > 0) {
    activeQuiz.currentIndex--;
    renderCurrentQuestion();
  }
}

function nextOrSubmitQuiz() {
  if (activeQuiz.currentIndex < activeQuiz.questions.length - 1) {
    activeQuiz.currentIndex++;
    renderCurrentQuestion();
  } else {
    submitQuizPaper();
  }
}

async function submitQuizPaper() {
  const total = activeQuiz.questions.length;
  const answeredCount = Object.keys(activeQuiz.userAnswers).length;

  if (answeredCount < total) {
    if (!confirm(`您還有 ${total - answeredCount} 題尚未作答，確定要現在交卷嗎？`)) {
      return;
    }
  }

  if (activeQuiz.timerInterval) clearInterval(activeQuiz.timerInterval);

  // 批改試卷 (若線上優先呼叫後端，若離線在前端批改)
  let result = null;
  try {
    const res = await fetch('/api/submit_quiz', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        student_id: currentUser.studentId || '匿名學生',
        student_name: currentUser.studentName || '同學',
        answers: activeQuiz.userAnswers,
        exam_mode: activeQuiz.examModeTitle
      })
    });
    if (res.ok) result = await res.json();
  } catch (e) {}

  if (!result) {
    // 前端自算
    let correct = 0;
    const wrongs = [];
    const radar = {};

    activeQuiz.questions.forEach(q => {
      const uAns = activeQuiz.userAnswers[q.id];
      const isCorrect = (uAns !== undefined && parseInt(uAns) === parseInt(q.answer));
      const mod = q.module || '一般題目';
      if (!radar[mod]) radar[mod] = { correct: 0, total: 0 };
      radar[mod].total++;

      if (isCorrect) {
        correct++;
        radar[mod].correct++;
      } else {
        wrongs.push({
          id: q.id,
          chapter_title: q.chapter_title,
          module: mod,
          ipas_cert: q.ipas_cert || 'IPAS 品牌規劃師',
          ipas_subject: q.ipas_subject || '品牌策略與規劃',
          question: q.question,
          options: q.options,
          user_answer: uAns,
          correct_answer: q.answer,
          explanation: q.explanation
        });
      }
    });

    const score = Math.round((correct / total) * 100);
    result = {
      score: score,
      passed: score >= 70,
      correct_count: correct,
      total_questions: total,
      feedback: score >= 90 ? '太神了！行銷企劃與 IPAS 檢定觀念超群！' : (score >= 70 ? '恭喜及格！已達 IPAS 檢定水準！' : '請再接再厲，多複習錯題解析！'),
      module_radar: radar,
      wrong_questions: wrongs
    };
  }

  renderQuizResult(result);
}

function renderQuizResult(result) {
  document.getElementById('quiz-active-panel').style.display = 'none';
  const resultPanel = document.getElementById('quiz-result-panel');
  resultPanel.style.display = 'block';

  document.getElementById('result-score-number').textContent = result.score;
  document.getElementById('result-correct-ratio').textContent = `${result.correct_count} / ${result.total_questions}`;
  document.getElementById('result-feedback-text').textContent = result.feedback;

  const passBadge = document.getElementById('result-pass-badge');
  if (result.passed) {
    passBadge.className = 'badge bg-success fs-6';
    passBadge.textContent = '檢定合格 (PASSED)';
  } else {
    passBadge.className = 'badge bg-danger fs-6';
    passBadge.textContent = '尚未達標 (需重練)';
  }

  // 錯題收集至 LocalStorage
  result.wrong_questions.forEach(w => wrongQuestionsSet.add(w.id));
  localStorage.setItem('vnu_wrong_questions', JSON.stringify([...wrongQuestionsSet]));

  // 成就解鎖
  unlockBadge('badge_weekly_quiz');
  if (result.score >= 90) unlockBadge('badge_score_90');
  if (wrongQuestionsSet.size === 0) unlockBadge('badge_wrong_review');

  // 渲染錯題解析清單
  const wrongListContainer = document.getElementById('result-wrong-list');
  if (result.wrong_questions.length === 0) {
    wrongListContainer.innerHTML = '<div class="alert alert-success">全對滿分！沒有任何答錯的題目，太厲害了！</div>';
  } else {
    const prefixes = ['A', 'B', 'C', 'D'];
    wrongListContainer.innerHTML = result.wrong_questions.map((wq, i) => `
      <div class="card p-3 mb-3 border-danger bg-white">
        <div class="d-flex justify-content-between small text-muted mb-1 align-items-center">
          <div>
            ${wq.ipas_cert ? `<span class="badge bg-dark me-1">${wq.ipas_cert}</span>` : ''}
            ${wq.ipas_subject ? `<span class="badge bg-info text-dark me-1">${wq.ipas_subject}</span>` : ''}
            <span>錯題 #${i + 1} ｜ ${wq.chapter_title}</span>
          </div>
          <span class="text-danger fw-bold">題號: ${wq.id}</span>
        </div>
        <h6 class="fw-bold text-dark">${wq.question}</h6>
        <div class="row g-2 small my-2">
          <div class="col-md-6">
            <span class="text-danger">您的作答：${wq.user_answer !== undefined ? prefixes[wq.user_answer] + '. ' + wq.options[wq.user_answer] : '未作答'}</span>
          </div>
          <div class="col-md-6">
            <span class="text-success fw-bold">正確解答：${prefixes[wq.correct_answer]}. ${wq.options[wq.correct_answer]}</span>
          </div>
        </div>
        <div class="alert alert-light border py-2 px-3 small mb-0">
          <strong><i class="fas fa-info-circle text-primary me-1"></i>觀念詳解：</strong>${wq.explanation}
        </div>
      </div>
    `).join('');
  }
}

function resetQuizToSetup() {
  document.getElementById('quiz-result-panel').style.display = 'none';
  document.getElementById('quiz-active-panel').style.display = 'none';
  document.getElementById('quiz-setup-panel').style.display = 'block';
}

function clearWrongQuestionsNotebook() {
  if (confirm('確定要清空個人錯題筆記本嗎？')) {
    wrongQuestionsSet.clear();
    localStorage.removeItem('vnu_wrong_questions');
    alert('已清空錯題筆記本！');
  }
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

/* ==========================================================================
   學生作品成果展示廊 (Student Works Gallery & Upload)
   ========================================================================== */
let allStudentWorks = [];
let filteredStudentWorks = [];
let currentWorksCategory = 'all';

async function loadStudentWorks() {
  try {
    const res = await fetch('/api/student_works');
    if (res.ok) {
      allStudentWorks = await res.json();
    }
  } catch (e) {
    // Offline fallback: try loading from window globals
    allStudentWorks = window.OFFLINE_SAMPLE_WORKS || [];
  }
  filteredStudentWorks = [...allStudentWorks];
  renderStudentWorksGallery(filteredStudentWorks);
}

function renderStudentWorksGallery(works) {
  const container = document.getElementById('student-works-gallery');
  if (!container) return;

  if (!works || works.length === 0) {
    container.innerHTML = `
      <div class="col-12 text-center py-5 text-muted">
        <i class="fas fa-folder-open fa-3x mb-3 text-secondary"></i>
        <h6 class="fw-bold">尚無作品展示</h6>
        <p class="small">點擊上方【上傳我的企劃成果】開始提交第一份行銷企劃作品！</p>
      </div>`;
    return;
  }

  container.innerHTML = works.map((w, idx) => {
    const thumbStyle = w.thumbnail || 'linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%)';
    const thumbIcon = w.thumbnail_icon || 'fas fa-briefcase';
    const ghUrl = w.github_page_url || w.live_url || '';
    const repoUrl = w.github_repo_url || '';
    const hasGH = ghUrl && ghUrl.startsWith('http');
    const hasRepo = repoUrl && repoUrl.startsWith('http');
    const tags = (w.tags || []).slice(0, 4);
    const scoreText = w.score || '';

    return `
    <div class="col-md-6 col-lg-4 work-card-item" data-category="${w.category || ''}" data-search="${(w.title||'')+(w.team_name||'')+(w.student_id||'')+(w.concept||'')+(w.author||'')}">
      <div class="card h-100 shadow-sm border-0 overflow-hidden" style="cursor:pointer;" onclick="showWorkDetail(${idx})">
        <div class="position-relative" style="height: 120px; background: ${thumbStyle}; display:flex; align-items:center; justify-content:center;">
          <i class="${thumbIcon} text-white" style="font-size: 2.5rem; opacity:0.4;"></i>
          ${scoreText ? `<span class="position-absolute top-0 end-0 m-2 badge bg-warning text-dark fw-bold" style="font-size:0.72rem;">${scoreText}</span>` : ''}
          ${hasGH ? `<span class="position-absolute bottom-0 start-0 m-2 badge bg-dark bg-opacity-75"><i class="fab fa-github me-1"></i>GitHub Pages</span>` : ''}
        </div>
        <div class="card-body p-3">
          <div class="d-flex justify-content-between align-items-start mb-1">
            <span class="badge bg-primary bg-opacity-10 text-primary fw-bold" style="font-size:0.68rem;"><i class="fas fa-user me-1"></i>${w.student_name ? `${w.student_name} (${w.student_id||''})` : (w.author || '個人獨立企劃')}</span>
            <span class="text-muted" style="font-size:0.65rem;">W${String(w.week||'').padStart(2,'0')}</span>
          </div>
          <h6 class="fw-bold text-dark mb-1 lh-sm" style="font-size:0.88rem;">${w.title || '未命名專案'}</h6>
          <p class="text-muted small mb-2 lh-sm" style="font-size:0.75rem; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">
            ${w.concept || w.desc || '暫無描述'}
          </p>
          <div class="d-flex flex-wrap gap-1 mb-2">
            ${tags.map(t => `<span class="badge bg-light text-dark border" style="font-size:0.62rem;">${t}</span>`).join('')}
          </div>
          <div class="d-flex gap-1 mt-auto">
            ${hasGH ? `<a href="${ghUrl}" target="_blank" rel="noopener" class="btn btn-sm btn-success flex-fill fw-bold" onclick="event.stopPropagation();" style="font-size:0.72rem;">
              <i class="fas fa-external-link-alt me-1"></i>開啟 GitHub Pages 成果
            </a>` : ''}
            ${hasRepo ? `<a href="${repoUrl}" target="_blank" rel="noopener" class="btn btn-sm btn-outline-dark" onclick="event.stopPropagation();" style="font-size:0.72rem;" title="GitHub Repo">
              <i class="fab fa-github"></i>
            </a>` : ''}
          </div>
        </div>
      </div>
    </div>`;
  }).join('');
}

function filterWorksByCategory(category, btn) {
  currentWorksCategory = category;
  // Update active button
  document.querySelectorAll('#works-category-filters button').forEach(b => {
    b.classList.remove('btn-dark', 'active');
    b.classList.add('btn-outline-secondary');
  });
  if (btn) {
    btn.classList.remove('btn-outline-secondary');
    btn.classList.add('btn-dark', 'active');
  }

  if (category === 'all') {
    filteredStudentWorks = [...allStudentWorks];
  } else {
    filteredStudentWorks = allStudentWorks.filter(w => (w.category || w.type || '').includes(category));
  }

  // Also apply search if present
  const searchVal = (document.getElementById('search-works-input')?.value || '').trim().toLowerCase();
  if (searchVal) {
    filteredStudentWorks = filteredStudentWorks.filter(w => {
      const haystack = ((w.title||'')+(w.team_name||'')+(w.student_id||'')+(w.concept||'')+(w.author||'')+(w.desc||'')).toLowerCase();
      return haystack.includes(searchVal);
    });
  }

  renderStudentWorksGallery(filteredStudentWorks);
}

function searchWorks(query) {
  const q = (query || '').trim().toLowerCase();
  let base = currentWorksCategory === 'all' ? [...allStudentWorks] :
    allStudentWorks.filter(w => (w.category || w.type || '').includes(currentWorksCategory));

  if (q) {
    base = base.filter(w => {
      const haystack = ((w.title||'')+(w.team_name||'')+(w.student_id||'')+(w.concept||'')+(w.author||'')+(w.desc||'')).toLowerCase();
      return haystack.includes(q);
    });
  }

  filteredStudentWorks = base;
  renderStudentWorksGallery(filteredStudentWorks);
}

function showWorkDetail(idx) {
  const w = filteredStudentWorks[idx];
  if (!w) return;

  document.getElementById('modal-detail-title').textContent = w.title || '未命名專案';
  document.getElementById('modal-detail-category').textContent = w.category || w.type || '成果專案';

  const ghUrl = w.github_page_url || w.live_url || '';
  const repoUrl = w.github_repo_url || '';
  const hasGH = ghUrl && ghUrl.startsWith('http');
  const hasRepo = repoUrl && repoUrl.startsWith('http');
  const hasDemoHtml = w.demo_html && w.demo_html.length > 10;

  let bodyHtml = `
    <div class="row g-3">
      <div class="col-md-6">
        <div class="small">
          <div class="mb-2"><strong class="text-secondary">專案模式：</strong><span class="badge bg-primary">個人獨立企劃</span></div>
          <div class="mb-2"><strong class="text-secondary">作者：</strong>${w.student_name || w.author || '—'}</div>
          <div class="mb-2"><strong class="text-secondary">學號：</strong>${w.student_id || '—'}</div>
          <div class="mb-2"><strong class="text-secondary">週次：</strong>第 ${String(w.week||'').padStart(2,'0')} 週 ${w.week_title || ''}</div>
          <div class="mb-2"><strong class="text-secondary">成績：</strong><span class="badge bg-success">${w.score || '待評'}</span></div>
          <div class="mb-2"><strong class="text-secondary">協同 Agent：</strong>${w.agent_used || '—'}</div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="small">
          <div class="mb-2"><strong class="text-secondary">痛點洞察與價值主張：</strong></div>
          <p class="text-muted lh-sm">${w.concept || w.desc || '暫無描述'}</p>
          ${w.prompt_summary ? `<div class="mb-2"><strong class="text-secondary">CLEAR 提示詞歷程：</strong></div><pre class="bg-light p-2 rounded small text-dark" style="white-space:pre-wrap;font-size:0.75rem;">${w.prompt_summary}</pre>` : ''}
        </div>
      </div>
    </div>`;

  // GitHub Pages link
  if (hasGH) {
    bodyHtml += `
    <div class="mt-3 p-3 bg-success bg-opacity-10 border border-success border-opacity-25 rounded-3">
      <strong class="text-success"><i class="fab fa-github me-1"></i>GitHub Pages 線上成果：</strong>
      <a href="${ghUrl}" target="_blank" rel="noopener" class="ms-2 fw-bold text-decoration-none">${ghUrl}</a>
    </div>`;
  }

  // Embedded demo preview
  if (hasDemoHtml) {
    bodyHtml += `
    <div class="mt-3">
      <strong class="text-secondary small">作品內嵌預覽：</strong>
      <div class="border rounded-3 mt-2 bg-white" style="height:280px; overflow:hidden;">
        <iframe srcdoc="${w.demo_html.replace(/"/g, '&quot;')}" style="width:100%;height:100%;border:none;" sandbox="allow-scripts"></iframe>
      </div>
    </div>`;
  }

  document.getElementById('modal-detail-body').innerHTML = bodyHtml;

  // Footer buttons
  let footerHtml = `<button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">關閉視窗</button>`;
  if (hasGH) {
    footerHtml = `<a href="${ghUrl}" target="_blank" rel="noopener" class="btn btn-success btn-sm fw-bold"><i class="fas fa-external-link-alt me-1"></i>開啟 GitHub Pages 成果</a>` + footerHtml;
  }
  if (hasRepo) {
    footerHtml = `<a href="${repoUrl}" target="_blank" rel="noopener" class="btn btn-outline-dark btn-sm"><i class="fab fa-github me-1"></i>GitHub Repo</a>` + footerHtml;
  }
  document.getElementById('modal-detail-footer').innerHTML = footerHtml;

  const modal = new bootstrap.Modal(document.getElementById('viewWorkDetailModal'));
  modal.show();
}

async function handleWorkSubmit(event) {
  event.preventDefault();
  const btn = document.getElementById('submit-work-btn');
  btn.disabled = true;
  btn.innerHTML = '<i class="fas fa-spinner fa-spin me-1"></i>上傳中...';

  // Collect form values
  const studentId = document.getElementById('work-student-id').value.trim();
  const studentName = document.getElementById('work-student-name').value.trim();
  const teamName = document.getElementById('work-team-name').value;
  const week = parseInt(document.getElementById('work-week').value);
  const weekOpt = document.getElementById('work-week');
  const weekTitle = weekOpt.options[weekOpt.selectedIndex].text;
  const title = document.getElementById('work-title').value.trim();
  const category = document.getElementById('work-category').value;
  const agentUsed = document.getElementById('work-agent-used').value;
  const concept = document.getElementById('work-concept').value.trim();
  const promptSummary = document.getElementById('work-prompt-summary').value.trim();

  let ghPageUrl = document.getElementById('work-github-page-url').value.trim();
  if (ghPageUrl && !ghPageUrl.startsWith('http')) ghPageUrl = 'https://' + ghPageUrl;
  const ghRepoUrl = document.getElementById('work-github-repo-url').value.trim();

  const fileInput = document.getElementById('work-file-input');
  const hasFile = fileInput && fileInput.files && fileInput.files.length > 0;
  const workDocId = 'WORK-' + Date.now();

  const newWorkData = {
    id: workDocId,
    student_id: studentId,
    student_name: studentName,
    team_name: teamName,
    week,
    week_title: weekTitle,
    title,
    category,
    agent_used: agentUsed,
    concept,
    prompt_summary: promptSummary,
    github_page_url: ghPageUrl,
    github_repo_url: ghRepoUrl,
    live_url: ghPageUrl,
    author: `${studentName} (${studentId})`,
    author_uid: currentFirebaseUser ? currentFirebaseUser.uid : '',
    author_email: currentFirebaseUser ? currentFirebaseUser.email : '',
    submitted_at: new Date().toLocaleString('zh-TW'),
    score: '已繳交 (雲端同步)',
    teacher_comment: '作品已成功發布至班級成果展。'
  };

  let firestoreSuccess = false;
  if (firestoreDb) {
    try {
      await firestoreDb.collection('works').doc(workDocId).set({
        ...newWorkData,
        createdAt: firebase.firestore.FieldValue.serverTimestamp()
      });
      firestoreSuccess = true;
      console.log('✅ 作品已成功寫入 Firebase Firestore:', workDocId);
    } catch (fsErr) {
      console.warn('Firestore works upload warning:', fsErr);
    }
  }

  try {
    let result = { success: firestoreSuccess };
    if (!firestoreSuccess) {
      if (hasFile) {
        // Multipart form upload
        const formData = new FormData();
        formData.append('student_id', studentId);
        formData.append('student_name', studentName);
        formData.append('team_name', teamName);
        formData.append('week', week);
        formData.append('week_title', weekTitle);
        formData.append('title', title);
        formData.append('category', category);
        formData.append('agent_used', agentUsed);
        formData.append('concept', concept);
        formData.append('prompt_summary', promptSummary);
        formData.append('github_page_url', ghPageUrl);
        formData.append('github_repo_url', ghRepoUrl);
        formData.append('live_url', ghPageUrl);
        formData.append('file', fileInput.files[0]);
        const res = await fetch('/api/upload_work', { method: 'POST', body: formData });
        result = await res.json();
      } else {
        // JSON upload
        const res = await fetch('/api/upload_work', {
          method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(newWorkData)
        });
        result = await res.json();
      }
    }

    if (result.success || firestoreSuccess) {
      alert('🎉 個人行銷企劃作品成果已成功上傳並發布！');
      const modal = bootstrap.Modal.getInstance(document.getElementById('uploadWorkModal'));
      if (modal) modal.hide();
      document.getElementById('upload-work-form').reset();
      await loadStudentWorks();
      document.getElementById('tab-works-btn')?.click();
      if (typeof unlockBadge === 'function') unlockBadge('badge_work_upload');
    } else {
      alert('上傳失敗：' + (result.error || '未知錯誤'));
    }
  } catch (e) {
    if (firestoreSuccess) {
      alert('🎉 個人行銷企劃作品已成功儲存至 Firebase 雲端展示廊！');
      const modal = bootstrap.Modal.getInstance(document.getElementById('uploadWorkModal'));
      if (modal) modal.hide();
      document.getElementById('upload-work-form').reset();
      await loadStudentWorks();
      document.getElementById('tab-works-btn')?.click();
      if (typeof unlockBadge === 'function') unlockBadge('badge_work_upload');
    } else {
      // Offline fallback: save to localStorage
      let offlineWorks = JSON.parse(localStorage.getItem('vnu_offline_works') || '[]');
      offlineWorks.unshift(newWorkData);
      localStorage.setItem('vnu_offline_works', JSON.stringify(offlineWorks));
      allStudentWorks.unshift(newWorkData);
      filteredStudentWorks = [...allStudentWorks];
      renderStudentWorksGallery(filteredStudentWorks);
      alert('⚠️ 目前為離線模式，作品已暫存於瀏覽器。下次連線時將自動同步。');
      const modal = bootstrap.Modal.getInstance(document.getElementById('uploadWorkModal'));
      if (modal) modal.hide();
      document.getElementById('upload-work-form').reset();
    }
  } finally {
    btn.disabled = false;
    btn.innerHTML = '<i class="fas fa-cloud-upload-alt me-1"></i>確認上傳並發布';
  }
}

/* ==========================================================================
   Vibe Coding 操作手冊 (Vibe Coding Manual Renderer)
   ========================================================================== */
async function loadVibeManual() {
  const container = document.getElementById('vibe-manual-content');
  if (!container) return;

  let guideData = null;
  try {
    const res = await fetch('/api/vibe_manual');
    if (res.ok) guideData = await res.json();
  } catch (e) {
    guideData = window.OFFLINE_VIBE_GUIDE || null;
  }

  if (!guideData) {
    container.innerHTML = '<div class="alert alert-warning">Vibe Coding 手冊資料載入失敗，請重新整理頁面。</div>';
    return;
  }

  let html = '';

  // 1. Overview: what is Vibe Coding + Agentic AI
  if (guideData.overview) {
    const ov = guideData.overview;
    html += `
    <div class="mb-4 p-4 bg-primary bg-opacity-10 rounded-3 border border-primary border-opacity-25">
      <h5 class="fw-bold text-primary mb-2"><i class="fas fa-lightbulb me-2"></i>${guideData.title || '什麼是 Vibe Coding？'}</h5>
      <p class="text-muted small mb-1">${guideData.subtitle || ''}</p>
      <hr class="my-2">
      <p class="mb-2 text-dark lh-sm" style="font-size:0.88rem;">${ov.what_is_vibe_coding || ''}</p>
      ${ov.what_is_agentic_ai ? `<p class="mb-2 text-dark lh-sm" style="font-size:0.88rem;"><strong class="text-primary">Agentic AI：</strong>${ov.what_is_agentic_ai}</p>` : ''}
      ${ov.why_business_students ? `<p class="mb-0 text-muted small lh-sm">${ov.why_business_students}</p>` : ''}
    </div>`;
  }

  // 2. CLEAR Framework (array of {key, name, desc, example})
  const cf = guideData.clear_framework;
  if (cf && Array.isArray(cf) && cf.length > 0) {
    html += `
    <div class="mb-4">
      <h5 class="fw-bold text-dark mb-3"><i class="fas fa-puzzle-piece text-warning me-2"></i>CLEAR 提問框架</h5>
      <div class="row g-2">
        ${cf.map(s => `
        <div class="col-md-6 col-lg">
          <div class="card h-100 border-0 shadow-sm">
            <div class="card-body p-3">
              <span class="badge bg-warning text-dark fw-bold mb-2">${s.key || ''}</span>
              <h6 class="fw-bold mb-1" style="font-size:0.85rem;">${s.name || ''}</h6>
              <p class="text-muted small mb-0">${s.desc || s.description || ''}</p>
              ${s.example ? `<div class="mt-2 bg-light p-2 rounded small text-dark"><strong>範例：</strong>${s.example}</div>` : ''}
            </div>
          </div>
        </div>`).join('')}
      </div>
    </div>`;
  }

  // 3. Three Golden Steps (array of {step, title, desc, tip, icon, color})
  const tgs = guideData.three_golden_steps;
  if (tgs && Array.isArray(tgs) && tgs.length > 0) {
    html += `
    <div class="mb-4">
      <h5 class="fw-bold text-dark mb-3"><i class="fas fa-rocket text-success me-2"></i>3 大黃金步驟</h5>
      <div class="row g-3">
        ${tgs.map((s, i) => `
        <div class="col-md-4">
          <div class="card h-100 border-success border-opacity-25 shadow-sm">
            <div class="card-body p-3">
              <span class="badge mb-2" style="background:${s.color || '#22c55e'};">${s.icon ? `<i class="fas ${s.icon} me-1"></i>` : ''}步驟 ${s.step || i+1}</span>
              <h6 class="fw-bold mb-1">${s.title || ''}</h6>
              <p class="text-muted small mb-1">${s.desc || s.description || ''}</p>
              ${s.tip ? `<div class="mt-2 text-success small fw-bold lh-sm"><i class="fas fa-check-circle me-1"></i>${s.tip}</div>` : ''}
            </div>
          </div>
        </div>`).join('')}
      </div>
    </div>`;
  }

  // 4. GitHub Pages 30-second guide
  if (guideData.github_pages_guide) {
    const gp = guideData.github_pages_guide;
    html += `
    <div class="mb-4 p-4 bg-dark text-white rounded-3">
      <h5 class="fw-bold mb-2"><i class="fab fa-github me-2"></i>${gp.title || '30 秒 GitHub Pages 部署指南'}</h5>
      <p class="text-white-50 small mb-3">${gp.subtitle || ''}</p>
      <ol class="mb-0">
        ${(gp.steps || []).map(s => `<li class="mb-2"><strong>${s.step_name || s.title || ''}：</strong><span class="text-white-50">${s.detail || ''}</span></li>`).join('')}
      </ol>
    </div>`;
  }

  // 5. Teacher Demo
  if (guideData.teacher_demo) {
    const td = guideData.teacher_demo;
    html += `
    <div class="mb-4 p-4 bg-info bg-opacity-10 rounded-3 border border-info border-opacity-25">
      <h5 class="fw-bold text-info mb-2"><i class="fas fa-play-circle me-2"></i>${td.title || '教師 Live Demo 示範'}</h5>
      <p class="text-muted small mb-2">${td.scenario || ''}</p>
      ${td.prompt_demo ? `<pre class="bg-white p-3 rounded small text-dark border" style="white-space:pre-wrap;">${td.prompt_demo}</pre>` : ''}
    </div>`;
  }

  // 6. FAQ (pitfalls_and_faq, array of {q, a})
  const faq = guideData.pitfalls_and_faq || guideData.faq;
  if (faq && Array.isArray(faq) && faq.length > 0) {
    html += `
    <div class="mb-2">
      <h5 class="fw-bold text-dark mb-3"><i class="fas fa-question-circle text-danger me-2"></i>常見問題與避坑指南 (FAQ)</h5>
      <div class="accordion" id="vibeFaqAccordion">
        ${faq.map((f, i) => `
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button class="accordion-button collapsed fw-bold small" type="button" data-bs-toggle="collapse" data-bs-target="#vibeFaq${i}">
              ${f.q || f.question || ''}
            </button>
          </h2>
          <div id="vibeFaq${i}" class="accordion-collapse collapse" data-bs-parent="#vibeFaqAccordion">
            <div class="accordion-body small text-muted">${f.a || f.answer || ''}</div>
          </div>
        </div>`).join('')}
      </div>
    </div>`;
  }

  container.innerHTML = html;
}
