# -*- coding: utf-8 -*-
"""
tools/build_agent_slides.py
Generates data/agent_slides.json containing 18 weeks x 12 slides = 216 unique slides.
Each week covers its dedicated Agent role, CLEAR prompt, ReAct workflow, local Taiwan case, and red-teaming checks.
"""
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(BASE_DIR, 'data', 'agent_slides.json')

AGENT_TOPICS = {
    1: ("市場情資洞察 Agent", "宏觀趨勢 PESTEL 與消費者心理洞察", "手搖飲與外送產業", "少子單身化與數位外送普及率"),
    2: ("市場情資洞察 Agent", "企劃十步標準程序推導與次級情資萃取", "連鎖餐飲轉型企劃", "官方主計總處與餐飲公會白皮書"),
    3: ("STP 市場定位 Agent", "SMART 目標轉化與受眾價值主張設定", "大專生文創保溫杯專案", "量化達成率與感知價值溢價率"),
    4: ("市場情資洞察 Agent", "總體環境 PESTEL 深度掃描與信號辨識", "桃園觀光工廠與在地文創", "淨零碳排政策與綠色採購法規"),
    5: ("市場情資洞察 Agent", "波特五力競爭分析與假想敵攻防矩陣", "連鎖早午餐與超商咖啡對決", "同業爭奪、替代品跨界與買方議價"),
    6: ("STP 市場定位 Agent", "內部資源 VRIO 檢驗與核心價值主張", "烘焙糕餅老店數位轉型", "百年配方與在地溫度的不可替代性"),
    7: ("受眾 Persona 畫像 Agent", "TOWS 交叉攻防戰略矩陣推導", "健康蔬食調理包切入外宿族", "SO/ST/WO/WT 四象限具體攻防"),
    8: ("SCAMPER 創意奔馳 Agent", "SCAMPER 7 步發散與逆向假設創新", "傳統夜市小吃伴手禮化包裝", "替代、結合、逆向與重組發散"),
    9: ("企劃審查評估 Agent", "期中提案商業痛點診斷與紅隊審查", "個人期中企劃全案提案", "邏輯斷裂點、預算黑洞與執行盲區"),
    10: ("受眾 Persona 畫像 Agent", "新產品概念測試問卷與精準 Persona", "AI 智慧寵物餵食器專案", "飼主痛點圖譜與支付意願階梯"),
    11: ("爆款文案與短影音 Agent", "新產品上市 48 小時節奏與時程排程", "新產品募資早鳥搶購", "黃金 3 秒鉤子與痛點解決短片"),
    12: ("公關活動與策展 Agent", "事件行銷話題策展與 5W1H 新聞稿", "中壢商圈在地永續快閃日", "新聞議題創造與社群打卡擴散"),
    13: ("公關活動與策展 Agent", "品牌危機黃金 3 小時闢謠與 FAQ 題庫", "食安或個資外洩突發公關", "事實澄清、道歉承諾與問答矩陣"),
    14: ("促銷活動與 ROI 試算 Agent", "促銷損益平衡 BEP 試算與誘因工具", "週年慶滿額贈與早鳥折價券", "毛利率扣抵、誘因成本與回本量"),
    15: ("MarTech 顧客旅程 Agent", "OMO 虛實融合顧客旅程地圖 CJM 繪製", "門市與線上 LINE 會員綁定", "五大接觸點與斷點修復策略"),
    16: ("企劃全案架構一鍵生成 Agent", "黃金一頁式執行摘要與十大章節整合", "個人期末行銷企劃正式全案", "邏輯連貫性檢驗與企劃書格式規範"),
    17: ("企劃全案架構一鍵生成 Agent", "3 分鐘 Pitch 閃電簡報與評審應答", "期末課堂個人公開提案簡報", "電梯簡報原則與刁鑽提問應答攻防"),
    18: ("全案 8 款行銷 Agent 整合", "期末企劃全案總體檢與個人作品集整合", "四下個人代表作數位作品集", "全流程 AI 協同沉澱與職涯履歷亮點")
}

