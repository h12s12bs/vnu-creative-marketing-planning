# -*- coding: utf-8 -*-
"""
萬能科技大學 11501 創意行銷企劃實務 - 18 週全景教學簡報生成器 (tools/build_presentation_html.py)
生成 Full_Screen_Presentation.html
班級：進企管四系3甲 ｜ 教室：F401 教室 ｜ 授課教師：邱俊維 博士
參考用書：曾光華《行銷企劃：邏輯、創意、執行力》(2026 第五版)
"""
import os
import sys
import json

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def generate_curriculum_slides():
    curriculum = []

    # =========================================================================
    # WEEK 01: 課程導覽、個人介紹、評分標準、曾光華行銷企劃與 Vibe Coding 啟蒙
    # =========================================================================
    w01_slides = [
        {
            "layout": "cover",
            "badge": "萬能科技大學 企業管理系 ｜ 11501 專業實務核心課程",
            "title": "創意行銷企劃實務 ✕ Agentic AI 協同實戰",
            "subtitle": "從邏輯、創意到執行力：指揮 AI 智能體打造真實商業企劃與線上服務",
            "meta": [
                "開課班級：進企管四系3甲 (週二 10~11 節 16:20 ~ 17:50)",
                "授課地點：F401 教室",
                "授課教師：邱俊維 博士 / 專案助理教授",
                "參考用書：曾光華《行銷企劃：邏輯、創意、執行力》(2026 第五版)"
            ]
        },
        {
            "layout": "2card",
            "badge": "FACULTY PROFILE",
            "sec": "授課教師介紹",
            "title": "授課教師介紹：邱俊維 博士 / 專案助理教授",
            "subtitle": "長庚大學管理學博士 ｜ 決策科學與 AI 跨域應用 ｜ 育英樓 J801-1 研究室",
            "left": {
                "title": "學術背景與核心研究專長",
                "theme": "blue",
                "points": [
                    "最高學歷：長庚大學 管理研究所 博士（主修決策科學與運籌管理）",
                    "學碩歷程：長庚大學 資訊管理研究所 碩士、資訊管理學系 學士",
                    "核心研究：多準則決策分析 (MCDM: AHP, DEMATEL, TOPSIS)",
                    "前沿科技：AI 行銷科技 (MarTech)、Agentic AI 智慧工作流架構",
                    "研究著作：多篇論文發表於國際頂尖 SCI 國際期刊 (ESWA, CIE 等)"
                ]
            },
            "right": {
                "title": "產學歷練與諮詢聯絡",
                "theme": "teal",
                "points": [
                    "業界歷練：生醫健康事業研發工程師兼董事長特助、明通化學製藥數位轉型顧問",
                    "校務決策：長庚大學校務研究中心分析師（視覺化大數據決策平台）",
                    "研究經歷：國科會多年期決策科學研究計畫 研究助理",
                    "研究室位置：萬能科技大學 育英樓 (J棟) J801-1 研究室",
                    "教師信箱：jimchiu@mail.vnu.edu.tw",
                    "諮詢時間：每週一 15:00 ~ 16:00、週四 14:00 ~ 16:00 (敬請事先預約)"
                ]
            }
        },
        {
            "layout": "3card",
            "badge": "COURSE OVERVIEW",
            "sec": "課程定位與核心精神",
            "title": "課程願景：進修部企管同學的行銷超能力賦能",
            "subtitle": "不背死板理論、不做無效空談，結合理論經典與現代 AI 智能體實戰落地",
            "cards": [
                {
                    "title": "曾光華權威經典架構",
                    "theme": "blue",
                    "points": [
                        "以曾光華《行銷企劃》第五版為全學期學理核心",
                        "深耕「邏輯思維、創意突破、執行控制」三位一體",
                        "從 PESTEL、STP、4P 到危機公關與損益試算",
                        "建構紮實的企管專業行銷企劃書撰寫功力"
                    ]
                },
                {
                    "title": "Agentic AI 智慧代理人",
                    "theme": "teal",
                    "points": [
                        "從手動文案搬運工躍升為「行銷戰略指揮官」",
                        "掌握 ReAct (思考 ➔ 行動 ➔ 觀察 ➔ 決策) 循環",
                        "學會 CLEAR 提示詞結構，精準引導 AI 分析市場",
                        "以大白話自然語言讓 AI 協同生成受眾 Persona"
                    ]
                },
                {
                    "title": "Vibe Coding 成果實踐",
                    "theme": "amber",
                    "points": [
                        "企管系同學不寫程式碼，也能打造真實運作的專案",
                        "透過 3 步驟將企劃化為一頁式互動網頁 (MVP)",
                        "以 GitHub Pages 取得全球免費用專屬網址",
                        "成果上傳教學平台展示廊，成為求職黃金作品集"
                    ]
                }
            ]
        },
        {
            "layout": "3card",
            "badge": "GRADING POLICY",
            "sec": "多元學期評分標準",
            "title": "學期成績評估標準與配分總覽（期中 30% / 期末 30% / 平時 40%）",
            "subtitle": "落實產學實戰導向，兼顧職場出勤素養、個人構想提案與期末專案落地能力（各做各的個人獨立企劃）",
            "cards": [
                {
                    "title": "期中行銷企劃構想書 (30%)",
                    "theme": "blue",
                    "points": [
                        "第 9 週【期中週】進行個人提案發表與審查",
                        "包含：市場痛點定義、PESTEL 趨勢與競品分析 (15%)",
                        "包含：期中 40 題企劃觀念鑑定與口頭發表 (15%)",
                        "每位同學上傳至教學平台【學生作品成果展示廊】存檔"
                    ]
                },
                {
                    "title": "期末行銷企劃全案發表 (30%)",
                    "theme": "teal",
                    "points": [
                        "第 15~17 週進行個人口頭精華簡報與答辯 (每人 3-5 分鐘)",
                        "包含：企劃架構與邏輯嚴謹度 (10%)",
                        "包含：創意突破與市場可行性 (10%)",
                        "包含：GitHub Pages 線上展示與口頭答辯台風 (10%)"
                    ]
                },
                {
                    "title": "平時表現與出勤素養 (40%)",
                    "theme": "amber",
                    "points": [
                        "隨堂觀念快測與課堂互動表現 (10%)",
                        "個人實務研討與靈感抽卡發表 (10%)",
                        "進修部專業出勤紀律與自主學習態度 (20%)",
                        "★ 榮譽加分：考取 IPAS 雙證照或參賽加 5~10 分"
                    ]
                }
            ]
        },
        {
            "layout": "2card",
            "badge": "IPAS DUAL CERTIFICATIONS",
            "sec": "專業證照對接",
            "title": "國家級專業鑑定對接：經濟部 IPAS 雙證照加分機制",
            "subtitle": "本課程題庫深度整合經濟部 IPAS 專業能力鑑定，輔導同學考取國家級認證",
            "left": {
                "title": "IPAS 品牌規劃師 (Brand Planner)",
                "theme": "blue",
                "points": [
                    "鑑定科目一：品牌規劃與策略（STP、品牌核心價值、品牌識別）",
                    "鑑定科目二：品牌傳播與推廣（整合行銷傳播 IMC、公關策展、數位行銷）",
                    "教學平台內建完整題庫，含詳盡解析與曾光華參考章節對照",
                    "考取同學於學期總成績直接給予 +5 ~ +10 分專案加分！"
                ]
            },
            "right": {
                "title": "IPAS AI 應用規劃師 (AI Planner)",
                "theme": "teal",
                "points": [
                    "鑑定科目一：生成式 AI 基礎概念與技術架構（LLM、Agent、ReAct）",
                    "鑑定科目二：AI 商業應用與倫理法規（智慧行銷、隱私合規、提示工程）",
                    "教學平台題庫完整收錄，課堂隨時可手機刷題自主檢測",
                    "考取同學亦享有學期總成績 +5 ~ +10 分加分獎勵！"
                ]
            }
        },
        {
            "layout": "2card",
            "badge": "VIBE CODING PHILOSOPHY",
            "sec": "Vibe Coding 理念",
            "title": "什麼是 Vibe Coding？企管系學生的自然語言創造力",
            "subtitle": "前 Tesla AI 總監 Andrej Karpathy 揭示的新一代軟體建構思維",
            "left": {
                "title": "從「How to Code」到「What to Build」",
                "theme": "blue",
                "points": [
                    "傳統開發：耗費數月死記 HTML/CSS/JavaScript 語法與排除 Bug",
                    "Vibe Coding：以人類母語（自然語言）精準描述商業需求與功能氛圍",
                    "底層代碼交由 AI Agent 自主生成，人類專注於商業大局觀與品質驗收",
                    "企管系的優勢在於懂市場、懂受眾、懂痛點，這正是 AI 最需要的指引！"
                ]
            },
            "right": {
                "title": "CLEAR 提示詞架構黃金五步驟",
                "theme": "teal",
                "points": [
                    "C (Context 情境脈絡)：交代商業背景、產業現況與目標客群",
                    "L (Limits 邊界限制)：指定不要什麼、預算限制、字數與無後端約束",
                    "E (Expectation 產出期待)：設定驗收標準、風格調性與成功指標",
                    "A (Action 具體行動)：條列逐步任務，例如先做受眾 Persona 再寫企劃",
                    "R (Role 角色設定)：賦予頂級行銷總監、品牌顧問或資深活動策展人身份"
                ]
            }
        },
        {
            "layout": "3card",
            "badge": "3-STEP DEPLOYMENT",
            "sec": "GitHub Pages 免費部署",
            "title": "3 步驟將企劃成果發布為全球可瀏覽的專屬網址",
            "subtitle": "不花半毛錢、不需架設伺服器，30 秒建立個人行銷作品集網站",
            "cards": [
                {
                    "title": "步驟 1：建立 GitHub 儲存庫",
                    "theme": "blue",
                    "points": [
                        "免費註冊 GitHub.com 帳號",
                        "點選「New Repository」建立專案",
                        "勾選「Add a README file」建立主分支",
                        "命名為簡潔英數字 (如 tea-flash-mob)"
                    ]
                },
                {
                    "title": "步驟 2：上傳 index.html",
                    "theme": "teal",
                    "points": [
                        "點選「Add file」➔「Upload files」",
                        "將 AI 生成的專案檔案命名為 index.html",
                        "直接拖曳上傳至 GitHub 網頁視窗",
                        "點擊綠色「Commit changes」儲存"
                    ]
                },
                {
                    "title": "步驟 3：啟用 GitHub Pages",
                    "theme": "amber",
                    "points": [
                        "進入儲存庫「Settings」➔「Pages」",
                        "Source 選擇「Deploy from a branch」",
                        "Branch 選擇「main」並點擊 Save",
                        "30 秒後取得專屬網址，上傳至教學平台展示！"
                    ]
                }
            ]
        },
        {
            "layout": "closing",
            "title": "第一週單元導覽完畢：準備展開行銷企劃之旅！",
            "subtitle": "請同學們確立個人專案方向，並於課後查閱【Vibe Coding 操作手冊】進行首次實戰體驗！",
            "final_message": "本週行動：確立個人選題方向 ➔ 體驗市場情資 Agent ➔ 熟悉教學平台題庫與作品上傳"
        }
    ]
    curriculum.append({
        "week_num": 1,
        "module": "模組一：行銷企劃視野與 AI 賦能啟蒙",
        "title": "課程導論與破冰：行銷企劃新視野 ✕ Agentic AI 革命",
        "subtitle": "曾光華行銷企劃思維 ✕ Vibe Coding ✕ 評分標準 ✕ 題庫與作品上傳指引",
        "slides": w01_slides
    })

    # =========================================================================
    # WEEKS 02 - 18: 依照課綱精準生成
    # =========================================================================
    week_configs = [
        {
            "week": 2, "module": "模組一：行銷企劃視野與 AI 賦能啟蒙",
            "title": "行銷企劃的本質與邏輯思維", "chapter": "曾光華 CH01 行銷企劃的本質",
            "badge": "CH01 企劃本質", "hook": "為什麼多數行銷活動熱鬧收場卻沒帶來真實營收？",
            "points_c1": ["行銷企劃三要素：邏輯、創意、執行力", "企劃書的本質是「為特定商業問題提供可落地的系統性解方」", "避免『偽需求』：先問使用者願不願意付費或採取行動", "企劃書標準結構：現況診斷 ➔ 目標設定 ➔ 策略擬定 ➔ 執行方案 ➔ 效益評估"],
            "points_c2": ["假說思考法 (Hypothesis Thinking)：以終為始，先提出可驗證的假說", "MECE 原則：相互獨立、完全窮盡，避免策略盲點與邏輯重疊", "黃金圈理論 (Why ➔ How ➔ What)：從品牌初衷驅動消費者情感共鳴", "曾光華金句：沒有邏輯的創意是災難，缺乏創意的邏輯是平庸"],
            "points_c3": ["Agentic AI 的 ReAct 推理循環：Thought (思考) ➔ Action (行動) ➔ Observation (觀察)", "如何向 AI 指派「假說驗證」任務，避免 AI 產出空泛大話", "運用 CLEAR 框架引導 AI 生成市場痛點假說清單", "課堂演練：以身邊知名手搖飲為例，寫出 3 個關鍵商業假說"]
        },
        {
            "week": 3, "module": "模組一：行銷企劃視野與 AI 賦能啟蒙",
            "title": "行銷企劃目標設定與效益評估", "chapter": "曾光華 CH02 行銷企劃目標",
            "badge": "CH02 目標效益", "hook": "「提升品牌知名度」是合格的行銷目標嗎？",
            "points_c1": ["SMART 原則檢視：Specific、Measurable、Attainable、Relevant、Time-bound", "質化目標 vs 量化目標：知名度指數、官網造訪數、名單轉換率", "北極星指標 (North Star Metric)：驅動業務成長最核心的單一關鍵指標", "曾光華提醒：無法衡量的目標就無法管理與執行！"],
            "points_c2": ["數位行銷三大財務量化公式：CAC (顧客獲取成本) = 總行銷支出 / 獲客數", "LTV (顧客終身價值) = 平均消費額 × 購買頻次 × 留存時間", "ROAS (廣告投資報酬率) = 廣告帶來的營收 / 廣告花費", "損益兩平點 (BEP) 試算：固定成本 / (單價 - 單位變動成本)"],
            "points_c3": ["運用 Agent 5：價格促銷試算 Agent 進行 ROI 與損益情境模擬", "課後練習：設計一份促銷活動的 SMART 目標卡與損益推估表", "將量化指標具體融入期中期末企劃書的「預期效益」章節", "IPAS 品牌規劃師考點：品牌權益衡量指標與財務評估指標"]
        },
        {
            "week": 4, "module": "模組二：市場情資洞察與策略定位",
            "title": "外部環境分析：掌握趨勢與競爭格局", "chapter": "曾光華 CH03 外部環境分析",
            "badge": "CH03 外部環境", "hook": "當柯達發明數位相機時，為何仍走向破產命運？",
            "points_c1": ["PESTEL 宏觀環境六大維度：政治、經濟、社會文化、科技、環境、法律", "社會文化趨勢：台灣少子化、超高齡社會、單身寵物經濟、宅家外送商機", "科技趨勢：生成式 AI、社群短影音、無人無接觸零售", "從環境變化中捕捉未被滿足的市場空白點 (Market Gap)"],
            "points_c2": ["Michael Porter 五力分析模型：現有競爭者爭奪強度、新進入者威脅", "替代品威脅、供應商議價能力、買方顧客議價能力", "直接競爭者 vs 間接競爭者：Netflix 的對手不是迪士尼，而是『使用者的睡眠時間』", "知己知彼：建立競品攻防矩陣與差異化護城河"],
            "points_c3": ["運用 Agent 1：市場情資洞察 Agent 快速爬梳產業現況與 PESTEL 洞察", "引導 AI 扮演特定產業的資深市場分析師，挖掘非顯而易見的潛在威脅", "課堂實務研討：選擇一個傳統產業，列出其面臨的 3 大 PESTEL 衝擊與轉型解方", "期中企劃第一章節核心：市場背景與產業環境分析實戰撰寫"]
        },
        {
            "week": 5, "module": "模組二：市場情資洞察與策略定位",
            "title": "內部環境分析、SWOT 矩陣與 STP 受眾畫像", "chapter": "曾光華 CH04 內部環境分析 & CH05 STP",
            "badge": "CH04-05 策略定位", "hook": "「所有人都喜歡我的產品」是行銷最大的謊言？",
            "points_c1": ["企業內部資源與核心能力 (VRIO 框架)：價值性、稀缺性、難以模仿性、組織適應性", "動態 SWOT 分析：優勢 (S)、劣勢 (W)、機會 (O)、威脅 (T)", "TOWS 交叉矩陣戰略制定：SO 乘勝追擊、ST 多元避險、WO 借力補短、WT 防禦收縮", "拒絕列出毫無關聯的流水帳，SWOT 必須直接對應策略行動！"],
            "points_c2": ["STP 策略黃金三部曲：S (市場區隔) ➔ T (目標市場選擇) ➔ P (品牌心智定位)", "市場區隔變數：地理、人口統計、心理性格、行為購買頻次", "Persona 虛擬人物誌四大要素：基本輪廓、核心目標、痛點阻礙、日常接觸媒體", "定位知覺圖 (Perceptual Map)：找出市場藍海的獨特座標點"],
            "points_c3": ["運用 Agent 2：STP 市場定位 Agent ✕ Agent 3：受眾 Persona 描繪 Agent", "以自然語言生成活靈活現的目標消費者（名字、年齡、一天的生活作息與口頭禪）", "實體演練：繪製個人專案的目標顧客 Persona 海報與定位陳述句", "曾光華定位句公式：為【目標受眾】，【品牌】是【品類】中，提供【核心利益】的最優選擇"]
        },
        {
            "week": 6, "module": "模組二：市場情資洞察與策略定位",
            "title": "激發行銷企劃創意：SCAMPER 奔馳法與腦力激盪", "chapter": "曾光華 CH05 激發行銷企劃創意",
            "badge": "CH05 創意發想", "hook": "創意思維可以被系統化訓練與公式化生成嗎？",
            "points_c1": ["創意的本質是「舊元素的全新組合」與「打破慣性思維盲點」", "SCAMPER 奔馳法七大創新思考角度：Substitute 替代、Combine 結合", "Adapt 調適、Modify 放大/縮小、Put to another use 轉變用途", "Eliminate 消除冗餘、Reverse 逆向重組：顛覆常規創造驚喜！"],
            "points_c2": ["腦力激盪 (Brainstorming) 四大不可違背原則：延遲批判、追求數量、搭便車借力、自由奔放", "Crazy 8s 極速發想工作坊：8 分鐘畫出 8 個不同解決方案草圖", "HMW (How Might We 我們如何能夠...) 提問法：將問題轉化為探索機會", "從 100 個平庸想法中收斂篩選出 3 個最具爆發力與可行性的金點子"],
            "points_c3": ["教學平台【靈感抽卡機】課堂實戰：受眾 ✕ 痛點 ✕ 科技 ✕ 情境 4 軸隨機碰撞", "指揮 AI Agent 扮演 SCAMPER 創意激發特工，一秒產出 10 個跨界行銷玩法", "課堂個人競賽：現場抽卡並於 15 分鐘內發表一個個人極限創意提案", "期中企劃核心章節：創新亮點與差異化價值主張"]
        },
        {
            "week": 7, "module": "模組二：市場情資洞察與策略定位",
            "title": "期中前觀念整合、個人企劃主題確立與實務審查", "chapter": "階段整合 & 實務審查",
            "badge": "階段整合", "hook": "你的行銷企劃案到底要賣什麼？給誰？為什麼非買不可？",
            "points_c1": ["企劃構想書 (Proposal Draft) 關鍵結構審查：企劃名稱、緣起與背景", "市場痛點定義、目標受眾 Persona、STP 定位知覺圖、初步 4P 方向", "甘特圖 (Gantt Chart) 時程規劃：各階段里程碑與個人進度排程", "曾光華診斷清單：檢查邏輯鏈條是否前後一致、有無自相矛盾之處"],
            "points_c2": ["教師一對一面對面深度輔導 (Office Hour 現場版)：診斷每位同學選題商業可行性", "常見新手致命病灶：客群定義太寬泛、痛點不痛、缺乏獲利邏輯", "同儕觀摩機制：同學間交換企劃構想草案，提出 3 個建設性改進建議", "進企管四系3甲各同學專案定錨：結合個人職場經歷或生活興趣選題"],
            "points_c3": ["教學平台【學生作品成果展示廊】：學習如何上傳期中企劃草案與備忘錄", "期中 40 題鑑定測驗複習重點：涵蓋 CH01~CH05 企劃觀念與 IPAS 核心題型", "個人備戰第 9 週期中發表：投影片製作與 3 分鐘電梯簡報演練", "成果存檔：將企劃大綱與提示詞歷程記錄於教學網站"]
        },
        {
            "week": 8, "module": "模組三：4P 策略實務與專案執行",
            "title": "新產品上市行銷企劃：從概念測試到上市引爆", "chapter": "曾光華 CH06 新產品上市行銷企劃",
            "badge": "CH06 新產品上市", "hook": "新產品上市失敗率高達 75%，如何打造爆款成功突圍？",
            "points_c1": ["新產品開發流程 (NPD)：構想產生 ➔ 概念發展與測試 ➔ 商業分析 ➔ 原型開發 ➔ 市場試銷 ➔ 全面商品化", "產品生命週期 (PLC) 四階段：導入期、成長期、成熟期、衰退期", "不同 PLC 階段的行銷目標與預算資源配置策略", "概念測試 (Concept Testing)：在投入大量生產前，先用一頁式網頁驗證購買意向"],
            "points_c2": ["新產品上市三階段引爆模型：預熱期 (Teaser 造勢、早鳥名單收集)", "引爆期 (Launch 發表會、KOL 評測開箱、限時首發優惠)", "延續期 (Sustain 口碑擴散、UGC 社群分享、轉化為常態營運)", "行銷包裝與視覺第一印象：黃金 3 秒吸引眼球的視覺焦點法則"],
            "points_c3": ["運用 Agent 4：產品價值主張與上市規劃 Agent，梳理產品 3 大殺手級賣點", "運用 Vibe Coding 理念：在上市前先用 AI 產出「一頁式預售概念頁」進行冒煙測試", "課堂個人實作：為個人新產品設計預熱期 7 天倒數社群貼文排程與早鳥誘因", "曾光華叮嚀：上市不是結束，而是持續依據市場反饋疊代優化的起點"]
        },
        {
            "week": 9, "module": "模組三：4P 策略實務與專案執行",
            "title": "【期中週】行銷企劃構想書 (Proposal Draft) 發表與期中測驗", "chapter": "期中檢核與成果展示",
            "badge": "期中週", "hook": "行銷人最重要的戰場：如何在 3 分鐘內說服台下主管與投資人？",
            "points_c1": ["【期中發表】每人 2 ~ 3 分鐘精實提案發表 (占期中 15%)", "評審指標：痛點清晰度 (30%)、策略邏輯度 (30%)、簡報台風與時間掌握 (40%)", "全班使用教學平台進行同儕即時評分與客觀留言反饋", "展現進修部同學專業素養：著正裝、條理分明、直球對決商業問題"],
            "points_c2": ["【期中測驗】企劃核心能力 40 題線上快測 (占期中 15%)", "涵蓋範圍：曾光華 CH01~CH06 核心企劃架構 ✕ IPAS 品牌與 AI 證照題庫", "手機即時點選作答，系統即時計算得分並產出雷達圖與錯題診斷筆記", "讓同學清楚掌握自身觀念強弱項，落實 OBE 成果導向學習成效驗證"],
            "points_c3": ["【成果繳交】每位同學將《期中行銷企劃構想書》上傳至教學平台作品展示廊", "上傳包含：提案標題、個人姓名、受眾 Persona 摘要與所使用的 Agent 提示詞", "教師期中總結回饋：彙整全班提案共通優點與下半學期深化方向", "期末目標預告：下半學期將企劃案全面升級為可點開操作的 GitHub Pages 線上服務！"]
        },
        {
            "week": 10, "module": "模組三：4P 策略實務與專案執行",
            "title": "公關與事件行銷企劃：話題造勢與危機預防", "chapter": "曾光華 CH07 公關與事件行銷企劃",
            "badge": "CH07 公關與事件", "hook": "當公關危機在社群網路 10 分鐘內發酵，品牌如何黃金滅火？",
            "points_c1": ["公共關係 (PR) 的本質：建立與維持企業與多元利害關係人間的信任資產", "公關企劃 vs 廣告投放：第三者背書的公信力價值遠勝自吹自擂的自營廣告", "新聞稿 (Press Release) 結構：倒金字塔寫法、吸睛標題、新聞五要素 (5W1H)、發言人引言", "媒體溝通守則：不提供假消息、尊重媒體截稿時間、建立良好媒體關係資料庫"],
            "points_c2": ["事件行銷 (Event Marketing) 策展關鍵：創造具備「自傳播屬性」的沉浸式話題場景", "快閃店 (Pop-up Store)、品牌聯名策展 (Co-branding)、社群挑戰賽機制設計", "公關危機應對三大黃金法則：真實誠懇、承擔責任、極速回應 (黃金 3 小時)", "負面輿情監測與應急預案 (SOP)：成立危機小組、統一口徑、避免火上加油"],
            "points_c3": ["運用 Agent 6：公關活動與危機預防 Agent 撰寫專業新聞稿與突發危機聲明稿", "課堂演練：模擬「外送餐點發現異物」或「產品標錯超低價格」之突發危機公關危機應對", "分析台灣近期知名餐飲/品牌公關翻車與神級滅火經典案例", "期末企劃章節要求：每人全案須包含一份具體的快閃公關事件與危機應急指引"]
        },
        {
            "week": 11, "module": "模組三：4P 策略實務與專案執行",
            "title": "促銷企劃案：誘因設計、排程與利潤損益試算", "chapter": "曾光華 CH08 促銷企劃案",
            "badge": "CH08 促銷企劃", "hook": "折扣打得越深越好賣？為什麼無腦降價只會加速品牌自毀？",
            "points_c1": ["促銷 (Sales Promotion) 的定義：在特定期間內提供額外誘因以刺激快速購買", "促銷三大對象：消費者促銷 (Pull 拉力)、通路商促銷 (Push 推力)、業務人員激勵", "常見消費者促銷手法：折價券、滿額贈品、抽獎刮刮樂、買一送一、集點回購", "曾光華警告：過度依賴價格折扣會侵蝕品牌價值與顧客心理參考價格！"],
            "points_c2": ["促銷排程與節慶行銷日曆：雙11、雙12、母親節、週年慶、中秋檔期佈局", "早鳥倒數優惠 (Early Bird) 與急迫感心理學：數量有限、限時 48 小時倒數", "促銷財務效益評估公式：活動邊際貢獻 = (增加銷量 × 單位毛利) - 促銷總成本", "防範套利漏洞：防刷單、防止大量囤貨倒賣之風控條款設計"],
            "points_c3": ["運用 Agent 5：價格促銷與利潤試算 Agent 快速推算不同折數下的損益兩平銷量", "實務試算演練：原價 $500，成本 $200，若打 8 折 ($400)，銷量必須成長多少才不會虧損？", "個人設計一份「下月主題促銷活動企劃案」：包含誘因組合、排程表與行銷預算表", "IPAS 品牌規劃師重要考點：推拉策略整合與促銷活動評估維度"]
        },
        {
            "week": 12, "module": "模組四：行銷科技應用與專案衝刺",
            "title": "其他類行銷企劃案例：數位行銷與行銷科技 (MarTech) 實務應用", "chapter": "曾光華 CH09 其他類行銷企劃案例",
            "badge": "CH09 數位與 MarTech", "hook": "當全球 MarTech 工具突破 14,000 種，現代行銷人該如何組裝工具鏈？",
            "points_c1": ["整合行銷傳播 (IMC)：橫跨線上與線下所有接觸點，傳遞始終如一的品牌核心訊息", "Scott Brinker MarTech 6 大構面：廣告促成、內容體驗、社群關係、商業銷售、數據分析、管理流程", "全通路 (Omnichannel) 零售 OMO 整合：實體門市體驗 ✕ 線上私域流量 (LINE OA) 沉澱", "顧客旅程地圖 (Customer Journey Map)：認知 ➔ 考慮 ➔ 購買 ➔ 留存 ➔ 倡導五階段接觸點優化"],
            "points_c2": ["社群短影音行銷實務：TikTok、Instagram Reels、YouTube Shorts 演算法邏輯", "黃金 3 秒抓眼球心法：提出反直覺觀點、拋出巨大懸念、展現強烈視覺對比", "爆款文案架構：痛點場景 ➔ 權威解方 ➔ 社會認同 ➔ 明確行動呼籲 (Call To Action)", "私域流量經營：LINE 官方帳號分眾標籤、自動化歡迎訊息與會員分級制度"],
            "points_c3": ["運用 Agent 7：社群短影音與爆款文案 Agent，一鍵產出 30 秒短影音分鏡腳本與文案", "指揮 AI Agent 扮演高轉換率社群小編，撰寫適合 IG 與 Threads 的吸睛貼文", "課堂體驗：拆解知名手搖飲與電商的 LINE 官方帳號互動閉環設計", "將數位行銷導流體系完整整合進個人期末企劃全案中"]
        },
        {
            "week": 13, "module": "模組四：行銷科技應用與專案衝刺",
            "title": "行銷企劃的撰寫與簡報：結構說服力與提案必勝技", "chapter": "曾光華 CH10 行銷企劃的撰寫與簡報",
            "badge": "CH10 企劃撰寫與簡報", "hook": "一份 50 頁的企劃書與一份 10 頁的企劃書，主管到底看哪裡？",
            "points_c1": ["企劃書標準十大骨幹結構：摘要 ➔ 環境分析 ➔ 目標 ➔ STP ➔ 4P方針 ➔ 時程 ➔ 預算 ➔ 效益 ➔ 應急 ➔ 附錄", "執行摘要 (Executive Summary) 的重要性：CEO 與投資人往往只花 2 分鐘閱讀這 1 頁！", "金字塔原理 (The Pyramid Principle)：結論先行、由上而下、歸納總結，論述層次分明", "版面排版美學：圖表大於表格、表格大於文字，統一主色調，拒絕五顏六色"],
            "points_c2": ["簡報說服結構 SCQA 架構：Situation (情境) ➔ Complication (衝突) ➔ Question (疑問) ➔ Answer (解方)", "10/20/30 簡報黃金法則：不超過 10 頁、不超過 20 分鐘、字體不小於 30pt (適應大教室投影機)", "口頭發表的舞台魅力：眼神接觸、肢體語言、停頓控場與答辯防禦邏輯", "進修部同學職場必備軟實力：如何優雅回答主管與評審的刁鑽提問"],
            "points_c3": ["運用 Agent 8：企劃書全案架構與審查評估 Agent 進行企劃書邏輯漏洞自主診斷", "檢核個人期末全案的財務預算表與甘特時程表是否自洽", "課堂發表模擬演練：每人上台進行 1 分鐘極限電梯簡報 (Elevator Pitch)", "準備進入第 14 週多代理人衝刺與第 15~17 週期末正式口頭發表！"]
        },
        {
            "week": 14, "module": "模組四：行銷科技應用與專案衝刺",
            "title": "期末企劃專案衝刺：Multi-Agent 多代理人協同企劃演練", "chapter": "專案整合與部署衝刺",
            "badge": "多特工衝刺", "hook": "一個人如何像一整間跨國廣告代理商一樣高效運作？",
            "points_c1": ["Multi-Agent (多代理人協同) 架構解析：任務分配 ➔ 專業代理人並行推理 ➔ 主管代理人總結", "將行銷企劃團隊化為 4 位虛擬專家：市場調查特工、策略顧問特工、創意文案特工、財務分析特工", "人類的角色：擔任最終決策者 (Human-in-the-Loop)，負責把關方向與驗收成果", "提升生產力 10 倍的秘訣：讓正確的 AI 特工做最專長的事！"],
            "points_c2": ["Vibe Coding 終極落地指南：將個人行銷企劃案化為真實可運作的單頁網頁 (MVP)", "首頁 Hero 視覺 ➔ 核心賣點 3 欄卡片 ➔ 顧客見證 ➔ 線上預約/訂購表單 ➔ 頁尾版權", "GitHub Pages 免費全球上線：30 秒取得公開網址 (https://username.github.io/repo/)", "手機自適應排版 (RWD) 檢查：確保手機掃碼即可秒開操作，無破版、無跑版"],
            "points_c3": ["教學平台【學生作品成果展示廊】期末全案上傳規範宣導", "必填項目：企劃標題、學生姓名與學號、企劃摘要、使用的 Agent 提示詞、GitHub Pages 網址", "教師面對面實機巡檢與給予個別優化建議：修正連結、微調文案、強化排版質感", "公布第 15~17 週個人口頭發表抽籤順序與答辯評分標準"]
        },
        {
            "week": 15, "module": "模組五：期末行銷企劃全案發表與驗收",
            "title": "期末企劃實作發表 (一)：個人成果口頭精華簡報 (第一梯次)", "chapter": "期末發表 Stage 1",
            "badge": "期末發表 01", "hook": "舞台已經準備好，進修部同學的精彩個人提案即刻登場！",
            "points_c1": ["【發表規範】每人 3 ~ 5 分鐘口頭簡報 + 2 分鐘評審答辯 (佔期末 30%)", "現場結合大螢幕投影展示簡報投影片與 GitHub Pages 線上運作網站", "檢核重點：痛點洞察真實性、曾光華 4P 策略深度、AI 協同歷程與網站互動體驗", "全班同學使用教學平台【學生作品展示廊】即時瀏覽成果並進行同儕互評"],
            "points_c2": ["第一梯次同學發表：涵蓋大園在地桑葚果茶、青埔毛孩友善輕食等生活化專案", "實務檢驗：現場展示手機掃描 GitHub Pages 實際預約或加入拼單流暢度", "答辯環節重點：面對客群規模質疑、預算 ROI 推估合理性之專業回應", "同儕即時評分：針對商業創意、可行性與台風進行星等評定與鼓勵"],
            "points_c3": ["教師講評與現場即時反饋：肯定商業切角創意、點評策略防禦力與執行細節", "互評學習：觀察發表同學在台風、簡報視覺與時間控制上的亮點與可借鏡之處", "後續發表同學觀摩吸取經驗，針對個人簡報做最後微調修正", "所有發表同學於下課前確認專案已完整存檔於教學平台展示中心"]
        },
        {
            "week": 16, "module": "模組五：期末行銷企劃全案發表與驗收",
            "title": "期末企劃實作發表 (二)：個人成果口頭精華簡報 (第二梯次)", "chapter": "期末發表 Stage 2",
            "badge": "期末發表 02", "hook": "跨領域行銷創意的激烈碰撞：大健康、文創與綠色永續！",
            "points_c1": ["【發表規範】每人 3 ~ 5 分鐘口頭簡報 + 2 分鐘評審答辯 (佔期末 30%)", "延續嚴謹評分規準：策略邏輯 (10%) + 創意突破 (10%) + 發表台風與網站展示 (10%)", "同儕線上互評機制：透過平台針對各專案痛點解方給予星等與實質建議", "時間控制精準度考核：按鈴提醒時間，訓練職場高管會議時間紀律"],
            "points_c2": ["第二梯次同學發表：涵蓋熟齡機能堅果奶、文青節氣香氛蠟燭、ESG 裸裝洗沐等", "展現多元產業觸角：高齡化商機、情緒療癒經濟、ESG 綠色消費轉型", "答辯互動：師生針對通路拓展門檻與社群獲客成本進行深入交流", "肯定各做各的獨立精神：每個人都有獨一無二的商業靈魂與熱忱"],
            "points_c3": ["教師深度講評：剖析在定價策略 (曾光華 CH07) 與通路整合 (CH08) 上的邏輯深度", "表揚具備真實市場驗證數據之專案（如三天內累積數百筆試飲名單）", "引導同學思考：如何將課堂企劃成果進一步轉化為校內外創新創業競賽提案", "確認第二梯次同學專案檔案與 GitHub Pages 連結正常載入"]
        },
        {
            "week": 17, "module": "模組五：期末行銷企劃全案發表與驗收",
            "title": "期末企劃實作發表 (三)：個人成果口頭精華簡報 (第三梯次) 與總結", "chapter": "期末發表 Stage 3",
            "badge": "期末發表 03", "hook": "最後一波精彩提案壓軸登場，見證全班行銷思維的蛻變！",
            "points_c1": ["【發表規範】每人 3 ~ 5 分鐘口頭簡報 + 2 分鐘評審答辯 (佔期末 30%)", "第三梯次壓軸展演：結合個人職場經歷與前沿 MarTech 工具之實務企劃", "全班同儕互評成績即時彙整，計入平時互動研討總成績", "每位同學都是專業評審：練習從主管或投資人角度評鑑企劃案的商業潛力"],
            "points_c2": ["壓軸同學亮點發表：涵蓋校園外送拼單、二手循環、健康輕食預約等實用專案", "評審答辯精采交鋒：針對競爭對手反制策略、促銷毛利底線進行實戰防禦", "全班同學全面完成課堂個人口頭發表，展現進企管四系3甲極高專業水準！", "見證成果：人人皆能運用 Agentic AI 與 Vibe Coding 將個人企劃想法落地為線上作品！"],
            "points_c3": ["教師針對全班個人發表進行總體趨勢講評：肯定同學白天工作繁忙仍能獨立產出高水準全案", "同儕互評數據公開：揭曉全班人氣最高專案與最佳簡報台風獎候選名單", "提醒期末成績最後結算叮嚀：補齊缺漏作業、核對平時出勤與快測紀錄", "預告第 18 週【期末週】總結表揚大會與未來職涯賦能展望"]
        },
        {
            "week": 18, "module": "模組五：期末行銷企劃全案發表與驗收",
            "title": "【期末週】學習成果總結、優秀專案表揚與未來展望", "chapter": "期末總結與未來展望",
            "badge": "期末結業", "hook": "這學期你收穫的不只是一張成績單，而是一套帶得走的行銷超能力！",
            "points_c1": ["全學期 18 週知識大圖鑑回顧：曾光華行銷企劃十大步驟 ✕ Agentic AI 工具鏈", "從 W01 破冰與 Vibe Coding 啟蒙，到 PESTEL、STP、4P 策略、危機公關與全案發表", "進修部企管同學的自信躍升：跳脫語法恐懼，以商業大局觀成為 AI 的戰略指揮官", "這份 GitHub Pages 線上專案將成為你履歷上最亮眼的實戰作品！"],
            "points_c2": ["【榮譽表揚】頒發學期優秀行銷企劃專案獎：最佳商業價值獎、最具創意突破獎、最佳視覺呈現獎", "【IPAS 證照加分結算】登記並核發經濟部 IPAS「品牌規劃師」與「AI 應用規劃師」榮譽加分 (+5~10分)", "學習歷程檔案匯出：每位同學可於教學平台【個人歷程與勳章】一鍵匯出學習成果報告", "同儕感言交流：分享白天工作與夜間進修如何激盪出更深刻的商業洞察"],
            "points_c3": ["未來展望：生成式 AI 浪潮下企管人才的不可替代性（同理心、策略決策、倫理判斷）", "邱俊維 博士結業寄語：永遠保持對市場的好奇心，勇敢用 AI 放大你的商業影響力！", "教學平台將持續開放在線，歡迎同學回顧題庫自主進修與更新作品", "11501 創意行銷企劃實務 圓滿結業！祝福各位在職場與人生成為最耀眼的行銷企劃大師！"]
        }
    ]

    for wc in week_configs:
        slides = [
            {
                "layout": "cover",
                "badge": f"第 {wc['week']:02d} 週 ｜ {wc['badge']} ｜ 萬能企管進修部",
                "title": wc["title"],
                "subtitle": f"{wc['chapter']} ✕ Agentic AI 智慧代理人實務應用",
                "meta": [
                    f"萬能科技大學 企業管理系 (進企管四系3甲)",
                    f"授課地點：F401 教室 ｜ 授課教師：邱俊維 博士",
                    f"參考用書：曾光華《行銷企劃：邏輯、創意、執行力》(2026 第五版)"
                ]
            },
            {
                "layout": "1card",
                "badge": "THEORETICAL CORE",
                "sec": "學理核心精講",
                "title": f"本週核心學理深度解析：{wc['chapter']}",
                "subtitle": wc["hook"],
                "card": {
                    "title": "曾光華權威企劃思維架構",
                    "theme": "blue",
                    "points": wc["points_c1"]
                }
            },
            {
                "layout": "2card",
                "badge": "STRATEGIC DEEP DIVE",
                "sec": "策略推演實務",
                "title": "商業策略推演與行銷分析工具落實",
                "subtitle": "以嚴謹管理邏輯剖析市場情境，避免陷入憑空猜想的無效企劃",
                "left": {
                    "title": "企劃方法論與分析模型",
                    "theme": "indigo",
                    "points": wc["points_c2"]
                },
                "right": {
                    "title": "Agentic AI 協同工作流",
                    "theme": "teal",
                    "points": wc["points_c3"]
                }
            },
            {
                "layout": "3card",
                "badge": "ACTION PLAN",
                "sec": "課堂演練與成果交付",
                "title": "本週 F401 課堂實務演練 ✕ 課後實踐任務",
                "subtitle": "結合理論講授、個人實作、隨堂快測與 GitHub Pages 專案累積（各做各的個人獨立企劃）",
                "cards": [
                    {
                        "title": "1. 課堂實務演練 (F401 教室)",
                        "theme": "blue",
                        "points": [
                            "手機開啟教學平台參與即時觀念快測",
                            "每位同學針對本週個案進行 25 分鐘獨立發想與實務討論",
                            "搭配靈感抽卡機與 SCAMPER 激發創意",
                            "參與隨機抽籤發表，爭取平時互動表現分"
                        ]
                    },
                    {
                        "title": "2. 課後 Agentic AI 企劃工坊",
                        "theme": "teal",
                        "points": [
                            "登入教學平台【回家練習：AI 企劃工坊】",
                            "操作 8 大行銷企劃 Agent 範本",
                            "以 CLEAR 框架引導 AI 產出企劃草稿",
                            "記錄優質提示詞歷程，充實專案附錄"
                        ]
                    },
                    {
                        "title": "3. 作品上傳與題庫練習",
                        "theme": "amber",
                        "points": [
                            "將本週進度上傳至【學生作品成果展示廊】",
                            "可附上 GitHub Pages 網址提供線上預覽",
                            "自主練習 IPAS 品牌規劃師/AI 題庫",
                            "累積解鎖學習成就徽章與個人歷程"
                        ]
                    }
                ]
            },
            {
                "layout": "closing",
                "title": f"第 {wc['week']:02d} 週單元授課完畢！",
                "subtitle": f"感謝各位進修部同學的專注投入！請妥善保存討論成果並推進企劃進度。",
                "final_message": "實踐承諾：扎實學理 (曾光華) ✕ Agentic AI 協同 ➔ GitHub Pages 成果落地 ➔ 職涯黃金作品集"
            }
        ]
        curriculum.append({
            "week_num": wc["week"],
            "module": wc["module"],
            "title": wc["title"],
            "subtitle": f"{wc['chapter']} ✕ Agentic AI 智慧代理人實務應用",
            "slides": slides
        })

    return curriculum

