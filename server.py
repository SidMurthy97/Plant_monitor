from flask import Flask, jsonify,render_template,request
import webbrowser
import time
import random
import threading 
import serial 


app = Flask(__name__)
#ser = serial.Serial("COM3",9600)



#def data_collection():




@app.route("/update", methods = ['GET'])
def update_chart():
    test_data = [1,2,3,4,5]
    return jsonify(results = [test_data,test_data,test_data])
    #get all data from thread 
    #send to client 


@app.route("/start", methods = ['GET'])
def begin():

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