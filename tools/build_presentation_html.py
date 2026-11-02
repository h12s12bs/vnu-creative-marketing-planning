# -*- coding: utf-8 -*-
"""
萬能科技大學 11501 創意行銷企劃實務 - 18 週全景教學簡報生成器 (tools/build_presentation_html.py)
生成 Full_Screen_Presentation.html
每週 51~62 頁，18 週共 973 頁全景簡報
班級：進企管四系3甲 ｜ 教室：F401 教室 ｜ 授課教師：邱俊維 博士 (jimchiu@mail.vnu.edu.tw)
參考教材：曾光華《行銷企劃：策略思維與實務運作》(第四版) ✕ Agentic AI 智慧代理人 ✕ Vibe Coding 操作手冊 ✕ IPAS 證照鑑定
已具備完整手機/平板/投影機 RWD 響應式適配與觸控滑動切頁功能
"""
import os
import sys
import json

# Ensure tools directory is in sys.path
tools_dir = os.path.dirname(os.path.abspath(__file__))
if tools_dir not in sys.path:
    sys.path.insert(0, tools_dir)

from week_configs import get_week_configs
from slide_engine import build_week_slides

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def generate_curriculum_slides():
    configs = get_week_configs()
    curriculum = []
    for wc in configs:
        slides = build_week_slides(wc)
        curriculum.append({
            "week_num": wc["week"],
            "module": wc["module"],
            "title": wc["title"],
            "subtitle": wc["subtitle"],
            "slides": slides
        })
    return curriculum

