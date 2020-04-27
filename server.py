from flask import Flask, jsonify,render_template,request
import webbrowser
import time
import random
from get_data import Get_data 
import serial 


app = Flask(__name__)


@app.route("/start", methods = ['GET'])
def begin():
    ser = serial.Serial("COM3",9600)
    temperature_reading = Get_data(ser).decode('utf-8')


    # return jsonify(results =random.randint(1,10))
    return jsonify(results =temperature_reading)



@app.route("/")
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 80,debug = True)