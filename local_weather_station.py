from multiprocessing.connection import wait
from os import close
from tkinter import Button, Grid
from guizero import App, Text, PushButton, Box
from sense_hat import SenseHat
import time
import os
import sys

sense = SenseHat()

temp_humidity = sense.get_temperature_from_humidity()
temp_pressure = sense.get_temperature_from_pressure()
humidity = sense.get_humidity()
pressure = sense.get_pressure()

#def update()

rounded_temp_humidity = round(temp_humidity, 2)
rounded_humidity = round(humidity, 2)

app = App(title="Home Nexus", height = 100, width = 500)

top_message = Text(app,"Home Interface",color="blue", align="top")

box_1 = Box(app, layout="grid", align="top")
text_0 = Text(box_1, "Temperature (deg C):", color="blue", grid=[0,0])
text_1 = Text(box_1, rounded_temp_humidity, color="blue", grid=[1,0])
text_2 = Text(box_1, "Relative Humidity (%)", color="green", grid=[0,1])
text_3 = Text(box_1, rounded_humidity, color="green", grid=[1,1])

box_2 = Box(app, align="right")
Button = PushButton(box_2, text="Close Window", command=sys.exit)



app.display()