def build_presentation_html():
    curriculum = generate_curriculum_slides()
    total_slides = sum(len(w["slides"]) for w in curriculum)
    print(f"Total weeks: {len(curriculum)}, Total slides generated: {total_slides}")

    curriculum_json = json.dumps(curriculum, ensure_ascii=False, indent=2)

    html_content = f"""<!DOCTYPE html>
<html lang="zh-TW" class="h-full">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>創意行銷企劃實務 ✕ Agentic AI ｜ 18 週全景教學簡報投影系統</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Noto+Sans+TC:wght@400;500;700;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['"Noto Sans TC"', '"Plus Jakarta Sans"', 'sans-serif'],
                        mono: ['"JetBrains Mono"', 'monospace'],
                    }},
                    colors: {{
                        navy: {{ 900: '#070d1e', 800: '#0f172a', 700: '#1e293b' }},
                        brand: {{ blue: '#2563eb', teal: '#0d9488', emerald: '#059669', amber: '#d97706', gold: '#f59e0b', indigo: '#4f46e5' }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{
            font-family: 'Noto Sans TC', sans-serif;
            background-color: #0b1120;
            color: #f1f5f9;
        }}
        .custom-scrollbar::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}
        .custom-scrollbar::-webkit-scrollbar-track {{
            background: #0f172a;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{
            background: #334155;
            border-radius: 4px;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {{
            background: #475569;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .animate-fadeIn {{
            animation: fadeIn 0.18s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }}

        /* 滿版無黑邊全螢幕模式 (100% 覆蓋投影幕，絕無四周空黑框) */
        :fullscreen, :-webkit-full-screen, body.is-fullscreen-active {{
            background-color: #020617 !important;
            width: 100vw !important;
            height: 100vh !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
        }}

        :fullscreen header, :-webkit-full-screen header, body.is-fullscreen-active header,
        :fullscreen footer, :-webkit-full-screen footer, body.is-fullscreen-active footer {{
            display: none !important;
        }}

        :fullscreen main, :-webkit-full-screen main, body.is-fullscreen-active main {{
            padding: 0 !important;
            margin: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            max-width: 100vw !important;
            max-height: 100vh !important;
            background: #020617 !important;
        }}

        :fullscreen #slideStage, :-webkit-full-screen #slideStage, body.is-fullscreen-active #slideStage {{
            max-width: 100vw !important;
            max-height: 100vh !important;
            width: 100vw !important;
            height: 100vh !important;
            border-radius: 0 !important;
            border: none !important;
            margin: 0 !important;
            padding: 2.5rem 4rem !important;
            background: #090e1a !important;
            box-shadow: none !important;
        }}

        /* 視窗模式自適應填滿 */
        #slideStage {{
            max-width: 100% !important;
            width: 100% !important;
            height: 100% !important;
        }}

        /* 全螢幕微型懸浮操控列 (滑鼠接近右上角時浮現，平常淡化避免干擾) */
        .fs-floating-bar {{
            display: none;
        }}
        :fullscreen .fs-floating-bar, :-webkit-full-screen .fs-floating-bar, body.is-fullscreen-active .fs-floating-bar {{
            display: flex !important;
            position: fixed;
            top: 1.25rem;
            right: 1.5rem;
            z-index: 99999;
            opacity: 0.2;
            transition: opacity 0.25s ease, transform 0.25s ease;
        }}
        .fs-floating-bar:hover {{
            opacity: 1;
            transform: scale(1.02);
        }}

        /* 內容字體大小 28 點規格 (28pt ≈ 37.33px，大教室投影機遠距專用) */
        .point-28pt {{
            font-size: 24pt !important;
            line-height: 1.48 !important;
        }}

        @media (max-width: 1536px) {{
            .point-28pt {{
                font-size: 20pt !important;
                line-height: 1.42 !important;
            }}
        }}
        @media (max-width: 1280px) {{
            .point-28pt {{
                font-size: 17pt !important;
                line-height: 1.38 !important;
            }}
        }}
        @media (max-width: 768px) {{
            .point-28pt {{
                font-size: 15pt !important;
                line-height: 1.35 !important;
            }}
        }}
    </style>
</head>
<body class="h-full flex flex-col overflow-hidden select-none bg-slate-950 text-slate-100">

    <!-- 全螢幕專用微型懸浮控制列 (僅在全螢幕時顯示於右上角) -->
    <div id="fsFloatingBar" class="fs-floating-bar items-center gap-2 bg-slate-900/90 border border-slate-700/80 px-3 py-1.5 rounded-xl shadow-2xl backdrop-blur-md">
        <button id="fsBtnPrev" class="bg-slate-800 hover:bg-slate-700 active:scale-95 text-white p-1.5 rounded-lg text-xs font-bold transition-all" title="上一頁 (←)">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7"/></svg>
        </button>
        <span id="fsPageIndicator" class="text-teal-300 font-mono text-xs font-bold px-2">1 / 5</span>
        <button id="fsBtnNext" class="bg-blue-600 hover:bg-blue-500 active:scale-95 text-white p-1.5 rounded-lg text-xs font-bold transition-all" title="下一頁 (→ 或 空白鍵)">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"/></svg>
        </button>
        <button id="fsBtnExit" class="bg-slate-800 hover:bg-red-600 text-slate-300 hover:text-white p-1.5 rounded-lg text-xs font-bold ml-1 transition-colors" title="退出全螢幕 (Esc 或 F)">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
    </div>

    <!-- Top Navigation Bar -->
    <header class="h-16 bg-slate-900/95 border-b border-slate-800 px-4 md:px-6 flex items-center justify-between shrink-0 shadow-lg z-30">
        <div class="flex items-center gap-3">
            <div class="w-3 h-8 bg-gradient-to-b from-blue-500 to-teal-400 rounded-full"></div>
            <div>
                <span class="text-xs text-teal-400 font-bold tracking-wider block">萬能科技大學 企業管理系 (進企管四系3甲) ｜ F401 教室</span>
                <h1 class="text-base md:text-lg font-black text-white tracking-wide truncate max-w-xs md:max-w-md">
                    創意行銷企劃實務 ✕ Agentic AI
                </h1>
            </div>
            <span id="curriculumModuleTag" class="hidden xl:inline-block text-xs font-bold px-2.5 py-1 bg-blue-950/80 border border-blue-600/50 text-blue-300 rounded-lg ml-2"></span>
        </div>

        <div class="flex items-center gap-2 md:gap-3">
            <!-- 回教學平台按鈕 -->
            <a href="index.html" class="hidden sm:inline-flex items-center gap-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white px-3 py-1.5 rounded-lg text-xs font-bold border border-slate-700 transition-colors">
                <i class="fas fa-home"></i> 教學首頁
            </a>

            <!-- Week Selector -->
            <select id="weekSelect" class="bg-slate-800 border border-slate-700 text-white text-xs md:text-sm font-bold rounded-lg px-2.5 py-1.5 focus:ring-2 focus:ring-blue-500 outline-none cursor-pointer hover:bg-slate-750 transition-colors">
            </select>

            <!-- Slide Selector -->
            <select id="slideSelect" class="bg-slate-800 border border-slate-700 text-white text-xs md:text-sm font-bold rounded-lg px-2.5 py-1.5 focus:ring-2 focus:ring-teal-500 outline-none cursor-pointer hover:bg-slate-750 transition-colors max-w-[140px] md:max-w-[260px] truncate">
            </select>

            <!-- Page Indicator -->
            <div id="pageIndicator" class="bg-slate-800/90 border border-slate-700 text-teal-300 font-mono text-xs md:text-sm font-bold px-3 py-1.5 rounded-lg shrink-0">
                1 / 8
            </div>

            <!-- Prev / Next Controls -->
            <button id="btnPrev" class="bg-slate-800 hover:bg-slate-700 active:scale-95 text-white p-1.5 md:px-3 md:py-1.5 rounded-lg text-sm font-bold border border-slate-700 flex items-center gap-1 transition-all shadow" title="上一頁 (←)">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7"/></svg>
                <span class="hidden md:inline">上一頁</span>
            </button>
            <button id="btnNext" class="bg-blue-600 hover:bg-blue-500 active:scale-95 text-white p-1.5 md:px-3 md:py-1.5 rounded-lg text-sm font-bold border border-blue-500 flex items-center gap-1 transition-all shadow-md shadow-blue-600/30" title="下一頁 (→ 或 空白鍵)">
                <span class="hidden md:inline">下一頁</span>
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"/></svg>
            </button>

            <!-- Fullscreen Button -->
            <button id="btnFullscreen" class="bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white p-1.5 rounded-lg border border-slate-700 transition-colors ml-1" title="全螢幕投影模式 (F 或 F11)">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-5h-4m4 0v4m0-4l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"/></svg>
            </button>
        </div>
    </header>

    <!-- Slide Presentation Canvas Stage -->
    <main class="flex-1 overflow-hidden p-1.5 md:p-3 flex items-center justify-center bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 w-full h-full">
        <div id="slideStage" class="w-full h-full bg-slate-900/90 rounded-2xl md:rounded-3xl border border-slate-800 shadow-2xl p-5 md:p-8 lg:p-10 flex flex-col justify-between relative overflow-hidden backdrop-blur-sm">
            <!-- Rendered dynamically -->
        </div>
    </main>

    <!-- Bottom Status Bar -->
    <footer class="h-9 bg-slate-950 border-t border-slate-800/80 px-6 flex items-center justify-between text-xs text-slate-400 shrink-0">
        <div class="flex items-center gap-4">
            <span class="flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                <span>授課教師：邱俊維 博士 (jimchiu@mail.vnu.edu.tw ｜ J801-1 研究室)</span>
            </span>
            <span class="text-slate-600">|</span>
            <span class="hidden sm:inline text-slate-400">快捷鍵：[← / →] 上下頁 ｜ [空白鍵] 下一頁 ｜ [F] 全螢幕投影 ｜ [Home/End] 首尾頁</span>
        </div>
        <div class="text-slate-400 font-medium">
            參考用書：曾光華《行銷企劃：邏輯、創意、執行力》(2026 第五版)
        </div>
    </footer>

    <script>
    // Embedded 18-Week Curriculum Slides Data
    const CURRICULUM = {curriculum_json};

    let currentWeekIdx = 0;
    let currentSlideIdx = 0;

    function initUI() {{
        const weekSelect = document.getElementById('weekSelect');
        weekSelect.innerHTML = '';
        CURRICULUM.forEach((w, idx) => {{
            const opt = document.createElement('option');
            opt.value = idx;
            opt.textContent = `第 ${{w.week_num < 10 ? '0' + w.week_num : w.week_num}} 週：${{w.title.slice(0, 16)}}...`;
            weekSelect.appendChild(opt);
        }});

        weekSelect.addEventListener('change', (e) => {{
            currentWeekIdx = parseInt(e.target.value);
            currentSlideIdx = 0;
            loadWeek();
        }});

        const slideSelect = document.getElementById('slideSelect');
        slideSelect.addEventListener('change', (e) => {{
            currentSlideIdx = parseInt(e.target.value);
            renderCurrentSlide();
        }});

        document.getElementById('btnPrev').addEventListener('click', prevSlide);
        document.getElementById('btnNext').addEventListener('click', nextSlide);
        document.getElementById('btnFullscreen').addEventListener('click', toggleFullscreen);

        // Floating full-screen buttons
        document.getElementById('fsBtnPrev').addEventListener('click', prevSlide);
        document.getElementById('fsBtnNext').addEventListener('click', nextSlide);
        document.getElementById('fsBtnExit').addEventListener('click', toggleFullscreen);

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {{
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT') return;
            if (e.key === 'ArrowRight' || e.key === 'Space' || e.key === 'PageDown') {{
                e.preventDefault();
                nextSlide();
            }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
                e.preventDefault();
                prevSlide();
            }} else if (e.key === 'Home') {{
                e.preventDefault();
                currentSlideIdx = 0;
                renderCurrentSlide();
            }} else if (e.key === 'End') {{
                e.preventDefault();
                const total = CURRICULUM[currentWeekIdx].slides.length;
                currentSlideIdx = total - 1;
                renderCurrentSlide();
            }} else if (e.key === 'f' || e.key === 'F') {{
                e.preventDefault();
                toggleFullscreen();
            }}
        }});

        // Fullscreen state listener
        document.addEventListener('fullscreenchange', () => {{
            if (document.fullscreenElement) {{
                document.body.classList.add('is-fullscreen-active');
            }} else {{
                document.body.classList.remove('is-fullscreen-active');
            }}
        }});

        loadWeek();
    }}

    function loadWeek() {{
        const week = CURRICULUM[currentWeekIdx];
        document.getElementById('weekSelect').value = currentWeekIdx;
        const tag = document.getElementById('curriculumModuleTag');
        if (tag) tag.textContent = week.module || '專業核心模組';

        const slideSelect = document.getElementById('slideSelect');
        slideSelect.innerHTML = '';
        week.slides.forEach((s, idx) => {{
            const opt = document.createElement('option');
            opt.value = idx;
            opt.textContent = `P.${{idx + 1}} ${{s.title ? s.title.slice(0, 18) : '簡報頁'}}...`;
            slideSelect.appendChild(opt);
        }});

        renderCurrentSlide();
    }}

    function escapeHtml(str) {{
        if (!str) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;');
    }}

    function getThemeStyles(theme) {{
        switch(theme) {{
            case 'teal':
                return {{ border: 'border-teal-500/70', bar: 'from-teal-500 to-emerald-400', text: 'text-teal-400', badge: 'bg-teal-950/80 text-teal-300 border-teal-600/50' }};
            case 'amber':
                return {{ border: 'border-amber-500/70', bar: 'from-amber-500 to-yellow-400', text: 'text-amber-400', badge: 'bg-amber-950/80 text-amber-300 border-amber-600/50' }};
            case 'indigo':
                return {{ border: 'border-indigo-500/70', bar: 'from-indigo-500 to-purple-400', text: 'text-indigo-400', badge: 'bg-indigo-950/80 text-indigo-300 border-indigo-600/50' }};
            case 'rose':
                return {{ border: 'border-rose-500/70', bar: 'from-rose-500 to-pink-400', text: 'text-rose-400', badge: 'bg-rose-950/80 text-rose-300 border-rose-600/50' }};
            case 'blue':
            default:
                return {{ border: 'border-blue-500/70', bar: 'from-blue-500 to-teal-400', text: 'text-blue-400', badge: 'bg-blue-950/80 text-blue-300 border-blue-600/50' }};
        }}
    }}

    function renderHeader(badge, sec, title, subtitle, curNum, total) {{
        return `
        <div class="border-b border-slate-800 pb-3 mb-3 shrink-0">
            <div class="flex items-center justify-between mb-1.5">
                <div class="flex items-center gap-2">
                    <span class="text-xs font-black tracking-widest px-2.5 py-0.5 rounded bg-blue-950/80 border border-blue-600/60 text-blue-300 uppercase">
                        ${{escapeHtml(badge || '萬能企管 創意行銷企劃實務')}}
                    </span>
                    ${{sec ? `<span class="text-xs font-bold text-slate-400">/ ${{escapeHtml(sec)}}</span>` : ''}}
                </div>
                <span class="text-xs font-mono font-bold text-teal-400 bg-slate-800/80 px-2 py-0.5 rounded border border-slate-700">
                    SLIDE ${{curNum}} OF ${{total}}
                </span>
            </div>
            <h2 class="text-2xl md:text-3xl font-black text-white tracking-tight leading-snug">
                ${{escapeHtml(title || '')}}
            </h2>
            ${{subtitle ? `<p class="text-slate-300 text-sm md:text-base font-semibold mt-1 leading-normal truncate">${{escapeHtml(subtitle)}}</p>` : ''}}
        </div>
        `;
    }}

    function renderCurrentSlide() {{
        const week = CURRICULUM[currentWeekIdx];
        const slides = week.slides;
        if (currentSlideIdx >= slides.length) currentSlideIdx = slides.length - 1;
        if (currentSlideIdx < 0) currentSlideIdx = 0;

        const slide = slides[currentSlideIdx];
        const stage = document.getElementById('slideStage');
        const curNum = currentSlideIdx + 1;
        const total = slides.length;

        document.getElementById('pageIndicator').textContent = `${{curNum}} / ${{total}}`;
        document.getElementById('fsPageIndicator').textContent = `${{curNum}} / ${{total}}`;
        document.getElementById('slideSelect').value = currentSlideIdx;

        let html = '';
        const layout = slide.layout || '1card';

        if (layout === 'cover') {{
            html = `
            <div class="h-full flex flex-col justify-between px-4 md:px-12 py-4 animate-fadeIn">
                <div class="flex items-center justify-between border-b border-slate-800 pb-4">
                    <span class="text-xs md:text-sm font-bold tracking-widest text-teal-400 px-3 py-1 rounded-full bg-teal-950/60 border border-teal-500/40">
                        ${{escapeHtml(slide.badge || '萬能科技大學 企業管理系')}}
                    </span>
                    <span class="text-xs md:text-sm font-mono text-slate-400">11501 學期 ｜ 進企管四系3甲</span>
                </div>
                <div class="my-auto py-6">
                    <h1 class="text-3xl md:text-5xl lg:text-6xl font-black text-white tracking-tight leading-tight mb-4 drop-shadow-lg">
                        ${{escapeHtml(slide.title)}}
                    </h1>
                    <p class="text-lg md:text-2xl font-bold text-teal-300 max-w-4xl leading-relaxed">
                        ${{escapeHtml(slide.subtitle)}}
                    </p>
                </div>
                <div class="pt-4 border-t border-slate-800 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs md:text-sm text-slate-300">
                    ${{(slide.meta || []).map(m => `
                    <div class="flex items-center gap-2 bg-slate-800/60 p-2.5 rounded-xl border border-slate-700/60">
                        <span class="w-2 h-2 rounded-full bg-blue-400 shrink-0"></span>
                        <span class="font-medium">${{escapeHtml(m)}}</span>
                    </div>
                    `).join('')}}
                </div>
            </div>
            `;
        }} else if (layout === '1card') {{
            const card = slide.card || {{}};
            const tCard = getThemeStyles(card.theme || 'blue');
            html = `
            <div class="h-full flex flex-col animate-fadeIn">
                ${{renderHeader(slide.badge, slide.sec, slide.title, slide.subtitle, curNum, total)}}
                <div class="flex-1 flex flex-col justify-center py-2 overflow-y-auto custom-scrollbar">
                    <div class="bg-slate-800/90 rounded-2xl border-2 ${{tCard.border}} p-6 md:p-8 shadow-2xl relative overflow-hidden">
                        <div class="absolute top-0 left-0 right-0 h-2 bg-gradient-to-r ${{tCard.bar}}"></div>
                        <h3 class="text-xl md:text-2xl font-black ${{tCard.text}} mb-4">
                            ${{escapeHtml(card.title)}}
                        </h3>
                        <ul class="space-y-3.5">
                            ${{(card.points || []).map(p => `
                            <li class="flex items-start gap-3 text-slate-100 point-28pt font-medium leading-relaxed">
                                <span class="${{tCard.text}} font-black text-2xl shrink-0 mt-0.5">•</span>
                                <span class="${{p.includes('★') ? 'text-amber-300 font-bold' : ''}}">${{escapeHtml(p)}}</span>
                            </li>
                            `).join('')}}
                        </ul>
                    </div>
                </div>
            </div>
            `;
        }} else if (layout === '2card') {{
            const left = slide.left || {{}};
            const right = slide.right || {{}};
            const tLeft = getThemeStyles(left.theme || 'blue');
            const tRight = getThemeStyles(right.theme || 'teal');
            html = `
            <div class="h-full flex flex-col animate-fadeIn">
                ${{renderHeader(slide.badge, slide.sec, slide.title, slide.subtitle, curNum, total)}}
                <div class="flex-1 grid grid-cols-1 md:grid-cols-2 gap-4 lg:gap-6 py-2 items-stretch overflow-y-auto custom-scrollbar">
                    <div class="bg-slate-800/90 rounded-2xl border-2 ${{tLeft.border}} p-5 lg:p-7 flex flex-col shadow-2xl relative overflow-hidden">
                        <div class="absolute top-0 left-0 right-0 h-2 bg-gradient-to-r ${{tLeft.bar}}"></div>
                        <h3 class="text-xl md:text-2xl font-black ${{tLeft.text}} mb-3.5">
                            ${{escapeHtml(left.title)}}
                        </h3>
                        <ul class="space-y-3">
                            ${{(left.points || []).map(p => `
                            <li class="flex items-start gap-2.5 text-slate-100 point-28pt font-medium leading-relaxed">
                                <span class="${{tLeft.text}} font-black text-2xl shrink-0 mt-0.5">•</span>
                                <span class="${{p.includes('★') ? 'text-amber-300 font-bold' : ''}}">${{escapeHtml(p)}}</span>
                            </li>
                            `).join('')}}
                        </ul>
                    </div>
                    <div class="bg-slate-800/90 rounded-2xl border-2 ${{tRight.border}} p-5 lg:p-7 flex flex-col shadow-2xl relative overflow-hidden">
                        <div class="absolute top-0 left-0 right-0 h-2 bg-gradient-to-r ${{tRight.bar}}"></div>
                        <h3 class="text-xl md:text-2xl font-black ${{tRight.text}} mb-3.5">
                            ${{escapeHtml(right.title)}}
                        </h3>
                        <ul class="space-y-3">
                            ${{(right.points || []).map(p => `
                            <li class="flex items-start gap-2.5 text-slate-100 point-28pt font-medium leading-relaxed">
                                <span class="${{tRight.text}} font-black text-2xl shrink-0 mt-0.5">•</span>
                                <span class="${{p.includes('★') ? 'text-amber-300 font-bold' : ''}}">${{escapeHtml(p)}}</span>
                            </li>
                            `).join('')}}
                        </ul>
                    </div>
                </div>
            </div>
            `;
        }} else if (layout === '3card') {{
            const cards = slide.cards || [];
            html = `
            <div class="h-full flex flex-col animate-fadeIn">
                ${{renderHeader(slide.badge, slide.sec, slide.title, slide.subtitle, curNum, total)}}
                <div class="flex-1 grid grid-cols-1 md:grid-cols-3 gap-4 lg:gap-5 py-2 items-stretch overflow-y-auto custom-scrollbar">
                    ${{cards.map((c, idx) => {{
                        const tCard = getThemeStyles(c.theme || (idx === 0 ? 'blue' : (idx === 1 ? 'teal' : 'amber')));
                        return `
                        <div class="bg-slate-800/90 rounded-2xl border-2 ${{tCard.border}} p-5 lg:p-6 flex flex-col shadow-2xl relative overflow-hidden">
                            <div class="absolute top-0 left-0 right-0 h-2 bg-gradient-to-r ${{tCard.bar}}"></div>
                            <h3 class="text-lg md:text-xl font-black ${{tCard.text}} mb-3.5">
                                ${{escapeHtml(c.title)}}
                            </h3>
                            <ul class="space-y-2.5">
                                ${{(c.points || []).map(p => `
                                <li class="flex items-start gap-2.5 text-slate-100 point-28pt font-medium leading-relaxed">
                                    <span class="${{tCard.text}} font-black text-xl shrink-0 mt-0.5">•</span>
                                    <span class="${{p.includes('★') ? 'text-amber-300 font-bold' : ''}}">${{escapeHtml(p)}}</span>
                                </li>
                                `).join('')}}
                            </ul>
                        </div>
                        `;
                    }}).join('')}}
                </div>
            </div>
            `;
        }} else if (layout === 'closing') {{
            html = `
            <div class="h-full flex flex-col justify-center px-6 md:px-16 animate-fadeIn">
                <div class="inline-block px-4 py-1.5 rounded-xl bg-amber-600 text-white font-black text-sm md:text-base tracking-widest mb-4 w-fit shadow-xl shadow-amber-500/30">
                    WEEKLY UNIT COMPLETED
                </div>
                <h2 class="text-3xl md:text-5xl lg:text-6xl font-black text-white mb-5 leading-tight max-w-5xl drop-shadow-md">
                    ${{escapeHtml(slide.title || '單元授課完畢')}}
                </h2>
                <p class="text-xl md:text-2xl text-slate-200 font-bold max-w-4xl leading-relaxed mb-6">
                    ${{escapeHtml(slide.subtitle || '感謝各位的專注投入與深度研討！請同學們妥善保存企劃進度。')}}
                </p>
                <div class="pt-5 border-t-2 border-slate-800 text-base md:text-lg font-bold text-teal-400">
                    ${{escapeHtml(slide.final_message || '期末成果閉環：曾光華企劃架構 ✕ Agentic AI 協同 ➔ GitHub Pages 全球發布 ➔ 期末發表全案展示')}}
                </div>
            </div>
            `;
        }}

        stage.innerHTML = html;
    }}

    function prevSlide() {{
        if (currentSlideIdx > 0) {{
            currentSlideIdx--;
            renderCurrentSlide();
        }} else if (currentWeekIdx > 0) {{
            currentWeekIdx--;
            const prevWeekSlides = CURRICULUM[currentWeekIdx].slides;
            currentSlideIdx = prevWeekSlides.length - 1;
            loadWeek();
        }}
    }}

    function nextSlide() {{
        const currentWeekSlides = CURRICULUM[currentWeekIdx].slides;
        if (currentSlideIdx < currentWeekSlides.length - 1) {{
            currentSlideIdx++;
            renderCurrentSlide();
        }} else if (currentWeekIdx < CURRICULUM.length - 1) {{
            currentWeekIdx++;
            currentSlideIdx = 0;
            loadWeek();
        }}
    }}

    function toggleFullscreen() {{
        if (!document.fullscreenElement) {{
            if (document.documentElement.requestFullscreen) {{
                document.documentElement.requestFullscreen().then(() => {{
                    document.body.classList.add('is-fullscreen-active');
                }}).catch(err => {{
                    console.log("Fullscreen request failed, applying fallback", err);
                    document.body.classList.toggle('is-fullscreen-active');
                }});
            }} else {{
                document.body.classList.toggle('is-fullscreen-active');
            }}
        }} else {{
            if (document.exitFullscreen) {{
                document.exitFullscreen().then(() => {{
                    document.body.classList.remove('is-fullscreen-active');
                }}).catch(() => {{
                    document.body.classList.remove('is-fullscreen-active');
                }});
            }} else {{
                document.body.classList.remove('is-fullscreen-active');
            }}
        }}
    }}

    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', initUI);
    }} else {{
        initUI();
    }}
    </script>
</body>
</html>
"""

    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Full_Screen_Presentation.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Successfully generated Full_Screen_Presentation.html at: {output_path}")

if __name__ == '__main__':
    build_presentation_html()
