# -*- coding: utf-8 -*-
"""
將 萬能科大 創意行銷企劃實務 平台打包為完全免安裝、零網路依賴的「單機離線 HTML 檔案」
"""
import os
import sys
import json

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def build_offline():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    html_path = os.path.join(base_dir, 'templates', 'index.html')
    css_path = os.path.join(base_dir, 'static', 'css', 'style.css')
    js_path = os.path.join(base_dir, 'static', 'js', 'app.js')
    curriculum_path = os.path.join(base_dir, 'data', 'curriculum.json')
    questions_path = os.path.join(base_dir, 'data', 'questions.json')
    templates_path = os.path.join(base_dir, 'data', 'agent_templates.json')
    works_path = os.path.join(base_dir, 'data', 'sample_works.json')
    vibe_path = os.path.join(base_dir, 'data', 'vibe_coding_guide.json')
    output_path = os.path.join(base_dir, '平台首頁(單機離線直接點開).html')

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()

    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()

    with open(curriculum_path, 'r', encoding='utf-8') as f:
        curriculum = f.read()

    with open(questions_path, 'r', encoding='utf-8') as f:
        questions = f.read()

    with open(templates_path, 'r', encoding='utf-8') as f:
        templates = f.read()

    sample_works = '[]'
    if os.path.exists(works_path):
        with open(works_path, 'r', encoding='utf-8') as f:
            sample_works = f.read()

    vibe_guide = '{}'
    if os.path.exists(vibe_path):
        with open(vibe_path, 'r', encoding='utf-8') as f:
            vibe_guide = f.read()

    # 1. 內嵌 CSS
    html = html.replace('<link rel="stylesheet" href="/static/css/style.css">', f'<style>\n{css}\n</style>')

    # 2. 注入離線全量資料庫
    embedded_data = f"""
  <!-- 離線全量內嵌資料庫 -->
  <script>
    window.OFFLINE_CURRICULUM = {curriculum};
    window.OFFLINE_QUESTIONS = {questions};
    window.OFFLINE_TEMPLATES = {templates};
    window.OFFLINE_SAMPLE_WORKS = {sample_works};
    window.OFFLINE_VIBE_GUIDE = {vibe_guide};
    window.IS_STANDALONE_OFFLINE = true;
  </script>
"""

    # 3. 處理 JS 離線優先呼叫與內嵌
    js_offline = js.replace(
        "console.warn('Backend API unavailable, using offline defaults.');",
        "console.log('單機離線版運行中，使用內嵌離線資料庫'); isOfflineMode = true;"
    )

    embedded_js = f"""
{embedded_data}
  <script>
{js_offline}
  </script>
"""
    html = html.replace('<script src="/static/js/app.js"></script>', embedded_js)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    # 另外同步複製一份為 創意行銷企劃實務.html
    alt_output_path = os.path.join(base_dir, '創意行銷企劃實務.html')
    with open(alt_output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    # 同步產出根目錄 index.html 供 GitHub Pages 靜態託管部署
    index_output_path = os.path.join(base_dir, 'index.html')
    with open(index_output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    size_kb = os.path.getsize(output_path) / 1024
    print(f"✅ 單機離線與 GitHub Pages 版打包成功！")
    print(f"📄 產出檔案：")
    print(f"   1. {output_path}")
    print(f"   2. {alt_output_path}")
    print(f"   3. {index_output_path} (GitHub Pages 部署主入口)")
    print(f"📦 檔案大小：{size_kb:.1f} KB (已內嵌 18 週課綱、180 題精選題庫、8 大行銷 Agent 與個人企劃展示)")

if __name__ == '__main__':
    build_offline()
