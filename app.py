

# Import our modules
import pymongo
import pandas as pd
from flask import Flask, render_template, jsonify

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'
# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. 
db = client.deathDB
# Available routes
@app.route("/")
def home():
    return (
        f"Welcome to the Heart and Stroke DataBase!<br/>"
        f"<br/>"
        f"Below route returns all heart records from database<br/>"
        f"/api/v1.0/Heart_Failure_Records<br/>"
        f"<br/>"
        f"Below route returns all stroke records from database<br/>"
        f"/api/v1.0/Stroke_Records<br/>"
        f"<br/>"
        f"Below route returns heart failure death by mean age. Death = 1, Non-Death = 0<br/>"
        f"/api/v1.0/Heart_Failure_by_Age<br/>"
        f"<br/>"
        f"Below route returns strokes by mean age. Stroke = 1, no stroke = 0<br/>"
        f"/api/v1.0/Stroke_by_Age<br/>"
        f"<br/>"
        f"Below route returns heart failure data by smoking or not. Input 1 for Smoker, 0 for Non-Smoker<br/>"
        f"/api/v1.0/Heart_Failure_by_Smoking/<smoking><br/>"
        f"<br/>"
        f"Below route returns stroke data by gender. Input Male or Female<br/>"
        f"/api/v1.0/Stroke_by_Gender/<gender>"
        
    )

@app.route("/api/v1.0/Heart_Failure_Records")
def heart():
    # Store collection in a list
    Heart_Failure_Records = db.Heart_Failure_Records.find()   
    # Create empty list and fill with collection records
    data=[]
    for item in Heart_Failure_Records:
        heart_dict={}
        heart_dict['age']=item['age']
        heart_dict['anaemia']=item['anaemia']
        heart_dict['diabetes']=item['diabetes']
        heart_dict['ejection_fraction']=item['ejection_fraction']
        heart_dict['high_blood_pressure']=item['high_blood_pressure']
        heart_dict['platelets']=item['platelets']
        heart_dict['serum_creatinine']=item['serum_creatinine']
        heart_dict['serum_sodium']=item['serum_sodium']
        heart_dict['sex']=item['sex']
        heart_dict['smoking']=item['smoking']
        heart_dict['time']=item['time']
        heart_dict['Death Event']=item['DEATH_EVENT']
        data.append(heart_dict)

    return jsonify(data)

@app.route("/api/v1.0/Stroke_Records")
def stroke():
    # Store collection in a list
    Stroke_Records = db.Stroke_Records.find()   
     # Create empty list and fill with collection records
    data=[]
    for item in Stroke_Records:
        stroke_dict={}
        stroke_dict['gender']=item['gender']
        stroke_dict['age']=item['age']
        stroke_dict['hypertension']=item['hypertension']
        stroke_dict['heart_disease']=item['heart_disease']
        stroke_dict['ever_married']=item['ever_married']
        stroke_dict['work_type']=item['work_type']
        stroke_dict['Residence_type']=item['Residence_type']
        stroke_dict['avg_glucose_level']=item['avg_glucose_level']
        stroke_dict['bmi']=item['bmi']
        stroke_dict['smoking_status']=item['smoking_status']
        stroke_dict['stroke']=item['stroke']
        data.append(stroke_dict)

    return jsonify(data)
@app.route("/api/v1.0/Heart_Failure_by_Age")
def heart_age():
    # Store collection in a list
    Heart_Failure_Records = db.Heart_Failure_Records.find()   
    # Create empty list and fill with collection records


    data=[]
    for item in Heart_Failure_Records:
        heart_dict={}
        heart_dict['age']=item['age']
        heart_dict['Death Event']=item['DEATH_EVENT']
        data.append(heart_dict)

    data_df = pd.DataFrame(data)
    death= data_df.groupby('Death Event').mean()
    age_death_dict = death.to_dict()

    return jsonify(f'Average age from data set. Death = 1, Non-Death = 0{age_death_dict}')


@app.route("/api/v1.0/Stroke_by_Age")
def stroke_age():
    # Store collection in a list
    Stroke_Records = db.Stroke_Records.find()   
    # Create empty list and fill with collection records


    data=[]
    for item in Stroke_Records:
        stroke_dict={}
        stroke_dict['age']=item['age']
        stroke_dict['Stroke']=item['stroke']
        data.append(stroke_dict)

    data_df = pd.DataFrame(data)
    stroke= data_df.groupby('Stroke').mean()
    stroke_dict = stroke.to_dict()

    return jsonify(f'Average age from data set. Stroke = 1, Non-Stroke = 0{stroke_dict}')

@app.route("/api/v1.0/Stroke_by_Gender/<gender>")
def stroke_gender(gender):
    # Store collection in a list
    stroke_records = db.Stroke_Records.find()  
    
    # Create empty list and fill with collection records
    
    data=[]
    for item in stroke_records:
        stroke_dict={}
        stroke_dict['gender']=item['gender']
        stroke_dict['age']=item['age']
        stroke_dict['hypertension']=item['hypertension']
        stroke_dict['heart_disease']=item['heart_disease']
        stroke_dict['ever_married']=item['ever_married']
        stroke_dict['work_type']=item['work_type']
        stroke_dict['Residence_type']=item['Residence_type']
        stroke_dict['avg_glucose_level']=item['avg_glucose_level']
        stroke_dict['bmi']=item['bmi']
        stroke_dict['smoking_status']=item['smoking_status']
        stroke_dict['stroke']=item['stroke']
        data.append(stroke_dict)

    data_df = pd.DataFrame(data)
    gender_filter = data_df.loc[:,'gender']==gender
    gender_df = data_df.loc[gender_filter,:]
    return jsonify(gender_df.to_dict())

@app.route("/api/v1.0/Heart_Failure_by_Smoking/<smoking>")
def heart_sex(smoking):
    # Store collection in a list
    Heart_Failure_Records = db.Heart_Failure_Records.find()   
    # Create empty list and fill with collection records
    data=[]
    for item in Heart_Failure_Records:
        heart_dict={}
        heart_dict['age']=item['age']
        heart_dict['anaemia']=item['anaemia']
        heart_dict['diabetes']=item['diabetes']
        heart_dict['ejection_fraction']=item['ejection_fraction']
        heart_dict['high_blood_pressure']=item['high_blood_pressure']
        heart_dict['platelets']=item['platelets']
        heart_dict['serum_creatinine']=item['serum_creatinine']
        heart_dict['serum_sodium']=item['serum_sodium']
        heart_dict['sex']=item['sex']
        heart_dict['smoking']=item['smoking']
        heart_dict['time']=item['time']
        heart_dict['Death Event']=item['DEATH_EVENT']
        data.append(heart_dict)

    data_df = pd.DataFrame(data)
    smoking_filter = data_df.loc[:,'smoking']==int(smoking)
    smoking_df = data_df.loc[smoking_filter,:]
    return jsonify(smoking_df.to_dict())

if __name__ == "__main__":
    app.run(debug=True)