def build_presentation_html():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(base_dir, 'Full_Screen_Presentation.html')

    curriculum = generate_curriculum_slides()
    total_slides = sum(len(w["slides"]) for w in curriculum)
    print(f"Total weeks: {len(curriculum)}, Total slides generated: {total_slides}")

    curriculum_json = json.dumps(curriculum, ensure_ascii=False, indent=2)

    html_content = f"""<!DOCTYPE html>
<html lang="zh-TW" class="h-full">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
    <title>創意行銷企劃實務 ✕ Agentic AI ｜ 18 週全景教學簡報投影系統 (共 {total_slides} 頁)</title>
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
            width: 6px;
            height: 6px;
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
        :fullscreen footer, :-webkit-full-screen footer, body.is-fullscreen-active footer,
        :fullscreen #mobileNavBar, :-webkit-full-screen #mobileNavBar, body.is-fullscreen-active #mobileNavBar {{
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

        /* 全螢幕微型懸浮操控列 (滑鼠接近右上角時浮現) */
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

        /* 統一超大字體投影規格 (大教室投影機遠距極致清晰，鎖定大字絕不縮小) */
        .point-28pt, .point-multi-card {{
            font-size: 28pt !important;
            line-height: 1.40 !important;
            font-weight: 700 !important;
            word-break: break-word;
        }}
        .card-title-28pt, .card-title-multi {{
            font-size: 30pt !important;
            line-height: 1.25 !important;
            font-weight: 900 !important;
        }}
        .header-title-34pt {{
            font-size: 36pt !important;
            line-height: 1.18 !important;
            font-weight: 900 !important;
        }}
        .header-subtitle-24pt {{
            font-size: 26pt !important;
            line-height: 1.30 !important;
            font-weight: 700 !important;
        }}
        .badge-16pt {{
            font-size: 18pt !important;
            font-weight: 800 !important;
        }}
        .cover-title-52pt {{
            font-size: 52px !important;
            font-weight: 900 !important;
            line-height: 1.15 !important;
        }}
        .cover-subtitle-28pt {{
            font-size: 28px !important;
            font-weight: 700 !important;
            line-height: 1.35 !important;
        }}
        .cover-meta-22pt {{
            font-size: 22px !important;
            font-weight: 700 !important;
            line-height: 1.4 !important;
        }}

        /* 📱 行動裝置響應式 RWD 規範 (Pad & 手機極致適配，告別跑版與文字截斷) */
        @media (max-width: 1024px) {{
            .point-28pt, .point-multi-card {{
                font-size: 1.35rem !important;
                line-height: 1.45 !important;
            }}
            .card-title-28pt, .card-title-multi {{
                font-size: 1.65rem !important;
            }}
            .header-title-34pt {{
                font-size: 2.1rem !important;
            }}
            .header-subtitle-24pt {{
                font-size: 1.35rem !important;
            }}
            .badge-16pt {{
                font-size: 1.05rem !important;
            }}
            .cover-title-52pt {{
                font-size: 2.5rem !important;
            }}
            .cover-subtitle-28pt {{
                font-size: 1.4rem !important;
            }}
            .cover-meta-22pt {{
                font-size: 1.15rem !important;
            }}
        }}

        @media (max-width: 768px) {{
            html, body {{
                height: 100% !important;
                overflow-x: hidden !important;
            }}
            #slideStage {{
                padding: 0.85rem !important;
                border-radius: 1rem !important;
                overflow-y: auto !important;
                -webkit-overflow-scrolling: touch !important;
            }}
            .point-28pt, .point-multi-card {{
                font-size: 0.95rem !important; /* ~15px */
                line-height: 1.50 !important;
            }}
            .card-title-28pt, .card-title-multi {{
                font-size: 1.15rem !important; /* ~18.5px */
                margin-bottom: 0.5rem !important;
            }}
            .header-title-34pt {{
                font-size: 1.25rem !important; /* ~20px */
                line-height: 1.28 !important;
            }}
            .header-subtitle-24pt {{
                font-size: 0.875rem !important; /* ~14px */
                line-height: 1.35 !important;
                margin-top: 0.25rem !important;
            }}
            .badge-16pt {{
                font-size: 0.72rem !important; /* ~11.5px */
                padding: 0.15rem 0.45rem !important;
                letter-spacing: normal !important;
            }}
            .cover-title-52pt {{
                font-size: 1.65rem !important; /* ~26px */
                line-height: 1.25 !important;
                margin-bottom: 0.75rem !important;
            }}
            .cover-subtitle-28pt {{
                font-size: 1.0rem !important; /* ~16px */
                line-height: 1.45 !important;
            }}
            .cover-meta-22pt {{
                font-size: 0.85rem !important; /* ~13.5px */
                line-height: 1.35 !important;
            }}
            .bullet-dot {{
                font-size: 1.3rem !important;
            }}
        }}

        @media (max-width: 480px) {{
            #slideStage {{
                padding: 0.65rem !important;
            }}
            .point-28pt, .point-multi-card {{
                font-size: 0.875rem !important; /* ~14px */
                line-height: 1.45 !important;
            }}
            .card-title-28pt, .card-title-multi {{
                font-size: 1.05rem !important; /* ~16.8px */
            }}
            .header-title-34pt {{
                font-size: 1.125rem !important; /* ~18px */
            }}
            .header-subtitle-24pt {{
                font-size: 0.8rem !important; /* ~12.8px */
            }}
            .badge-16pt {{
                font-size: 0.65rem !important;
                padding: 0.1rem 0.35rem !important;
            }}
            .cover-title-52pt {{
                font-size: 1.4rem !important;
            }}
            .cover-subtitle-28pt {{
                font-size: 0.9rem !important;
            }}
            .cover-meta-22pt {{
                font-size: 0.78rem !important;
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
        <span id="fsPageIndicator" class="text-teal-300 font-mono text-xs font-bold px-2">1 / 51</span>
        <button id="fsBtnNext" class="bg-blue-600 hover:bg-blue-500 active:scale-95 text-white p-1.5 rounded-lg text-xs font-bold transition-all" title="下一頁 (→ 或 空白鍵)">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"/></svg>
        </button>
        <button id="fsBtnExit" class="bg-slate-800 hover:bg-red-600 text-slate-300 hover:text-white p-1.5 rounded-lg text-xs font-bold ml-1 transition-colors" title="退出全螢幕 (Esc 或 F)">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
    </div>

    <!-- Top Navigation Bar -->
    <header class="min-h-[50px] md:h-16 bg-slate-900/95 border-b border-slate-800 px-2.5 sm:px-4 md:px-6 py-1 md:py-0 flex items-center justify-between shrink-0 shadow-lg z-30 gap-1.5">
        <div class="flex items-center gap-1.5 sm:gap-2 md:gap-3 shrink-0">
            <div class="w-2.5 h-6 md:w-3 md:h-8 bg-gradient-to-b from-blue-500 to-teal-400 rounded-full shrink-0"></div>
            <div>
                <span class="text-[10px] md:text-xs text-teal-400 font-bold tracking-wider hidden sm:block">萬能科技大學 企管系 (進企管四系3甲) ｜ F401 教室</span>
                <h1 class="text-xs sm:text-sm md:text-lg font-black text-white tracking-wide truncate max-w-[105px] sm:max-w-xs md:max-w-md">
                    創意行銷企劃實務
                </h1>
            </div>
            <span id="curriculumModuleTag" class="hidden xl:inline-block text-xs font-bold px-2.5 py-1 bg-blue-950/80 border border-blue-600/50 text-blue-300 rounded-lg ml-2"></span>
        </div>

        <div class="flex items-center gap-1 sm:gap-2 md:gap-3 shrink-0">
            <!-- 回教學平台按鈕 -->
            <a href="index.html" class="hidden sm:inline-flex items-center gap-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white px-2.5 py-1.5 rounded-lg text-xs font-bold border border-slate-700 transition-colors">
                <i class="fas fa-home"></i><span class="hidden md:inline">教學首頁</span>
            </a>

            <!-- Week Selector -->
            <select id="weekSelect" class="bg-slate-800 border border-slate-700 text-white text-[11px] sm:text-xs md:text-sm font-bold rounded-lg px-1.5 py-1 sm:px-2 sm:py-1.5 md:px-2.5 md:py-1.5 focus:ring-2 focus:ring-blue-500 outline-none cursor-pointer hover:bg-slate-750 transition-colors max-w-[95px] sm:max-w-[140px] md:max-w-none">
            </select>

            <!-- Slide Selector -->
            <select id="slideSelect" class="bg-slate-800 border border-slate-700 text-white text-[11px] sm:text-xs md:text-sm font-bold rounded-lg px-1.5 py-1 sm:px-2 sm:py-1.5 md:px-2.5 md:py-1.5 focus:ring-2 focus:ring-teal-500 outline-none cursor-pointer hover:bg-slate-750 transition-colors max-w-[80px] sm:max-w-[120px] md:max-w-[260px] truncate">
            </select>

            <!-- Page Indicator (Desktop / Tablet) -->
            <div id="pageIndicator" class="hidden sm:block bg-slate-800/90 border border-slate-700 text-teal-300 font-mono text-xs md:text-sm font-bold px-2 md:px-3 py-1 md:py-1.5 rounded-lg shrink-0">
                1 / 51
            </div>

            <!-- Prev / Next Controls (Desktop / Tablet) -->
            <button id="btnPrev" class="hidden sm:flex bg-slate-800 hover:bg-slate-700 active:scale-95 text-white p-1.5 md:px-3 md:py-1.5 rounded-lg text-sm font-bold border border-slate-700 items-center gap-1 transition-all shadow" title="上一頁 (←)">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7"/></svg>
                <span class="hidden md:inline">上一頁</span>
            </button>
            <button id="btnNext" class="hidden sm:flex bg-blue-600 hover:bg-blue-500 active:scale-95 text-white p-1.5 md:px-3 md:py-1.5 rounded-lg text-sm font-bold border border-blue-500 items-center gap-1 transition-all shadow-md shadow-blue-600/30" title="下一頁 (→ 或 空白鍵)">
                <span class="hidden md:inline">下一頁</span>
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"/></svg>
            </button>

            <!-- Fullscreen Button -->
            <button id="btnFullscreen" class="bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white p-1 sm:p-1.5 rounded-lg border border-slate-700 transition-colors" title="全螢幕投影模式 (F 或 F11)">
                <svg class="w-4 h-4 md:w-5 md:h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-5h-4m4 0v4m0-4l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"/></svg>
            </button>
        </div>
    </header>

    <!-- Slide Presentation Canvas Stage -->
    <main class="flex-1 overflow-hidden p-1 sm:p-2 md:p-3 flex items-center justify-center bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 w-full h-full">
        <div id="slideStage" class="w-full h-full bg-slate-900/90 rounded-xl sm:rounded-2xl md:rounded-3xl border border-slate-800 shadow-2xl p-3 sm:p-6 md:p-8 lg:p-10 flex flex-col justify-between relative overflow-hidden backdrop-blur-sm">
            <!-- Rendered dynamically -->
        </div>
    </main>

    <!-- 📱 行動端專屬底部懸浮切頁列 (符合拇指人體工學，方便學生單手操作) -->
    <div id="mobileNavBar" class="sm:hidden flex items-center justify-between bg-slate-900/95 border-t border-slate-800 px-3 py-2 shrink-0 z-30 shadow-lg">
        <button id="mBtnPrev" class="bg-slate-800 hover:bg-slate-700 active:scale-95 text-white px-3.5 py-1.5 rounded-lg text-xs font-bold border border-slate-700 flex items-center gap-1.5 shadow">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7"/></svg>
            <span>上一頁</span>
        </button>
        <span id="mPageIndicator" class="text-teal-300 font-mono text-xs font-bold px-2">1 / 51</span>
        <button id="mBtnNext" class="bg-blue-600 hover:bg-blue-500 active:scale-95 text-white px-3.5 py-1.5 rounded-lg text-xs font-bold flex items-center gap-1.5 shadow-md shadow-blue-600/30">
            <span>下一頁</span>
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"/></svg>
        </button>
    </div>

    <!-- Bottom Status Bar (Desktop only) -->
    <footer class="hidden sm:flex h-9 bg-slate-950 border-t border-slate-800/80 px-6 items-center justify-between text-xs text-slate-400 shrink-0">
        <div class="flex items-center gap-4">
            <span class="flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                <span>授課教師：邱俊維 博士 (jimchiu@mail.vnu.edu.tw ｜ J801-1 研究室)</span>
            </span>
            <span class="text-slate-600">|</span>
            <span class="hidden sm:inline text-slate-400">快捷鍵：[← / →] 上下頁 ｜ [空白鍵] 下一頁 ｜ [F] 全螢幕投影 ｜ [Home/End] 首尾頁</span>
        </div>
        <div class="text-slate-400 font-medium">
            參考用書：曾光華《行銷企劃：策略思維與實務運作》(第四版)
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

        // Mobile bottom navigation bar buttons
        const mBtnPrev = document.getElementById('mBtnPrev');
        const mBtnNext = document.getElementById('mBtnNext');
        if (mBtnPrev) mBtnPrev.addEventListener('click', prevSlide);
        if (mBtnNext) mBtnNext.addEventListener('click', nextSlide);

        // Floating full-screen buttons
        document.getElementById('fsBtnPrev').addEventListener('click', prevSlide);
        document.getElementById('fsBtnNext').addEventListener('click', nextSlide);
        document.getElementById('fsBtnExit').addEventListener('click', toggleFullscreen);

        // 📱 觸控手勢滑動支援 (Swipe Left: 下一頁 / Swipe Right: 上一頁)
        const stage = document.getElementById('slideStage');
        let touchStartX = 0;
        let touchStartY = 0;
        let touchEndX = 0;
        let touchEndY = 0;

        stage.addEventListener('touchstart', (e) => {{
            touchStartX = e.changedTouches[0].screenX;
            touchStartY = e.changedTouches[0].screenY;
        }}, {{ passive: true }});

        stage.addEventListener('touchend', (e) => {{
            touchEndX = e.changedTouches[0].screenX;
            touchEndY = e.changedTouches[0].screenY;
            const dx = touchEndX - touchStartX;
            const dy = touchEndY - touchStartY;
            if (Math.abs(dx) > 45 && Math.abs(dx) > Math.abs(dy) * 1.5) {{
                if (dx < 0) {{
                    nextSlide();
                }} else {{
                    prevSlide();
                }}
            }}
        }}, {{ passive: true }});

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
        <div class="border-b border-slate-800 pb-2 md:pb-3 mb-2 md:mb-3 shrink-0">
            <div class="flex flex-wrap items-center justify-between gap-1 mb-1">
                <div class="flex flex-wrap items-center gap-1.5 md:gap-2.5">
                    <span class="badge-16pt tracking-wider px-2 md:px-3 py-0.5 md:py-1 rounded bg-blue-950/80 border border-blue-600/60 text-blue-300 uppercase">
                        ${{escapeHtml(badge || '萬能企管 創意行銷企劃實務')}}
                    </span>
                    ${{sec ? `<span class="badge-16pt font-bold text-slate-300">/ ${{escapeHtml(sec)}}</span>` : ''}}
                </div>
                <span class="badge-16pt font-mono font-bold text-teal-400 bg-slate-800/80 px-2 md:px-3 py-0.5 md:py-1 rounded border border-slate-700">
                    SLIDE ${{curNum}} / ${{total}}
                </span>
            </div>
            <h2 class="header-title-34pt text-white tracking-tight leading-snug">
                ${{escapeHtml(title || '')}}
            </h2>
            ${{subtitle ? `<p class="header-subtitle-24pt text-teal-300 mt-0.5 md:mt-1 leading-normal">${{escapeHtml(subtitle)}}</p>` : ''}}
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
        const mPageInd = document.getElementById('mPageIndicator');
        if (mPageInd) mPageInd.textContent = `${{curNum}} / ${{total}}`;
        document.getElementById('slideSelect').value = currentSlideIdx;

        let html = '';
        const layout = slide.layout || '1card';

        if (layout === 'cover') {{
            html = `
            <div class="h-full flex flex-col justify-between px-3 sm:px-6 md:px-12 py-3 md:py-4 overflow-y-auto custom-scrollbar animate-fadeIn">
                <div class="flex flex-wrap items-center justify-between border-b border-slate-800 pb-3 gap-2">
                    <span class="badge-16pt font-bold tracking-wider text-teal-400 px-3 md:px-4 py-1 md:py-1.5 rounded-full bg-teal-950/60 border border-teal-500/40">
                        ${{escapeHtml(slide.badge || '萬能科技大學 企業管理系')}}
                    </span>
                    <span class="badge-16pt font-mono text-slate-400">11501 學期 ｜ 進企管四系3甲</span>
                </div>
                <div class="my-auto py-4 md:py-6">
                    <h1 class="cover-title-52pt text-white tracking-tight leading-tight mb-3 md:mb-4 drop-shadow-lg">
                        ${{escapeHtml(slide.title)}}
                    </h1>
                    <p class="cover-subtitle-28pt text-teal-300 max-w-4xl leading-relaxed">
                        ${{escapeHtml(slide.subtitle)}}
                    </p>
                </div>
                <div class="pt-3 md:pt-4 border-t border-slate-800 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-2 md:gap-3 text-slate-200 cover-meta-22pt">
                    ${{(slide.meta || []).map(m => `
                    <div class="flex items-center gap-2 bg-slate-800/80 p-2.5 md:p-3 rounded-xl border border-slate-700/80">
                        <span class="w-2.5 h-2.5 rounded-full bg-teal-400 shrink-0"></span>
                        <span class="font-bold">${{escapeHtml(m)}}</span>
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
                <div class="flex-1 flex flex-col justify-center py-1 md:py-2 overflow-y-auto custom-scrollbar">
                    <div class="bg-slate-800/90 rounded-xl md:rounded-2xl border-2 ${{tCard.border}} p-4 md:p-8 shadow-2xl relative overflow-hidden">
                        <div class="absolute top-0 left-0 right-0 h-1.5 md:h-2 bg-gradient-to-r ${{tCard.bar}}"></div>
                        <h3 class="card-title-28pt ${{tCard.text}} mb-2.5 md:mb-4">
                            ${{escapeHtml(card.title)}}
                        </h3>
                        <ul class="space-y-2.5 md:space-y-4 my-auto">
                            ${{(card.points || []).map(p => `
                            <li class="flex items-start gap-2.5 md:gap-3.5 text-slate-100 point-28pt font-bold leading-relaxed">
                                <span class="${{tCard.text}} bullet-dot font-black text-2xl md:text-4xl shrink-0 mt-0.5">•</span>
                                <span class="${{p.includes('★') ? 'text-amber-300 font-black' : ''}}">${{escapeHtml(p)}}</span>
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
                <div class="flex-1 grid grid-cols-1 md:grid-cols-2 gap-3 md:gap-4 lg:gap-6 py-1 md:py-2 items-stretch overflow-y-auto custom-scrollbar">
                    <div class="bg-slate-800/90 rounded-xl md:rounded-2xl border-2 ${{tLeft.border}} p-3.5 sm:p-5 lg:p-7 flex flex-col shadow-2xl relative overflow-hidden">
                        <div class="absolute top-0 left-0 right-0 h-1.5 md:h-2 bg-gradient-to-r ${{tLeft.bar}}"></div>
                        <h3 class="card-title-28pt ${{tLeft.text}} mb-2 md:mb-3.5">
                            ${{escapeHtml(left.title)}}
                        </h3>
                        <ul class="space-y-2 md:space-y-3.5 my-auto">
                            ${{(left.points || []).map(p => `
                            <li class="flex items-start gap-2 md:gap-3 text-slate-100 point-28pt font-bold leading-relaxed">
                                <span class="${{tLeft.text}} bullet-dot font-black text-xl md:text-3xl shrink-0 mt-0.5">•</span>
                                <span class="${{p.includes('★') ? 'text-amber-300 font-black' : ''}}">${{escapeHtml(p)}}</span>
                            </li>
                            `).join('')}}
                        </ul>
                    </div>
                    <div class="bg-slate-800/90 rounded-xl md:rounded-2xl border-2 ${{tRight.border}} p-3.5 sm:p-5 lg:p-7 flex flex-col shadow-2xl relative overflow-hidden">
                        <div class="absolute top-0 left-0 right-0 h-1.5 md:h-2 bg-gradient-to-r ${{tRight.bar}}"></div>
                        <h3 class="card-title-28pt ${{tRight.text}} mb-2 md:mb-3.5">
                            ${{escapeHtml(right.title)}}
                        </h3>
                        <ul class="space-y-2 md:space-y-3.5 my-auto">
                            ${{(right.points || []).map(p => `
                            <li class="flex items-start gap-2 md:gap-3 text-slate-100 point-28pt font-bold leading-relaxed">
                                <span class="${{tRight.text}} bullet-dot font-black text-xl md:text-3xl shrink-0 mt-0.5">•</span>
                                <span class="${{p.includes('★') ? 'text-amber-300 font-black' : ''}}">${{escapeHtml(p)}}</span>
                            </li>
                            `).join('')}}
                        </ul>
                    </div>
                </div>
            </div>
            `;
        }} else if (layout === 'section') {{
            html = `
            <div class="h-full flex flex-col justify-center px-4 py-4 sm:px-8 md:px-20 overflow-y-auto custom-scrollbar animate-fadeIn">
                <div class="inline-block px-3.5 sm:px-5 py-1.5 sm:py-2.5 rounded-xl bg-blue-600 text-white font-black text-xs sm:text-base md:text-lg tracking-widest mb-4 sm:mb-6 w-fit shadow-xl shadow-blue-500/30">
                    ${{escapeHtml(slide.num || 'CHAPTER SECTION')}}
                </div>
                <h2 class="text-2xl sm:text-4xl md:text-5xl lg:text-6xl font-black text-white mb-3 sm:mb-6 leading-tight max-w-5xl drop-shadow-md">
                    ${{escapeHtml(slide.title)}}
                </h2>
                ${{slide.desc ? `<p class="text-sm sm:text-xl md:text-2xl lg:text-3xl text-slate-300 font-semibold max-w-4xl leading-relaxed">${{escapeHtml(slide.desc)}}</p>` : ''}}
            </div>
            `;
        }} else if (layout === '3card') {{
            const cards = slide.cards || (slide.col1 ? [slide.col1, slide.col2, slide.col3] : (slide.c1 ? [slide.c1, slide.c2, slide.c3, slide.c4] : []));
            html = `
            <div class="h-full flex flex-col animate-fadeIn">
                ${{renderHeader(slide.badge, slide.sec, slide.title, slide.subtitle, curNum, total)}}
                <div class="flex-1 grid grid-cols-1 md:grid-cols-3 gap-3 md:gap-4 lg:gap-5 py-1 md:py-2 items-stretch overflow-y-auto custom-scrollbar">
                    ${{cards.map((c, idx) => {{
                        const tCard = getThemeStyles(c.theme || (idx === 0 ? 'blue' : (idx === 1 ? 'teal' : 'amber')));
                        const pointsList = Array.isArray(c.points) ? c.points : (typeof c.points === 'string' ? [c.points] : (c.points ? [c.points] : []));
                        return `
                        <div class="bg-slate-800/90 rounded-xl md:rounded-2xl border-2 ${{tCard.border}} p-3.5 sm:p-5 lg:p-6 flex flex-col shadow-2xl relative overflow-hidden">
                            <div class="absolute top-0 left-0 right-0 h-1.5 md:h-2 bg-gradient-to-r ${{tCard.bar}}"></div>
                            <h3 class="card-title-28pt ${{tCard.text}} mb-2 md:mb-3.5">
                                ${{escapeHtml(c.title)}}
                            </h3>
                            <ul class="space-y-2 md:space-y-3 my-auto">
                                ${{pointsList.map(p => `
                                <li class="flex items-start gap-2 text-slate-100 point-28pt font-bold leading-relaxed">
                                    <span class="${{tCard.text}} bullet-dot font-black text-xl md:text-3xl shrink-0 mt-0.5">•</span>
                                    <span class="${{p.includes('★') ? 'text-amber-300 font-black' : ''}}">${{escapeHtml(p)}}</span>
                                </li>
                                `).join('')}}
                            </ul>
                        </div>
                        `;
                    }}).join('')}}
                </div>
            </div>
            `;
        }} else if (layout === '4card') {{
            const cards = slide.cards || (slide.c1 ? [slide.c1, slide.c2, slide.c3, slide.c4] : (slide.col1 ? [slide.col1, slide.col2, slide.col3, slide.col4] : []));
            html = `
            <div class="h-full flex flex-col animate-fadeIn">
                ${{renderHeader(slide.badge, slide.sec, slide.title, slide.subtitle, curNum, total)}}
                <div class="flex-1 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 md:gap-4 lg:gap-5 py-1 md:py-2 items-stretch overflow-y-auto custom-scrollbar">
                    ${{cards.map((c, idx) => {{
                        const tCard = getThemeStyles(c.theme || (idx === 0 ? 'blue' : (idx === 1 ? 'teal' : (idx === 2 ? 'indigo' : 'amber'))));
                        const pointsList = Array.isArray(c.points) ? c.points : (typeof c.points === 'string' ? [c.points] : (c.points ? [c.points] : []));
                        return `
                        <div class="bg-slate-800/90 rounded-xl md:rounded-2xl border-2 ${{tCard.border}} p-3 sm:p-4 lg:p-5 flex flex-col shadow-2xl relative overflow-hidden">
                            <div class="absolute top-0 left-0 right-0 h-1.5 md:h-2 bg-gradient-to-r ${{tCard.bar}}"></div>
                            ${{c.num ? `
                            <span class="text-xs font-black tracking-wider px-2 py-0.5 rounded ${{tCard.badge}} w-fit mb-1.5">
                                ${{escapeHtml(c.num)}}
                            </span>
                            ` : ''}}
                            <h3 class="card-title-28pt ${{tCard.text}} mb-2 md:mb-3">
                                ${{escapeHtml(c.title)}}
                            </h3>
                            <ul class="space-y-1.5 md:space-y-2.5 my-auto">
                                ${{pointsList.map(p => `
                                <li class="flex items-start gap-1.5 md:gap-2 text-slate-100 point-28pt font-bold leading-relaxed">
                                    <span class="${{tCard.text}} bullet-dot font-black text-lg md:text-2xl shrink-0 mt-0.5">•</span>
                                    <span class="${{p.includes('★') ? 'text-amber-300 font-black' : ''}}">${{escapeHtml(p)}}</span>
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
            <div class="h-full flex flex-col justify-center px-4 sm:px-8 md:px-16 overflow-y-auto custom-scrollbar animate-fadeIn">
                <div class="inline-block px-3 md:px-4 py-1 md:py-1.5 rounded-xl bg-amber-600 text-white font-black text-xs md:text-base tracking-widest mb-3 md:mb-4 w-fit shadow-xl shadow-amber-500/30">
                    WEEKLY UNIT COMPLETED
                </div>
                <h2 class="cover-title-52pt text-white mb-3 md:mb-5 leading-tight max-w-5xl drop-shadow-md">
                    ${{escapeHtml(slide.title || '單元授課完畢')}}
                </h2>
                <p class="cover-subtitle-28pt text-slate-200 font-bold max-w-4xl leading-relaxed mb-4 md:mb-6">
                    ${{escapeHtml(slide.subtitle || '感謝各位進修部同學的專注聽講！請大家課後自主溫習，輕鬆準備考試。')}}
                </p>
                <div class="pt-3 md:pt-5 border-t-2 border-slate-800 font-bold text-teal-400 cover-meta-22pt">
                    ${{escapeHtml(slide.final_message || '學期考核評分：期中考 40% ✕ 期末考 40% ✕ 平時出席 20%')}}
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
                }}).catch(err => {{
                    console.log("Exit fullscreen failed", err);
                    document.body.classList.remove('is-fullscreen-active');
                }});
            }} else {{
                document.body.classList.remove('is-fullscreen-active');
            }}
        }}
    }}

    document.addEventListener('DOMContentLoaded', () => {{
        initUI();
    }});
    </script>
</body>
</html>"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Successfully generated Full_Screen_Presentation.html at: {output_path}")

if __name__ == '__main__':
    build_presentation_html()
