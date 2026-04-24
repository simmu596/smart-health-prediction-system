import pandas as pd
import numpy as np

def get_heart_data():
    np.random.seed(42)
    n_samples = 303
    data = pd.DataFrame({
        'age': np.random.randint(28, 77, n_samples),
        'sex': np.random.randint(0, 2, n_samples),  # 0: female, 1: male
        'cp': np.random.randint(0, 4, n_samples),  # chest pain type
        'trestbps': np.random.normal(130, 17, n_samples).astype(int),  # resting bp
        'chol': np.random.normal(247, 51, n_samples).astype(int),  # cholesterol
        'fbs': np.random.randint(0, 2, n_samples),  # fasting blood sugar
        'restecg': np.random.randint(0, 3, n_samples),
        'thalach': np.random.randint(71, 202, n_samples),  # max heart rate
        'exang': np.random.randint(0, 2, n_samples),  # exercise angina
        'oldpeak': np.round(np.random.uniform(0, 6.2, n_samples), 1),
        'slope': np.random.randint(0, 3, n_samples),
        'ca': np.random.randint(0, 4, n_samples),  # vessels
        'thal': np.random.randint(0, 4, n_samples)
    })
    data['target'] = (data['age'] > 50) & (data['chol'] > 240) | (data['trestbps'] > 160)
    data['target'] = data['target'].astype(int)  # 0: no disease, 1: disease
    return data

def get_diabetes_data():
    np.random.seed(42)
    n_samples = 303
    data = pd.DataFrame({
        'bmi': np.round(np.random.normal(32, 7, n_samples), 1),
        'glucose': np.random.normal(120, 30, n_samples).astype(int),
        'age': np.random.randint(20, 80, n_samples),
        'insulin': np.random.exponential(80, n_samples).astype(int),
        'bp': np.random.normal(80, 15, n_samples).astype(int)  # blood pressure
    })
    data['diabetes'] = ((data['bmi'] > 30) | (data['glucose'] > 140)).astype(int)
    return data

if __name__ == '__main__':
    print(get_heart_data().head())

