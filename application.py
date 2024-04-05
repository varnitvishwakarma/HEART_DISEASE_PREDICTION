from flask import Flask,render_template,request,app
import pickle
from flask import Response


ran_model=pickle.load(open("C:\\Users\\tusha\\OneDrive\\Desktop\\heart\\HEART_DISEASE_PREDICTION\\Models\\random.pkl","rb"))




application = Flask(__name__)
app=application




@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/predict",methods=["GET","POST"])
def predict_data():
    if request.method=="POST":
        AGE=int(request.form.get("AGE"))
        SEX=(request.form.get("SEX"))
        if SEX=="Male":
            SEX=1
        else:
            SEX=0
       
        ChestPain=request.form.get("ChestPain")
        if ChestPain=="Typical Angina":
            ChestPain=0
        elif ChestPain=="Atypical Angina":
            ChestPain=1
        elif ChestPain=="Non-Anginal Pain":
            ChestPain=2
        else:
            ChestPain=3
       
        Trestbps=int(request.form.get("Trestbps"))
        Chol=int(request.form.get("Chol"))
        FastingBloodSugar=request.form.get("FastingBloodSugar")
        if FastingBloodSugar=="Yes":
            FastingBloodSugar=1
        else:
            FastingBloodSugar=0
        RestECG=request.form.get("RestECG")
        if RestECG=="Normal":
            RestECG=0
        elif RestECG=="ST-T Wave Abnormalities":
            RestECG=1
        else:
            RestECG=2
        Thalach=int(request.form.get("Thalach"))
        ExerciseInducedAngina=request.form.get("ExerciseInducedAngina")
        if ExerciseInducedAngina=="Yes":
            ExerciseInducedAngina=1
        else:
            ExerciseInducedAngina=0
        Oldpeak=int(request.form.get("Oldpeak"))
        Slope=request.form.get("Slope")
        if Slope=="Upsloping":
            Slope=0
        elif Slope=="Flat":
            Slope=1
        else:
            Slope=2
        NumberOfMajorVessels=request.form.get("NumberOfMajorVessels")
        if NumberOfMajorVessels=="0 Major Vessels":
            NumberOfMajorVessels=0
        elif NumberOfMajorVessels=="1 Major Vessel":
            NumberOfMajorVessels=1
        elif NumberOfMajorVessels=="2 Major Vessels":
            NumberOfMajorVessels=2
        elif NumberOfMajorVessels=="3 Major Vessels":
            NumberOfMajorVessels=3
        else:
            NumberOfMajorVessels=4
       
        Thalassemia=request.form.get("Thalassemia")
        if Thalassemia=="Normal":
            Thalassemia=1
        elif Thalassemia=="Fixed Defect":
            Thalassemia=2
        else:
            Thalassemia=3
       
       
        result=""
        new_data=[[AGE,SEX,ChestPain,Trestbps,Chol,FastingBloodSugar,RestECG,Thalach,ExerciseInducedAngina,Oldpeak,Slope,NumberOfMajorVessels,Thalassemia]]


        result=ran_model.predict(new_data)
        if result==0:
            result="According to the analysis, you do not have heart disease"
        else:
            result="According to the analysis, you have heart disease"






        return render_template("predict.html",result=result)
   


   
   
   
   
    else:
        return render_template("predict.html")


if __name__=="__main__":
    app.run(host="0.0.0.0")



