import serial 

def Get_data(ser):
    
    while(not ser.in_waiting):
        continue
    return ser.read(7)
    
