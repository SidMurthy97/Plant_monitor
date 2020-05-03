from flask import Flask, jsonify,render_template,request
import webbrowser
import time
import random
import threading, queue
import serial 

ser = serial.Serial("COM3",9600)
app = Flask(__name__)
q = queue.Queue()



def data_collection():

    temp_readings =[]
    humidity_readings = []
    soil_moisture_readings = []
    try: 
        while(1):
            temp_readings.append(ser.read(5).decode('utf-8'))
            humidity_readings.append(ser.read(5).decode('utf-8'))
            soil_moisture_readings.append(ser.read(2).decode('utf-8'))
            print(temp_readings[-1])
            #if live stream required, send data 
            if not q.empty():
                print("checking queue")
                if q.get(block=False) == 'get data':
                    print("sending live data")
                    q.put(temp_readings[-1])
                    q.put(humidity_readings[-1])
                    q.put(soil_moisture_readings[-1])
                
    except KeyboardInterrupt:
        print("interrupted")


@app.route("/update", methods = ['GET'])
def update_chart():
    return jsonify(results = [test_data,test_data,test_data])


@app.route("/start", methods = ['GET'])
def begin():
    print("seinding request for data")
    q.put('get data')

    temperature = q.get()
    humidity = q.get()
    soil_moisture = q.get()
   
    return jsonify(results =[random.randint(1,10),random.randint(1,10), random.randint(1,10)])
   
   
   
    # temperature = ser.read(5).decode('utf-8')
    # humidity = ser.read(5).decode('utf-8')
    # soil_moisture = ser.read(2).decode('utf-8')

    #return jsonify(results = [temperature,humidity,soil_moisture])

@app.route("/")
def index():
    
    return render_template('index.html')


if __name__ == '__main__':
    x = threading.Thread(target=data_collection)
    x.start()
    app.run()