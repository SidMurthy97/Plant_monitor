from flask import Flask, jsonify,render_template,request
import webbrowser
import time
import random
import threading, queue
import serial 
import sys

ser = serial.Serial("COM3",9600)
app = Flask(__name__)
q = queue.Queue()
q2 = queue.Queue()
lock = threading.Lock()


def data_collection():

    temp_readings =[]
    humidity_readings = []
    soil_moisture_readings = []
    time_ax = []
    i = 0
    try: 
        while(1):
            time_ax.append(str(i))
            temp_readings.append(ser.read(5).decode('utf-8'))
            humidity_readings.append(ser.read(5).decode('utf-8'))
            soil_moisture_readings.append(ser.read(2).decode('utf-8'))
            i = i + 1
            print(temp_readings[-1])
            #if live stream required, send data 
            if not q.empty():
                command = q.get()
                if command == 'get data':
                    print("sending live data")
                    
                    q.put(temp_readings[-1])
                    q.put(humidity_readings[-1])
                    q.put(soil_moisture_readings[-1])
                    q2.put(1)
                
                elif command == 'get all data':

                    q.put(temp_readings)
                    q.put(humidity_readings)
                    q.put(soil_moisture_readings)
                    q.put(time_ax)
                    q2.put(1)
                    
                
    except KeyboardInterrupt:
        sys.exit()
        
        print("interrupted")


@app.route("/update", methods = ['GET'])
def update_chart():
    q.put('get all data')

    while not q2.get():
        continue
    
    temperature = q.get()
    humidity = q.get()
    soil_moisture = q.get()
    time_ax = q.get()

    return jsonify(results = [temperature,humidity,soil_moisture,time_ax])


@app.route("/start", methods = ['GET'])
def begin():
    print("seinding request for data")
    q.put('get data')
    
    while not q2.get():
        continue
    temperature = q.get()
    humidity = q.get()
    soil_moisture = q.get()
    

    return jsonify(results = [temperature,humidity,soil_moisture])
    #return jsonify(results =[random.randint(1,10),random.randint(1,10), random.randint(1,10)])

@app.route("/")
def index():
    
    return render_template('index.html')


if __name__ == '__main__':
    x = threading.Thread(target=data_collection)
    x.start()
    app.run()