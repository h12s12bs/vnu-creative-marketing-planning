# -*- coding: utf-8 -*-
import sys, json, os

ref = json.load(open('w6_ref_dump.json', encoding='utf-8'))
raw = ref['slides']

def clean_text(t):
    if not isinstance(t, str):
        return t
    # Replace crass words
    t = t.replace('廢話', '口號套話')
    t = t.replace('空洞', '抽象空泛')
    # Replace cramming / preview words
    t = t.replace('下周單元預告', '次週單元研討')
    t = t.replace('下週單元預告', '次週單元研討')
    t = t.replace('下週主題預告', '次週單元研討')
    t = t.replace('下週課程預告', '學理閉環與思維深化')
    t = t.replace('下週精彩預告', '學理閉環與思維深化')
    t = t.replace('下週預告', '次週單元研討')
    t = t.replace('下週見', '共同邁進')
    t = t.replace('自主溫習指引', '課後重點複習')
    t = t.replace('自主溫習', '自主研讀')
    t = t.replace('自我檢核清單', '專業思維維度診斷')
    t = t.replace('自我檢核', '專業維度診斷')
    t = t.replace('自我評量', '專業評估')
    t = t.replace('掌握期中期末重點', '深化策略分析涵養')
    t = t.replace('輕鬆準備考試', '從容掌握商管本質')
    t = t.replace('曾光華', '經典行銷企劃學理')
    t = t.replace('核心考點', '專業核心要點')
    t = t.replace('應試精華', '策略分析精華')
    # Replace student activities / homework
    t = t.replace('抽籤', '隨機演示')
    t = t.replace('作業一', '實務練習一')
    t = t.replace('作業二', '實務練習二')
    t = t.replace('作業三', '實務練習三')
    t = t.replace('作業驗收', '實務驗證')
    t = t.replace('課後作業', '課後實踐思考')
    t = t.replace('繳交報告', '研究彙整')
    t = t.replace('交報告', '研究整理')
    t = t.replace('期中報告', '期中企劃專案')
    t = t.replace('期末報告', '期末企劃成果')
    t = t.replace('手稿妥善保存', '成果妥善存檔')
    t = t.replace('學生作品展示廊', '企業案例展示廊')
    t = t.replace('大亂鬥實戰', '商業模式重組推演實戰')
    t = t.replace('大一小組', '專案團隊')
    t = t.replace('各組同學', '企劃團隊')
    t = t.replace('各位同學', '企劃人員')
    t = t.replace('各組', '專案團隊')
    t = t.replace('小組', '團隊')
    t = t.replace('分組', '團隊')
    t = t.replace('工作坊任務一', '實務推演階段一')
    t = t.replace('工作坊任務二', '實務推演階段二')
    t = t.replace('工作坊任務三', '實務推演階段三')
    t = t.replace('工作坊', '實務專題')
    return t

def format_pt(p):
    p = clean_text(p).strip()
    if p.startswith('★') or p.startswith('•'):
        return p
    return '★ ' + p

slides = []

# Slide 1: Cover
slides.append({
    'layout': 'cover',
    'badge': 'WEEK 06 ｜ CH05 激發行銷企劃創意（上） · 01/62',
    'title': '激發行銷企劃創意（上）：逆向假設分析法、全新情境法與加減乘除移五法',
    'subtitle': '破除慣性思維 ✕ 產品重組創新 ✕ 全新情境法 ✕ 智慧發散推演',
    'meta': [
        '萬能科技大學 企業管理系 (進企管四系3甲)',
        '授課地點：F401 教室 ｜ 授課教師：邱俊維 博士',
        '參考教材：激發行銷企劃創意經典理論體系',
        '核心能力：逆向假設分析、全新情境構建與加減乘除移重組創新'
    ]
})

