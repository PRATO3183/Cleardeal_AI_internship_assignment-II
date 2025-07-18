@echo off
echo.
:: Step 1: Activating Venv
echo 🔄 Activating virtual environment...
::call cleardealII\Scripts\activate

echo.

:: Step 2: Install dependencies
::echo 📦 Installing required packages...
::pip install -r requirements.txt


echo.

:: Step 3: Train model and save model
echo 🧠 Processing data and saving features...
echo 🤖 Training the model...
python model\train_model.py

::echo cd backend

echo.

:: Step 4: Launch FastAPI server
echo 🚀 Starting FastAPI server on http://localhost:8000 ...
uvicorn api.main:app --reload

pause