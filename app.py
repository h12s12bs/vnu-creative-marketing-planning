# -*- coding: utf-8 -*-
"""
萬能科技大學 - 創意行銷企劃實務 ✕ Agentic AI 互動教學平台
授課教師：邱俊維 博士 (Dr. Chun-Wei Chiu)
開課班級：進企管四系3甲 ｜ 授課地點：F401 教室
"""
import os
import sys
import json
import socket
import random
from datetime import datetime
from flask import Flask, render_template, jsonify, request, send_from_directory

app = Flask(__name__, static_folder='static', template_folder='templates')

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
os.makedirs(UPLOAD_DIR, exist_ok=True)

def load_json_file(filename):
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_json_file(filename, data):
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_local_ip():
    """Get LAN IP address for classroom sharing"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 1))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return '127.0.0.1'

# In-memory session tracking for classroom live submissions
CLASSROOM_SUBMISSIONS = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/presentation')
@app.route('/Full_Screen_Presentation.html')
def presentation():
    """Launch full-screen 18-week projection presentation system"""
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(root_dir, 'Full_Screen_Presentation.html')

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    """Serve uploaded student project files"""
    return send_from_directory(UPLOAD_DIR, filename)

@app.route('/api/vibe_manual')
def get_vibe_manual():
    """Get Vibe Coding Guide and CLEAR Framework manual"""
    data = load_json_file('vibe_coding_guide.json')
    return jsonify(data)

@app.route('/api/system_info')
def system_info():
    local_ip = get_local_ip()
    port = 5000
    return jsonify({
        'status': 'online',
        'course': '萬能科技大學 - 創意行銷企劃實務 (11501)',
        'class_name': '進企管四系3甲',
        'classroom': 'F401 教室',
        'instructor': '邱俊維 博士',
        'server_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'local_ip': local_ip,
        'port': port,
        'classroom_url': f"http://{local_ip}:{port}",
        'dual_mode': {
            'in_class': '課堂實務演練 ✕ 互動工具即時體驗',
            'at_home': '課後 Agentic AI 企劃工作坊 ✕ 8 大 Agent 實戰'
        },
        'total_submissions': len(CLASSROOM_SUBMISSIONS)
    })

@app.route('/api/curriculum')
def get_curriculum():
    data = load_json_file('curriculum.json')
    return jsonify(data)

@app.route('/api/questions')
def get_questions():
    all_q = load_json_file('questions.json')
    
    week = request.args.get('week', type=int)
    chapter = request.args.get('chapter', type=int)
    module = request.args.get('module')
    cert = request.args.get('cert')
    count = request.args.get('count', type=int)
    shuffle = request.args.get('shuffle', default='true').lower() == 'true'
    exam_type = request.args.get('exam_type') # 'midterm_40', 'final_60', 'weekly_5', 'ipas_brand', 'ipas_ai', 'all'

    filtered = all_q
    if week:
        filtered = [q for q in filtered if week in q.get('weeks', [])]
    elif chapter:
        filtered = [q for q in filtered if q.get('chapter') == chapter]
    elif module:
        filtered = [q for q in filtered if q.get('module') == module]
    elif cert:
        filtered = [q for q in filtered if q.get('ipas_cert') == cert]
    elif exam_type == 'midterm_40':
        # Part 1 chapters CH01 ~ CH06 + AI fundamentals
        filtered = [q for q in filtered if q.get('chapter', 1) <= 6 or '內容' in q.get('module', '') or '社群' in q.get('module', '')]
        count = 40
    elif exam_type == 'final_60':
        # Full bank comprehensive test
        count = 60
    elif exam_type == 'ipas_brand':
        filtered = [q for q in filtered if q.get('ipas_cert') == 'IPAS 品牌規劃師']
        count = 25
    elif exam_type == 'ipas_ai':
        filtered = [q for q in filtered if q.get('ipas_cert') == 'IPAS AI 應用規劃師']
        count = 25
    elif exam_type == 'weekly_5':
        count = 5

    if shuffle:
        filtered = list(filtered)
        random.shuffle(filtered)

    if count and count > 0:
        filtered = filtered[:count]

    return jsonify({
        'total_matched': len(filtered),
        'questions': filtered
    })

@app.route('/api/agent_templates')
def get_agent_templates():
    data = load_json_file('agent_templates.json')
    return jsonify(data)

@app.route('/api/student_works', methods=['GET'])
def get_student_works():
    """Retrieve submitted student works and showcase examples"""
    student_id = request.args.get('student_id', '').strip()
    category = request.args.get('category', '').strip()
    week = request.args.get('week', type=int)

    sample_works = load_json_file('sample_works.json') or []
    user_works = load_json_file('submitted_works.json') or []
    all_works = list(user_works) + list(sample_works)

    if student_id:
        all_works = [w for w in all_works if str(w.get('student_id', '')).strip() == student_id]
    if category:
        all_works = [w for w in all_works if w.get('category') == category]
    if week:
        all_works = [w for w in all_works if w.get('week') == week]

    return jsonify(all_works)

@app.route('/api/upload_work', methods=['POST'])
def upload_work():
    """Allow students to submit projects, GitHub Pages links, HTML prototypes, prompts, and notes"""
    try:
        # Check if multipart form data or json
        if request.content_type and 'multipart/form-data' in request.content_type:
            student_id = request.form.get('student_id', '11109000').strip()
            student_name = request.form.get('student_name', '進企管同學').strip()
            team_name = request.form.get('team_name', '個人獨立企劃').strip()
            week = int(request.form.get('week', 16))
            week_title = request.form.get('week_title', f'第 {week:02d} 週企劃成果')
            title = request.form.get('title', '行銷企劃與 Vibe Coding 實踐專案').strip()
            category = request.form.get('category', 'GitHub Pages 線上專案').strip()
            concept = request.form.get('concept', '').strip()
            agent_used = request.form.get('agent_used', 'Agent 1：市場情資洞察 Agent').strip()
            prompt_summary = request.form.get('prompt_summary', '').strip()
            github_page_url = request.form.get('github_page_url', '').strip()
            github_repo_url = request.form.get('github_repo_url', '').strip()
            live_url = request.form.get('live_url', github_page_url).strip()
            
            file_name = ''
            file_url = ''
            if 'file' in request.files:
                uploaded_f = request.files['file']
                if uploaded_f and uploaded_f.filename:
                    orig_name = uploaded_f.filename.replace(' ', '_')
                    timestamp_prefix = datetime.now().strftime('%Y%m%d_%H%M%S_')
                    safe_filename = f"{student_id}_{timestamp_prefix}{orig_name}"
                    save_path = os.path.join(UPLOAD_DIR, safe_filename)
                    uploaded_f.save(save_path)
                    file_name = orig_name
                    file_url = f"/uploads/{safe_filename}"
        else:
            data = request.get_json() or {}
            student_id = data.get('student_id', '11109000').strip()
            student_name = data.get('student_name', '進企管同學').strip()
            team_name = data.get('team_name', '個人獨立企劃').strip()
            week = int(data.get('week', 16))
            week_title = data.get('week_title', f'第 {week:02d} 週企劃成果')
            title = data.get('title', '行銷企劃與 Vibe Coding 實踐專案').strip()
            category = data.get('category', 'GitHub Pages 線上專案').strip()
            concept = data.get('concept', '').strip()
            agent_used = data.get('agent_used', 'Agent 1：市場情資洞察 Agent').strip()
            prompt_summary = data.get('prompt_summary', '').strip()
            github_page_url = data.get('github_page_url', '').strip()
            github_repo_url = data.get('github_repo_url', '').strip()
            live_url = data.get('live_url', github_page_url).strip()
            file_name = data.get('file_name', '')
            file_url = data.get('file_url', '')

        work_id = f"WORK-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(100, 999)}"
        new_record = {
            'id': work_id,
            'student_id': student_id,
            'student_name': student_name,
            'author': f"進企管四系3甲 {student_name} (學號 {student_id})",
            'team_name': team_name or '個人獨立企劃',
            'group_num': int(''.join(filter(str.isdigit, team_name)) or '1'),
            'week': week,
            'week_title': week_title,
            'title': title,
            'category': category,
            'concept': concept,
            'agent_used': agent_used,
            'prompt_summary': prompt_summary,
            'github_page_url': github_page_url or live_url,
            'github_repo_url': github_repo_url,
            'live_url': live_url or github_page_url,
            'file_name': file_name,
            'file_url': file_url,
            'submitted_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'score': '92 分 (已登記)',
            'teacher_comment': '已成功繳交！曾光華企劃架構完整，GitHub Pages 線上預覽正常！'
        }

        existing_works = load_json_file('submitted_works.json') or []
        existing_works.insert(0, new_record)
        save_json_file('submitted_works.json', existing_works)

        return jsonify({
            'success': True,
            'message': '🎉 企劃作品上傳成功！已登記於個人歷程與作品成果展示廊。',
            'work': new_record
        })
    except Exception as e:
        return jsonify({'error': f'作品上傳失敗: {str(e)}'}), 500

@app.route('/api/submit_quiz', methods=['POST'])
def submit_quiz():
    """Score quiz submissions and provide detailed diagnostic feedback"""
    payload = request.get_json() or {}
    student_id = payload.get('student_id', '匿名學生')
    student_name = payload.get('student_name', '同學')
    answers = payload.get('answers', {}) # {question_id: selected_option_int}
    exam_mode = payload.get('exam_mode', '自主測驗')

    all_q_map = {q['id']: q for q in load_json_file('questions.json')}
    
    total = len(answers)
    if total == 0:
        return jsonify({'error': '未提供任何作答'}), 400

    correct_count = 0
    wrong_questions = []
    module_stats = {} # {module_name: {'correct': 0, 'total': 0}}

    for qid, user_ans in answers.items():
        q_obj = all_q_map.get(qid)
        if not q_obj:
            continue
        
        mod = q_obj.get('module', '綜合企劃觀念')
        if mod not in module_stats:
            module_stats[mod] = {'correct': 0, 'total': 0}
        module_stats[mod]['total'] += 1

        is_correct = (int(user_ans) == int(q_obj['answer']))
        if is_correct:
            correct_count += 1
            module_stats[mod]['correct'] += 1
        else:
            wrong_questions.append({
                'id': qid,
                'chapter_title': q_obj.get('chapter_title'),
                'module': mod,
                'ipas_cert': q_obj.get('ipas_cert', 'IPAS 品牌規劃師'),
                'ipas_subject': q_obj.get('ipas_subject', '品牌規劃與策略'),
                'question': q_obj.get('question'),
                'options': q_obj.get('options'),
                'user_answer': int(user_ans),
                'correct_answer': q_obj.get('answer'),
                'explanation': q_obj.get('explanation')
            })

    score = round((correct_count / total) * 100, 1)
    passed = score >= 70

    # Diagnostic feedback message
    if score >= 90:
        feedback = '太優秀了！行銷企劃觀念與 MarTech 知識非常紮實，具備專業行銷總監實力！'
    elif score >= 70:
        feedback = '恭喜達標！已具備行銷企劃核心素養，多加複習錯題將更加精熟！'
    else:
        feedback = '請繼續加油！建議檢視下方錯題筆記，釐清易混淆觀念與相關章節。'

    record = {
        'student_id': student_id,
        'student_name': student_name,
        'score': score,
        'passed': passed,
        'total': total,
        'correct_count': correct_count,
        'exam_mode': exam_mode,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    CLASSROOM_SUBMISSIONS.append(record)

    return jsonify({
        'score': score,
        'passed': passed,
        'correct_count': correct_count,
        'total_questions': total,
        'feedback': feedback,
        'module_radar': module_stats,
        'wrong_questions': wrong_questions
    })

@app.route('/api/random_cards')
def get_random_cards():
    """Classroom live ice-breaker: Random combination of Target + Pain + Tech + Scene"""
    targets = [
        '每天加班到 9 點的科技業工程師', '追求極致自律的 28 歲瑜伽愛好者', '預算有限但重視天然的雙薪新手爸媽', 
        '喜愛拍照打卡發 IG Reels 的大學生', '白天上班、晚上讀進修部的大學三年級同學', '退休後追求活力人生的 60 歲樂齡族群'
    ]
    pains = [
        '下午 3 點精神極度崩潰但不敢吃高糖手搖飲', '想買高品質伴手禮送長輩，但怕包裝俗氣或太甜太油', 
        '週末想去戶外露營放鬆，但裝備繁重且不知道怎麼準備食材', '下班回到家已經累癱，想要 10 分鐘吃到米其林等級熱騰騰料理',
        '買過很多保健品但常常忘記吃，最後整罐過期丟掉', '想支持台灣在地小農，但不知道哪裡買最安全又有保障'
    ]
    techs = [
        'LINE 官方帳號 + AI 對話式自動點餐推薦', '包裝內嵌 NFC 晶片，手機感應即可看產地溯源與虛擬籤詩',
        '社群短影音 30 秒挑戰 ✕ 步數折抵現金機制', '結合外送平台 30 分鐘急速冷鏈直達辦公桌',
        '個人化 AI 體態測驗，推薦專屬低卡高纖配方', '限時深夜快閃線上盲盒，每晚 9 點搶購'
    ]
    scenes = [
        '週三小週末辦公室下午茶集體療癒時光', '跨年連假親友到家聚會派對開箱',
        '週日早晨晨跑完犒賞自己的第一餐', '情人節前夕不知道送什麼的緊急救火禮物',
        '母親節感謝全家人聚餐的壓軸亮點', '公司尾牙抽獎最想拿到的驚喜大獎'
    ]
    
    return jsonify({
        'target': random.choice(targets),
        'pain': random.choice(pains),
        'tech': random.choice(techs),
        'scene': random.choice(scenes),
        'generated_at': datetime.now().strftime('%H:%M:%S')
    })

if __name__ == '__main__':
    local_ip = get_local_ip()
    port = 5000
    print("=" * 70)
    print(" 萬能科技大學【創意行銷企劃實務 ✕ Agentic AI】教學平台已啟動！")
    print(f" 授課教師：邱俊維 博士 ｜ 開課班級：進企管四系3甲")
    print(f" 授課地點：F401 教室")
    print("-" * 70)
    print(f" 本機網址： http://localhost:{port}")
    print(f" 區域網路連線網址： http://{local_ip}:{port}")
    print("=" * 70)
    app.run(host='0.0.0.0', port=port, debug=False)
