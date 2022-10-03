
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

    funding_rounds=int(request.form["funding_rounds"])
    funding_total_usd=int(request.form['TOTAL_FUNDING_USD'])
    milestones=int(request.form['MILESTONES'])
    relationships=int(request.form['relationships'])
    lat=float(request.form['latitude'])
    lng=float(request.form['longitude'])
    active_days=int(request.form['active_days'])
    
    data=['funding_rounds','funding_total_usd','milestones','relationships','lat','lng','active_days']

    
    features_value=[np.array(data)]

    feature_name=['funding_rounds','funding_total_usd','milestones','relationships','lat','lng','active_days']

    df=pd.DataFrame(features_value,columns=feature_name)
    mypred=model.predict(df)
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
