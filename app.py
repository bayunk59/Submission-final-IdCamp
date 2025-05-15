import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing
from prediction import prediction

col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeDeyMHCgnWg5l6dc9ojBy51apxUs1qfuntw&s", width=130)
with col2:
    st.header('Jaya Institute App (Prototype)')


# Membaca data dengan delimiter ';'
data = pd.read_csv("data.csv", delimiter=';')
data.columns = data.columns.str.strip()  # Bersihkan spasi

st.subheader('Identitas')

col1, col2 = st.columns(2)
with col1:
    Gender = st.selectbox("Gender", ["Laki-laki", "Perempuan"])
    gender_value = 1 if Gender == "Laki-laki" else 0
    
with col2:
    Age = st.number_input("Age At Enrollment", min_value=0, max_value=100, value=18)


col1, col2, col3 = st.columns(3)
with col1:
    Debtor = st.selectbox("Debtor", ["Iya", "Tidak"])
    debtor_value = 1 if Debtor == "Iya" else 0
    
with col2:
    Scholarship = st.selectbox("Scholarship holder", ["Iya", "Tidak"])
    scholarship_value = 1 if Scholarship == "Iya" else 0
    
with col3:
    Tuition = st.selectbox("Tuition Fees Up To Date", ["Iya", "Tidak"])
    tuition_value = 1 if Tuition == "Iya" else 0
    

st.subheader('Curricular Units 1st Semester')

col1, col2, col3, col4 = st.columns(4)
with col1:
    Enrolled1 = st.number_input("Enrolled 1st (0 - 30)", min_value=0, max_value=30, value=0)

with col2:
    Approved1 = st.number_input("Approved 1st (0 - 30)", min_value=0, max_value=30, value=0)
    
with col3:
    Grade1 = st.number_input("Grade 1st (0 - 20)", min_value=0, max_value=20, value=0)
  
with col4:
    Evaluations1 = st.number_input("Evaluations 1st (0 - 50)", min_value=0, max_value=50, value=0)
 

st.subheader('Curricular Units 2nd Semester')

col1, col2, col3, col4 = st.columns(4)
with col1:
    Enrolled2 = st.number_input("Enrolled 2nd (0 - 30)", min_value=0, max_value=30, value=0)

with col2:
    Approved2 = st.number_input("Approved 2nd (0 - 30)", min_value=0, max_value=30, value=0)
    
with col3:
    Grade2 = st.number_input("Grade 2nd (0 - 20)", min_value=0, max_value=20, value=0) 

with col4:
    Evaluations2 = st.number_input("Evaluations 2nd (0 - 50)", min_value=0, max_value=50, value=0)


    
# Simpan input user ke dictionary (untuk prediksi)
input_data = {
    "Age_at_enrollment": Age,
    "Gender": gender_value,
    "Scholarship_holder": scholarship_value,
    "Curricular_units_1st_sem_enrolled": Enrolled1,
    "Curricular_units_1st_sem_evaluations": Evaluations1,
    "Curricular_units_1st_sem_approved": Approved1,
    "Curricular_units_1st_sem_grade": Grade1,
    "Curricular_units_2nd_sem_enrolled": Enrolled2,
    "Curricular_units_2nd_sem_evaluations": Evaluations2,
    "Curricular_units_2nd_sem_approved": Approved2,
    "Curricular_units_2nd_sem_grade": Grade2,
    "Debtor": debtor_value,
    "Tuition_fees_up_to_date": tuition_value,
}

input_df = pd.DataFrame([input_data])

with st.expander("View the Raw Data"):
    st.dataframe(input_df, width=800, height=10)
    
if st.button('Predict'):
    new_data = data_preprocessing(data=input_df)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Status: {}".format(prediction(new_data)))