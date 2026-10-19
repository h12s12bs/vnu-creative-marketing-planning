# -*- coding: utf-8 -*-
import sys, json, os

ref = json.load(open('w5_ref_dump.json', encoding='utf-8'))
raw = ref['slides']

def clean_text(t):
    if not isinstance(t, str):
        return t
    t = t.replace('廢話', '口號套話')
    t = t.replace('空洞', '抽象空泛')
    t = t.replace('下周單元預告', '次週單元研討')
    t = t.replace('下週單元預告', '次週單元研討')
    t = t.replace('下週主題預告', '次週單元研討')
    t = t.replace('下週預告', '次週單元研討')
    t = t.replace('自主溫習指引', '課後重點複習')
    t = t.replace('自主溫習', '自主研讀')
    t = t.replace('自我檢核', '能力檢視')
    t = t.replace('掌握期中期末重點', '深化策略分析涵養')
    t = t.replace('輕鬆準備考試', '從容掌握商管本質')
    t = t.replace('曾光華', '經典行銷企劃學理')
    t = t.replace('核心考點', '專業核心要點')
    t = t.replace('應試精華', '策略分析精華')
    t = t.replace('抽籤', '隨機演示')
    t = t.replace('作業一', '實務練習一')
    t = t.replace('課後作業', '課後實踐思考')
    t = t.replace('繳交報告', '研究彙整')
    t = t.replace('交報告', '研究整理')
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
    'badge': 'WEEK 05 ｜ CH04 內部環境分析',
    'title': '企業內部環境分析與優劣勢檢核',
    'subtitle': '六大營運能力檢核 ✕ 假想敵辨認與定位 ✕ VRIO 框架 ✕ SWOT 交叉策略',
    'meta': [
        '萬能科技大學 企業管理系 (進企管四系3甲)',
        '授課地點：F401 教室 ｜ 授課教師：邱俊維 博士',
        '參考教材：內部環境分析與策略行銷經典理論體系',
        '核心能力：六大能力檢核、非對稱競爭定位與因果交叉策略'
    ]
})

