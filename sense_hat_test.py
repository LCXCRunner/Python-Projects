from asyncio import get_event_loop
from sense_hat import SenseHat

sense = SenseHat()
#count=0
#while (count<1):

   #count =count +1
   # sense.show_message("Fire Up Chips!",text_colour=(106,0,50),back_colour=(255,200,46))

while True:
    for x in sense.stick.get_events():
        if x.direction == 'up':
            sense.show_message("Goodnight Ruby",text_colour=(255,0,00),back_colour=(255,255,255))
        elif x.direction == 'down':
            sense.show_letter("D")
        elif x.direction == 'left':
            sense.show_letter("L")
        elif x.direction == 'right':
            sense.show_letter("R")
        elif x.direction == 'middle':
            sense.show_letter("M")
