# importing the necessary libraries
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# reading the csv files and storing it in the respective dataframes
patients_df = pd.read_csv(r"C:\Users\vish9\Downloads\SUNY\question\question\patient.csv")
visits_df = pd.read_csv(r"C:\Users\vish9\Downloads\SUNY\question\question\visit.csv", parse_dates = ['visit_date'])
diagnosis_df = pd.read_csv(r"C:\Users\vish9\Downloads\SUNY\question\question\diagnosis.csv", parse_dates = ['diagnosis_date'])

# assigning the variables according to the task
diagnosis_code = "D1.2"
days_within = 7
unit_name = "Unit01"

# patients diagnosed with D1.2
diagnosed_patient = diagnosis_df[diagnosis_df["diagnosis"] == diagnosis_code]["person_id"]

# filtering patients in Unit01 as well diagnosed with D1.2
U1_visits = visits_df[(visits_df["unit_name"]== unit_name) & (visits_df["person_id"].isin(diagnosed_patient))]

# to calculate the number of patients
count = 0

#iterating the Unit01 D1.2 patients
for _, visit in U1_visits.iterrows():
    visit_date = visit['visit_date']    #storing the visit date
    patient_id = visit['person_id']     #storing the patient id

   
# iterating over the diagnosis_df and checking whether the person_id matches as well as the diagnosis code D1.2
    for _, diagnosis in diagnosis_df[(diagnosis_df['person_id']==patient_id) & (diagnosis_df["diagnosis"] == diagnosis_code)].iterrows():
        diagnosed_date = diagnosis['diagnosis_date']    

        #if its within 7days then incrementing the count
        if (visit_date - diagnosed_date).days <= days_within:
            count+=1
            break

print("The number of patients diagnosed with", diagnosis_code,"who visited", unit_name, "within 7 days is", count)

# plotting the result for better understanding
labels = ['D1.2 Diagnosed Patients', 'Count of patients within 7 days in Unit01']
values = [len(diagnosed_patient), count]

plt.bar(labels, values, color=['blue', 'green'])
plt.xlabel('D1.2 Patients in Unit01')
plt.ylabel('Number of Patients')
plt.title('Patients Diagnosed with D1.2 and visited Unit01 within 7 Days')
plt.show()