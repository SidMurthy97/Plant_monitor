from flask import Flask, jsonify,render_template,request
import webbrowser
import time
import random
from get_data import Get_data 
import serial 


app = Flask(__name__)

@app.route("/update", methods = 'GET'])
def update_chart():
    #get all data from thread 
    #send to client 


@app.route("/start", methods = ['GET'])
def begin():
    # ser = serial.Serial("COM3",9600)
    # temperature = ser.read(5).decode('utf-8')
    # humidity = ser.read(5).decode('utf-8')
    # soil_moisture = ser.read(2).decode('utf-8')
    
    return jsonify(results =[random.randint(1,10),random.randint(1,10), random.randint(1,10)])
    #return jsonify(results = [temperature,humidity,soil_moisture])

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 80,debug = True)