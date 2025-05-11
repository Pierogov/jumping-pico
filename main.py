from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd

#Adress Pinout according to GPIO notation
SDA_PIN = 0
SCL_PIN = 1
SWITCH_PIN = 28

def init_pico():
    #init lcd
    i2c = I2C(0, sda=Pin(SDA_PIN), scl=Pin(SCL_PIN), freq=400000)
    i2c_adress = i2c.scan()[0]
    lcd=I2cLcd(i2c, i2c_adress, 2, 16)

    #init button
    button = Pin(28, Pin.IN, Pin.PULL_DOWN)

def start():
    #prepare lcd for work
    lcd.clear()
    lcd.putstr("Jumping Pico\nby Pierogov")

init_pico()
start()

#lcd.putstr("Przed")
#while True:
#    if(button.value()==1):
#        lcd.clear()
#        lcd.putstr("Po")
#        sleep(1)
#        lcd.clear()
#        lcd.putstr("Przed")


