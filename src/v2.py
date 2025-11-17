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

while 1:
    LED = input("ON eller OFF för att ändra tillstånd på Lampan")
    if LED == "ON":
        ser.write(b'A')
        print(ser.readline().decode())
    elif LED == "OFF":
        ser.write(b'B')
        print(ser.readline().decode())
    elif LED == "EXIT":
        ser.close()
        break