
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

    FUNDING_ROUNDS=int(request.form["funding_rounds"])
    TOTAL_FUNDING_USD=int(request.form['TOTAL_FUNDING_USD'])
    MILESTONES=int(request.form['MILESTONES'])
    RELATIONSHIPS=int(request.form['relationships'])
    latitude=float(request.form['latitude'])
    longitude=float(request.form['longitude'])
    active_days=int(request.form['active_days'])
    

    data=['FUNDING_ROUNDS','TOTAL_FUNDING_USD','MILESTONES','RELATIONSHIPS','langitude','longitude','active_days']    
    features_value=[np.array(data)]

    feature_name=['funding_rounds','funding_total_usd','milestones','relationships','lat','lng','active_days']

    df=pd.DataFrame(features_value,columns=feature_name)
    mypred=model.predict(df)

    if mypred==1:
       mypred='acquired'
    elif mypred==2:
         mypred='operating'
    elif mypred==3:
         mypred='closed'
    else:
         mypred='ipo'
    
    return render_template('result.html',prediction=mypred) 




if __name__=="main":
    app.run(debug=True)
