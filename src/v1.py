import serial
import serial.tools.list_ports as port_list
import time

p = list(port_list.comports())
for i in p:
    d = i.description
    if "Arduino" in d:
        print(d)

ser = serial.Serial('COM12', 9600)
time.sleep(2)  # Arduino resets on connect

ser.write(b'A')  # turn LED on
print(ser.readline().decode())

time.sleep(2)  # Arduino resets on connect

ser.write(b'B')  # turn LED off
print(ser.readline().decode())

time.sleep(2)  # Arduino resets on connect

ser.write(b'A')  # turn LED on
print(ser.readline().decode())

time.sleep(2)  # Arduino resets on connect

ser.write(b'B')  # turn LED off
print(ser.readline().decode())




ser.close()