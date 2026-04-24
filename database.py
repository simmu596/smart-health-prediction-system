import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "health_predictions.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            heart_age INTEGER,
            heart_sex INTEGER,
            heart_cp INTEGER,
            heart_trestbps INTEGER,
            heart_chol INTEGER,
            heart_fbs INTEGER,
            heart_restecg INTEGER,
            heart_thalach INTEGER,
            heart_exang INTEGER,
            heart_oldpeak REAL,
            heart_slope INTEGER,
            heart_ca INTEGER,
            heart_thal INTEGER,
            heart_prob REAL,
            heart_pred TEXT,
            diabetes_bmi REAL,
            diabetes_glucose INTEGER,
            diabetes_age INTEGER,
            diabetes_insulin INTEGER,
            diabetes_bp INTEGER,
            diabetes_prob REAL,
            diabetes_pred TEXT
        )
    """
    )
    conn.commit()
    conn.close()


def save_prediction(data: dict):
    init_db()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO predictions (
            timestamp, heart_age, heart_sex, heart_cp, heart_trestbps, heart_chol, heart_fbs,
            heart_restecg, heart_thalach, heart_exang, heart_oldpeak, heart_slope, heart_ca, heart_thal,
            heart_prob, heart_pred, diabetes_bmi, diabetes_glucose, diabetes_age, diabetes_insulin,
            diabetes_bp, diabetes_prob, diabetes_pred
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (
            datetime.now().isoformat(),
            data.get("heart_age"),
            data.get("heart_sex"),
            data.get("heart_cp"),
            data.get("heart_trestbps"),
            data.get("heart_chol"),
            data.get("heart_fbs"),
            data.get("heart_restecg"),
            data.get("heart_thalach"),
            data.get("heart_exang"),
            data.get("heart_oldpeak"),
            data.get("heart_slope"),
            data.get("heart_ca"),
            data.get("heart_thal"),
            data.get("heart_prob"),
            data.get("heart_pred"),
            data.get("diabetes_bmi"),
            data.get("diabetes_glucose"),
            data.get("diabetes_age"),
            data.get("diabetes_insulin"),
            data.get("diabetes_bp"),
            data.get("diabetes_prob"),
            data.get("diabetes_pred"),
        ),
    )
    conn.commit()
    conn.close()


def get_predictions(limit: int = 50):
    init_db()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT id, timestamp, heart_age, heart_sex, heart_cp, heart_trestbps, heart_chol, heart_fbs,
               heart_restecg, heart_thalach, heart_exang, heart_oldpeak, heart_slope, heart_ca, heart_thal,
               heart_prob, heart_pred, diabetes_bmi, diabetes_glucose, diabetes_age, diabetes_insulin,
               diabetes_bp, diabetes_prob, diabetes_pred
        FROM predictions ORDER BY timestamp DESC LIMIT ?
    """,
        (limit,),
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

