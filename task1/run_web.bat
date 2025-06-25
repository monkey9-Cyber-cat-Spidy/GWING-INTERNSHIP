@echo off
echo Starting Quiz Game Web Interface...
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting Flask web server...
echo The game will be available at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python app.py
pause 