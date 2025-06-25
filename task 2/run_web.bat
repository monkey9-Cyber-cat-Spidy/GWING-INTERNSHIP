@echo off
echo Starting Number Guessing Game Web Interface...
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting Flask web server...
echo The game will be available at: http://localhost:5001
echo Press Ctrl+C to stop the server
echo.
python app.py
pause 