# Slides 2 to 32: Adapt from raw with clean_text and format_pt
for i in range(1, 32):
    s = raw[i]
    layout = s.get('layout')
    badge = f'WEEK 06 ｜ CH05 激發行銷企劃創意（上） · {i+1:02d}/62'
    sec = clean_text(s.get('sec', '創意思考學理'))
    title = clean_text(s.get('title', ''))
    subtitle = clean_text(s.get('subtitle', ''))

    if layout == '2card':
        left = {
            'title': clean_text(s.get('leftTitle', s.get('left', {}).get('title', ''))),
            'theme': s.get('left', {}).get('theme', 'blue'),
            'points': [format_pt(p) for p in (s.get('leftPoints') or s.get('left', {}).get('points', []))]
        }
        right = {
            'title': clean_text(s.get('rightTitle', s.get('right', {}).get('title', ''))),
            'theme': s.get('right', {}).get('theme', 'teal'),
            'points': [format_pt(p) for p in (s.get('rightPoints') or s.get('right', {}).get('points', []))]
        }
        slides.append({
            'layout': '2card',
            'badge': badge,
            'sec': sec,
            'title': title,
            'subtitle': subtitle,
            'left': left,
            'right': right
        })
    elif layout == '1card':
        card_data = s.get('card', {})
        c_title = clean_text(card_data.get('title', title))
        c_points = [format_pt(p) for p in card_data.get('points', [])]
        slides.append({
            'layout': '1card',
            'badge': badge,
            'sec': sec,
            'title': title,
            'subtitle': subtitle,
            'card': {
                'title': c_title,
                'theme': card_data.get('theme', 'blue'),
                'points': c_points
            }
        })
    elif layout == '3card':
        cards_raw = s.get('cards', [])
        cards = []
        themes = ['blue', 'teal', 'amber']
        for c_idx, c in enumerate(cards_raw):
            cards.append({
                'num': f'0{c_idx+1}',
                'title': clean_text(c.get('title', '')),
                'theme': themes[c_idx % 3],
                'points': [format_pt(p) for p in c.get('points', [])]
            })
        slides.append({
            'layout': '3card',
            'badge': badge,
            'sec': sec,
            'title': title,
            'subtitle': subtitle,
            'cards': cards
        })
    elif layout == 'section':
        slides.append({
            'layout': 'section',
            'num': s.get('num', 'CHAPTER SECTION'),
            'title': clean_text(s.get('title', '')),
            'desc': clean_text(s.get('desc', ''))
        })

# Slide 33: Section 06
slides.append({
    'layout': 'section',
    'num': 'CHAPTER 06',
    'title': '加減乘除移五法：企業商業模式重組推演實戰',
    'desc': '系統化解構企業慣性假設，以加減乘除移五大運算法則推演顛覆性商業模式'
})

# Slide 34: 商業假設大盤點
slides.append({
    'layout': '2card',
    'badge': 'WEEK 06 ｜ CH05 激發行銷企劃創意（上） · 34/62',
    'sec': '商業模式重組實戰',
    'title': '商業假設大盤點：企業慣性思維之深層解構',
    'subtitle': '揭示阻礙產業創新的隱形枷鎖，系統化盤點五大理所當然的營運偏見',
    'left': {
        'title': '企業常見的慣性假設盲區',
        'theme': 'rose',
        'points': [
            '★【通路依賴假設】：認定產品必須透過既有實體門市或大型電商貨架才能抵達顧客',
            '★【計價常規假設】：堅信服務必須以次數或時間計費，價格必須比照市場現有行情折讓',
            '★【交付流程假設】：認定顧客必須親臨現場挑選，流程所有環節均需人工逐項核對交付',
            '★【顧客心智認知】：習慣認定既有客群的偏好不可改變，忽視非典型客群的隱性潛在渴望'
        ]
    },
    'right': {
        'title': '批判性逆向反思路徑',
        'theme': 'teal',
        'points': [
            '★【本質詰問反思】：這項限制究竟是物理法則的客觀必然，抑或只是團隊懶於思考的陳規？',
            '★【非典型破局可能】：若將核心業務環節徹底推翻，市場將誕生何種意想不到的全新生機？',
            '★【價值重塑宣告】：撕掉最根深蒂固的一條營運枷鎖，正式向產業傳統陳規發起價值創新！'
        ]
    }
})

