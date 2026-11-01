# -*- coding: utf-8 -*-
"""
tools/week06_master_slides.py
Master 62-slide lecture deck for Week 06:
激發行銷企劃創意（上）：逆向假設分析法、全新情境法與加減乘除移五法
破除慣性思維 ✕ 產品重組創新 ✕ 全新情境法 ✕ 智慧發散推演
專為萬能科技大學進修部企管系 (進企管四系3甲) 設計：
- 純課程教授模式 (大學資深教授講授風範、論述嚴謹、學術與實務底蘊兼備)
- 零學生互動、零分組討論、零課外作業、免交期末報告
- 純粹專業學術講授、零非必要文字、零口號套話
- 聚焦創意思考工具學理深度、商業模式重組與顛覆性價值創新
- 秉持經典管理學與行銷策略理論體系，不反覆提及特定教科書作者姓名
- 字體採用 28pt / 30pt / 36pt 超大字遠距極致清晰排版
"""
import json
import os

def get_week06_slides(wc=None):
    slides_json_path = os.path.join(os.path.dirname(__file__), 'week06_generated_slides.json')
    if os.path.exists(slides_json_path):
        with open(slides_json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

if __name__ == '__main__':
    slides = get_week06_slides()
    print(f"Successfully loaded {len(slides)} slides for Week 6.")
