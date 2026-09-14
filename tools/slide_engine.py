# -*- coding: utf-8 -*-
"""
萬能科技大學 11501 創意行銷企劃實務 - 51 頁全景投影片生成引擎 (tools/slide_engine.py)
負責將每一週的週次配置，精準生成 51 張高畫質、符合 28 號字排版、零溢出的投影片
"""
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

with open(os.path.join(DATA_DIR, 'chapter_slides.json'), 'r', encoding='utf-8') as f:
    CHAPTER_SLIDES = json.load(f)

with open(os.path.join(DATA_DIR, 'agent_slides.json'), 'r', encoding='utf-8') as f:
    AGENT_SLIDES = json.load(f)

with open(os.path.join(DATA_DIR, 'vibe_slides.json'), 'r', encoding='utf-8') as f:
    VIBE_SLIDES = json.load(f)

def build_week_slides(wc):
    week_num = wc['week']
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

    # -------------------------------------------------------------
    # P.01: 單元封面 (cover)
    # -------------------------------------------------------------
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

    # -------------------------------------------------------------
    # P.02: 教師介紹 (僅第 1 週) 或 本週學習目標 (第 2~18 週)
    # -------------------------------------------------------------
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
    else:
        slides.append({
            'layout': '2card',
            'badge': 'LEARNING OBJECTIVES',
            'sec': '本週學習目標',
            'title': f'第 {week_num:02d} 週學習目標與企劃能力地圖',
            'subtitle': f'結合曾光華學理權威 ✕ Agentic AI 智慧協同 ✕ Vibe Coding 實踐',
            'left': {
                'title': '學理與企劃核心能力',
                'theme': 'blue',
                'points': [
                    f'深入掌握：{chap} 核心邏輯',
                    f'學會應用：{concept}',
                    f'避開盲點：{pitfall}',
                    '落實個人企劃本週實體進度撰寫'
                ]
            },
            'right': {
                'title': 'AI 協同與數位原型能力',
                'theme': 'teal',
                'points': [
                    f'熟練操作：{agent}',
                    '掌握 CLEAR 商務提示詞結構',
                    f'實作原型：{vibe}',
                    f'對標鑑定：{ipas}'
                ]
            }
        })

    # -------------------------------------------------------------
    # P.03: 實務痛點破冰 (2card)
    # -------------------------------------------------------------
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

    # -------------------------------------------------------------
    # P.04: 曾光華教科書學理定位 (2card)
    # -------------------------------------------------------------
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

    # -------------------------------------------------------------
    # P.05: 三維學習模型 (3card)
    # -------------------------------------------------------------
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
                    f'實機操作：{agent}',
                    '掌握 ReAct 循環 (思考/行動/觀察/決策)',
                    '以 CLEAR 框架引導 AI 深度分析',
                    '從手動文案搬運工躍升為戰略指揮官'
                ]
            },
            {
                'title': '3. Vibe Coding 原型',
                'theme': 'amber',
                'points': [
                    '企管系同學零代碼也能打造互動網頁',
                    f'打造主題組件：{vibe}',
                    '免費發布至 GitHub Pages 取得公開網址',
                    '成果上傳教學平台展示廊，累積個人履歷'
                ]
            }
        ]
    })

    # -------------------------------------------------------------
    # Section 2: 曾光華《行銷企劃》經典學理深度拆解 (P.06 ~ P.23, 18 slides)
    # -------------------------------------------------------------
    slides.extend(CHAPTER_SLIDES.get(str(week_num), []))

    # -------------------------------------------------------------
    # Section 3: Agentic AI 智慧代理人協同實戰 (P.24 ~ P.35, 12 slides)
    # -------------------------------------------------------------
    slides.extend(AGENT_SLIDES.get(str(week_num), []))

    # -------------------------------------------------------------
    # Section 4: Vibe Coding 操作手冊與數位原型開發 (P.36 ~ P.43, 8 slides)
    # -------------------------------------------------------------
    slides.extend(VIBE_SLIDES.get(str(week_num), []))

    # -------------------------------------------------------------
    # Section 5: 課堂個人獨立實作演練 ✕ IPAS 證照題庫解析 (P.44 ~ P.48, 5 slides)
    # -------------------------------------------------------------
    slides.append({
        'layout': '2card',
        'badge': 'F401 課堂實務演練',
        'sec': '個人獨立實作',
        'title': f'本週 F401 課堂任務：個人獨立實作指引',
        'subtitle': '落實個人實務獨立企劃（各做各的，免除分組搭便車與開會協調負擔）',
        'left': {
            'title': '個人實務任務執行要點',
            'theme': 'blue',
            'points': [
                f'任務範疇：落實 {concept}',
                '獨立作業：每人獨立挑選目標專案',
                '課堂進度：完成本週 1 頁企劃工作紙',
                '參與互動：隨機抽籤發表爭取平時分'
            ]
        },
        'right': {
            'title': '課堂自律與評量規範',
            'theme': 'amber',
            'points': [
                '專業素養：課堂專注投入、不滑無關手機',
                '實體研討：善用紙本便利貼敏捷整理想法',
                '真實痛點：取材自日常生活或在職職場',
                '誠信原則：AI 僅供輔助，個人親自把關'
            ]
        }
    })

    slides.append({
        'layout': '2card',
        'badge': 'SCAMPER 創意奔馳',
        'sec': '敏捷發想法',
        'title': f'SCAMPER 創意奔馳演練：{scamper}',
        'subtitle': '桌面便利貼 7 步奔馳法，強制大腦跳脫常規路徑，激發意想不到的突破行銷切角',
        'left': {
            'title': 'SCAMPER 本週發想挑戰',
            'theme': 'teal',
            'points': [
                f'發想主軸：{scamper}',
                '破框思維：大膽打破既有業界常規',
                '便利貼法：每張便利貼只寫一個點子',
                '限時衝刺：15 分鐘產出 5 個跨界創意'
            ]
        },
        'right': {
            'title': '創意收斂與商業評估',
            'theme': 'blue',
            'points': [
                '吸引力評估：是否真能引起客群驚呼',
                '可行性評估：技術、法規與成本是否可控',
                '差異化評估：競品是否已經大同小異',
                '落地轉化：挑選最佳 1 項納入企劃全案'
            ]
        }
    })

    slides.append({
        'layout': '3card',
        'badge': 'CLASSROOM INTERACTION',
        'sec': '即時互動機制',
        'title': '課堂即時互動：靈感抽卡機與大轉盤',
        'subtitle': '運用教學平台內建互動工具，活躍課堂思維，公平隨機抽取學員發表',
        'cards': [
            {
                'title': '1. 靈感抽卡機',
                'theme': 'blue',
                'points': [
                    '內建 50+ 張行銷策略靈感卡片',
                    '一鍵隨機抽取非對稱行銷切角',
                    '強迫將抽到卡片與個人企劃結合',
                    '突破思維盲區創造驚艷亮點'
                ]
            },
            {
                'title': '2. 創意大轉盤',
                'theme': 'teal',
                'points': [
                    '公平隨機抽取學員座號 (01~08號...)',
                    '每人 1~2 分鐘精簡分享本週發想',
                    '老師針對痛點與定位即時回饋',
                    '即時記錄課堂主動發言表現加分'
                ]
            },
            {
                'title': '3. 便利貼計時器',
                'theme': 'amber',
                'points': [
                    '大螢幕 15 分鐘敏捷發想倒數計時',
                    '實體便利貼黏貼於個人企劃手卡',
                    '同儕課堂無壓力相互觀摩學習',
                    '建立進修部專屬高凝聚力學習社群'
                ]
            }
        ]
    })

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

    # -------------------------------------------------------------
    # Section 6: 學習總結、作品上傳與課後延伸 (P.49 ~ P.51, 3 slides)
    # -------------------------------------------------------------
    slides.append({
        'layout': '3card',
        'badge': 'WEEKLY CHECKLIST',
        'sec': '學習成果檢核',
        'title': f'第 {week_num:02d} 週學習成效自我檢核清單',
        'subtitle': '課堂結束前請花 3 分鐘自主檢核，確認本週核心知識點已全數吸收掌握',
        'cards': [
            {
                'title': '學理吸收檢核',
                'theme': 'blue',
                'points': [
                    f'能否大白話解釋 {concept}？',
                    f'是否理解 {pitfall} 嚴重後果？',
                    f'能否舉出 1 個 {case} 類似案例？',
                    '是否已完成個人企劃本週紙本手稿？'
                ]
            },
            {
                'title': 'AI 協同實作檢核',
                'theme': 'teal',
                'points': [
                    f'是否登入平台體驗 {agent}？',
                    '是否能寫出完整的 CLEAR 提示詞？',
                    '是否對 AI 輸出進行客觀查核調優？',
                    '是否妥善保存優質提示詞至個人筆記？'
                ]
            },
            {
                'title': '數位原型檢核',
                'theme': 'amber',
                'points': [
                    f'是否完成 {vibe} 網頁代碼生成？',
                    '在手機直式瀏覽下是否完全無破版？',
                    '是否成功取得 GitHub Pages 公開網址？',
                    '是否將網址上傳至教學平台作品廊？'
                ]
            }
        ]
    })

    slides.append({
        'layout': '2card',
        'badge': 'HOMEWORK & SUBMISSION',
        'sec': '作業與作品上傳',
        'title': '課後延伸任務：成果上傳至【學生作品展示廊】',
        'subtitle': '持續推進個人行銷企劃進度，累積具備真實公開網址的求職黃金作品集',
        'left': {
            'title': '課後自主作業內容',
            'theme': 'blue',
            'points': [
                f'作業一：完善本週企劃進度段落手稿',
                f'作業二：操作 {agent} 深化情資分析',
                f'作業三：更新 {vibe} 網頁組件',
                '自主練習：完成 IPAS 證照題庫 10 題快測'
            ]
        },
        'right': {
            'title': '作品成果展示廊繳交步驟',
            'theme': 'teal',
            'points': [
                '登入教學平台：點擊右上角 Google 登入',
                '進入作品廊：切換至【學生作品成果展示廊】',
                '填寫表單：登記企劃標題、摘要與 GitHub 網址',
                '即時預覽：作品卡片秒級同步，全班即時觀摩'
            ]
        }
    })

    slides.append({
        'layout': 'closing',
        'title': f'第 {week_num:02d} 週單元授課完畢！',
        'subtitle': f'感謝各位進修部同學的專注投入與熱烈研討！請大家妥善保存本週企劃成果。',
        'final_message': f'下週主題預告：第 {week_num+1 if week_num < 18 else 18:02d} 週單元 ｜ 諮詢時間：週一 15:00~16:00、週四 14:00~16:00 (J801-1 研究室)'
    })

    return slides
