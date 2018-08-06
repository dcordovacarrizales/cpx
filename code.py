from adafruit_circuitplayground.express import cpx 
import time


redval = 255
pink = (150, 40, 50)
white = (50, 50, 50)
turquoise = (64, 225, 208)
purple = (150, 0, 150) 
red = (255, 0, 0)




def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0) or (pos > 255):
        return (0, 0, 0)
    if pos < 85:
        return (int(255 - pos*3), int(pos*3), 0)
    elif pos < 170:
        pos -= 85
        return (0, int(255 - (pos*3)), int(pos*3))
    else:
        pos -= 170
    return (int(pos*3), 0, int(255 - pos*3))
    
pixeln = 0 

while True: 
    for p in range(10):
        color = wheel(25 * ((pixeln + p)%10))
        cpx.pixels[p] = [int(c * ( (10 - (pixeln+p)%10)) / 10.0) for c in color]
 
#wheel(255)



#cpx.play_file("techloop.wav")

"""while True: 
    cpx.pixels.fill((0,0,0))
    time.sleep(10)
    wheel(255)
    time.sleep(10)
    """







"""
while True: 
    if cpx.switch: 
        value = cpx.light 
        print("Light Sensor:", value)
        cpx.pixels.fill((10, 10, 10))
        time.sleep(3)
        break

while True: 
    newvalue = cpx.light

    if newvalue < (value-10): 
        print("Light Sensor:", newvalue)
        cpx.pixels.fill((100, 40, 50))
        time.sleep(1)
    if newvalue > (value+ 10): 
        print("Light Sensor:", newvalue)
        cpx.pixels.fill((turquoise))
        time.sleep(1)
    
    
    """
    
"""
while True: 
    cpx.pixels.fill(white)
    time.sleep(1)
    cpx.pixels.fill(pink)
    time.sleep(1)
    cpx.pixels.fill(turquoise)
    time.sleep(1)
    cpx.pixels.fill(purple)
    time.sleep(2)
   # cpx.play_tone(2000, 1)"""
   
#while True: 
   # cpx.pixels.fill(reddish)





"""
while True:
    cpx.pixels.fill((redval, 0, 0))
    redval -= 5
    if redval < 0: 
        redval = 255
"""

    
"""while True: 
    print(cpx.switch)
    time.sleep(1)"""


"""while True: 
    if cpx.switch:
        cpx.pixels.fill(purple)
    else: 
        cpx.pixels.fill((0, 0, 0))"""
        
"""while True: 
    if cpx.switch: 
        cpx.pixels[1] = purple"""
        


"""while True: 
    for i in range(11): 
        cpx.pixels[i] = red
        time.sleep(1)"""
    