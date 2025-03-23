import dht
from machine import Pin
import utime


sensor = dht.DHT22(Pin(4))

while True:
        sensor.measure() 
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        print(f"Temperature: {temp}°C, Humidity: {hum}%")
    
        utime.sleep(2)