def generate_agent_slides():
    agent_slides = {}

    for w in range(1, 19):
        agent_name, topic, case, focus = AGENT_TOPICS[w]
        w_slides = []

        # P.24 (AI.01)
        w_slides.append({
            'badge': f'AGENTIC AI 智慧協同 ｜ 第 {w:02d} 週',
            'sec': 'AI 工坊 P.01',
            'title': f'{agent_name}：戰略定位與職責使命',
            'subtitle': f'第 {w} 週專屬智能體：在「{case}」任務中扮演核心策略智囊',
            'layout': '2card',
            'left': {
                'title': f'{agent_name} 的核心職能',
                'theme': 'blue',
                'points': [
                    f'專精領域：深度鎖定{topic}',
                    f'輔助目標：加速完成{case}情資處理',
                    '減少繁瑣摸索：秒級整理結構化論據',
                    '突破盲點：以客觀推論協助個人決策'
                ]
            },
            'right': {
                'title': '行銷企劃師的主導權責',
                'theme': 'teal',
                'points': [
                    '指揮而非盲從：由你下達精確業務指令',
                    '業務真實驗證：審核產出是否合乎常理',
                    '在地語境轉化：融入台灣真實市場特色',
                    '對全案成敗當責：AI 是副手你是主帥'
                ]
            }
        })

        # P.25 (AI.02)
        w_slides.append({
            'badge': f'AGENTIC AI 智慧協同 ｜ 第 {w:02d} 週',
            'sec': 'AI 工坊 P.02',
            'title': f'系統提示詞角色設定 (System Prompt)',
            'subtitle': f'為 {agent_name} 注入 20 年實戰經驗，確立專業嚴謹思維底色',
            'layout': '2card',
            'left': {
                'title': '角色特質與專業背景設定',
                'theme': 'blue',
                'points': [
                    '角色：擁有 20 年資深行銷總監經驗',
                    f'專長：精通曾光華教授行銷企劃理論',
                    f'任務焦點：專注於{focus}',
                    '風格：數據導向、切中痛點、邏輯嚴密'
                ]
            },
            'right': {
                'title': '輸出邊界約束與防呆規則',
                'theme': 'rose',
                'points': [
                    '嚴禁憑空捏造假數據與過時資訊',
                    '拒絕空泛套話，每項建議需有依據',
                    '限制篇幅與要點，聚焦關鍵決策點',
                    '強制標註假設前提，便於人工核驗'
                ]
            }
        })

        # P.26 (AI.03)
        w_slides.append({
            'badge': f'AGENTIC AI 智慧協同 ｜ 第 {w:02d} 週',
            'sec': 'AI 工坊 P.03',
            'title': f'情境變數與上下文背景配置',
            'subtitle': f'提供給 {agent_name} 的專案背景包，確保產出量身定做',
            'layout': '3card',
            'cards': [
                {
                    'title': '1. 企業與產品設定',
                    'theme': 'blue',
                    'points': [
                        f'產業類型：鎖定{case}',
                        '企業規模：本土中小型創新品牌',
                        '既有資源：預算有限、團隊精簡敏捷',
                        '核心挑戰：市場飽和需快速切入利基'
                    ]
                },
                {
                    'title': '2. 目標受眾與市場',
                    'theme': 'teal',
                    'points': [
                        '地理範疇：以台灣都會區及桃園在地為主',
                        '客群特徵：20~40歲重視性價比與體驗',
                        '消費習慣：手機黏著度高、偏好數位互動',
                        '未解痛點：渴望高品質且透明信賴的解方'
                    ]
                },
                {
                    'title': '3. 本週交付成果指標',
                    'theme': 'amber',
                    'points': [
                        f'核心交付：完成{topic}',
                        '規格要求：列出 3 大關鍵支撐論據',
                        '檢驗準則：符合曾光華企劃架構規範',
                        '後續銜接：直接作為期末企劃章節草稿'
                    ]
                }
            ]
        })

        # P.27 (AI.04)
        w_slides.append({
            'badge': f'AGENTIC AI 智慧協同 ｜ 第 {w:02d} 週',
            'sec': 'AI 工坊 P.04',
            'title': f'CLEAR 提示詞框架實戰剖析',
            'subtitle': f'運用 CLEAR 五大維度撰寫精準指令，指揮 {agent_name}',
            'layout': '2card',
            'left': {
                'title': 'CLEAR 前三維度：情境、限制、期望',
                'theme': 'blue',
                'points': [
                    f'C (Context)：說明專案正進行{case}',
                    'L (Limits)：限制字數並禁用模糊術語',
                    'E (Expectation)：期望產出條列式矩陣',
                    '提供背景：讓 AI 掌握真實商業制約'
                ]
            },
            'right': {
                'title': 'CLEAR 後兩維度：行動、角色',
                'theme': 'teal',
                'points': [
                    f'A (Action)：執行{focus}深度剖析',
                    f'R (Role)：擔任嚴謹專業的{agent_name}',
                    '一鍵指令：結構分明提高回應準確度',
                    '可重現性：團隊成員皆能複製相同品質'
                ]
            }
        })

        # P.28 (AI.05)
        w_slides.append({
            'badge': f'AGENTIC AI 智慧協同 ｜ 第 {w:02d} 週',
            'sec': 'AI 工坊 P.05',
            'title': '提示詞對比演練：劣質 vs 專業級 CLEAR',
            'subtitle': f'針對「{topic}」任務，一字之差帶來的巨大品質鴻溝',
            'layout': '2card',
            'left': {
                'title': '常見劣質提問（產出空洞廢話）',
                'theme': 'rose',
                'points': [
                    f'錯誤範例：「幫我想一個{case}的點子」',
                    '致命缺陷一：無背景情境與目標受眾說明',
                    '致命缺陷二：無字數格式限制與驗證標準',
                    '結果：AI 給出人盡皆知的常識與空話'
                ]
            },
            'right': {
                'title': '專業 CLEAR 提問（精準商業解方）',
                'theme': 'teal',
                'points': [
                    f'專業示範：「你身為{agent_name}…」',
                    f'明確限制：「以桃園在地為場景，聚焦{focus}」',
                    '格式規範：「分3點輸出痛點、解方與KPI」',
                    '結果：產出具備即時可落地的實戰提案'
                ]
            }
        })

        # P.29 (AI.06)
        w_slides.append({
            'badge': f'AGENTIC AI 智慧協同 ｜ 第 {w:02d} 週',
            'sec': 'AI 工坊 P.06',
            'title': f'{agent_name} 的 ReAct 推理軌跡',
            'subtitle': 'Thought ➔ Action ➔ Observation ➔ Decision 智能體自主推理流程',
            'layout': '3card',
            'cards': [
                {
                    'title': '1. 思考 (Thought)',
                    'theme': 'blue',
                    'points': [
                        f'拆解問題：分析{case}的關鍵成敗因子',
                        '檢視資源：核對現有預算與客群限制',
                        '搜尋模型：比對曾光華教科書對應章節',
                        '設定路徑：規劃三階段推導步驟'
                    ]
                },
                {
                    'title': '2. 行動 (Action) & 觀察',
                    'theme': 'teal',
                    'points': [
                        f'行動調用：調取{focus}相關實務數據',
                        '跨維交叉：將市場痛點與產品特性配對',
                        '觀察反饋：檢驗推導結果是否符合邏輯',
                        '自我修正：剔除可行性偏低的極端方案'
                    ]
                },
                {
                    'title': '3. 決策 (Decision)',
                    'theme': 'amber',
                    'points': [
                        '形成結論：精煉出最具性價比的提案',
                        '排定優先序：標明短中長期推進步驟',
                        '標註風險：提醒企劃師需防範的漏洞',
                        '格式化輸出：轉為易於閱讀的結構表格'
                    ]
                }
            ]
        })

        # P.30 (AI.07)
        w_slides.append({
            'badge': f'AGENTIC AI 智慧協同 ｜ 第 {w:02d} 週',
            'sec': 'AI 工坊 P.07',
            'title': '實機示範：智慧智能體結構化輸出展示',
            'subtitle': f'{agent_name} 針對「{case}」產出的高水準分析範例',
            'layout': '2card',
            'left': {
                'title': '核心痛點診斷與策略方針',
                'theme': 'blue',
                'points': [
                    f'痛點一：{focus}缺乏系統性整理',
                    '痛點二：行銷訊息無法引起受眾情感共鳴',
                    '策略方針：建立差異化心智定位認知',
                    '戰術抓手：以數據驗證強化提案信賴感'
                ]
            },
            'right': {
                'title': '落地執行步驟與成效預估',
                'theme': 'teal',
                'points': [
                    '第一階段：完成目標客群深度輪廓標定',
                    '第二階段：佈局高轉化率行銷接觸節點',
                    '預估成效：提升受眾認知與互動意願 30%',
                    '檢核機制：以每週儀表板追蹤核心指標'
                ]
            }
        })

        # P.31 (AI.08)
        w_slides.append({
            'badge': f'AGENTIC AI 智慧協同 ｜ 第 {w:02d} 週',
            'sec': 'AI 工坊 P.08',
            'title': '多輪追問與校準：深化分析層次',
            'subtitle': '好企劃是聊出來的！如何運用追問技巧榨出 AI 最深層價值',
            'layout': '3card',
            'cards': [
                {
                    'title': '第一輪追問：質疑前提',
                    'theme': 'blue',
                    'points': [
                        '詢問：「如果對手立刻跟進，優勢在哪？」',
                        '逼出護城河：要求 AI 找出難以複製的關鍵',
                        '加深防禦力：排除易被模仿的單純降價招數',
                        '強化專案獨特性：確保企劃具備長期效益'
                    ]
                },
                {
                    'title': '第二輪追問：壓縮預算',
                    'theme': 'teal',
                    'points': [
                        '詢問：「若行銷預算砍半，核心策略如何變？」',
                        '逼出最精華路徑：找出投報率最高的關鍵單點',
                        '捨棄多餘枝節：將資源集中於刀口上',
                        '提升方案彈性：設計分階段推進的備案'
                    ]
                },
                {
                    'title': '第三輪追問：在地轉化',
                    'theme': 'amber',
                    'points': [
                        '詢問：「這套在桃園在地市場能行得通嗎？」',
                        '結合在地商圈：融入中壢或桃園生活圈特色',
                        '接地氣文案：使用台灣在地熟悉的語言習慣',
                        '真實場景測試：模擬一線消費者的直接反饋'
                    ]
                }
            ]
        })

        # P.32 (AI.09)
        w_slides.append({
            'badge': f'AGENTIC AI 智慧協同 ｜ 第 {w:02d} 週',
            'sec': 'AI 工坊 P.09',
            'title': '台灣在地化與桃園生活圈情境校準',
            'subtitle': f'杜絕美式或對岸用語，確保 {agent_name} 的輸出完全契合在地市場',
            'layout': '2card',
            'left': {
                'title': '語意與文化在地轉化',
                'theme': 'blue',
                'points': [
                    '用語校正：將「宣發/裂變」轉為「宣傳/口碑」',
                    '法規遵循：符合台灣消保法與公平交易規範',
                    '消費文化：掌握台灣人偏好集點、贈品心理',
                    '通路習慣：考慮超商密度與機車外帶生活模式'
                ]
            },
            'right': {
                'title': '桃園中壢商圈實景融入',
                'theme': 'teal',
                'points': [
                    '學區商圈：結合大專院校學生消費時段',
                    '通勤節點：高鐵、機捷與客運轉乘人潮特性',
                    '多元族群：融入科技園區工程師與在地居民',
                    '場景落地：讓提案方案具備真實空間立足點'
                ]
            }
        })

        # P.33 (AI.10)
        w_slides.append({
            'badge': f'AGENTIC AI 智慧協同 ｜ 第 {w:02d} 週',
            'sec': 'AI 工坊 P.10',
            'title': '人工紅隊審查三原則 (Human-in-the-loop)',
            'subtitle': 'AI 是頂級智囊，但企劃成敗全由你負責！三關嚴格查驗',
            'layout': '3card',
            'cards': [
                {
                    'title': '原則一：防數據幻覺',
                    'theme': 'rose',
                    'points': [
                        '逐筆核實 AI 引用的統計數字真實出處',
                        '確認數據年份在 3 年內，避免過期資訊',
                        '對異常偏高或樂觀的數字保持高度懷疑',
                        '官方智庫驗證：主計總處、MIC 或公會'
                    ]
                },
                {
                    'title': '原則二：防邏輯斷裂',
                    'theme': 'amber',
                    'points': [
                        '檢視結論是否真能推導自前面列出的依據',
                        '檢查策略方案是否真正打中最初界定的痛點',
                        '杜絕因果倒置或將戰術當成戰略的低級錯誤',
                        '確保通篇企劃前後呼應、首尾連貫'
                    ]
                },
                {
                    'title': '原則三：防落地脫節',
                    'theme': 'teal',
                    'points': [
                        '以一線執行者視角評估人力工時是否可行',
                        '檢查方案成本是否超出預算負荷上限',
                        '評估合作夥伴與供應鏈是否有能力配合',
                        '確認法律合規與商標著作權零侵權風險'
                    ]
                }
            ]
        })

        # P.34 (AI.11)
        w_slides.append({
            'badge': f'AGENTIC AI 智慧協同 ｜ 第 {w:02d} 週',
            'sec': 'AI 工坊 P.11',
            'title': f'{agent_name} 專屬提示詞咒語卡',
            'subtitle': '可直接複製保存於個人提示詞庫的即用型高階咒語',
            'layout': '2card',
            'left': {
                'title': '即用型核心 Prompt 模板',
                'theme': 'blue',
                'points': [
                    f'「你是專業{agent_name}，具備20年經驗」',
                    f'「專案背景：我們正在規劃{case}」',
                    f'「請針對{focus}進行深度結構化分析」',
                    '「請依序產出：痛點診斷、3大方案、預期KPI」'
                ]
            },
            'right': {
                'title': '微調參數與版本迭代建議',
                'theme': 'teal',
                'points': [
                    '溫度值 (Temperature)：設為 0.4 確保邏輯嚴密',
                    '指定長度：要求每點控制於 100 字內精準陳述',
                    '記錄版本：標記 v1.0 依據實作回饋定期優化',
                    '匯入附錄：將對話歷程截圖作為個人企劃佐證'
                ]
            }
        })

        # P.35 (AI.12)
        w_slides.append({
            'badge': f'AGENTIC AI 智慧協同 ｜ 第 {w:02d} 週',
            'sec': 'AI 工坊 P.12',
            'title': '本週 Agentic AI 協同實作小結',
            'subtitle': f'總結本週與 {agent_name} 的協同成果，打通個人企劃關鍵環節',
            'layout': '3card',
            'cards': [
                {
                    'title': '智慧賦能收穫',
                    'theme': 'blue',
                    'points': [
                        f'成功調用：{agent_name}',
                        f'掌握核心：掌握{topic}推導技巧',
                        '效率躍升：分析耗時從數小時縮短至數分鐘',
                        '提升深度：獲得超越同業平均水準之策略視野'
                    ]
                },
                {
                    'title': '個人企劃資產',
                    'theme': 'teal',
                    'points': [
                        '完成本週專案草案，文字內容條理清晰',
                        '產出結構化表格，可直接套入期末全案',
                        '累積專屬提示詞咒語卡，建立 AI 數位資產',
                        '個人獨立完成，展現 AI 時代全新企劃素養'
                    ]
                },
                {
                    'title': '下週銜接方向',
                    'theme': 'amber',
                    'points': [
                        '將本週分析結論輸入下週 Agent 繼續深化',
                        '保持批判思考，持續以人類直覺校準 AI 輸出',
                        '準備將策略轉化為 Vibe Coding 網頁元件',
                        '讓企劃不僅停留在紙上，更具備即時互動展示力'
                    ]
                }
            ]
        })

        agent_slides[str(w)] = w_slides

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(agent_slides, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated {len(agent_slides)} weeks of agent slides to {OUTPUT_PATH}")

if __name__ == '__main__':
    generate_agent_slides()
