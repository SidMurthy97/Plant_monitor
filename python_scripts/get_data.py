import serial 

def get_data(ser):
    
    while(not ser.in_waiting):
        continue;
    
    
    bytes_waiting = ser.in_waiting
    return ser.read(7),bytes_waiting
    
if __name__ == '__main__': 
    print("test")
    ser = serial.Serial('COM18',9600)

    buffer_size = 1
    while(buffer_size > 0):
        temp,buffer_size = get_data(ser)
        print(temp,buffer_size)