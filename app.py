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

    funding_rounds=float(request.form["funding_rounds"])
    funding_total_usd=float(request.form['funding_total_usd'])
    milestones=float(request.form['milestones'])
    relationships=float(request.form['relationships'])
    lat=float(request.form['lat'])
    lng=float(request.form['lng'])
    active_days=float(request.form['active_days'])
    
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
