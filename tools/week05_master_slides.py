# -*- coding: utf-8 -*-
"""
tools/week05_master_slides.py
Master 62-slide lecture deck for Week 05:
企業內部環境分析與優劣勢檢核
六大營運能力檢核 ✕ 假想敵辨認與定位 ✕ VRIO 框架 ✕ SWOT 因果交叉矩陣推演
專為萬能科技大學進修部企管系 (進企管四系3甲) 設計：
- 純課程教授模式 (大學資深教授講授風範、論述嚴謹、學術與實務底蘊兼備)
- 零學生互動、零分組討論、零課外作業、免交期末報告
- 純粹專業學術講授、零非必要文字、零口號套話
- 聚焦策略管理理論深度、內部能力資源盤點與企業實務定位突圍決策
- 秉持經典管理學與行銷策略理論體系，不反覆提及特定教科書作者姓名
- 字體採用 28pt / 30pt / 36pt 超大字遠距極致清晰排版
"""
import json
import os

def get_week05_slides(wc=None):
    slides_json_path = os.path.join(os.path.dirname(__file__), 'week05_generated_slides.json')
    if os.path.exists(slides_json_path):
        with open(slides_json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

if __name__ == '__main__':
    slides = get_week05_slides()
    print(f"Successfully loaded {len(slides)} slides for Week 5.")
