import pandas as pd
import joblib

model = joblib.load("model/model.pkl")
encoder = joblib.load("model/encoder.pkl")

data_baru = pd.DataFrame({
    "JobRole": ["Sales Executive"],
    "OverTime": ["Yes"],
    "MaritalStatus": ["Single"],
    "Age": [28],
    "JobInvolvement": [3],
    "YearsWithCurrManager": [2],
    "StockOptionLevel": [1],
    "YearsAtCompany": [3],
    "YearsInCurrentRole": [2],
    "TotalWorkingYears": [5],
    "JobSatisfaction": [4],
    "MonthlyIncome": [4500]
})

import_cat = ['JobRole', 'OverTime', 'MaritalStatus']
import_num = ['Age', 'JobInvolvement', 'YearsWithCurrManager', 'StockOptionLevel', 'YearsAtCompany', 'YearsInCurrentRole', 'TotalWorkingYears', 'JobSatisfaction', 'MonthlyIncome']

X_cat = encoder.transform(data_baru[import_cat])
cat_cols = encoder.get_feature_names_out(import_cat)

X_num = data_baru[import_num].reset_index(drop=True)
X_ready = pd.concat([X_num, pd.DataFrame(X_cat, columns=cat_cols)], axis=1)

prediction = model.predict(X_ready)
proba = model.predict_proba(X_ready)

print("Hasil Prediksi:")
if prediction == 1:
    print(f"Karyawan diprediksi AKAN keluar (Attrition = 1), kemungkinan: {proba[0][1]:.2%}")
else:
    print(f"Karyawan diprediksi TIDAK AKAN keluar (Attrition = 0), kemungkinan keluar: {proba[0][0]:.2%}")