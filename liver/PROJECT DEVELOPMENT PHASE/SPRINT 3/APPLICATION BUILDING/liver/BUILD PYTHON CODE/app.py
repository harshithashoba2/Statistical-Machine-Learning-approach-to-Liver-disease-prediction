import os
import numpy as np #used for numerical analysis
from flask import Flask,request,render_template # Flask-It is our framework which we are going to use to run/serve our application.
#request-for accessing file which was uploaded by the user on our application.
#render_template- used for rendering the html pages
from tensorflow.keras.models import load_model #to load our trained model
from tensorflow.keras.preprocessing import image
from werkzeug.datastructures import ImmutableMultiDict
import pickle
from sklearn.preprocessing import RobustScaler

app=Flask(__name__)#our flask app
model=pickle.load(open("./model/model.pkl","rb"))#loading the model
@app.route("/") #default route
def about():
    return render_template("about.html")#rendering html page

@app.route("/about") #route about page
def home():
    return render_template("about.html")#rendering html page

@app.route("/info") # route for info page
def information():
    return render_template("info.html")#rendering html page

@app.route("/classify") # route for uploads
def test():
    return render_template("index6.html")#rendering html page

@app.route("/predict",methods=["GET","POST"]) #route for our prediction
def upload():
    if request.method=='POST':
        print(request.form)
        # imd = ImmutableMultiDict(request.form)
        res = request.form.to_dict(flat=False)
        print(res)
        Age = int(res['Age'][0])
        Gender = res['gender'][0]
        if(Gender == 'male'):
            Gender = 0
        else:
            Gender = 1
        Total_Bilirubin = int(res['Total_Bilirubin'][0])
        Direct_Bilirubin = int(res['Direct_Bilirubin'][0])
        Alkaline_Phosphotase = int(res['Alkaline_Phosphotase'][0])
        Alamine_Aminotransferase = int(res['Alamine_Aminotransferase'][0])
        Aspartate_Aminotransferase = int(res['Aspartate_Aminotransferase'][0])
        Total_Protiens = float(res['Total_Protiens'][0])
        Albumin = float(res['Albumin'][0])
        Albumin_and_Globulin_Ratio = float(res['Albumin_and_Globulin_Ratio'][0])
        arr = [Age,Gender,Total_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Albumin_and_Globulin_Ratio]
        print(arr)
        pred = model.predict([arr])
        pred = pred[0]
        print("prediction",pred)#printing the prediction
        if(pred==0):#checking the results
            result="UnInfected"
        else:
            result="Infected"
        return result#resturing the result
    return None

#port = int(os.getenv("PORT"))
if __name__=="__main__":
    app.run(debug=False)#running our app
    #app.run(host='0.0.0.0', port=8000,debug=False)
            
            