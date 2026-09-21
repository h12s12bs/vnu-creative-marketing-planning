# -*- coding: utf-8 -*-
"""
萬能科技大學 11501 創意行銷企劃實務 - 51 頁全景投影片生成引擎 (tools/slide_engine.py)
負責將每一週的週次配置，精準生成 51 張高畫質、符合 28 號字排版、零溢出的投影片
嚴格緊扣：曾光華《行銷企劃：邏輯、創意、執行力》(2026 第五版) CH01 ~ CH10
融入：Agentic AI 智慧代理人 ✕ Vibe Coding 操作手冊 ✕ 經濟部 IPAS 品牌企劃師證照模擬試題
"""
import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
TOOLS_DIR = os.path.join(BASE_DIR, 'tools')
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

from ipas_mock_exams import IPAS_EXAMS
from week_pedagogy import WEEK_PEDAGOGY

with open(os.path.join(DATA_DIR, 'chapter_slides.json'), 'r', encoding='utf-8') as f:
    CHAPTER_SLIDES = json.load(f)

with open(os.path.join(DATA_DIR, 'agent_slides.json'), 'r', encoding='utf-8') as f:
    AGENT_SLIDES = json.load(f)

with open(os.path.join(DATA_DIR, 'vibe_slides.json'), 'r', encoding='utf-8') as f:
    VIBE_SLIDES = json.load(f)

def split_text(text, max_len=36):
    """Splits a long text cleanly into 2 parts around punctuation if possible."""
    if not text:
        return "", ""
    if len(text) <= max_len:
        return text, ""
    puncs = ['，', '。', '；', '、', '：', '？', '！', ' ']
    best_idx = -1
    target = len(text) // 2
    for p in puncs:
        idx = text.find(p, int(target * 0.65), int(target * 1.35))
        if idx != -1:
            best_idx = idx + 1
            break
    if best_idx == -1:
        best_idx = max_len
    return text[:best_idx].strip(), text[best_idx:].strip()

