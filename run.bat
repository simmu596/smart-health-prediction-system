@echo off
echo Setting up and running Smart Health Prediction System...
cd /d %~dp0

if not exist venv (
echo Creating virtual environment...
python -m venv venv
)

echo Activating venv...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo Starting app...
streamlit run app.py

pause