# Slide 35: 五法輪盤矩陣
slides.append({
    'layout': '2card',
    'badge': 'WEEK 06 ｜ CH05 激發行銷企劃創意（上） · 35/62',
    'sec': '商業模式重組實戰',
    'title': '加減乘除移五法輪盤矩陣：商業模式重構推演',
    'subtitle': '強迫以五大運算符號對核心業務進行全方位重組與壓力測試',
    'left': {
        'title': '五法運算符號具體工序',
        'theme': 'blue',
        'points': [
            '★【＋法運算】：若為既有業務注入一項非典型跨界驚喜（如香氛、音樂、文化策展），將激發何種溢價？',
            '★【－法運算】：若將最耗費營運成本、程序最繁瑣的核心環節徹底刪除，如何依然極致流暢運轉？',
            '★【×法運算】：與周邊非競爭生態夥伴進行深度異業跨界，能碰撞出何種全新商業複合體？',
            '★【÷法運算】：將龐大笨重的產品或服務拆解為高頻微型體驗，能開拓多少長尾客群？',
            '★【↗法運算】：若將服務時間或交付場景徹底移轉至極端時空，會激發出哪些藍海商機？'
        ]
    },
    'right': {
        'title': '商業重組矩陣成果指標',
        'theme': 'amber',
        'points': [
            '★【成本結構突破】：透過減法與除法徹底削減傳統固定資產沉沒成本，實現輕資產高流動性',
            '★【溢價能力躍升】：透過加法與乘法打造獨特心智定錨，使產品脫離同質化惡性價格戰泥淖',
            '★【競爭維度重塑】：以時空情境移轉開闢無人防守的全新戰場，建立難以被模仿的非對稱優勢'
        ]
    }
})

# Slide 36: 智慧工具協同
slides.append({
    'layout': '3card',
    'badge': 'WEEK 06 ｜ CH05 激發行銷企劃創意（上） · 36/62',
    'sec': '商業模式重組實戰',
    'title': '智慧決策工具協同發散實戰：從極端情境推演到商業收斂',
    'subtitle': '以高階提示詞約束演算法，展開人機雙向對話並提煉突破性價值主張',
    'cards': [
        {
            'num': '01',
            'title': '步驟一：基準假設與痛點約束',
            'theme': 'blue',
            'points': [
                '★ 規格化定義現有產品架構與服務流程',
                '★ 強制指出三條產業公認的理所當然假設',
                '★ 設定追求非線性突破而非漸進改善目標'
            ]
        },
        {
            'num': '02',
            'title': '步驟二：極端情境與異業刺激',
            'theme': 'teal',
            'points': [
                '★ 要求調用跨十個不同產業的經典重組案例',
                '★ 模擬極端使用條件下的產品形態與交付',
                '★ 捕捉非直覺性的功能重組與情感定錨靈感'
            ]
        },
        {
            'num': '03',
            'title': '步驟三：可行性與商業收斂',
            'theme': 'amber',
            'points': [
                '★ 評估企業現有核心資源是否足以支撐落地',
                '★ 驗證目標客群對新重組方案之付費意願',
                '★ 提煉具備震撼力之核心價值主張規格書'
            ]
        }
    ]
})

# Slide 37: 提案結構
slides.append({
    'layout': '2card',
    'badge': 'WEEK 06 ｜ CH05 激發行銷企劃創意（上） · 37/62',
    'sec': '商務提案呈現',
    'title': '創新企劃提案結構：商業重組亮點之高效提報架構',
    'subtitle': '向決策層或投資人精準傳達破框創新，以鋼鐵般邏輯展現顛覆性價值',
    'left': {
        'title': '高說服力提案黃金架構',
        'theme': 'blue',
        'points': [
            '★【前 30 秒破題破框】：直擊市場痛點，無情揭露產業長年墨守成規之荒謬與集體盲點',
            '★【中段 45 秒奇術拆解】：展示加減乘除移運算重組之核心機制，闡明全新價值主張由來',
            '★【後 45 秒商業閉環】：清晰交代成本優勢、客群共鳴依據與首期落地驗證里程碑'
        ]
    },
    'right': {
        'title': '資深企劃大腦核心準則',
        'theme': 'teal',
        'points': [
            '★【不賣弄術語口號】：用具體商業數據與顧客利益說服決策層，杜絕抽象自嗨',
            '★【嚴密因果支撐】：為每一個看似狂妄的大膽假設，鋪設步步為營的客觀推論階梯',
            '★【守護戰略底線】：破框創新絕不脫離商業獲利本質，追求極致想像力與落地力的平衡'
        ]
    }
})

