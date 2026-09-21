# -*- coding: utf-8 -*-
"""
tools/build_curriculum_json.py
Generates data/curriculum.json to be 100% consistent with:
- tools/week_configs.py (18 weeks matching 曾光華《行銷企劃》(2026 第五版))
- Grading: Midterm 40% + Final 40% + Attendance 20%
- Lecture-only mode (no student interaction, no group work, no homework, no reports)
- Week 1 kept untouched
"""
import os
import json
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(BASE_DIR, 'data', 'curriculum.json')

TOOLS_DIR = os.path.join(BASE_DIR, 'tools')
if TOOLS_DIR not in sys.path:
    sys.path.insert(0, TOOLS_DIR)

from week_configs import get_week_configs

def generate_curriculum():
    configs = get_week_configs()

    # Load existing to preserve Week 1 exactly
    with open(OUTPUT_PATH, 'r', encoding='utf-8') as f:
        existing = json.load(f)

    week_1_data = existing['weeks'][0]

    weeks = [week_1_data]

    for wc in configs[1:]:
        wn = wc['week']
        title = wc['title']
        chap = wc['chapter']
        concept = wc['core_concept']
        case = wc['case_name']
        pitfall = wc['pitfall']
        ipas = wc['ipas']
        mod = wc['module']

        if wn == 9:
            activity = "【期中考試】期中筆試與實務測驗 ➔ 曾光華 CH01~CH05 前半冊重點檢定 ➔ 試卷核心解題要領歸納。"
            task = "期中考試圓滿結束！請同學課後回顧試卷觀念，自主預習後半學期實務章節。"
            concepts = [
                "期中考試觀念筆試與實務個案分析",
                "曾光華 CH01~CH05 前半冊全域核心觀念回顧",
                "企劃三位一體與十步標準程序實踐檢核",
                "SMART 目標、PESTEL、五力分析與 TOWS 交叉矩陣",
                "期中成績核算（佔學期總成績 40%）"
            ]
        elif wn == 18:
            activity = "【期末考試】期末筆試與實務測驗 ➔ 曾光華 CH01~CH10 全冊重點總檢定 ➔ 學期總成績核算與說明。"
            task = "全學期課程圓滿結束！感謝同學專注聽講，祝願大家在職場將行銷企劃專業發揮淋漓盡致！"
            concepts = [
                "期末考試綜合筆試與全案實務測驗",
                "曾光華 CH01~CH10 全書核心學理融會貫通",
                "新產品上市、公關事件、促銷 ROI 與 OMO 通路整合",
                "專業企劃書黃金十大章節與商業說服力",
                "學期總成績核算（期中 40% + 期末 40% + 出席 20%）"
            ]
        else:
            activity = f"曾光華教授學理講授 ➔ {case} 經典案例深度剖析 ➔ 決策盲點破解指引 ➔ 核心考點提煉與 IPAS 題型解構。"
            task = "零課外作業與報告負擔！請課後自主溫習本週投影片核心考點與 IPAS 題型，輕鬆準備期中期末考試。"
            concepts = [
                f"{concept}",
                f"{case} 商業個案實務解析",
                f"行銷決策防呆盲點：{pitfall}",
                f"IPAS 證照考點：{ipas}",
                f"{wc['agent']} 原型示範與應用"
            ]

        weeks.append({
            "week": wn,
            "title": title,
            "chapter": chap,
            "textbook_ref": f"參考用書：{chap}",
            "martech_domain": mod,
            "break_ice": f"決策思維檢視：面對「{pitfall}」，優秀企劃人如何運用學理精準破局？",
            "traditional_vs_ai": f"曾光華核心學理：「{concept}」；結合 Agentic AI 智慧代理人協同示範，大幅提升企劃決策效能。",
            "classroom_activity": activity,
            "homework_task": task,
            "key_concepts": concepts
        })

    curriculum_data = {
        "course_info": {
            "title": "創意行銷企劃實務 (Creative Marketing Planning Practice)",
            "subtitle": "實務行銷企劃 ✕ Agentic AI 智慧代理人協同實戰",
            "course_code": "H0930003",
            "semester": "11501 學期",
            "class_name": "進企管四系3甲 (進修部企管系三年級甲班)",
            "credits": 2,
            "hours": 2,
            "time_slot": "每週一 第 10、11 節 (16:20 ~ 17:50)",
            "location": "F401 教室",
            "reference_book": "曾光華《行銷企劃：邏輯、創意、執行力》(2026 第五版)",
            "textbook": "參考用書：曾光華《行銷企劃：邏輯、創意、執行力》(2026 第五版)",
            "instructor": existing["course_info"]["instructor"],
            "grading_policy": {
                "midterm_exam": {
                    "percentage": 40,
                    "title": "期中考試 (40%)",
                    "description": "第 9 週舉行期中考試（筆試/實務測驗），檢測前半學期行銷企劃核心學理與實務觀念。",
                    "breakdown": [
                        {
                            "item": "期中考試成績",
                            "weight": "40%",
                            "desc": "涵蓋曾光華教科書 CH01~CH05 重點觀念、企劃架構邏輯與實務案例分析題型。"
                        }
                    ]
                },
                "final_exam": {
                    "percentage": 40,
                    "title": "期末考試 (40%)",
                    "description": "第 18 週舉行期末考試（筆試/實務測驗），綜合檢驗全學期行銷企劃整合與個案應用能力。",
                    "breakdown": [
                        {
                            "item": "期末考試成績",
                            "weight": "40%",
                            "desc": "涵蓋全學期行銷企劃架構、4P 執行策略、公關促銷與商業實務綜合整合題型。"
                        }
                    ]
                },
                "attendance": {
                    "percentage": 20,
                    "title": "平時出席 (20%)",
                    "description": "降低出席佔比以體恤進修部在職同學！每週課堂常態點名，出席即得基本加分。",
                    "breakdown": [
                        {
                            "item": "課堂出勤紀錄",
                            "weight": "20%",
                            "desc": "每週課堂常態點名紀錄，佔比降為 20%，讓同學能以期中期末考專心衝刺及格。"
                        }
                    ]
                }
            },
            "classroom_guide": {
                "classroom_type": "F401 教室",
                "teaching_method": "【教授專業講授 ✕ 案例深度剖析 ✕ 考點精華歸納】講授模式",
                "dual_mode_solution": {
                    "in_class": "【課堂講授：曾光華商業案例剖析 ✕ 企劃決策盲點指引 ✕ 核心考點整理】每週緊扣曾光華教科書章節，以高對比 28pt 大字簡報進行深度講授，剖析企業經典案例、拆解盲點並歸納期中期末考試重點。",
                    "at_home": "【課後自主溫習：零額外作業負擔 ✕ 題庫自主演練】本課程無分組、無作業、免交期末報告。課後依個人步調自主溫習投影片與 IPAS 證照題庫，輕鬆準備期中期末考。"
                }
            }
        },
        "weeks": weeks
    }

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(curriculum_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated curriculum.json ({len(weeks)} weeks) to {OUTPUT_PATH}")

if __name__ == '__main__':
    generate_curriculum()
