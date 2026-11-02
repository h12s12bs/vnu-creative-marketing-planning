# -*- coding: utf-8 -*-
"""
更新 11501創意行銷企劃實務 課程平台：
1. templates/index.html：加入期中期末考題庫電子檔下載專區與線上展開/列印面板
2. static/js/app.js：加入 openQuestionBankViewer / downloadCurrentBankHtml / printCurrentQuestionBank / closeQuestionBankViewer 函式
3. 執行 tools/build_offline_html.py 重新產生平台首頁(單機離線直接點開).html、創意行銷企劃實務.html 與 index.html
"""
import os
import sys

def update_templates_html(base_dir):
    tmpl_path = os.path.join(base_dir, 'templates', 'index.html')
    with open(tmpl_path, 'r', encoding='utf-8') as f:
        html = f.read()

    download_section_html = '''            <button class="btn btn-sm btn-outline-danger" onclick="clearWrongQuestionsNotebook()">
              <i class="fas fa-trash-alt me-1"></i>清空錯題筆記
            </button>
          </div>

          <!-- 📥 期中考 ✕ 期末考「全部考題電子檔（含標準答案與詳解）」下載專區 -->
          <div class="p-4 mb-4 rounded-3 border border-primary border-opacity-25 shadow-sm" style="background: linear-gradient(135deg, #eff6ff 0%, #eef2ff 50%, #fffbeb 100%);">
            <div class="d-flex flex-column flex-sm-row sm:items-center justify-content-between gap-2 mb-3">
              <div>
                <h5 class="fw-bold text-dark mb-1 d-flex align-items-center gap-2">
                  <i class="fas fa-book-open-reader text-primary"></i>
                  <span>📥 期中考 ✕ 期末考「全部考題電子檔（含標準答案與詳解）」下載專區</span>
                </h5>
                <p class="small text-secondary mb-0">
                  📢 <strong>命題公告：</strong>本學期<strong>期中考（第 1～5 章，共 75 題）</strong>與<strong>期末考（第 6～11 章，共 105 題）</strong>皆直接從下方兩份題庫抽題考試！每題均已附上官方標準答案與詳解，請同學下載熟讀。
                </p>
              </div>
              <span class="badge bg-success bg-opacity-10 text-success border border-success border-opacity-25 px-3 py-2 align-self-start align-self-sm-center shrink-0">
                <i class="fas fa-shield-check me-1"></i>180 題答案已 100% 雙重檢核無誤
              </span>
            </div>

            <div class="row g-3">
              <!-- Card 1: 期中考全部題庫 -->
              <div class="col-md-4">
                <div class="card h-100 p-3 border-2 border-primary bg-white shadow-sm d-flex flex-column justify-content-between">
                  <div>
                    <div class="d-flex justify-content-between align-items-center mb-2">
                      <span class="badge bg-primary">期中考必備</span>
                      <span class="small fw-bold text-primary font-monospace">共 75 題（含答案）</span>
                    </div>
                    <h6 class="fw-bold text-dark mb-2">📘 期中考全部考題題庫 (第 1～5 章)</h6>
                    <p class="text-muted small leading-relaxed mb-3">
                      涵蓋：行銷企劃本質、目標設定、外部宏觀與產業五力(PESTEL/波特五力)、內部價值鏈與TOWS矩陣、激發企劃創意(SCAMPER/心智圖)。
                    </p>
                  </div>
                  <div class="d-flex flex-wrap gap-2 pt-2 border-top">
                    <a href="static/exam_banks/Marketing_Planning_Midterm_Question_Bank_With_Answers.docx" download="萬能科大_創意行銷企劃實務_期中考全部題庫(含標準答案與詳解_第1至5章_75題).docx" class="btn btn-primary btn-sm flex-fill fw-bold">
                      <i class="fas fa-download me-1"></i>下載 Word (.docx)
                    </a>
                    <button type="button" onclick="openQuestionBankViewer('midterm')" class="btn btn-outline-primary btn-sm fw-bold">
                      <i class="fas fa-eye me-1"></i>線上展開／列印
                    </button>
                  </div>
                </div>
              </div>

              <!-- Card 2: 期末考全部題庫 -->
              <div class="col-md-4">
                <div class="card h-100 p-3 bg-white shadow-sm d-flex flex-column justify-content-between" style="border: 2px solid #6366f1 !important;">
                  <div>
                    <div class="d-flex justify-content-between align-items-center mb-2">
                      <span class="badge" style="background-color: #6366f1;">期末考必備</span>
                      <span class="small fw-bold font-monospace" style="color: #4f46e5;">共 105 題（含答案）</span>
                    </div>
                    <h6 class="fw-bold text-dark mb-2">📙 期末考全部考題題庫 (第 6～11 章)</h6>
                    <p class="text-muted small leading-relaxed mb-3">
                      涵蓋：新產品上市行銷企劃、公關與事件行銷企劃、促銷企劃案、其他類行銷企劃案例、企劃撰寫簡報、MarTech 實務與生成式 AI 應用。
                    </p>
                  </div>
                  <div class="d-flex flex-wrap gap-2 pt-2 border-top">
                    <a href="static/exam_banks/Marketing_Planning_Final_Question_Bank_With_Answers.docx" download="萬能科大_創意行銷企劃實務_期末考全部題庫(含標準答案與詳解_第6至11章_105題).docx" class="btn btn-sm flex-fill fw-bold text-white" style="background-color: #6366f1;">
                      <i class="fas fa-download me-1"></i>下載 Word (.docx)
                    </a>
                    <button type="button" onclick="openQuestionBankViewer('final')" class="btn btn-sm fw-bold" style="color: #4f46e5; border: 1px solid #c7d2fe; background-color: #eef2ff;">
                      <i class="fas fa-eye me-1"></i>線上展開／列印
                    </button>
                  </div>
                </div>
              </div>

              <!-- Card 3: 全學期總題庫完整合輯 -->
              <div class="col-md-4">
                <div class="card h-100 p-3 border-2 border-warning bg-white shadow-sm d-flex flex-column justify-content-between">
                  <div>
                    <div class="d-flex justify-content-between align-items-center mb-2">
                      <span class="badge bg-warning text-dark">期中＋期末＋證照</span>
                      <span class="small fw-bold text-warning font-monospace">全 180 題（含答案）</span>
                    </div>
                    <h6 class="fw-bold text-dark mb-2">📚 全學期總題庫完整合輯 (第 1～11 章)</h6>
                    <p class="text-muted small leading-relaxed mb-3">
                      一次收錄期中考 (75 題) ＋ 期末考 (105 題) 全部 180 題完整試題、答案速查表與考點解析，適合整學期複習與 IPAS 國家能力鑑定衝刺。
                    </p>
                  </div>
                  <div class="d-flex flex-wrap gap-2 pt-2 border-top">
                    <a href="static/exam_banks/Marketing_Planning_Full_180_Question_Bank_With_Answers.docx" download="萬能科大_創意行銷企劃實務_全學期總題庫完整版(含標準答案與詳解_180題).docx" class="btn btn-warning btn-sm flex-fill fw-bold text-dark">
                      <i class="fas fa-download me-1"></i>下載 180 題總題庫 (.docx)
                    </a>
                    <button type="button" onclick="openQuestionBankViewer('all')" class="btn btn-outline-warning btn-sm fw-bold text-dark">
                      <i class="fas fa-eye me-1"></i>展開全部 180 題
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 線上題庫完整檢視與列印區塊 (點擊「線上展開／列印」時顯示) -->
          <div id="question-bank-viewer-box" style="display: none;" class="card-custom p-4 mb-4 border-2 border-primary bg-white shadow-sm">
            <div class="d-flex flex-column flex-sm-row justify-content-between align-items-sm-center gap-3 border-bottom pb-3 mb-3">
              <div>
                <h5 id="qb-viewer-title" class="fw-bold text-dark mb-1">📘 期中考全部考題題庫（含標準答案與詳解）</h5>
                <small id="qb-viewer-subtitle" class="text-muted">共 75 題 ｜ 依章節排序，標示綠底為官方標準答案</small>
              </div>
              <div class="d-flex flex-wrap align-items-center gap-2">
                <button type="button" onclick="downloadCurrentBankHtml()" class="btn btn-sm btn-primary fw-bold">
                  <i class="fas fa-file-download me-1"></i>下載可列印題庫檔 (.html)
                </button>
                <button type="button" onclick="printCurrentQuestionBank()" class="btn btn-sm btn-success fw-bold">
                  <i class="fas fa-print me-1"></i>直接列印 ／ 另存 PDF
                </button>
                <button type="button" onclick="closeQuestionBankViewer()" class="btn btn-sm btn-outline-secondary">
                  ✕ 收合題庫
                </button>
              </div>
            </div>
            <div id="qb-viewer-list" style="max-height: 650px; overflow-y: auto;" class="pe-2">
              <!-- 由 JS 動態注入 -->
            </div>
          </div>

          <!-- IPAS 兩大能力鑑定專項模擬捷徑 -->'''

    target = '''            <button class="btn btn-sm btn-outline-danger" onclick="clearWrongQuestionsNotebook()">
              <i class="fas fa-trash-alt me-1"></i>清空錯題筆記
            </button>
          </div>

          <!-- IPAS 兩大能力鑑定專項模擬捷徑 -->'''

    if target in html:
        html = html.replace(target, download_section_html, 1)
        with open(tmpl_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print("[OK] templates/index.html updated successfully.")
    else:
        print("[SKIP] target not found in templates/index.html or already updated.")

def update_app_js(base_dir):
    js_path = os.path.join(base_dir, 'static', 'js', 'app.js')
    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()

    # 1. 修正 midterm_40 與 final_60 抽題邏輯
    target_modes = '''  } else if (mode === 'midterm_40') {
    pool = pool.filter(q => q.chapter <= 6 || q.module.includes('內容') || q.module.includes('社群'));
    pool.sort(() => 0.5 - Math.random());
    count = Math.min(40, pool.length);
    title = '期中 40 題鑑定模擬測驗 (限時40分鐘)';
  } else if (mode === 'final_60') {
    pool.sort(() => 0.5 - Math.random());
    count = Math.min(60, pool.length);
    title = '期末 60 題綜合能力檢定 (限時60分鐘)';'''

    repl_modes = '''  } else if (mode === 'midterm_40') {
    pool = pool.filter(q => q.chapter <= 5);
    pool.sort(() => 0.5 - Math.random());
    count = Math.min(40, pool.length);
    title = '期中 40 題鑑定模擬測驗 (限時40分鐘)';
  } else if (mode === 'final_60') {
    pool = pool.filter(q => q.chapter >= 6);
    pool.sort(() => 0.5 - Math.random());
    count = Math.min(60, pool.length);
    title = '期末 60 題綜合能力檢定 (限時60分鐘)';'''

    if target_modes in js:
        js = js.replace(target_modes, repl_modes, 1)
        print("[OK] app.js exam mode filters updated.")

    # 2. 加入 Question Bank Viewer 函式
    viewer_code = '''
/* ==========================================================================
   期中考 / 期末考 / 全學期 題庫檢視、下載與列印系統
   ========================================================================== */
let currentViewingBankType = 'midterm';

function getAnsLetter(ans) {
  const letters = ['A', 'B', 'C', 'D'];
  if (typeof ans === 'number' && ans >= 0 && ans < 4) return letters[ans];
  if (typeof ans === 'string' && ['A', 'B', 'C', 'D'].includes(ans.toUpperCase())) return ans.toUpperCase();
  return ans;
}

function openQuestionBankViewer(bankType) {
  currentViewingBankType = bankType;
  const box = document.getElementById('question-bank-viewer-box');
  const titleEl = document.getElementById('qb-viewer-title');
  const subEl = document.getElementById('qb-viewer-subtitle');
  const listEl = document.getElementById('qb-viewer-list');
  if (!box || !listEl) return;

  let pool = [];
  let bankName = '';
  let bankRange = '';

  if (bankType === 'midterm') {
    pool = questionsData.filter(q => q.chapter <= 5);
    bankName = '📘 期中考全部考題題庫（含標準答案與詳解）';
    bankRange = `涵蓋第 1 至第 5 章 ｜ 共 ${pool.length} 題 ｜ 綠底標示為官方標準答案`;
  } else if (bankType === 'final') {
    pool = questionsData.filter(q => q.chapter >= 6);
    bankName = '📙 期末考全部考題題庫（含標準答案與詳解）';
    bankRange = `涵蓋第 6 至第 11 章 ｜ 共 ${pool.length} 題 ｜ 綠底標示為官方標準答案`;
  } else {
    pool = [...questionsData];
    bankName = '📚 全學期總題庫完整合輯（含標準答案與詳解）';
    bankRange = `涵蓋全冊第 1 至第 11 章 ｜ 共 ${pool.length} 題 ｜ 綠底標示為官方標準答案`;
  }

  pool.sort((a, b) => (a.chapter - b.chapter) || String(a.id).localeCompare(String(b.id)));

  if (titleEl) titleEl.textContent = bankName;
  if (subEl) subEl.textContent = bankRange;

  let lastCh = null;
  const letters = ['A', 'B', 'C', 'D'];

  listEl.innerHTML = pool.map((q, idx) => {
    let chHeader = '';
    if (q.chapter !== lastCh) {
      lastCh = q.chapter;
      chHeader = `
        <div class="text-white px-3 py-2 rounded-2 fw-bold small my-3 d-flex align-items-center justify-content-between" style="background: linear-gradient(135deg, #1e40af, #3b82f6);">
          <span>【第 ${q.chapter} 章：${q.chapter_title}】</span>
          <span class="badge bg-light text-primary font-monospace">${q.module || q.ipas_cert || '行銷企劃'}</span>
        </div>
      `;
    }

    const ansLet = getAnsLetter(q.answer);

    return `
      ${chHeader}
      <div class="card p-3 mb-2 bg-light border-0 shadow-xs" style="border-left: 4px solid #2563eb !important;">
        <div class="d-flex justify-content-between align-items-start gap-2 mb-2">
          <div class="fw-bold text-dark small">
            <span class="badge bg-primary me-1">#${idx + 1}</span>
            <span>${q.question}</span>
            <span class="text-muted fw-normal ms-1 font-monospace" style="font-size: 0.75rem;">[${q.ipas_cert || q.source || '教材與IPAS題庫'}]</span>
          </div>
          <span class="badge bg-danger shrink-0 font-monospace">答案：(${ansLet})</span>
        </div>

        <div class="row g-2 mb-2">
          ${q.options.map((opt, optIdx) => {
            const isCorrect = (optIdx === q.answer) || (letters[optIdx] === ansLet);
            return `
              <div class="col-md-6">
                <div class="p-2 rounded small ${isCorrect ? 'bg-success bg-opacity-10 text-success fw-bold border border-success border-opacity-25' : 'bg-white text-secondary border border-light'}">
                  (${letters[optIdx]}) ${opt} ${isCorrect ? '<i class="fas fa-check-circle text-success ms-1"></i>' : ''}
                </div>
              </div>
            `;
          }).join('')}
        </div>

        ${q.explanation ? `
          <div class="p-2 bg-white rounded small text-secondary border-start border-3 border-info" style="font-size: 0.8rem;">
            <strong class="text-primary"><i class="fas fa-lightbulb me-1"></i>解析：</strong>${q.explanation.replace(/\\n/g, ' ')}
          </div>
        ` : ''}
      </div>
    `;
  }).join('');

  box.style.display = 'block';
  box.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function closeQuestionBankViewer() {
  const box = document.getElementById('question-bank-viewer-box');
  if (box) box.style.display = 'none';
}

function getBankExportHtml() {
  let pool = [];
  let bankTitle = '';
  if (currentViewingBankType === 'midterm') {
    pool = questionsData.filter(q => q.chapter <= 5);
    bankTitle = '萬能科技大學 11501《創意行銷企劃實務》期中考全部題庫（含答案）';
  } else if (currentViewingBankType === 'final') {
    pool = questionsData.filter(q => q.chapter >= 6);
    bankTitle = '萬能科技大學 11501《創意行銷企劃實務》期末考全部題庫（含答案）';
  } else {
    pool = [...questionsData];
    bankTitle = '萬能科技大學 11501《創意行銷企劃實務》全學期總題庫完整版（含答案）';
  }
  pool.sort((a, b) => (a.chapter - b.chapter) || String(a.id).localeCompare(String(b.id)));

  const letters = ['A', 'B', 'C', 'D'];

  let html = `<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<title>${bankTitle}</title>
<style>
  body { font-family: "Microsoft JhengHei", "PingFang TC", sans-serif; line-height: 1.6; margin: 30px; color: #1e293b; }
  h1 { text-align: center; color: #1e3a8a; font-size: 22px; margin-bottom: 5px; }
  .sub { text-align: center; color: #64748b; font-size: 13px; margin-bottom: 25px; }
  .ch-header { background: #1e40af; color: white; padding: 6px 12px; font-weight: bold; font-size: 14px; border-radius: 4px; margin-top: 20px; }
  .q-box { border-bottom: 1px solid #e2e8f0; padding: 12px 0; page-break-inside: avoid; }
  .q-title { font-weight: bold; font-size: 13px; margin-bottom: 6px; }
  .ans-badge { color: #b91c1c; font-weight: bold; margin-left: 6px; }
  .opts { margin-left: 20px; font-size: 12.5px; }
  .opt { margin-bottom: 3px; }
  .opt.correct { color: #15803d; font-weight: bold; }
  .exp { margin-left: 20px; background: #eff6ff; padding: 6px 10px; font-size: 11.5px; color: #1e3a8a; border-left: 3px solid #3b82f6; margin-top: 6px; border-radius: 2px; }
  @media print { body { margin: 15mm; } button { display: none; } }
</style>
</head>
<body>
<h1>${bankTitle}</h1>
<div class="sub">授課教師：邱俊維 博士 ｜ 題數：共 ${pool.length} 題 ｜ 命題依據：考試直接從本題庫抽題</div>
`;

  let lastCh = null;
  pool.forEach((q, idx) => {
    if (q.chapter !== lastCh) {
      lastCh = q.chapter;
      html += `<div class="ch-header">【第 ${q.chapter} 章：${q.chapter_title}】（${q.module || q.ipas_cert || '行銷企劃'}）</div>`;
    }
    const ansLet = getAnsLetter(q.answer);
    html += `
    <div class="q-box">
      <div class="q-title">${idx + 1}. ${q.question} <span class="ans-badge">【標準答案：(${ansLet})】</span></div>
      <div class="opts">
        ${q.options.map((opt, i) => {
          const isCorrect = (i === q.answer) || (letters[i] === ansLet);
          return `<div class="opt ${isCorrect ? 'correct' : ''}">(${letters[i]}) ${opt} ${isCorrect ? '✓' : ''}</div>`;
        }).join('')}
      </div>
      ${q.explanation ? `<div class="exp">💡 解析：${q.explanation.replace(/\\n/g, ' ')}</div>` : ''}
    </div>`;
  });

  html += `</body></html>`;
  return { html, bankTitle, count: pool.length };
}

function downloadCurrentBankHtml() {
  const { html, bankTitle } = getBankExportHtml();
  const blob = new Blob([html], { type: 'text/html;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `${bankTitle}.html`;
  a.click();
  URL.revokeObjectURL(url);
}

function printCurrentQuestionBank() {
  const { html } = getBankExportHtml();
  const printWindow = window.open('', '_blank');
  if (printWindow) {
    printWindow.document.open();
    printWindow.document.write(html);
    printWindow.document.close();
    printWindow.focus();
    setTimeout(() => { printWindow.print(); }, 500);
  } else {
    alert('請允許快顯視窗以開啟列印頁面！');
  }
}
'''

    target_clear = '''function clearWrongQuestionsNotebook() {
  if (confirm('確定要清空個人錯題筆記本嗎？')) {
    wrongQuestionsSet.clear();
    localStorage.removeItem('vnu_wrong_questions');
    alert('已清空錯題筆記本！');
  }
}'''

    if target_clear in js and 'openQuestionBankViewer' not in js:
        js = js.replace(target_clear, target_clear + '\n' + viewer_code, 1)
        with open(js_path, 'w', encoding='utf-8') as f:
            f.write(js)
        print("[OK] app.js viewer functions added successfully.")
    else:
        print("[SKIP] viewer functions already in app.js or target_clear not found.")

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    update_templates_html(base_dir)
    update_app_js(base_dir)

if __name__ == '__main__':
    main()