# Slide 38: 顧問講評三大誤區
slides.append({
    'layout': '2card',
    'badge': 'WEEK 06 ｜ CH05 激發行銷企劃創意（上） · 38/62',
    'sec': '商務提案呈現',
    'title': '資深策略顧問講評：企業創意思考的三大常見誤區',
    'subtitle': '從數十家企業轉型成敗中萃取的智慧：保持清醒大腦，創意方能轉化為真實財富',
    'left': {
        'title': '常見三大創意思維誤區',
        'theme': 'rose',
        'points': [
            '★【誤區一：為創新而搞怪】：脫離顧客真實痛點的自我陶醉，把嘩眾取寵誤當成獨特優勢',
            '★【誤區二：忽視落地執行代價】：狂想天馬行空，卻忽視組織資源極限與高昂供應鏈改造成本',
            '★【誤區三：局部優化盲區】：過度著迷於細枝末節的點綴，未能在商業模式核心維度帶來突破'
        ]
    },
    'right': {
        'title': '資深顧問破局關鍵心法',
        'theme': 'teal',
        'points': [
            '★【緊扣真實未滿足需求】：不能實質解決顧客痛苦或創造深層愉悅的創意，皆是無效雜音',
            '★【同步規劃承載資源】：提出顛覆性構想時，同步備妥資源調度方案與風險對沖機制',
            '★【以全局系統護航】：將單點靈感置入全流程商業模式中，打造環環相扣之競爭壁壘'
        ]
    }
})

# Slide 39: 落地路徑
slides.append({
    'layout': '2card',
    'badge': 'WEEK 06 ｜ CH05 激發行銷企劃創意（上） · 39/62',
    'sec': '企劃落地轉化',
    'title': '企劃創新落地路徑：從靈感構想到可行性規格之轉化',
    'subtitle': '將閃電靈感精雕細琢為具備商業可行性的企劃章節規格',
    'left': {
        'title': '創意落地轉化三大工序',
        'theme': 'blue',
        'points': [
            '★【建立重組全景表】：系統化歸檔加減乘除移運算成果，篩選出 3 組具備突破性之方案',
            '★【構建情境動線草圖】：繪製產品與服務於全新情境中的使用者接觸點與關鍵體驗時刻',
            '★【可行性邊界檢驗】：預先核算新方案在法規、財務現金流與供應鏈能力之承載極限'
        ]
    },
    'right': {
        'title': '高階企劃案專業品質規格',
        'theme': 'teal',
        'points': [
            '★【因果邏輯嚴密】：每一項運算重組皆具備清晰的前提假設、推導過程與量化驗收指標',
            '★【市場客觀佐證】：附帶小規模焦點訪談或田野觀察數據，證明重組方案確實切中要害',
            '★【心智定位對齊】：確保所有創意亮點百分之百服膺於品牌長期核心定位，絕不自我稀釋'
        ]
    }
})

