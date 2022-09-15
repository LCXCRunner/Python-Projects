from os import close
from tkinter import Button, Grid
from guizero import App, Text, PushButton, Box
from sense_hat import SenseHat
import time
import os
import sys

sense = SenseHat()

app = App(title="Home Nexus", height = 1000, width = 1000, layout="grid")

#box = Box(app, layout="grid", grid=[1,0])

top_message = Text(app,"Home Interface",color="blue", grid=[0,0])

temp_humidity = sense.get_temperature_from_humidity()
temp_pressure = sense.get_temperature_from_pressure()
humidity = sense.get_humidity()
pressure = sense.get_pressure()

rounded_temp_humidity = round(temp_humidity, 2)

#temp_humidity_title = "Temerature from Humidity"

text_0 = Text(app, "Temperature (deg C)", color="blue", grid=[1,0])
text_1 = Text(app,  rounded_temp_humidity, color="blue", grid=[2,0])
text_2 = Text(app, temp_humidity, grid=[3,0])

Button = PushButton(app, text="Close Window", command=sys.exit, grid=[2,2])


app.display()