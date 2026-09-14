# -*- coding: utf-8 -*-
"""
tools/build_vibe_slides.py
Generates data/vibe_slides.json containing 18 weeks x 8 slides = 144 unique slides.
Each week covers its dedicated UI component, prompt, HTML/CSS/JS, RWD, GitHub Pages deploy, and debugging.
"""
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(BASE_DIR, 'data', 'vibe_slides.json')

VIBE_COMPONENTS = {
    1: ("Hero 視覺區塊 ✕ 品牌調性", "首屏全寬大標題、漸層背景與核心價值", "header.hero", "現代深藍紫微漸層搭配白色大字"),
    2: ("一頁式標準 5 大區塊搭建", "Header、痛點、解方、證明、Footer", "main.landing-container", "高對比清爽卡片式模組排版"),
    3: ("Hero 區塊大標題與 CTA 按鈕", "高轉換率 Call-to-Action 行動按鈕", "button.cta-primary", "亮橘色按鈕帶有呼吸光暈動態效果"),
    4: ("PESTEL 6 欄響應式網格卡片組件", "政治、經濟、社會、科技、環境、法規", "div.pestel-grid", "CSS Grid 響應式 3 欄自適應排版"),
    5: ("3 欄式競品對比卡片網頁組件", "我方優勢 vs 直接對手 vs 跨界替代品", "div.pricing-compare", "中間推薦卡片凸起且加金邊微陰影"),
    6: ("核心價值主張 (UVP) 卡片", "獨特價值主張與顧客三大核心利益", "div.uvp-card-group", "毛玻璃磨砂效果搭配圓角微投影"),
    7: ("互動式 SWOT 九宮格點擊展開模組", "點擊卡片彈出視窗查看策略詳情", "div.swot-matrix-modal", "CSS Flex 佈局搭配 JavaScript Modal 彈窗"),
    8: ("課堂靈感抽卡機與便利貼倒數計時", "隨機抽選 SCAMPER 靈感卡與限時器", "div.card-picker-timer", "隨機數演算法與純 CSS 翻卡動畫"),
    9: ("期中提案一頁式成果展示頁發布", "章節平滑滾動導覽與成果卡片", "nav.sticky-nav", "平滑滾動 smooth-scroll 與 Sticky 導航"),
    10: ("新產品線上早鳥預購一頁式網頁", "預購數量選擇器與前台表單驗證", "form.preorder-form", "原生 HTML5 表單驗證與即時金額加總"),
    11: ("倒數計時器 (Countdown) 與限量標籤", "最後席次急迫感與倒數計時", "div.countdown-badge", "setInterval 遞減秒數與紅標跳動動畫"),
    12: ("快閃活動報名表單與時間軸組件", "垂直時序圖呈現活動三大流程", "div.vertical-timeline", "垂直線條連接圓點節點之時間軸"),
    13: ("常見問答 (FAQ) 折疊手風琴組件", "點擊展開收合解答與平滑過渡", "div.accordion-item", "details/summary 或 JS 點擊切換高度"),
    14: ("折價券領取彈窗與滿額免運進度條", "新客折價券彈窗與消費進度條", "div.coupon-popup-bar", "固定底端浮動條搭配動態寬度進度"),
    15: ("LINE 官方帳號導流與多連結導航頁", "手機版專屬 Link in Bio 多功能跳轉", "div.link-in-bio", "直式卡片堆疊與社群圖示漸變按鈕"),
    16: ("個人行銷企劃全案單頁展示官網", "十大章節錨點跳轉與全案目錄", "section.full-case-site", "側邊目錄欄與滾動監聽 active 狀態"),
    17: ("個人成果作品集首頁 (Portfolio)", "作品網格瀑布流展示與外鏈預覽", "div.portfolio-grid", "懸停圖片放大與作品資訊浮現效果"),
    18: ("作品上傳教學展示廊並永久保存", "整合 Google 試算表與雲端展示", "div.gallery-viewer", "動態讀取 JSON 渲染全班作品展示牆")
}