# Slide 40: 學理回顧
slides.append({
    'layout': '3card',
    'badge': 'WEEK 06 ｜ CH05 激發行銷企劃創意（上） · 40/62',
    'sec': '核心學理總結',
    'title': '第 06 週核心學理全景回顧：創意思考心法備忘錄',
    'subtitle': '打破常規，重組元素，讓創意成為推動商業巨輪的澎湃燃料',
    'cards': [
        {
            'num': '01',
            'title': '1. 逆向假設分析法',
            'theme': 'blue',
            'points': [
                '★ 挑戰習慣成自然的隱形枷鎖與產業教條',
                '★ 如果不是這樣呢？大膽向常規常理說不',
                '★ 在被大眾忽視的反轉盲區發現無人競爭的藍海'
            ]
        },
        {
            'num': '02',
            'title': '2. 全新情境五法重組',
            'theme': 'teal',
            'points': [
                '★ 如果...在...情境下，該有多好！',
                '★ ＋法添驚喜、－法去多餘、×法搞跨界生態',
                '★ ÷法碎拆解、↗法大移轉，重塑任何平凡商品'
            ]
        },
        {
            'num': '03',
            'title': '3. 智慧協同發散放大',
            'theme': 'amber',
            'points': [
                '★ 以規格化提示詞驅動高維度跨界聯想外腦',
                '★ 嚴格依照驚艷度、真解度與落地度三階漏斗篩選',
                '★ 策略大腦永遠掌握價值取捨與商業決策主權'
            ]
        }
    ]
})

# Slide 41: 思維深化
slides.append({
    'layout': '2card',
    'badge': 'WEEK 06 ｜ CH05 激發行銷企劃創意（上） · 41/62',
    'sec': '思維格局深化',
    'title': '企劃思維深化：逆向思考與理性審查的辯證統一',
    'subtitle': '狂歡之後必須有紀律，天馬行空之後必須有穩固扎實的地基',
    'left': {
        'title': '大師思維核心箴言',
        'theme': 'indigo',
        'points': [
            '★【狂歡與紀律並重】：好的創意既需要想像力的無拘無束，更需要商業邏輯的冷靜滋養',
            '★【創意的生命週期】：從發散狂想到系統驗證，唯有歷經千錘百煉方能淬煉為傳世經典',
            '★【企劃者的修煉】：既要擁有敢於顛覆常規的戰略膽識，更要有承受真實市場檢驗的定力'
        ]
    },
    'right': {
        'title': '理性審查與策略收斂核心意涵',
        'theme': 'teal',
        'points': [
            '★【多維度全方位審查】：從客觀數據、潛在風險、價值獲益與全局戰略視角檢驗創新方案',
            '★【消除無效內耗摩擦】：以結構化思考模型替代團隊無休止的憑感覺爭執與主觀內耗',
            '★【終極商業目標導向】：確保每一項令人拍案叫絕的創意方案，皆能精準轉化為商業勝勢'
        ]
    }
})

# Slide 42: 創意品質診斷
slides.append({
    'layout': '2card',
    'badge': 'WEEK 06 ｜ CH05 激發行銷企劃創意（上） · 42/62',
    'sec': '品質診斷指標',
    'title': '創意思維品質診斷：創新思考五大關鍵檢定維度',
    'subtitle': '資深教授審查指引：以五項嚴謹準則檢驗行銷企劃創意的含金量與可行性',
    'left': {
        'title': '五大關鍵檢定指標',
        'theme': 'blue',
        'points': [
            '★【檢定一：顛覆性】：是否真正破除了既有行業慣性假設，而非換湯不換藥的表面包裝',
            '★【檢定二：情境適配】：所構建之全新情境能否強烈激發受眾的情感共鳴與深層渴望',
            '★【檢定三：運算精準】：加減乘除移之應用是否精準切中痛點本質，創造實質價值增量',
            '★【檢定四：智能協同】：是否充分善用決策工具拓寬跨界視野，展現人機協同之綜效',
            '★【檢定五：商業真實】：方案是否切實具備落地可行性與回報預期，杜絕脫離現實之空想'
        ]
    },
    'right': {
        'title': '策略研判總結',
        'theme': 'teal',
        'points': [
            '★【深植經典企劃學理】：融會貫通逆向假設與情境重組精髓，厚積薄發展現專業底蘊',
            '★【實踐檢驗真理】：能在激烈市場競局中活下來並取得商業回報的創意，才是真正的卓越創意'
        ]
    }
})

