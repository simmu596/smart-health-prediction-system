# Smart Health Prediction System

A machine learning web app to predict health risks like heart disease and diabetes using user inputs (age, BMI, etc.). Powered by Streamlit and scikit-learn.

## Features
- Predict heart disease risk
- Predict diabetes risk  
- Visual results and recommendations
- Trained on realistic sample data
- Save predictions to SQLite database
- View prediction history in-app

## Easy Run (Windows) - Double-click!
1. Double-click `run.bat` (handles venv, deps, launch automatically)

Or manual:
1. `cd C:/Users/Sanjay/Desktop/smart_health_prediction_system`
2. `run.bat`

App opens in browser.

## Deploy to Streamlit Cloud (Public URL)
1. Install Git: [git-scm.com/download/win](https://git-scm.com/download/win)
2. `git init`, `git add .`, `git commit -m "init"`
3. Create GitHub repo, `git remote add origin URL`, `git branch -M main`, `git push -u origin main`
4. Visit [share.streamlit.io/new](https://share.streamlit.io/new), connect repo, "Deploy" → Instant public URL!

## Database
Predictions are automatically saved to a local SQLite database (`health_predictions.db`) when you click **Get Recommendations**. You can view your prediction history directly in the app.

> **Note:** On Streamlit Cloud, the filesystem is ephemeral, so SQLite data resets on redeploy. For persistent cloud storage, switch to PostgreSQL (e.g., Supabase, Neon) or connect an external database.

## Tech
- Streamlit (UI)
- scikit-learn (ML)
- Pandas/Numpy (data)
- Plotly (charts)
- SQLite (database)

