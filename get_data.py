import serial 

def split_data(ser):
    
    while(not ser.in_waiting):
        continue
    
    
    bytes_waiting = ser.in_waiting
    return ser.read(7),bytes_waiting
    
def Get_data(ser): 
    print("test")
    ser = serial.Serial('COM18',9600)

    buffer_size = 1
    while(buffer_size > 0):
        temp,buffer_size = split_data(ser)
        print(temp,buffer_size)