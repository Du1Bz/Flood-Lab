@echo off
cd /d "%~dp0"
chcp 65001 >nul
setlocal
title Flood-Lab

cls
echo.
echo  ____                                   __        ____    ___                       __     
echo /\  _`\               __               /\ \__    /\  _`\ /\_ \                     /\ \    
echo \ \ \L\ \_ __   ___  /\_\     __    ___\ \ ,_\   \ \ \L\_\//\ \     ___     ___    \_\ \   
echo  \ \ ,__/\`'__\/ __`\\/\ \  /'__`\ /'___\ \ \/    \ \  _\/ \ \ \   / __`\  / __`\  /'_` \  
echo   \ \ \/\ \ \//\ \L\ \\ \ \/\  __//\ \__/\ \ \_    \ \ \/   \_\ \_/\ \L\ \/\ \L\ \/\ \L\ \ 
echo    \ \_\ \ \_\\ \____/_\ \ \ \____\ \____\\ \__\    \ \_\   /\____\ \____/\ \____/\ \___,_\
echo     \/_/  \/_/ \/___//\ \_\ \/____/\/____/ \/__/     \/_/   \/____/\/___/  \/___/  \/__,_ /
echo                      \ \____/                                                              
echo                       \/___/                                                               
echo.
echo ===========================================================================================
echo                                     Flood-Lab  起動中...
echo ===========================================================================================
echo.

:: --------------------------------------------------
:: 1. Python チェック
:: --------------------------------------------------
python --version >nul 2>&1
if errorlevel 1 (
    echo [Error] Python が見つかりませんでした。
    echo         https://www.python.org/downloads/
    goto :error
)

:: --------------------------------------------------
:: 2. Python バージョンチェック（3.11 未満は警告）
:: --------------------------------------------------
for /f "tokens=2" %%V in ('python --version 2^>^&1') do set "PY_VER=%%V"
for /f "tokens=1,2 delims=." %%A in ("%PY_VER%") do (
    set "PY_MAJOR=%%A"
    set "PY_MINOR=%%B"
)
if %PY_MAJOR% LSS 3 (
    echo [Error] Python %PY_VER% が検出されました。Python 3.11 以上が必要です。
    goto :error
)
if %PY_MAJOR% EQU 3 if %PY_MINOR% LSS 11 (
    echo [Warning] Python %PY_VER% detected. Python 3.11 or later is recommended.
    echo.
) else (
    echo [OK] Python %PY_VER%
    echo.
)

:: --------------------------------------------------
:: 3. ポート 8501 の使用状況チェック
:: --------------------------------------------------
netstat -ano | findstr ":8501 " | findstr "LISTENING" >nul 2>&1
if not errorlevel 1 (
    :: PID を取得
    for /f "tokens=5" %%P in ('netstat -ano ^| findstr ":8501 " ^| findstr "LISTENING"') do set "PORT_PID=%%P"

    :: そのPIDのプロセス名を取得して streamlit か確認
    set "IS_STREAMLIT=0"
    for /f "tokens=1" %%N in ('tasklist /fi "pid eq %PORT_PID%" /fo csv /nh 2^>nul') do (
        echo %%N | findstr /i "streamlit python" >nul 2>&1
        if not errorlevel 1 set "IS_STREAMLIT=1"
    )

    if "%IS_STREAMLIT%"=="1" (
        echo [Info] Flood-Lab is already running.
        echo        Opening http://localhost:8501 ...
        start "" "http://localhost:8501"
        goto :end
    ) else (
        echo [Error] Port 8501 is already in use by another application.
        echo         PID: %PORT_PID%
        echo         Please close that application and try again.
        goto :error
    )
)

:: --------------------------------------------------
:: 4. .venv がなければ作成
:: --------------------------------------------------
if not exist ".venv\" (
    echo [Setup] Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo [Error] Failed to create virtual environment.
        goto :error
    )
    echo [Setup] Virtual environment created.
    echo.
)

:: --------------------------------------------------
:: 5. requirements.txt チェック
:: --------------------------------------------------
if not exist "requirements.txt" (
    echo [Error] requirements.txt not found.
    echo         Please check the Flood-Lab folder.
    goto :error
)

:: --------------------------------------------------
:: 6. 依存関係インストール
:: --------------------------------------------------
echo [Setup] Installing dependencies...
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 (
    echo [Error] Failed to install dependencies.
    echo         Please check your network connection.
    goto :error
)
echo [Setup] Dependencies are up to date.
echo.

:: --------------------------------------------------
:: 7. config.ini がなければ example からコピー
:: --------------------------------------------------
if not exist "config.ini" (
    if exist "config.ini.example" (
        copy config.ini.example config.ini >nul
        echo [Setup] config.ini created from example.
        echo.
    ) else (
        echo [Warning] config.ini.example not found. config.ini was not created.
        echo.
    )
)

:: --------------------------------------------------
:: 8. app.py チェック
:: --------------------------------------------------
if not exist "app.py" (
    echo [Error] app.py not found.
    echo         Please check the Flood-Lab folder.
    goto :error
)

:: --------------------------------------------------
:: 9. OpenSpartan DB チェック
:: --------------------------------------------------
echo [Check] Checking OpenSpartan data files...
set "OS_DATA_DIR=%LOCALAPPDATA%\OpenSpartan.Workshop\data"

if not exist "%OS_DATA_DIR%\" (
    echo [Warning] OpenSpartan data folder not found.
    echo           %OS_DATA_DIR%
    echo           Please launch OpenSpartan Workshop and sync your data.
    echo.
    goto :launch
)

set "DB_FOUND=0"
for %%F in ("%OS_DATA_DIR%\*.db") do set "DB_FOUND=1"

if "%DB_FOUND%"=="0" (
    echo [Warning] No .db file found in OpenSpartan data folder.
    echo           %OS_DATA_DIR%
    echo           Please launch OpenSpartan Workshop and sync your data.
    echo.
) else (
    echo [OK] OpenSpartan data file confirmed.
    echo.
)

:: --------------------------------------------------
:: 10. Streamlit 起動
:: --------------------------------------------------
:launch
echo ===========================================================================================
echo  Open http://localhost:8501 in your browser.
echo  Press Ctrl+C or close this window to stop.
echo ===========================================================================================
echo.
.venv\Scripts\streamlit run app.py
if errorlevel 1 (
    echo.
    echo [Error] Streamlit exited with an error.
    echo         Please check the log above.
    goto :error
)
goto :end

:: --------------------------------------------------
:: エラー終了
:: --------------------------------------------------
:error
echo.
echo -------------------------------------------------------------------------------------------
echo  An error occurred. Process aborted.
echo -------------------------------------------------------------------------------------------
pause
exit /b 1

:end
endlocal