# Slides 43 to 60: Rich business case studies from raw
for i in range(42, 60):
    s = raw[i]
    layout = s.get('layout')
    badge = f'WEEK 06 ｜ CH05 激發行銷企劃創意（上） · {i+1:02d}/62'
    sec = clean_text(s.get('sec', '經典商業案例'))
    title = clean_text(s.get('title', ''))
    subtitle = clean_text(s.get('subtitle', ''))

    left = {
        'title': clean_text(s.get('leftTitle', s.get('left', {}).get('title', ''))),
        'theme': s.get('left', {}).get('theme', 'blue'),
        'points': [format_pt(p) for p in (s.get('leftPoints') or s.get('left', {}).get('points', []))]
    }
    right = {
        'title': clean_text(s.get('rightTitle', s.get('right', {}).get('title', ''))),
        'theme': s.get('right', {}).get('theme', 'teal'),
        'points': [format_pt(p) for p in (s.get('rightPoints') or s.get('right', {}).get('points', []))]
    }
    slides.append({
        'layout': '2card',
        'badge': badge,
        'sec': sec,
        'title': title,
        'subtitle': subtitle,
        'left': left,
        'right': right
    })

# Slide 61: 全景思維總結
slides.append({
    'layout': '2card',
    'badge': 'WEEK 06 ｜ CH05 激發行銷企劃創意（上） · 61/62',
    'sec': '全景思維總結',
    'title': '全景思維總結：創新思考工具之學理閉環與實務沉澱',
    'subtitle': '把逆向思維化作本能，把加減乘除融入血液，成就大師級企劃格局',
    'left': {
        'title': '核心心法沉澱',
        'theme': 'indigo',
        'points': [
            '★【打破常規是創新的唯一起點】：敢於挑戰所有理所當然的慣性假設，在盲區洞見商機',
            '★【重組元素是創造價值的核心手段】：加減乘除移靈活調度，為平凡產品注入非凡靈魂',
            '★【商業落地是檢驗創意的最高標準】：以嚴謹因果邏輯支撐大膽狂想，創造可持續之競爭優勢'
        ]
    },
    'right': {
        'title': '策略大腦格局躍升',
        'theme': 'teal',
        'points': [
            '★【辯證統一之戰略修煉】：在極致發散中保持清醒冷靜，在嚴謹收斂中守護創新火種',
            '★【知行合一的專業素養】：將科學創意思維內化為直覺本能，從容駕馭複雜多變的商業挑戰'
        ]
    }
})

# Slide 62: Closing
slides.append({
    'layout': 'closing',
    'title': '第 06 週單元授課完畢：激發行銷企劃創意（上）',
    'subtitle': '破除慣性假設，重組情境元素；讓科學化創意思考成為行銷企劃的制勝支柱。',
    'final_message': '學術講授模式 ✕ 逆向假設分析法 ✕ 全新情境法 ✕ 加減乘除移重組矩陣'
})

print('Total generated slides:', len(slides))
assert len(slides) == 62

# Verify prohibited terms in generated slides
prohibited_terms = [
    '下周單元預告', '下週單元預告', '下週主題預告', '下週預告', '掌握期中期末重點',
    '自主溫習指引', '輕鬆準備考試', '曾光華', '核心考點', '應試精華', '自我檢核',
    '自主溫習', '廢話', '空洞', '抽籤', '大轉盤', '靈感抽卡機', '便利貼計時器',
    '作業一', '作業二', '作業三', '作業驗收', '課後作業', '繳交報告', '交報告',
    '手稿妥善保存', '學生作品展示廊'
]

s_str = json.dumps(slides, ensure_ascii=False)
violations = [t for t in prohibited_terms if t in s_str]
print('Prohibited terms violations:', violations)
assert len(violations) == 0, f'Found violations: {violations}'

output_path = os.path.join(os.path.dirname(__file__), 'week06_generated_slides.json')
with open(output_path, 'w', encoding='utf-8') as out:
    json.dump(slides, out, ensure_ascii=False, indent=2)

print(f'Wrote {output_path} successfully!')
