
from flask import Flask




app=Flask(__name__)

@app.route('/')

def home():
    return "this is flask application"

 




if __name__=="main":
    app.run(debug=True)
