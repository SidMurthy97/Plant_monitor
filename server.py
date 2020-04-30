from flask import Flask, jsonify,render_template,request
import webbrowser
import time
import random
from get_data import Get_data 
import serial 


app = Flask(__name__)


@app.route("/start", methods = ['GET'])
def begin():
    ser = serial.Serial("COM18",9600)
    
    temperature_reading,humidity_reading = Get_data(ser)

    #return jsonify(results =random.randint(1,10))
    return jsonify(results = [temperature_reading,humidity_reading])

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 80,debug = True)

    #test serial 
    # ser = serial.Serial("COM18",9600)
    # temp,hum = Get_data(ser)

    # print(temp,hum)