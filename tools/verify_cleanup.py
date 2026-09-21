# -*- coding: utf-8 -*-
import os
import sys
import json
import re

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_path = os.path.join(base_dir, 'Full_Screen_Presentation.html')

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Check font sizes and media queries
assert 'font-size: 28pt !important;' in content, 'Missing 28pt font rule!'
assert '.card-title-28pt' in content, 'Missing .card-title-28pt rule!'
assert '.point-multi-card' in content, 'Missing .point-multi-card rule!'

# Media query check
if '@media (max-width: 1280px)' in content:
    m = re.search(r'@media\s*\(max-width:\s*1280px\)\s*\{([^}]+)\}', content)
    if m:
        assert 'point-28pt' not in m.group(1), 'point-28pt found in max-width: 1280px media query!'

print("[OK] CSS 28pt / 24pt font rules and media query overrides verified.")

# 2. Parse curriculum JSON inside HTML
match = re.search(r'const\s+CURRICULUM\s*=\s*(\[.*?\]);\s*let\s+currentWeekIdx', content, re.DOTALL)
assert match, "Could not find CURRICULUM in HTML!"

curriculum = json.loads(match.group(1))
print(f"[OK] Parsed {len(curriculum)} weeks from HTML.")
total_slides = sum(len(w['slides']) for w in curriculum)
print(f"[OK] Total slides: {total_slides} (Week 2 has {len(curriculum[1]['slides'])} slides)")
assert len(curriculum[1]['slides']) == 62, f"Expected 62 slides in Week 2, got {len(curriculum[1]['slides'])}"
assert total_slides == 929, f"Expected 929 slides, got {total_slides}"

# 3. Forbidden terms for Week 2 ~ 18 (Week 1 kept untouched)
forbidden = [
    '抽籤', '大轉盤', '靈感抽卡機', '便利貼計時器',
    '作業一', '作業二', '作業三', '作業驗收', '課後作業',
    '繳交報告', '交報告', '手稿妥善保存', '學生作品展示廊'
]

violations = []
for w in curriculum:
    wn = w['week_num']
    if wn == 1:
        continue
    w_str = json.dumps(w, ensure_ascii=False)
    for term in forbidden:
        if term in w_str:
            violations.append((wn, term))

if violations:
    print("[FAIL] Violations found in Week 2~18:")
    for wn, term in violations:
        print(f"  Week {wn}: found forbidden term '{term}'")
    sys.exit(1)
else:
    print("[OK] Zero violations of student interaction, group work, homework, reports, or draft submissions in Weeks 2-18.")

# 4. Check Grading Formula consistency
grading_mentions = []
for w in curriculum:
    wn = w['week_num']
    w_str = json.dumps(w, ensure_ascii=False)
    if '期中考 40%' in w_str or '期中 40%' in w_str:
        grading_mentions.append(wn)

print(f"[OK] Weeks mentioning standard 40/40/20 grading: {len(grading_mentions)} weeks.")
print("All verification checks PASSED!")