def generate_vibe_slides():
    vibe_slides = {}

    for w in range(1, 19):
        comp_name, comp_desc, dom_sel, visual_style = VIBE_COMPONENTS[w]
        w_slides = []

        # P.36 (Vibe.01)
        w_slides.append({
            'badge': f'VIBE CODING 原型實作 ｜ 第 {w:02d} 週',
            'sec': '數位原型 P.01',
            'title': f'{comp_name}：轉換戰略定位',
            'subtitle': f'第 {w} 週主題組件：為何「{comp_name}」是行銷網頁的核心抓手',
            'layout': '2card',
            'left': {
                'title': '行銷溝通痛點與目標',
                'theme': 'blue',
                'points': [
                    f'痛點：傳統書面企劃缺乏即時互動感',
                    f'角色：{comp_desc}',
                    '吸睛力：在 3 秒內抓住目標客群目光',
                    '引導力：降低認知負荷引導採取行動'
                ]
            },
            'right': {
                'title': '零代碼意圖驅動理念',
                'theme': 'teal',
                'points': [
                    '無需背誦語法：以自然語言下達意圖',
                    '企管核心：專注於內容訊息與排版邏輯',
                    '即時回饋：所見即所得快速修改微調',
                    '商務價值：企劃案附帶可點擊網頁原型'
                ]
            }
        })

        # P.37 (Vibe.02)
        w_slides.append({
            'badge': f'VIBE CODING 原型實作 ｜ 第 {w:02d} 週',
            'sec': '數位原型 P.02',
            'title': '自然語言意圖提示詞 (Vibe Prompt)',
            'subtitle': f'如何對 AI Studio 或 Cursor 下達指令生成「{comp_name}」',
            'layout': '2card',
            'left': {
                'title': '結構化提示詞公式',
                'theme': 'blue',
                'points': [
                    f'「請幫我建立一個行銷網頁組件：{comp_name}」',
                    f'「視覺風格要求：{visual_style}」',
                    '「響應式規範：確保手機與電腦皆完美呈現」',
                    '「技術要求：純 HTML/CSS/JS 單一檔案產出」'
                ]
            },
            'right': {
                'title': '行銷文案內嵌指示',
                'theme': 'teal',
                'points': [
                    '填入真實企劃文案，杜絕 Lorem Ipsum',
                    '字體要求：使用乾淨微軟正黑體或思源黑體',
                    '行動呼籲：文字需具備強烈召喚力',
                    '色彩規範：呼應品牌主題調性色彩'
                ]
            }
        })

        # P.38 (Vibe.03)
        w_slides.append({
            'badge': f'VIBE CODING 原型實作 ｜ 第 {w:02d} 週',
            'sec': '數位原型 P.03',
            'title': 'HTML 語意化結構骨架剖析',
            'subtitle': f'看懂「{dom_sel}」骨架結構，掌握網頁組件之積木原理',
            'layout': '3card',
            'cards': [
                {
                    'title': '1. 外層容器 (Container)',
                    'theme': 'blue',
                    'points': [
                        f'標籤選擇：使用語意化 {dom_sel.split(".")[0]}',
                        '類別命名：給予清楚 class 易於辨識',
                        '最大寬度限制：設定 max-width 1200px',
                        '自動水平置中：margin: 0 auto 規範'
                    ]
                },
                {
                    'title': '2. 核心內容層 (Body)',
                    'theme': 'teal',
                    'points': [
                        '主標題：以 h2 或 h3 標註核心訊息',
                        '段落說明：以 p 標籤承載輔助說明文字',
                        '資訊群組：善用 div 包裹獨立資訊單元',
                        '圖文整合：使用 img 或 svg 圖示強化焦點'
                    ]
                },
                {
                    'title': '3. 互動按鈕層 (Action)',
                    'theme': 'amber',
                    'points': [
                        '觸發元件：使用 a 連結或 button 標籤',
                        '無障礙標籤：標記 aria-label 增進體驗',
                        '點擊回饋：設定指針游標 cursor: pointer',
                        '跳轉錨點：設定 href 導向特定轉換段落'
                    ]
                }
            ]
        })

        # P.39 (Vibe.04)
        w_slides.append({
            'badge': f'VIBE CODING 原型實作 ｜ 第 {w:02d} 週',
            'sec': '數位原型 P.04',
            'title': 'CSS 現代美學排版與視覺調教',
            'subtitle': f'打造「{visual_style}」的高質感商業介面美學',
            'layout': '2card',
            'left': {
                'title': '色彩與背景設計規範',
                'theme': 'blue',
                'points': [
                    '主色調配置：佔比 60% 營造沉穩品牌氛圍',
                    '強調色配置：佔比 10% 用於關鍵按鈕焦點',
                    '字體對比：確保深淺對比符合閱讀舒適度',
                    '留白呼吸感：加大 padding 避免擁擠窒息'
                ]
            },
            'right': {
                'title': '圓角、陰影與微互動',
                'theme': 'teal',
                'points': [
                    '圓角設計：border-radius: 12px 溫潤現代',
                    '多層微陰影：box-shadow 營造精緻立體懸浮',
                    '懸停過渡：transition: all 0.3s 平滑反饋',
                    '按鈕按壓感：transform: translateY(-2px)'
                ]
            }
        })

        # P.40 (Vibe.05)
        w_slides.append({
            'badge': f'VIBE CODING 原型實作 ｜ 第 {w:02d} 週',
            'sec': '數位原型 P.05',
            'title': 'JavaScript 核心互動控制要領',
            'subtitle': f'賦予「{comp_name}」動態生命力，零基礎也能看懂的邏輯',
            'layout': '3card',
            'cards': [
                {
                    'title': '1. 選取目標元素',
                    'theme': 'blue',
                    'points': [
                        '語法：document.querySelector()',
                        f'目標：準確鎖定 {dom_sel}',
                        '指派變數：儲存元件方便後續操作',
                        '安全防護：檢查元素是否存在防報錯'
                    ]
                },
                {
                    'title': '2. 監聽使用者動作',
                    'theme': 'teal',
                    'points': [
                        '事件綁定：addEventListener()',
                        '常見動作：click 點擊、scroll 滾動',
                        '即時反應：使用者一觸碰立刻觸發指令',
                        '防止跳頁：event.preventDefault()'
                    ]
                },
                {
                    'title': '3. 切換視覺狀態',
                    'theme': 'amber',
                    'points': [
                        '類別切換：classList.toggle("active")',
                        '顯示隱藏：修改 display 或 opacity',
                        '數值計算：即時更新購物金額或折扣',
                        '彈出提示：優雅呈現操作成功訊息'
                    ]
                }
            ]
        })

        # P.41 (Vibe.06)
        w_slides.append({
            'badge': f'VIBE CODING 原型實作 ｜ 第 {w:02d} 週',
            'sec': '數位原型 P.06',
            'title': '手機直式瀏覽 (RWD) 響應式檢測',
            'subtitle': '台灣超過 85% 訪客使用手機瀏覽！排版絕不能跑版破裂',
            'layout': '2card',
            'left': {
                'title': '手機端版面自適應法則',
                'theme': 'blue',
                'points': [
                    '視窗標籤：必備 viewport meta 宣告',
                    '多欄自動折行：電腦 3 欄變為手機單欄',
                    '按鈕觸控區域：高度至少 44px 方便大拇指',
                    '字體大小調降：標題縮減至 22~26px 適配小螢幕'
                ]
            },
            'right': {
                'title': 'F12 開發者工具檢驗三步驟',
                'theme': 'teal',
                'points': [
                    '按下 F12：切換至手機模擬裝置視角',
                    '選擇機型：切換 iPhone 14/15 尺寸測試',
                    '水平滑動檢查：杜絕出現惱人的左右捲軸',
                    '字級閱讀檢核：確認免放大即可舒適閱讀'
                ]
            }
        })

        # P.42 (Vibe.07)
        w_slides.append({
            'badge': f'VIBE CODING 原型實作 ｜ 第 {w:02d} 週',
            'sec': '數位原型 P.07',
            'title': 'GitHub Pages 30 秒一鍵全球上線',
            'subtitle': '完全免費、免伺服器，將你的數位原型變成全世界可開網址',
            'layout': '3card',
            'cards': [
                {
                    'title': '步驟一：建立倉庫',
                    'theme': 'blue',
                    'points': [
                        '登入個人的 GitHub 免費帳號',
                        '新建 Repository 並勾選 Public 公開',
                        '專案命名規範：英文字母無空格',
                        '將網頁代碼命名為 index.html'
                    ]
                },
                {
                    'title': '步驟二：上傳檔案',
                    'theme': 'teal',
                    'points': [
                        '點擊 Upload files 將檔案拖拉上傳',
                        '輸入 Commit message 點擊綠色確認',
                        '等待檔案完成雲端儲存與版控',
                        '單一 html 檔架構維護最為簡便'
                    ]
                },
                {
                    'title': '步驟三：啟用 Pages',
                    'theme': 'amber',
                    'points': [
                        '進入專案 Settings ➔ 左側 Pages 分頁',
                        'Branch 選擇 main 點擊 Save 儲存',
                        '等待 30 秒重新整理獲得專屬網址',
                        '複製網址即可分享至社群或履歷'
                    ]
                }
            ]
        })

        # P.43 (Vibe.08)
        w_slides.append({
            'badge': f'VIBE CODING 原型實作 ｜ 第 {w:02d} 週',
            'sec': '數位原型 P.08',
            'title': '零基礎除錯急救包與避坑指引',
            'subtitle': f'遇到跑版、按鈕沒反應？三句指令讓 AI 瞬間修復「{comp_name}」',
            'layout': '2card',
            'left': {
                'title': '常見初學者三大地雷',
                'theme': 'rose',
                'points': [
                    '地雷一：檔名未命名為 index.html 導致 404',
                    '地雷二：CSS 漏寫關閉括號導致整頁破版',
                    '地雷三：圖片外鏈失效顯示破損打叉圖標',
                    '警惕：不要手動亂改不懂的代碼片段'
                ]
            },
            'right': {
                'title': 'AI 急救修復指令模板',
                'theme': 'teal',
                'points': [
                    '「我手機上看按鈕文字被截斷，請修正」',
                    '「點擊時彈窗沒有跳出來，請檢查 JS 語法」',
                    '「請將所有 CSS 與 JS 合併回單一檔案」',
                    '將整段代碼貼給 AI，要求一鍵修復即可'
                ]
            }
        })

        vibe_slides[str(w)] = w_slides

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(vibe_slides, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated {len(vibe_slides)} weeks of vibe slides to {OUTPUT_PATH}")

if __name__ == '__main__':
    generate_vibe_slides()