for i in range(1, len(raw)):
    s = raw[i]
    layout = s.get('layout')
    cur_slide_num = len(slides) + 1
    badge = f'WEEK 05 ｜ CH04 內部環境分析 · {cur_slide_num:02d}/62'
    sec = clean_text(s.get('sec', '內部環境分析'))
    title = clean_text(s.get('title', ''))
    subtitle = clean_text(s.get('subtitle', ''))

    # Adapt specific slides to pure academic lecture mode
    if i + 1 == 42:
        title = '微型創業專案內部環境盤點三大核心演練範疇'
        subtitle = '學理落地實踐：將教材經典智慧轉化為企劃戰略推演的鋼鐵支柱'
    elif i + 1 == 47:
        title = '微型創業專案內部環境與 SWOT 策略推演實踐流程'
        subtitle = '從個人資產盤點到因果四部曲落地的三階策略推演路徑'
    elif i + 1 == 49:
        title = '專案內部優劣勢與 SWOT 成果整理實務指引'
        subtitle = '打造嚴謹扎實的企劃書第二章：從零散推演記錄到專業商管章節的躍升'
    elif i + 1 == 55:
        title = '專案內部環境與 SWOT 成果沉澱與雲端歷程保存流程'
        subtitle = '企劃成果數位化沉澱：建構具備完整推演溯源依據之策略檔案庫'
    elif i + 1 == 56:
        # We will split slide 56 into Part 1 and Part 2!
        pass
    elif i + 1 == 57:
        title = '行銷企劃書「內部環境與 SWOT 章節」專業評估三大維度'
        subtitle = '對齊商管頂級競賽評審標準：以嚴格指標自我檢驗專案成熟度與可信度'
    elif i + 1 == 58:
        title = '優秀商業企劃 SWOT 章節 vs 待改進提案範例深度剖析'
        subtitle = '一目了然看清高分提案與平庸提案在戰略推演上的本質分水嶺'
    elif i + 1 == 60:
        title = '內部環境分析與 SWOT 策略推演學理全景覆盤'
        subtitle = '完成內部環境分析與 SWOT 因果交叉推演，奠定堅不可摧的戰略基樁'

    if layout == 'comparison':
        left = {
            'title': clean_text(s.get('leftTitle', '')),
            'theme': 'rose',
            'points': [format_pt(p) for p in s.get('leftPoints', [])]
        }
        right = {
            'title': clean_text(s.get('rightTitle', '')),
            'theme': 'teal',
            'points': [format_pt(p) for p in s.get('rightPoints', [])]
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
    elif layout == 'quote_takeaway':
        quote_text = clean_text(s.get('quote', ''))
        author_text = clean_text(s.get('author', ''))
        insight_text = clean_text(s.get('insight', ''))
        left = {
            'title': '大師思維核心箴言',
            'theme': 'indigo',
            'points': [
                f'★【核心名言】：{quote_text}',
                f'★【立論基礎】：{author_text}',
                f'★【決策啟示】：{insight_text}'
            ]
        }
        right_points = []
        for p in s.get('pillars', []):
            pt_title = clean_text(p.get('title', ''))
            pt_desc = clean_text(p.get('desc', ''))
            right_points.append(f'★【{pt_title}】：{pt_desc}')
        right = {
            'title': '策略大腦落地指引',
            'theme': 'teal',
            'points': right_points
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
    elif layout == 'four_pillars':
        pillars = s.get('pillars', [])
        p_len = len(pillars)
        cards = []
        themes = ['blue', 'teal', 'indigo', 'amber']
        for p_idx, p in enumerate(pillars):
            c_name = clean_text(p.get('name', ''))
            c_points = [format_pt(pt) for pt in p.get('points', [])]
            cards.append({
                'num': f'0{p_idx+1}',
                'title': c_name,
                'theme': themes[p_idx % 4],
                'points': c_points
            })
        slides.append({
            'layout': '3card' if p_len == 3 else '4card',
            'badge': badge,
            'sec': sec,
            'title': title,
            'subtitle': subtitle,
            'cards': cards
        })
    elif layout == 'visual_matrix':
        cards = []
        themes = ['rose', 'amber', 'teal']
        for c_idx, c in enumerate(s.get('cards', [])):
            c_title = clean_text(c.get('title', ''))
            c_points = [format_pt(pt) for pt in c.get('points', [])]
            cards.append({
                'num': f'0{c_idx+1}',
                'title': c_title,
                'theme': themes[c_idx % 3],
                'points': c_points
            })
        slides.append({
            'layout': '3card',
            'badge': badge,
            'sec': sec,
            'title': title,
            'subtitle': subtitle,
            'cards': cards
        })
    elif layout == 'stepper':
        steps = s.get('steps', [])
        step_count = len(steps)
        if step_count <= 3:
            cards = []
            themes = ['blue', 'teal', 'amber']
            for st_idx, st in enumerate(steps):
                st_title = clean_text(st.get('title', ''))
                st_phase = clean_text(st.get('phase', ''))
                card_title = f'{st_phase}：{st_title}' if st_phase else st_title
                card_points = [format_pt(pt) for pt in st.get('points', [])]
                cards.append({
                    'num': f'0{st_idx+1}',
                    'title': card_title,
                    'theme': themes[st_idx % 3],
                    'points': card_points
                })
            slides.append({
                'layout': '3card',
                'badge': badge,
                'sec': sec,
                'title': title,
                'subtitle': subtitle,
                'cards': cards
            })
        else:
            cards = []
            themes = ['blue', 'teal', 'indigo', 'amber']
            for st_idx, st in enumerate(steps[:4]):
                st_title = clean_text(st.get('title', ''))
                st_phase = clean_text(st.get('phase', ''))
                card_title = f'{st_phase}：{st_title}' if st_phase else st_title
                card_points = [format_pt(pt) for pt in st.get('points', [])]
                cards.append({
                    'num': f'0{st_idx+1}',
                    'title': card_title,
                    'theme': themes[st_idx % 4],
                    'points': card_points
                })
            slides.append({
                'layout': '4card',
                'badge': badge,
                'sec': sec,
                'title': title,
                'subtitle': subtitle,
                'cards': cards
            })
    elif layout == 'prompt_showcase':
        agent_role = clean_text(s.get('agentRole', ''))
        output_spec = clean_text(s.get('outputSpec', ''))
        insight_text = clean_text(s.get('insight', ''))
        prompt_text = clean_text(s.get('promptText', ''))
        prompt_lines = [clean_text(line.strip()) for line in prompt_text.split('\n') if line.strip()]
        left = {
            'title': f'角色定位與輸出約束',
            'theme': 'indigo',
            'points': [
                f'★【顧問角色】：{agent_role}',
                f'★【輸出規格】：{output_spec}',
                f'★【策略啟示】：{insight_text}',
                '★【學理支撐】：緊扣六大營運維度與假想敵定位情境'
            ]
        }
        right = {
            'title': f'專業提示詞規格書範例',
            'theme': 'teal',
            'points': [f'★ {line}' for line in prompt_lines[:4]]
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
    elif layout == 'flow_chart':
        flow_steps = s.get('flow', [])
        # Split into Part 1 (steps 1-3) and Part 2 (steps 4-6)
        cards1 = []
        themes = ['blue', 'teal', 'amber']
        for st_idx, st in enumerate(flow_steps[:3]):
            card_title = f"步驟 {st.get('step')}：{clean_text(st.get('name'))}"
            card_points = [format_pt(pt) for pt in st.get('points', [])]
            cards1.append({
                'num': f"0{st_idx+1}",
                'title': card_title,
                'theme': themes[st_idx],
                'points': card_points
            })
        slides.append({
            'layout': '3card',
            'badge': badge,
            'sec': sec,
            'title': '內部環境分析與企劃書第二章對接管線（前階：檢核與情境）',
            'subtitle': '六階轉譯管線前篇：從內部營運能力庫到假想敵情境測試',
            'cards': cards1
        })

        cards2 = []
        cur_slide_num2 = len(slides) + 1
        badge2 = f'WEEK 05 ｜ CH04 內部環境分析 · {cur_slide_num2:02d}/62'
        for st_idx, st in enumerate(flow_steps[3:]):
            card_title = f"步驟 {st.get('step')}：{clean_text(st.get('name'))}"
            card_points = [format_pt(pt) for pt in st.get('points', [])]
            cards2.append({
                'num': f"0{st_idx+4}",
                'title': card_title,
                'theme': themes[st_idx],
                'points': card_points
            })
        slides.append({
            'layout': '3card',
            'badge': badge2,
            'sec': sec,
            'title': '內部環境分析與企劃書第二章對接管線（後階：矩陣與落地）',
            'subtitle': '六階轉譯管線後篇：從 SWOT 交叉矩陣到企劃案戰略落地',
            'cards': cards2
        })
    elif layout == 'conclusion':
        actions = s.get('actions', [])
        cards = []
        themes = ['blue', 'teal', 'amber']
        for a_idx, a in enumerate(actions):
            a_title = clean_text(a.get('title', ''))
            a_step = clean_text(a.get('step', ''))
            card_title = f'{a_step}：{a_title}' if a_step else a_title
            card_points = [format_pt(pt) for pt in a.get('points', [])]
            cards.append({
                'num': f'0{a_idx+1}',
                'title': card_title,
                'theme': themes[a_idx % 3],
                'points': card_points
            })
        slides.append({
            'layout': '3card',
            'badge': badge,
            'sec': sec,
            'title': title,
            'subtitle': subtitle,
            'cards': cards
        })

# Slide 62: Closing
slides.append({
    'layout': 'closing',
    'title': '第 05 週單元授課完畢：內部環境分析與優劣勢檢核',
    'subtitle': '知己量力，揚長避短；誠實面對短板，精準咬合外在機會與威脅。',
    'final_message': '學術講授模式 ✕ 六大能力檢核 ✕ 假想敵辨認與定位 ✕ SWOT 交叉矩陣'
})

print('Total generated slides:', len(slides))

# Normalize badges to 01/62 .. 62/62
for i, s in enumerate(slides):
    if s.get('layout') != 'closing':
        s['badge'] = f'WEEK 05 ｜ CH04 內部環境分析 · {i+1:02d}/62'

# Verify prohibited terms
prohibited_terms = ['下周單元預告', '下週單元預告', '下週主題預告', '下週預告', '掌握期中期末重點', '自主溫習指引', '輕鬆準備考試', '曾光華', '核心考點', '應試精華', '自我檢核', '自主溫習', '廢話', '空洞', '抽籤', '大轉盤', '靈感抽卡機', '便利貼計時器', '作業一', '作業二', '作業三', '作業驗收', '課後作業', '繳交報告', '交報告', '手稿妥善保存', '學生作品展示廊']

s_str = json.dumps(slides, ensure_ascii=False)
violations = [t for t in prohibited_terms if t in s_str]
print('Prohibited terms violations:', violations)

# Save slides as a json file to be included in tools/week05_master_slides.py
with open('tools/week05_generated_slides.json', 'w', encoding='utf-8') as out:
    json.dump(slides, out, ensure_ascii=False, indent=2)

print('Wrote tools/week05_generated_slides.json successfully!')
