# -*- coding: utf-8 -*-
"""
tools/build_chapter_slides.py
Consolidates chapter slides from:
- chapter_content_w01_w09.py (Weeks 1 to 4)
- chapter_content_w05_w09.py (Weeks 5 to 9)
- chapter_content_w10_w14.py (Weeks 10 to 14)
- chapter_content_w15_w18.py (Weeks 15 to 18)
And saves to data/chapter_slides.json
"""
import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'tools'))

from chapter_content_w01_w09 import get_weeks_1_to_9
from chapter_content_w05_w09 import get_weeks_5_to_9
from chapter_content_w10_w14 import get_weeks_10_to_14
from chapter_content_w15_w18 import get_weeks_15_to_18

def main():
    all_slides = {}

    w1_4 = get_weeks_1_to_9()
    for k in ["1", "2", "3", "4"]:
        if k in w1_4:
            all_slides[k] = w1_4[k]

    w5_9 = get_weeks_5_to_9()
    for k in ["5", "6", "7", "8", "9"]:
        if k in w5_9:
            all_slides[k] = w5_9[k]

    w10_14 = get_weeks_10_to_14()
    for k in ["10", "11", "12", "13", "14"]:
        if k in w10_14:
            all_slides[k] = w10_14[k]

    w15_18 = get_weeks_15_to_18()
    for k in ["15", "16", "17", "18"]:
        if k in w15_18:
            all_slides[k] = w15_18[k]

    print(f"Total weeks loaded: {len(all_slides)}")
    for k in sorted(all_slides.keys(), key=lambda x: int(x)):
        print(f"Week {k}: {len(all_slides[k])} slides")

    out_path = os.path.join(BASE_DIR, 'data', 'chapter_slides.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(all_slides, f, ensure_ascii=False, indent=2)

    print(f"Saved to {out_path} ({os.path.getsize(out_path)} bytes)")

if __name__ == '__main__':
    main()
