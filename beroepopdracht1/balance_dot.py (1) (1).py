# Add your Python code here. E.g.
from microbit import *



display.scroll('Press A')
while True:
    if button_a.is_pressed():
        x=2
        y=2
        display.set_pixel(x, y, 9)
        sleep(1000)
        while True:
            if x == 4 or x == 0 or y == 4 or y == 0:
                display.scroll('Game Over')
                display.scroll('press A to restart')
                break
            else: 
                reading_x = accelerometer.get_x()
                reading_y = accelerometer.get_y()
                print(reading_x, reading_y)
                if reading_x >= 200:
                    x += 1
                if reading_x <= -200:
                    x += -1
                if reading_y >= 200:
                    y += 1
                if reading_y <= -200:
                    y += -1
                display.clear()
                display.set_pixel(x, y, 9)
                sleep(500)
        
        

    


    
    
    
   
