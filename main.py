from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd
import random

#Adress Pinout according to GPIO notation
SDA_PIN = 0
SCL_PIN = 1
SWITCH_PIN = 28

#variables
FULL_CHAR = "X"
BLANK_CHAR = " "
PLAYER_CHAR = "o"
top = [BLANK_CHAR] * 16
bottom = [BLANK_CHAR] * 16
isGameOver = 0
jumpIndex = 0
toNextSpawn = 0

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
    sleep(2)

def frame(array):
    lcd.clear()
    
    
start()

#while True:


#lcd.putstr("Przed")
#while True:
#    if(button.value()==1):
#        lcd.clear()
#        lcd.putstr("Po")
#        sleep(1)
#        lcd.clear()
#        lcd.putstr("Przed")

#for i in range(0, 16):
#    for k in range(0, 2):
#        array [k][i] = BLANK_CHAR
        #print(str(i) + ", " + str(k))
def toLCDString():
    x = ""
    for i in range(0, 16):
        x += top[i]
    x+="\n"
    for i in range(0, 16):
        x += bottom[i]
    return x

def fill(x, y, character):
    if(y == 0):
        bottom[x] = character
    else:
        top[x] = character

def nextFrame():
    global isGameOver
    global toNextSpawn
    del top[0]
    del bottom[0]
    top.append(BLANK_CHAR)
    bottom.append(BLANK_CHAR)
    if(jumpIndex>0):
        fill(0, 1, BLANK_CHAR)
        if(top[1]==FULL_CHAR):
            isGameOver = 1
        else:
            fill(1, 1, PLAYER_CHAR)
    else:
        fill(0, 0, BLANK_CHAR )
        if(bottom[1]==FULL_CHAR):
            isGameOver = 1
        else:
            fill(1, 0, PLAYER_CHAR)
    if(toNextSpawn<=0):
        spawn()
    lcd.clear()
    lcd.putstr(toLCDString())

def jump():
    jumpIndex = 3

def spawn():
    global toNextSpawn
    fill(15, 0, FULL_CHAR)
    toNextSpawn = random.randint(3, 5)

while True:
    while (isGameOver==0):
        lcd.clear()
        nextFrame()
        if(isGameOver==1):
            lcd.clear()
            lcd.putstr("Game over!")
            sleep(2)
            lcd.clear()
            lcd.putstr("Press to start!")
            break
        if (jumpIndex>0): 
            jumpIndex -= 1
        toNextSpawn-=1
        #print(toNextSpawn)
        if(button.value()==1):
            jump()
        sleep(1)
    while (True):
        #change to Button
        if():
            top = [BLANK_CHAR] * 16
            bottom = [BLANK_CHAR] * 16
            isGameOver=0
            jumpIndex=0
            toNextSpawn=0
            break





