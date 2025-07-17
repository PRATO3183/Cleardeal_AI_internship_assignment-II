@echo off
echo Activating virtual environment...
call cleardealII\Scripts\activate

echo Starting FastAPI server...
uvicorn backend.main:app --reload

pause