from machine import Pin
import utime
from time import sleep

trigger = Pin(2, Pin.OUT)  
echo = Pin(3, Pin.IN)     

while True:
    trigger.low() 
    utime.sleep_us(2)  # ২ মাইক্রোসেকেন্ড অপেক্ষা
    trigger.high() 
    utime.sleep_us(5)  # ৫ মাইক্রোসেকেন্ড অপেক্ষা
    trigger.low() 

    while echo.value() == 0:  
        signaloff = utime.ticks_us()  # ট্রিগার পাঠানোর সময় সংরক্ষণ করা হলো

    while echo.value() == 1:  
        signalon = utime.ticks_us()  # প্রতিধ্বনি ফেরত আসার সময় সংরক্ষণ করা হলো

    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2  

    print("Distance:", distance, "cm")
    utime.sleep(1)  # ১ সেকেন্ড অপেক্ষা করে আবার পরিমাপ করা হবে
