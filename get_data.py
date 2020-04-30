import serial 

def Get_data(ser):
    
    temp = ser.read(5).decode('utf-8')
    humidity = ser.read(5).decode('utf-8')
    
    return temp,humidity