def build_week_slides(wc):
    week_num = wc['week']
    if week_num == 2:
        from week02_master_slides import get_week02_slides
        return get_week02_slides(wc)

    mod = wc['module']
    title = wc['title']
    sub = wc['subtitle']
    chap = wc['chapter']
    agent = wc['agent']
    vibe = wc['vibe']
    ipas = wc['ipas']
    concept = wc['core_concept']
    case = wc['case_name']
    pitfall = wc['pitfall']
    scamper = wc['scamper_q']

    slides = []

    # =============================================================
    # P.01: 單元封面 (cover)
    # =============================================================
    slides.append({
        'layout': 'cover',
        'badge': f'萬能科技大學 企業管理系 ｜ 11501 專業實務核心課程 ｜ {mod}',
        'title': f'第 {week_num:02d} 週：{title}',
        'subtitle': f'{sub}',
        'meta': [
            '開課班級：進企管四系3甲 (週一 10~11 節 16:20~17:50)',
            '授課地點：F401 教室',
            '授課教師：邱俊維 博士 (jimchiu@mail.vnu.edu.tw)',
            f'參考教材：{chap}'
        ]
    })

    # =============================================================
    # P.02: 教師介紹 (僅第 1 週) 或 本週學習目標 (第 2~18 週)
    # =============================================================
    if week_num == 1:
        slides.append({
            'layout': '2card',
            'badge': 'FACULTY PROFILE',
            'sec': '授課教師介紹',
            'title': '授課教師介紹：邱俊維 博士 / 專案助理教授',
            'subtitle': '長庚大學管理學博士 ｜ 決策科學與 AI 跨域應用 ｜ 育英樓 J801-1 研究室',
            'left': {
                'title': '學術背景與核心專長',
                'theme': 'blue',
                'points': [
                    '學歷：長庚大學管理學博士 (主修決策科學)',
                    '專長：多準則決策分析 (MCDM)、MarTech',
                    '研究：Agentic AI 智慧行銷工作流架構',
                    '著作：發表多篇國際 SCI 頂尖期刊論文'
                ]
            },
            'right': {
                'title': '實務歷練與聯絡方式',
                'theme': 'teal',
                'points': [
                    '經歷：生醫研發特助、企業數位轉型顧問',
                    '研究室：萬能科大 育英樓 (J棟) J801-1',
                    '信箱：jimchiu@mail.vnu.edu.tw',
                    '諮詢：週一 15:00~16:00、週四 14:00~16:00'
                ]
            }
        })
    elif week_num == 9:
        slides.append({
            'layout': '2card',
            'badge': 'MIDTERM OBJECTIVES',
            'sec': '期中評量目標',
            'title': '第 09 週期中考試學習成效檢定目標',
            'subtitle': '曾光華 CH01~CH05 前半學期精華考點盤點 ✕ 實務情境答辯 ✕ 核心素養驗收',
            'left': {
                'title': '期中學理與觀念考評指標',
                'theme': 'blue',
                'points': [
                    '熟練掌握：CH01~CH05 核心理論骨架',
                    '名詞辨析：企劃與計畫、冰山理論、VRIO護城河',
                    '矩陣推導：波特五力、PESTC、TOWS 交叉攻防',
                    '計分權重：期中考試成績佔學期總成績 40%'
                ]
            },
            'right': {
                'title': '實務案例題解與應考規範',
                'theme': 'teal',
                'points': [
                    '商業個案：四步驟情境拆解與破題推導',
                    '避開失分：審題圈出關鍵字、拒絕死背名詞',
                    '作答紀律：手機收起放包包、獨立作答',
                    '評量標準：觀念選擇題 60 分 ✕ 案例推導題 40 分'
                ]
            }
        })
    elif week_num == 18:
        slides.append({
            'layout': '2card',
            'badge': 'FINAL OBJECTIVES',
            'sec': '期末評量目標',
            'title': '第 18 週期末考試與學期總結算目標',
            'subtitle': '全書 CH01~CH10 精華大貫通 ✕ 綜合實務大題型解構 ✕ 學期成績總核算',
            'left': {
                'title': '期末學理大貫通考評指標',
                'theme': 'blue',
                'points': [
                    '全書貫通：CH01~CH10 十步標準企劃程序',
                    '整合策略：新產品上市、公關危機、促銷ROI、OMO',
                    '最高思維：企劃是高度不確定下的價值創造擔當',
                    '計分權重：期末考試成績佔學期總成績 40%'
                ]
            },
            'right': {
                'title': '學期總結算與及格確認',
                'theme': 'teal',
                'points': [
                    '計分結構：期中考 40% ✕ 期末考 40% ✕ 出席 20%',
                    '出席保障：不搞繁複算式，出席 20% 清清楚楚',
                    '及格門檻：學期總成績達 60 分即獲取專業學分',
                    '成績公告：考後一週內登錄校務系統開放複查'
                ]
            }
        })
    else:
        slides.append({
            'layout': '2card',
            'badge': 'LEARNING OBJECTIVES',
            'sec': '本週學習目標',
            'title': f'第 {week_num:02d} 週學習目標與企劃能力地圖',
            'subtitle': f'曾光華學理權威剖析 ✕ Agentic AI 協同思維 ✕ 期中期末應試核心',
            'left': {
                'title': '學理與企劃核心能力',
                'theme': 'blue',
                'points': [
                    f'深入掌握：{chap} 核心邏輯與名詞定義',
                    f'學會應用：{concept} 決策模型',
                    f'避開盲點：{pitfall} 決策誤區',
                    '掌握重點：期中期末考試核心命題考點'
                ]
            },
            'right': {
                'title': 'AI 協同與數位原型概念',
                'theme': 'teal',
                'points': [
                    f'了解架構：{agent} 運作邏輯',
                    '掌握方法：CLEAR 結構化商務提示詞',
                    f'觀摩原型：{vibe} 商業應用價值',
                    f'對標鑑定：{ipas} 證照命題要領'
                ]
            }
        })

    # =============================================================
    # P.03: 實務痛點破冰 (2card)
    # =============================================================
    if week_num == 1:
        slides.append({
            'layout': '2card',
            'badge': 'REAL-WORLD PAIN POINT',
            'sec': '實務痛點破冰',
            'title': '行銷實務痛點破冰：真實市場情境挑戰',
            'subtitle': '為什麼許多看似完美的企劃案在實際推向市場時慘遭滑鐵盧？關鍵盲點剖析',
            'left': {
                'title': '職場企劃常見四大致命困境',
                'theme': 'rose',
                'points': [
                    '困境一：痛點不明，自嗨式提案無人買單',
                    '困境二：缺乏邏輯，策略與目標前後矛盾',
                    '困境三：無數據支撐，全憑個人主觀猜測',
                    '困境四：執行落地困難，預算時程難控管'
                ]
            },
            'right': {
                'title': '本週企劃破局策略與思維',
                'theme': 'teal',
                'points': [
                    '突破一：以曾光華學理建構扎實推導骨架',
                    f'突破二：以 {agent} 擴展情資視野',
                    f'突破三：以 Vibe Coding 打造 {vibe} 原型',
                    '突破四：以客觀數據與清晰 KPI 說服決策層'
                ]
            }
        })
    else:
        ped = WEEK_PEDAGOGY.get(week_num, {})
        slides.append({
            'layout': '2card',
            'badge': 'REAL-WORLD PAIN POINT',
            'sec': '實務痛點破冰',
            'title': f'行銷實務痛點破冰：{title}',
            'subtitle': f'深入診斷職場實務盲點 ✕ 曾光華學理破解 ✕ 避開{pitfall}',
            'left': ped.get('pain_left', {
                'title': '職場企劃常見四大致命困境',
                'theme': 'rose',
                'points': [
                    f'盲點一：{pitfall}',
                    '盲點二：缺乏數據支撐，全憑個人主觀猜測',
                    '盲點三：未做深入診斷，策略與目標前後矛盾',
                    '盲點四：執行落地困難，預算時程缺乏控管'
                ]
            }),
            'right': ped.get('pain_right', {
                'title': '本週企劃破局策略與思維',
                'theme': 'teal',
                'points': [
                    f'突破一：落實 {concept} 核心方法論',
                    f'突破二：以 {agent} 輔助情資與策略推導',
                    f'突破三：借鏡 {case} 成功商業運作實務',
                    '突破四：以客觀數據與清晰 KPI 說服決策層'
                ]
            })
        })

    # =============================================================
    # P.04: 曾光華教科書學理定位 (2card)
    # =============================================================
    if week_num == 1:
        slides.append({
            'layout': '2card',
            'badge': 'TEXTBOOK CONTEXT',
            'sec': '學理定位與脈絡',
            'title': f'曾光華教科書學理定位：{chap}',
            'subtitle': f'深入理解本章節在行銷企劃全案體系中的戰略地位與推導邏輯',
            'left': {
                'title': '章節在企劃全案中之戰略角色',
                'theme': 'blue',
                'points': [
                    f'全案定位階段：{mod}',
                    f'理論核心基石：{concept}',
                    '前承上週進度，後啟下週執行規劃',
                    '建構進修部同學職場專業企劃素養'
                ]
            },
            'right': {
                'title': '本章必備之核心企劃能力',
                'theme': 'amber',
                'points': [
                    '能力一：結構化拆解複雜商業問題',
                    '能力二：精準判讀市場與競品動態信號',
                    '能力三：設計符合商業閉環的行銷策略',
                    '能力四：將策略具體轉化為可執行方案'
                ]
            }
        })
    else:
        ped = WEEK_PEDAGOGY.get(week_num, {})
        slides.append({
            'layout': '2card',
            'badge': 'TEXTBOOK CONTEXT',
            'sec': '學理定位與脈絡',
            'title': f'曾光華教科書學理定位：{chap}',
            'subtitle': '深入掌握本單元在企劃全案體系之戰略角色與核心推導能力',
            'left': ped.get('textbook_left', {
                'title': '章節在企劃全案中之戰略角色',
                'theme': 'blue',
                'points': [
                    f'全案定位階段：{mod}',
                    f'理論核心基石：{concept}',
                    '前承上週進度，後啟下週執行規劃',
                    '建構進修部同學職場專業企劃素養'
                ]
            }),
            'right': ped.get('textbook_right', {
                'title': '本單元必備核心企劃能力',
                'theme': 'amber',
                'points': [
                    '能力一：結構化拆解複雜商業問題',
                    '能力二：精準判讀市場與競品動態信號',
                    '能力三：設計符合商業閉環的行銷策略',
                    '能力四：將策略具體轉化為可執行方案'
                ]
            })
        })

    # =============================================================
    # P.05: 三維學習模型 (3card)
    # =============================================================
    if week_num == 9:
        slides.append({
            'layout': '3card',
            'badge': 'MIDTERM EVALUATION MODEL',
            'sec': '期中評量維度',
            'title': '期中考試三大評量構面：觀念 ✕ 案例 ✕ 實務',
            'subtitle': '全面檢驗前半學期核心企劃素養，建立客觀量化評核機制',
            'cards': [
                {
                    'title': '1. 核心學理觀念 (40%)',
                    'theme': 'blue',
                    'points': [
                        'CH01~05 名詞定義與邏輯架構',
                        '企劃本質、十步程序不可逆性',
                        'SMART 目標檢定與冰山診斷',
                        '次級資料三等級可信度查核標準'
                    ]
                },
                {
                    'title': '2. 實務情境推導 (40%)',
                    'theme': 'teal',
                    'points': [
                        '真實商業情境案例深度診斷',
                        '波特五力與競品優劣矩陣推導',
                        'VRIO 核心能力護城河檢驗',
                        'TOWS 交叉攻防戰略對策擬定'
                    ]
                },
                {
                    'title': '3. 企劃實務執行 (20%)',
                    'theme': 'amber',
                    'points': [
                        'SCAMPER 創意奔馳具體落地應用',
                        '痛點與目標前後邏輯嚴密咬合',
                        '方案具備商業變現與可行性閉環',
                        '答案卷書寫工整層次結構分明'
                    ]
                }
            ]
        })
    elif week_num == 18:
        slides.append({
            'layout': '3card',
            'badge': 'SEMESTER GRADING SYSTEM',
            'sec': '成績計分結構',
            'title': '學期成績三大核算維度：期中 40% ✕ 期末 40% ✕ 出席 20%',
            'subtitle': '簡明清晰、杜絕繁複算式，保障認真投入同學權益與及格確認',
            'cards': [
                {
                    'title': '1. 期中考試成績 (40%)',
                    'theme': 'blue',
                    'points': [
                        '第 09 週期中考試卷面成績',
                        '考查 CH01~CH05 前半學期精華',
                        '客觀量化計分，直接計入總分 40%',
                        '缺考或未及格依學校補考程序辦理'
                    ]
                },
                {
                    'title': '2. 期末考試成績 (40%)',
                    'theme': 'teal',
                    'points': [
                        '第 18 週期末考試卷面成績',
                        '考查全書 CH01~CH10 綜合全案題型',
                        '客觀量化計分，直接計入總分 40%',
                        '展現全學期整合企劃實務終極能力'
                    ]
                },
                {
                    'title': '3. 平時出席成績 (20%)',
                    'theme': 'amber',
                    'points': [
                        '每週 F401 課堂點名出席紀錄',
                        '比率適度設定 20%（考量進修部出勤）',
                        '準時出席參與研討即穩拿基本分',
                        '總成績達 60 分即獲本專業學分'
                    ]
                }
            ]
        })
    else:
        slides.append({
            'layout': '3card',
            'badge': 'THREE-PILLAR MODEL',
            'sec': '三維學習模型',
            'title': '三維學習閉環：學理 ✕ 智能體 ✕ 數位原型',
            'subtitle': '從邏輯思維、創意突破到成果落地，打造無可取代的行銷企劃競爭力',
            'cards': [
                {
                    'title': '1. 曾光華權威學理',
                    'theme': 'blue',
                    'points': [
                        f'深入理解 {chap} 核心哲學',
                        '深耕「邏輯思維、創意突破、執行控制」',
                        '掌握專業行銷企劃書標準結構法規',
                        '打下進修部同學終身受用的分析底子'
                    ]
                },
                {
                    'title': '2. Agentic AI 智能體',
                    'theme': 'teal',
                    'points': [
                        f'觀摩理解：{agent}',
                        '掌握 ReAct 循環 (思考/行動/觀察/決策)',
                        '以 CLEAR 框架引導 AI 深度分析',
                        '從手動文案搬運工躍升為戰略指揮官'
                    ]
                },
                {
                    'title': '3. 數位原型與教授示範',
                    'theme': 'amber',
                    'points': [
                        '企管行銷視角理解數位原型邏輯',
                        f'教授現場展示主題互動原型：{vibe}',
                        '了解數位工具如何加速企劃視覺化呈現',
                        '銜接期中期末考試對於數位行銷工具之理解'
                    ]
                }
            ]
        })

    # =============================================================
    # Section 2: 曾光華《行銷企劃》經典學理深度拆解 (P.06 ~ P.23, 18 slides)
    # =============================================================
    slides.extend(CHAPTER_SLIDES.get(str(week_num), []))

    # =============================================================
    # Section 3: Agentic AI 智慧代理人協同實戰 (P.24 ~ P.35, 12 slides)
    # =============================================================
    slides.extend(AGENT_SLIDES.get(str(week_num), []))

    # =============================================================
    # Section 4: Vibe Coding 操作手冊與數位原型開發 (P.36 ~ P.43, 8 slides)
    # =============================================================
    slides.extend(VIBE_SLIDES.get(str(week_num), []))

    # =============================================================
    # Section 5: 課堂個人獨立實作演練 ✕ IPAS 證照題庫解析 (P.44 ~ P.48, 5 slides)
    # =============================================================
    if week_num == 9:
        # P.44
        slides.append({
            'layout': '2card',
            'badge': 'MIDTERM INSTRUCTION',
            'sec': '應考規範指引',
            'title': '期中考試現場作答規範與時間分配指引',
            'subtitle': '嚴格遵守考場紀律，發揮專業企劃實力，爭取期中高分佳績',
            'left': {
                'title': '考試時間與配分規劃',
                'theme': 'blue',
                'points': [
                    '考試時間：共 80 分鐘 (16:20~17:40)',
                    '第一部分：單元觀念選擇題 (30題/60分/限30分)',
                    '第二部分：商業個案情境推導題 (2大題/40分/限50分)',
                    '交卷時間：開考 40 分鐘後始得交卷'
                ]
            },
            'right': {
                'title': '考場紀律與作答規範',
                'theme': 'amber',
                'points': [
                    '紀律第一：手機一律關機或靜音收進包包',
                    '獨立作答：嚴禁交頭接耳或窺視他人答案',
                    '作答工具：黑色或藍色原子筆，字跡保持工整',
                    '誠信原則：作弊者該科零分並送校規議處'
                ]
            }
        })
        # P.45
        slides.append({
            'layout': '2card',
            'badge': 'CASE SOLVING METHOD',
            'sec': '案例破題心法',
            'title': '期中考實務案例題作答邏輯（四步破題法）',
            'subtitle': '結構化拆解商業個案，展現邏輯推導深度，直擊評審給分點',
            'left': {
                'title': '案例破題四大標準步驟',
                'theme': 'teal',
                'points': [
                    '步驟一：審題圈出企業核心病徵與痛點 (冰山水下)',
                    '步驟二：援引曾光華對應學理模型（如五力/VRIO/TOWS）',
                    '步驟三：結合題幹數據與情境進行因果推導分析',
                    '步驟四：提出具備商業可行性之具體解決方案'
                ]
            },
            'right': {
                'title': '得高分關鍵答題技巧',
                'theme': 'blue',
                'points': [
                    '條理分明：善用編號 (一、1、(1)) 條列回答',
                    '學理名詞：精確寫出專有名詞，切忌通篇口語化',
                    '拒絕空話：方案必須有預期效益與目標對照',
                    '時間控管：切勿在單一小題過度卡關耽誤全卷'
                ]
            }
        })
        # P.46
        slides.append({
            'layout': '3card',
            'badge': 'EXAM ADMINISTRATION',
            'sec': '試務與成績說明',
            'title': '期中考卷繳交與成績登錄說明',
            'subtitle': '完卷收件流程、閱卷標準與學期成績登錄期程說明',
            'cards': [
                {
                    'title': '1. 完卷檢查與繳交',
                    'theme': 'blue',
                    'points': [
                        '檢查座號、姓名是否填寫完整無誤',
                        '確認答題卷無遺漏頁面與作答題號',
                        '交卷時依座號順序整齊置於講桌',
                        '交卷後請安靜離場，勿在走廊喧嘩'
                    ]
                },
                {
                    'title': '2. 閱卷與核分標準',
                    'theme': 'teal',
                    'points': [
                        '選擇題依標準答案電腦/手動精確讀卡',
                        '案例題採評分尺規 (Rubric) 客觀給分',
                        '針對推導邏輯合理性給予部分給分',
                        '成績複查將提供評分要點對照'
                    ]
                },
                {
                    'title': '3. 成績公告與登錄',
                    'theme': 'amber',
                    'points': [
                        '考後一週內完成閱卷與校務系統登錄',
                        '期中考佔學期總成績 40% 正式採計',
                        '下週課堂發還考卷並進行試題深度檢討',
                        '提供未達標準同學加強輔導機制'
                    ]
                }
            ]
        })
    elif week_num == 18:
        # P.44
        slides.append({
            'layout': '2card',
            'badge': 'FINAL INSTRUCTION',
            'sec': '期末應考規範',
            'title': '期末考試現場作答規範與時間配比說明',
            'subtitle': '全書 CH01~CH10 綜合全案題型驗收，展現一學期專業企劃真本領',
            'left': {
                'title': '考試時間與配分規劃',
                'theme': 'blue',
                'points': [
                    '考試時間：共 80 分鐘 (16:20~17:40)',
                    '第一部分：全書綜合觀念選擇題 (25題/50分)',
                    '第二部分：綜合企劃全案情境題 (2大題/50分)',
                    '交卷時間：開考 40 分鐘後始得交卷'
                ]
            },
            'right': {
                'title': '考場紀律與誠信守則',
                'theme': 'amber',
                'points': [
                    '紀律第一：手機務必關機放入書包中',
                    '嚴禁作弊：各憑真本事獨立作答',
                    '書寫清晰：企劃邏輯圖請用原子筆工整繪製',
                    '時間分配：選擇題限 25 分，個案題留足 55 分'
                ]
            }
        })
        # P.45
        slides.append({
            'layout': '2card',
            'badge': 'CASE SYNTHESIS METHOD',
            'sec': '全案破題心法',
            'title': '期末綜合個案題作答邏輯（十步流程診斷）',
            'subtitle': '融會貫通曾光華十步標準程序，從問題診斷至執行控制展現商業閉環',
            'left': {
                'title': '全案題型診斷四部曲',
                'theme': 'teal',
                'points': [
                    '診斷部：界定本質痛點與外部環境威脅 (PESTC/五力)',
                    '定位部：提出精準 STP 與無可取代之價值主張',
                    '方案部：整合 4P/新產品上市/公關事件/促銷策略',
                    '效益部：計算 BEP 損益平衡與可衡量 SMART 指標'
                ]
            },
            'right': {
                'title': '閱卷給分四大關鍵維度',
                'theme': 'blue',
                'points': [
                    '邏輯咬合：前後章節是否前後呼應、拒絕兩張皮',
                    '商業閉環：方案是否真能賺錢並控制財務風險',
                    '學理落地：靈活運用曾光華全書核心模型工具',
                    '專業素養：展現進修部同學成熟穩健之職場思維'
                ]
            }
        })
        # P.46
        slides.append({
            'layout': '3card',
            'badge': 'FINAL ADMINISTRATION',
            'sec': '成績結算說明',
            'title': '學期總成績核算結算與及格確認指引',
            'subtitle': '期中 40% ✕ 期末 40% ✕ 出席 20%，結算公告與學分取得程序',
            'cards': [
                {
                    'title': '1. 試卷收繳與封存',
                    'theme': 'blue',
                    'points': [
                        '完卷後依座號整齊點收封存備查',
                        '確保每位同學作答卷皆完整收齊',
                        '依學校試務法規存檔保存以供查核',
                        '當場確認應考人數與繳卷數量相符'
                    ]
                },
                {
                    'title': '2. 學期總成績結算',
                    'theme': 'teal',
                    'points': [
                        '期中考 (40%) + 期末考 (40%) + 出席 (20%)',
                        '嚴格遵循學校教務處成績評定規章',
                        '系統自動加總結算，絕無人為偏頗',
                        '總成績達 60 分即獲本專業學分'
                    ]
                },
                {
                    'title': '3. 校務系統公告複查',
                    'theme': 'amber',
                    'points': [
                        '考後一週內正式登錄萬能校務系統',
                        '依學校行事曆開放成績線上查詢',
                        '對成績有疑義者可依程序提出複查',
                        '預祝全體進修部同學順利通過及格'
                    ]
                }
            ]
        })
    else:
        # P.44: 曾光華經典商業個案深度講授與策略剖析
        slides.append({
            'layout': '2card',
            'badge': 'CASE STUDY LECTURE',
            'sec': '經典個案剖析',
            'title': f'曾光華經典案例講授：{case} 實務推演',
            'subtitle': f'借鏡台灣知名品牌商業戰略 ✕ 驗證曾光華企劃學理 ✕ 深度剖析決策脈絡',
            'left': {
                'title': '個案背景情境與市場挑戰',
                'theme': 'blue',
                'points': [
                    f'品牌情境：{case} 在高度競爭環境中尋求突破',
                    '核心痛點：傳統模式遭遇成長瓶頸與新進者威脅',
                    f'學理對照：精準對應曾光華 {chap} 核心架構',
                    f'策略驗證：透過 {concept} 重新檢視核心競爭優勢'
                ]
            },
            'right': {
                'title': '教授示範：企劃破局策略推演',
                'theme': 'teal',
                'points': [
                    '策略推導一：從市場真實痛點切入，拒絕自嗨式方案',
                    '策略推導二：靈活調配資源，構築無可取代之護城河',
                    '策略推導三：制定可衡量 SMART 指標與效益評估模型',
                    '應考啟發：此類商業轉型情境為期中期末考個案分析高頻題型'
                ]
            }
        })

        # P.45: 行銷企劃決策常見致命盲點與教授破解指引
        slides.append({
            'layout': '2card',
            'badge': 'DECISION PITFALLS',
            'sec': '決策盲點剖析',
            'title': '企劃決策常見致命盲點與教授破解指引',
            'subtitle': '深入拆解業界與考試最易犯之思維誤區 ✕ 曾光華教授四步破解心法',
            'left': {
                'title': '本單元核心決策盲點診斷',
                'theme': 'rose',
                'points': [
                    f'致命盲點：{pitfall}',
                    '盲點成因：死背名詞或直奔促銷，缺乏前端嚴謹診斷',
                    '連鎖反應：目標與策略前後矛盾，導致方案無法落地',
                    '考試警訊：期中期末考案例題若犯此盲點將嚴重失分'
                ]
            },
            'right': {
                'title': '曾光華教授破局心法指引',
                'theme': 'teal',
                'points': [
                    '心法一：回歸冰山模型，徹底探究問題本質與真實痛點',
                    '心法二：嚴格遵循十步企劃程序，前後邏輯嚴密咬合',
                    f'心法三：結合 {concept} 建立堅實的學理分析防線',
                    '心法四：以客觀數據與商業可行性作為策略抉擇準則'
                ]
            }
        })

        # P.46: 本週核心考點整理與期中期末應試精華
        slides.append({
            'layout': '3card',
            'badge': 'EXAM FOCUS & SUMMARY',
            'sec': '應試考點精華',
            'title': f'第 {week_num:02d} 週核心考點整理與期中期末應試精華',
            'subtitle': '提煉本週曾光華學理精華 ✕ 期中期末考命題重點 ✕ 輕鬆自主溫習',
            'cards': [
                {
                    'title': '1. 名詞定義與學理考點',
                    'theme': 'blue',
                    'points': [
                        f'核心概念：精準掌握 {concept} 之學術定義',
                        '辨析重點：清楚區分易混淆概念與使用邊界',
                        '程序邏輯：熟記該階段在十步程序中前後承接關係',
                        '應考要領：名詞解釋與選擇題必備核心基礎分'
                    ]
                },
                {
                    'title': '2. 案例分析情境題解構',
                    'theme': 'teal',
                    'points': [
                        '題型特徵：給予企業情境，要求診斷問題並提對策',
                        '破題步驟：先審題抓病徵 ➔ 援引學理 ➔ 提可行方案',
                        '答題規範：善用條列式與架構圖，拒絕通篇口語敘述',
                        '給分關鍵：展現清晰因果推導邏輯與商業可行性'
                    ]
                },
                {
                    'title': '3. 課程考核與溫習導引',
                    'theme': 'amber',
                    'points': [
                        '評分結構：期中考 40% ✕ 期末考 40% ✕ 出席 20%',
                        '零額外負擔：課堂專注聽講吸收，無需承擔課外繁重專案',
                        '輕鬆應試：課堂專注聽講，課後自主溫習投影片即可',
                        '及格保障：掌握每週精華考點，順利高分通過及格'
                    ]
                }
            ]
        })

    # =============================================================
    # P.47: 經濟部 IPAS 專業能力鑑定試題 (2card)
    # =============================================================
    if week_num == 1:
        # Week 1 untouched
        slides.append({
            'layout': '2card',
            'badge': 'IPAS 證照能力鑑定',
            'sec': '高頻考題解析',
            'title': f'經濟部 IPAS 專業能力鑑定精析：{ipas}',
            'subtitle': '本課程題庫深度對標國家級專業能力鑑定，輔導同學無痛考取國家級證照',
            'left': {
                'title': 'IPAS 鑑定核心考點觀念',
                'theme': 'blue',
                'points': [
                    f'考科範疇：{ipas}',
                    '題型風格：實務商業情境選擇題',
                    '鑑別重點：能否靈活運用企劃學理',
                    f'理論對照：對應 {chap} 核心重點'
                ]
            },
            'right': {
                'title': '常見考生失分陷阱剖析',
                'theme': 'rose',
                'points': [
                    '陷阱一：死背名詞解釋缺乏情境判斷',
                    '陷阱二：混淆不同策略工具之使用時機',
                    '陷阱三：忽略題幹中「何者為非」關鍵字',
                    '破解法：多做平台內建 180 題精選題庫'
                ]
            }
        })
    else:
        exam = IPAS_EXAMS.get(week_num, {})
        q1, q2 = split_text(exam.get('question', ''), 38)
        opts = exam.get('options', ['(A)', '(B)', '(C)', '(D)'])
        slides.append({
            'layout': '2card',
            'badge': 'IPAS 證照能力鑑定',
            'sec': '模擬情境試題',
            'title': f'經濟部 IPAS 品牌企劃師鑑定試題：{ipas}',
            'subtitle': '國家級專業能力鑑定模擬實戰 ｜ 實務商業情境選擇題演練 (本週核心考點)',
            'left': {
                'title': '【能力指標與題幹情境】',
                'theme': 'blue',
                'points': [
                    f"【能力指標】：{exam.get('competency', '')}",
                    f"【核心範疇】：{exam.get('key_knowledge', '')[:30]}",
                    f"【情境背景】：{q1}",
                    f"【考題提問】：{q2 if q2 else '請選出最符合曾光華企劃學理之正確選項。'}"
                ]
            },
            'right': {
                'title': '【情境試題選項 (四選一)】',
                'theme': 'amber',
                'points': [
                    opts[0] if len(opts) > 0 else '(A)',
                    opts[1] if len(opts) > 1 else '(B)',
                    opts[2] if len(opts) > 2 else '(C)',
                    opts[3] if len(opts) > 3 else '(D)'
                ]
            }
        })

    # =============================================================
    # P.48: IPAS 試題深度解析與學理對照 (2card)
    # =============================================================
    if week_num == 1:
        # Week 1 untouched
        slides.append({
            'layout': '2card',
            'badge': 'IPAS 證照能力鑑定',
            'sec': '考題深度解析',
            'title': f'IPAS 證照歷年精選試題解構與延伸思考',
            'subtitle': '透過題目拆解深入掌握出題者思維脈絡，融會貫通曾光華教科書學理',
            'left': {
                'title': '精選情境試題拆解',
                'theme': 'blue',
                'points': [
                    '題幹情境：企業面臨市場飽和新進者威脅',
                    '核心問題：此時應優先採取何種行銷策略',
                    '干擾選項：降價促銷、全面擴張產品線',
                    '正解推導：聚焦利基市場進行差異化定位'
                ]
            },
            'right': {
                'title': '曾光華學理深度對照',
                'theme': 'teal',
                'points': [
                    f'教科書對應：{concept}',
                    '策略邏輯：避免陷入流血價格戰泥淖',
                    '個人企劃應用：檢驗自身專案差異化程度',
                    '加分機制：考取證照總成績直接加 5~10 分'
                ]
            }
        })
    else:
        exam = IPAS_EXAMS.get(week_num, {})
        e1, e2 = split_text(exam.get('explanation', ''), 38)
        t1, t2 = split_text(exam.get('traps', ''), 38)
        slides.append({
            'layout': '2card',
            'badge': 'IPAS 證照深度解析',
            'sec': '正解推導與陷阱',
            'title': 'IPAS 證照試題深度剖析與曾光華學理對照',
            'subtitle': '標準答案推導 ✕ 考生失分盲點辨析 ✕ 企劃實務應用借鏡',
            'left': {
                'title': '【標準答案與學理推導】',
                'theme': 'teal',
                'points': [
                    f"★【標準答案】：{exam.get('answer', '')}（點擊/思考確認）",
                    f"【學理依據】：曾光華《行銷企劃》對應章節核心學理",
                    f"【推導要點】：{e1}",
                    f"【決策邏輯】：{e2 if e2 else '落實科學企劃程序，避免直奔促銷盲點。'}"
                ]
            },
            'right': {
                'title': '【考生失分陷阱與實務借鏡】',
                'theme': 'rose',
                'points': [
                    f"【干擾辨析】：{t1}",
                    f"【陷阱拆解】：{t2 if t2 else '切忌死記硬背名詞，應結合商業情境靈活推導。'}",
                    '【實務借鏡】：避免在個人企劃專案犯下相同決策盲點',
                    '【證照效益】：IPAS 品牌企劃師為經濟部採認之國家級專業證照'
                ]
            }
        })

    # =============================================================
    # Section 6: 學習總結、作品上傳與課後延伸 (P.49 ~ P.51, 3 slides)
    # =============================================================
    if week_num == 9:
        slides.append({
            'layout': '3card',
            'badge': 'MIDTERM CHECKLIST',
            'sec': '期中成果檢核',
            'title': '第 09 週期中學習成效自我檢核清單',
            'subtitle': '期中考後自主盤點前半學期核心觀念吸收程度，及時查漏補缺',
            'cards': [
                {
                    'title': '學理吸收檢核',
                    'theme': 'blue',
                    'points': [
                        '能否清楚區分企劃與計畫本質差異？',
                        '是否能熟練畫出十步企劃標準程序？',
                        '是否掌握五力分析與 VRIO 護城河？',
                        '能否正確完成 TOWS 交叉攻防矩陣？'
                    ]
                },
                {
                    'title': '應考與實務檢核',
                    'theme': 'teal',
                    'points': [
                        '選擇題作答是否避開常見題目陷阱？',
                        '案例題是否遵循「情境➔學理➔方案」？',
                        '答卷時間分配是否得宜無缺漏？',
                        '是否對前半學期學習投入給予客觀反思？'
                    ]
                },
                {
                    'title': '後半學期展望',
                    'theme': 'amber',
                    'points': [
                        '做好準備迎接下週第 10 週新產品上市',
                        '持續推進個人行銷企劃書全案進度',
                        '練習平台 IPAS 題庫保持題感',
                        '累積職場企劃實務無可取代之戰力'
                    ]
                }
            ]
        })
        slides.append({
            'layout': '2card',
            'badge': 'EXAM REVIEW & GRADES',
            'sec': '成績查核與複習',
            'title': '期中考成績登錄、查核與後續學習指引',
            'subtitle': '成績透明公開、落實學期考核規範，持續深化行銷企劃專業能力',
            'left': {
                'title': '期中成績核算與公告期程',
                'theme': 'blue',
                'points': [
                    '系統登錄：考後一週內將成績送交校務系統',
                    '考卷檢討：下週課堂完整解析易錯題型與爭議點',
                    '成績複查：若有疑義可於公告後三日內向教師申請',
                    '成績比重：期中考佔學期總成績 40%'
                ]
            },
            'right': {
                'title': '後半學期實務進度銜接',
                'theme': 'teal',
                'points': [
                    '下半學期主軸：行銷組合實務與企劃全案發表',
                    '第 10 週主題：新產品上市企劃與受眾 Persona',
                    '進度銜接：依據期中檢討持續深化後半學期學理核心',
                    '持續操作：運用平台 AI 工具輔助商業策略推導'
                ]
            }
        })
        slides.append({
            'layout': 'closing',
            'title': '第 09 週【期中考試】圓滿結束！',
            'subtitle': '感謝各位進修部同學的專注投入與全力以赴！辛苦大家完成前半學期檢定。',
            'final_message': '下週主題預告：第 10 週 新產品上市行銷企劃 ｜ 諮詢時間：週一 15:00~16:00、週四 14:00~16:00 (J801-1 研究室)'
        })
    elif week_num == 18:
        slides.append({
            'layout': '3card',
            'badge': 'SEMESTER CHECKLIST',
            'sec': '學期核心素養檢核',
            'title': '全學期行銷企劃核心素養終極自我檢核',
            'subtitle': '回顧 18 週扎實歷練，確認自己已從門外漢蛻變為具備實戰力之專業企劃人才',
            'cards': [
                {
                    'title': '學理思維核心素養',
                    'theme': 'blue',
                    'points': [
                        '精通曾光華十步標準企劃程序邏輯鏈條',
                        '能以數據與可衡量 SMART 檢定定義目標',
                        '精準運用 PESTC、五力、VRIO 與 TOWS',
                        '掌握新產品、公關危機、促銷與 OMO 策略'
                    ]
                },
                {
                    'title': '數位賦能核心素養',
                    'theme': 'teal',
                    'points': [
                        '熟練指揮 Agentic AI 執行市場情資洞察',
                        '掌握 CLEAR 結構化提示詞與在地化校準',
                        '具備 Vibe Coding 零代碼網頁原型搭建力',
                        '熟悉 GitHub Pages 免費發布全球公開網址'
                    ]
                },
                {
                    'title': '職場與證照競爭力',
                    'theme': 'amber',
                    'points': [
                        '掌握具備黃金十大章節之完整企劃書邏輯體系',
                        '具備 3 分鐘電梯簡報閃電 Pitch 風采與台風',
                        '融會貫通經濟部 IPAS 品牌企劃師鑑定題庫',
                        '在就業市場展現無可取代的專業企劃即戰力'
                    ]
                }
            ]
        })
        slides.append({
            'layout': '2card',
            'badge': 'SEMESTER ARCHIVE',
            'sec': '成績核算與檔案保存',
            'title': '學期總成績核算、登錄與學習檔案典藏',
            'subtitle': '完成學期學習旅程，妥善保存個人企劃學習資產，為職涯履歷大加分',
            'left': {
                'title': '學期成績核算與發布說明',
                'theme': 'blue',
                'points': [
                    '計分結構：期中考 40% ✕ 期末考 40% ✕ 出席 20%',
                    '系統登錄：本週試卷批閱完畢後依限送教務處',
                    '成績查詢：請同學依學校規定登入校務系統查詢',
                    '及格確認：總分達 60 分即獲本專業實務 2 學分'
                ]
            },
            'right': {
                'title': '個人企劃學習資產終身典藏',
                'theme': 'teal',
                'points': [
                    '知識留存：妥善留存本學期企劃講義與核心精華筆記',
                    '原型網址：GitHub Pages 公開網址終身有效',
                    '履歷加分：將網址與 IPAS 模擬成果列入個人求職履歷',
                    '終身學習：祝願各位在職場開拓非凡燦爛的行銷生涯！'
                ]
            }
        })
        slides.append({
            'layout': 'closing',
            'title': '第 18 週【期末考試與學期總結】圓滿結束！',
            'subtitle': '恭喜各位進修部同學圓滿完成本學期 18 週專業實務課程！邱老師為大家的堅持與成長深感驕傲！',
            'final_message': '學期總成績將於考後一週內登錄校務系統 ｜ 祝福大家職場順遂、行銷企劃所向披靡！'
        })
    else:
        # P.49: Weekly checklist
        slides.append({
            'layout': '3card',
            'badge': 'WEEKLY CHECKLIST',
            'sec': '學習成效自我檢核',
            'title': f'第 {week_num:02d} 週學習成效自我檢核清單',
            'subtitle': '課堂結束前自主盤點本週核心知識點，確認理解無盲點，從容應試',
            'cards': [
                {
                    'title': '1. 學理吸收檢核',
                    'theme': 'blue',
                    'points': [
                        f'能否大白話解釋 {concept} 之意涵？',
                        f'是否理解 {pitfall} 致命後果？',
                        f'能否理解 {case} 案例之破局邏輯？',
                        '是否掌握本週期中期末考核心學理考點？'
                    ]
                },
                {
                    'title': '2. 智能工具理解檢核',
                    'theme': 'teal',
                    'points': [
                        f'是否理解 {agent} 之基本運作架構？',
                        '是否認識 CLEAR 結構化提示詞設計邏輯？',
                        '是否理解 AI 輔助行銷企劃的優勢與邊界？',
                        '是否明白「人機協同、人類主導決策」之原則？'
                    ]
                },
                {
                    'title': '3. 數位思維與應用檢核',
                    'theme': 'amber',
                    'points': [
                        f'是否理解 {vibe} 之商業應用情境？',
                        '是否認識數位原型在行銷提案中的展示價值？',
                        '是否能將數位行銷概念與企劃學理融會貫通？',
                        '是否為後續期中期末考建立完整知識架構？'
                    ]
                }
            ]
        })

        # P.50: Exam guide & Self-study
        slides.append({
            'layout': '2card',
            'badge': 'EXAM & SELF-STUDY GUIDE',
            'sec': '自主溫習指引',
            'title': '期中期末考試導引與課後自主溫習指引',
            'subtitle': '評分結構維持：期中 40% ✕ 期末 40% ✕ 出席 20%，專注應試核心、輕鬆自主溫習',
            'left': {
                'title': '本週學理自主溫習重點',
                'theme': 'blue',
                'points': [
                    f'溫習重點一：複習 {chap} 之核心觀念與定義',
                    f'溫習重點二：熟記 {concept} 之實務推導步驟',
                    '溫習重點三：對照題庫演練本週 IPAS 選擇題與解析',
                    '應考準備：將本週投影片重點列入期中期末考複習範圍'
                ]
            },
            'right': {
                'title': '學期考核評分與應考說明',
                'theme': 'teal',
                'points': [
                    '評分純粹：期中考 40% ✕ 期末考 40% ✕ 出席 20%',
                    '成績計算純粹：僅計期中、期末兩次考試與平時出席，簡單明確',
                    '專注應試準備：課堂講授核心學理，免除課外討論與繁瑣專案',
                    '自主溫習：課後依個人工作步調自主溫習，輕鬆準備考試'
                ]
            }
        })

        # P.51: Closing slide
        slides.append({
            'layout': 'closing',
            'title': f'第 {week_num:02d} 週單元授課完畢！',
            'subtitle': '感謝各位進修部同學的專注聽講！請大家課後自主溫習，輕鬆準備考試。',
            'final_message': f'下週主題預告：第 {week_num+1 if week_num < 18 else 18:02d} 週單元 ｜ 諮詢時間：週一 15:00~16:00、週四 14:00~16:00 (J801-1 研究室)'
        })

    return slides
