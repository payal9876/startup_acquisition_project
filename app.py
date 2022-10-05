from flask import Flask,request,render_template
import pickle
import numpy as np
import pandas as pd


model=pickle.load(open('model2.pkl','rb'))
app=Flask(__name__)

@app.route('/')

def home():
    return render_template("index.html")


@app.route('/',methods=['POST'])

def predict():

    funding_rounds=request.form["funding_rounds"]
    funding_total_usd=request.form['funding_total_usd']
    milestones=request.form['milestones']
    relationships=request.form['relationships']
    lat=request.form['lat']
    lng=request.form['lng']
    active_days=request.form['active_days']
    
    data=[['funding_rounds','funding_total_usd','milestones','relationships','lat','lng','active_days']]

   
    mypred=model.predict(data)
    output=mypred[0]

    if output==1:
       output='acquired'
    elif output==2:
         output='operating'
    elif output==3:
         output='closed'
    else:
        output='ipo'
    
    return render_template('result.html',prediction=output)





if __name__=="main":
    app.run()
