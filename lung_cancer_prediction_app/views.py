from django.shortcuts import render
import joblib
def frontview(request):
    return render(request,"fors.html",{})
def backview(request):
    file = joblib.load(open("data.xlsx.svc","rb"))
    cls = file
    lis = []
    lis.append(request.GET["Age"])
    lis.append(request.GET["Gender"])
    lis.append(request.GET["Air Pollution"])
    lis.append(request.GET["Alcohol use"])
    lis.append(request.GET["Dust Allergy"])
    lis.append(request.GET["OccuPational Hazards"])
    lis.append(request.GET["Genetic Risk"])
    lis.append(request.GET["chronic Lung Disease"])
    lis.append(request.GET["Balanced Diet"])
    lis.append(request.GET["Obesity"])
    lis.append(request.GET["Smoking"])
    lis.append(request.GET["Passive Smoker"])
    lis.append(request.GET["Chest Pain"])
    lis.append(request.GET["Coughing of Blood"])
    lis.append(request.GET["Fatigue"])
    lis.append(request.GET["Weight Loss"])
    lis.append(request.GET["Shortness of Breath"])
    lis.append(request.GET["Wheezing"])
    lis.append(request.GET["Swallowing Difficulty"])
    lis.append(request.GET["Clubbing of Finger Nails"])
    lis.append(request.GET["Frequent Cold"])
    lis.append(request.GET["Dry Cough"])
    lis.append(request.GET["Snoring"])
    
    Result = cls.predict([lis])
    return render(request,"backes.html",{"Result":Result})

# Create your views here.
