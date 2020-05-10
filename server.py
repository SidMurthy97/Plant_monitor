from flask import Flask, jsonify,render_template,request
import webbrowser
import time
import random
import threading, queue
import serial 
import sys
from datetime import datetime

ser = serial.Serial("/dev/ttyACM0",9600)
app = Flask(__name__)
q = queue.Queue()

temperature = []
humidity = []
soil_moisture = []
time_ax = []

def data_collection():
    
    while(1):
        #set variables
        i = 0
        #read is blocking so waits till next packet of data is sent
        temperature_r = ser.read(5).decode('utf-8')
        humidity_r = ser.read(5).decode('utf-8')
        soil_m_r = ser.read(2).decode('utf-8')
        time_of_reading = datetime.now()
        #put data in queue
        q.put(temperature_r)
        q.put(humidity_r)
        q.put(soil_m_r)
        q.put(time_of_reading.strftime("%H:%M"))


@app.route("/update", methods = ['GET'])
def update_chart():
    
    while not q.empty():
        temperature.append(q.get())
        humidity.append(q.get())
        soil_moisture.append(q.get())
        time_ax.append(q.get())
    
    return jsonify(results = [temperature,humidity,soil_moisture,time_ax])

'''
@app.route("/start", methods = ['GET'])
def begin():
    q.put('get data')
    
    while not q2.get():
        continue
    temperature = q.get()
    humidity = q.get()
    soil_moisture = q.get()
    

    return jsonify(results = [temperature,humidity,soil_moisture])
    #return jsonify(results =[random.randint(1,10),random.randint(1,10), random.randint(1,10)])
'''
@app.route("/")
def index():
    
    return render_template('index.html')


if __name__ == '__main__':
    x = threading.Thread(target=data_collection)
    x.start()
    app.run(host = '0.0.0.0', port = 5000)