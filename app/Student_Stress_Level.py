import joblib
import pandas as pd 
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
model_path = BASE_DIR / "pickle_files" / "student_stress_model.pkl"

model = joblib.load(model_path)

def app():
    while True:
        situation = input("lets predict your data (for exit please write : exit) else click Enter or write anything you want. ")
        if situation != "exit":
            Student_Type= input("Student_Type(school, college, working_student): ")
            Sleep_Hours= int(input("Sleep_Hours: "))
            Study_Hours= int(input("Study_Hours: "))
            Social_Media_Hours= int(input("Social_Media_Hours: "))
            Attendance= int(input("Attendance: "))
            Exam_Pressure= int(input("Exam_Pressure: "))
            Family_Support= int(input("Family_Support: "))
            Month= int(input("Month: "))

            user_data = pd.DataFrame([{
                "Student_Type": Student_Type,
                "Sleep_Hours": Sleep_Hours,
                "Study_Hours": Study_Hours,
                "Social_Media_Hours": Social_Media_Hours,
                "Attendance": Attendance,
                "Exam_Pressure": Exam_Pressure,
                "Family_Support": Family_Support,
                "Month": Month
            }])

            try:
                print("result :", model.predict(user_data)[0])
            except:
                print("please write Valid Data !!")
        else:
            break

app()