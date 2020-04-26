from flask import Flask, jsonify,render_template,request
import webbrowser
import time
import random
from data_acquisition import Get_data 
import serial 


app = Flask(__name__)


@app.route("/start", methods = ['GET'])
def begin():
    ser = serial.Serial("com18",9600)
    Get_data(ser)



@app.route("/")
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 80,debug = True)