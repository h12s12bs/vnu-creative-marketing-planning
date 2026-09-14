@echo off
chcp 65001 >nul
title 萬能科技大學 - 創意行銷企劃實務 ✕ Agentic AI 教學平台

echo ======================================================================
echo   萬能科技大學【創意行銷企劃實務 ✕ Agentic AI】互動教學與練習平台
echo   授課教師：邱俊維 博士 (Dr. Chun-Wei Chiu)
echo   開課班級：進企管四系3甲 (週一 10~11 節)
echo   授課地點：F401 教室
echo ======================================================================
echo.

where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [提示] 找不到 Python 環境。
    echo 本平台具備免安裝單機離線版，正在為您開啟：平台首頁(單機離線直接點開).html
    start "" "平台首頁(單機離線直接點開).html"
    pause
    exit /b 0
)

echo [1/2] 正在為您啟動教學伺服器...
start "" http://localhost:5000

echo [2/2] 系統已就緒！瀏覽器已自動為您開啟：
echo.
python app.py

pause
