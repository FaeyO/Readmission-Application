from flask import Flask,request,jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('random_forest_model.pkl', 'rb'))

@app.route('/')
def home():
    return "Greetings and welcome to the Patient Readmission Detector Api!"

@app.route("/predict", methods=['GET'])
def predict():
    #float_features = [float(x) for x in request.form.values()]
    #features = [np.array(float_features)]
    time_in_hospital = request.args.get('time_in_hospital')
    n_lab_procedures = request.args.get('n_lab_procedures')
    n_procedures = request.args.get('n_procedures')
    n_medications = request.args.get('n_medications')
    n_outpatient = request.args.get('n_outpatient')
    n_inpatient = request.args.get('n_inpatient')
    n_emergency = request.args.get('n_emergency')
    primary_diagnosis_Diabetes = request.args.get('primary_diagnosis_Diabetes')
    primary_diagnosis_Digestive = request.args.get('primary_diagnosis_Digestive')
    primary_diagnosis_Injury = request.args.get('primary_diagnosis_Injury')
    primary_diagnosis_Missing = request.args.get('primary_diagnosis_Missing')
    primary_diagnosis_Musculoskeletal = request.args.get('primary_diagnosis_Musculoskeletal')
    primary_diagnosis_Other = request.args.get('primary_diagnosis_Other')
    primary_diagnosis_Respiratory = request.args.get('primary_diagnosis_Respiratory')
    sec_diagnosis_Diabetes = request.args.get('sec_diagnosis_Diabetes')
    sec_diagnosis_Digestive = request.args.get('sec_diagnosis_Digestive')
    sec_diagnosis_Injury = request.args.get('sec_diagnosis_Injury')
    sec_diagnosis_Missing = request.args.get('sec_diagnosis_Missing')
    sec_diagnosis_Musculoskeletal = request.args.get('sec_diagnosis_Musculoskeletal')
    sec_diagnosis_Other = request.args.get('sec_diagnosis_Other')
    sec_diagnosis_Respiratory = request.args.get('sec_diagnosis_Respiratory')
    additional_sec_diag_Diabetes = request.args.get('additional_sec_diag_Diabetes')
    additional_sec_diag_Digestive = request.args.get('additional_sec_diag_Digestive')
    additional_sec_diag_Injury = request.args.get('additional_sec_diag_Injury')
    additional_sec_diag_Missing = request.args.get('additional_sec_diag_Missing')
    additional_sec_diag_Musculoskeletal = request.args.get('additional_sec_diag_Musculoskeletal')
    additional_sec_diag_Other = request.args.get('additional_sec_diag_Other')
    additional_sec_diag_Respiratory = request.args.get('additional_sec_diag_Respiratory')
    glucose_test_no  = request.args.get('glucose_test_no')
    glucose_test_normal  = request.args.get('glucose_test_normal')
    HbA1ctest_no = request.args.get('HbA1ctest_no')
    HbA1ctest_normal = request.args.get('HbA1ctest_normal')
    med_change_yes = request.args.get('med_change_yes')
    diabetes_med_yes = request.args.get('diabetes_med_yes')
    age_cat_early_middle_age = request.args.get('age_cat_early-middle age')
    age_cat_late_middle_age = request.args.get('age_cat_late-middle age')
    age_cat_mid_old_age = request.args.get('age_cat_mid-old age')
    age_cat_senior_old_age = request.args.get('age_cat_senior-old age')
    age_cat_very_senior_old = request.args.get('age_cat_very senior-old')
 

    
    #makepredictions = model.predict(features)
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
    return jsonify({'Your readmission status is':output})

if __name__ == "__main__":
    app.run(debug=True)