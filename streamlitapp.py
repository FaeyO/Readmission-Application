import pickle
import streamlit as st
import sys
import path


dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)


model = pickle.load(open('./random_forest_model.pkl','rb'))

def main():
    st.title('Patient Readmission Detector Api!')

    time_in_hospital = st.text_input('time_in_hospital')
    n_lab_procedures = st.text_input('n_lab_procedures')
    n_procedures = st.text_input('n_procedures')
    n_medications = st.text_input('n_medications')
    n_outpatient = st.text_input('n_outpatient')
    n_inpatient = st.text_input('n_inpatient')
    n_emergency = st.text_input('n_emergency')
    # primary_diag_list = ['primary_diagnosis_Diabetes','primary_diagnosis_Digestive','primary_diagnosis_Injury','primary_diagnosis_Missing','primary_diagnosis_Musculoskeletal','primary_diagnosis_Other','primary_diagnosis_Respiratory']
    # primary_diagnosis = st.selectbox('Primary_diagnosis', primary_diag_list)
    primary_diagnosis_Diabetes = st.text_input('primary_diagnosis_Diabetes')
    primary_diagnosis_Digestive = st.text_input('primary_diagnosis_Digestive')
    primary_diagnosis_Injury = st.text_input('primary_diagnosis_Injury')
    primary_diagnosis_Missing = st.text_input('primary_diagnosis_Missing')
    primary_diagnosis_Musculoskeletal = st.text_input('primary_diagnosis_Musculoskeletal')
    primary_diagnosis_Other = st.text_input('primary_diagnosis_Other')
    primary_diagnosis_Respiratory = st.text_input('primary_diagnosis_Respiratory')
    sec_diagnosis_Diabetes = st.text_input('sec_diagnosis_Diabetes')
    sec_diagnosis_Digestive = st.text_input('sec_diagnosis_Digestive')
    sec_diagnosis_Injury = st.text_input('sec_diagnosis_Injury')
    sec_diagnosis_Missing = st.text_input('sec_diagnosis_Missing')
    sec_diagnosis_Musculoskeletal = st.text_input('sec_diagnosis_Musculoskeletal')
    sec_diagnosis_Other = st.text_input('sec_diagnosis_Other')
    sec_diagnosis_Respiratory = st.text_input('sec_diagnosis_Respiratory')
    additional_sec_diag_Diabetes = st.text_input('additional_sec_diag_Diabetes')
    additional_sec_diag_Digestive = st.text_input('additional_sec_diag_Digestive')
    additional_sec_diag_Injury = st.text_input('additional_sec_diag_Injury')
    additional_sec_diag_Missing = st.text_input('additional_sec_diag_Missing')
    additional_sec_diag_Musculoskeletal = st.text_input('additional_sec_diag_Musculoskeletal')
    additional_sec_diag_Other = st.text_input('additional_sec_diag_Other')
    additional_sec_diag_Respiratory = st.text_input('additional_sec_diag_Respiratory')
    glucose_test_no  = st.text_input('glucose_test_no')
    glucose_test_normal  = st.text_input('glucose_test_normal')
    HbA1ctest_no = st.text_input('HbA1ctest_no')
    HbA1ctest_normal = st.text_input('HbA1ctest_normal')
    med_change_yes = st.text_input('med_change_yes')
    diabetes_med_yes = st.text_input('diabetes_med_yes')
    age_cat_early_middle_age = st.text_input('age_cat_early-middle age')
    age_cat_late_middle_age = st.text_input('age_cat_late-middle age')
    age_cat_mid_old_age = st.text_input('age_cat_mid-old age')
    age_cat_senior_old_age =st.text_input('age_cat_senior-old age')
    age_cat_very_senior_old = st.text_input('age_cat_very senior-old')

    if st.button('Predict'):
        makepredictions = model.predict([[time_in_hospital,n_lab_procedures,
                                      n_procedures,n_medications,n_outpatient,n_inpatient,n_emergency,
                                      primary_diagnosis_Diabetes,primary_diagnosis_Digestive,primary_diagnosis_Injury,
                                      primary_diagnosis_Missing,primary_diagnosis_Musculoskeletal,primary_diagnosis_Other,
                                      primary_diagnosis_Respiratory,sec_diagnosis_Diabetes,sec_diagnosis_Digestive,sec_diagnosis_Injury,
                                      sec_diagnosis_Missing,sec_diagnosis_Musculoskeletal,sec_diagnosis_Other,sec_diagnosis_Respiratory,
                                      additional_sec_diag_Diabetes,additional_sec_diag_Digestive,additional_sec_diag_Injury,additional_sec_diag_Missing,
                                      additional_sec_diag_Musculoskeletal,additional_sec_diag_Other,additional_sec_diag_Respiratory,
                                      glucose_test_no,glucose_test_normal,HbA1ctest_no,HbA1ctest_normal,med_change_yes,diabetes_med_yes,
                                      age_cat_early_middle_age,age_cat_late_middle_age,age_cat_mid_old_age,age_cat_senior_old_age,age_cat_very_senior_old]])

        output = round(int(makepredictions[0]))

        st.success('Your readmission status is {}'.format(output))

if __name__ == '__main__':
    main()

 