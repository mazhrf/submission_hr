import joblib
import pandas as pd

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

data_baru = pd.DataFrame([{
    'Age': 28,
    'Department': 'Sales',
    'Education': 2,
    'EducationField': 'Marketing',
    'EnvironmentSatisfaction': 1,
    'Gender': 'Female',
    'JobInvolvement': 1,
    'JobLevel': 1,
    'JobRole': 'Sales Executive',
    'MaritalStatus': 'Single',
    'MonthlyIncome': 2000,
    'PerformanceRating': 2,
    'RelationshipSatisfaction': 1,
    'TotalWorkingYears': 3,
    'WorkLifeBalance': 1,
    'YearsAtCompany': 2,
}])

map_gender = {'Male': 1, 'Female': 0}
map_dept = {'Sales': 2, 'Research & Development': 1, 'Human Resources': 0}
map_edu_field = {'Life Sciences': 1, 'Medical': 3, 'Marketing': 2, 'Technical Degree': 5, 'Other': 4, 'Human Resources': 0}
map_role = {
    'Research Scientist': 6, 'Laboratory Technician': 3, 'Sales Executive': 8, 'Manufacturing Director': 4,
    'Healthcare Representative': 2, 'Manager': 5, 'Sales Representative': 9,
    'Research Director': 7, 'Human Resources': 1
}
map_marital = {'Single': 2, 'Married': 1, 'Divorced': 0}

data_baru['Gender'] = data_baru['Gender'].map(map_gender)
data_baru['Department'] = data_baru['Department'].map(map_dept)
data_baru['EducationField'] = data_baru['EducationField'].map(map_edu_field)
data_baru['JobRole'] = data_baru['JobRole'].map(map_role)
data_baru['MaritalStatus'] = data_baru['MaritalStatus'].map(map_marital)

urutan_kolom = [
    'Age', 'Department', 'Education', 'EducationField', 'EnvironmentSatisfaction',
    'Gender', 'JobInvolvement', 'JobLevel', 'JobRole', 'MaritalStatus',
    'MonthlyIncome', 'PerformanceRating', 'RelationshipSatisfaction',
    'TotalWorkingYears', 'WorkLifeBalance', 'YearsAtCompany'
]

data_baru = data_baru[urutan_kolom]
data_scaled = scaler.transform(data_baru)

prediction = model.predict(data_scaled)
proba = model.predict_proba(data_scaled)

print("Hasil Prediksi:")
if prediction[0] == 1:
    print(f"Karyawan diprediksi AKAN keluar (Attrition = 1), kemungkinan: {proba[0][1]:.2%}")
else:
    print(f"Karyawan diprediksi TIDAK AKAN keluar (Attrition = 0), kemungkinan keluar: {proba[0][0]:.2%}")