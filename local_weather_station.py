from guizero import App, Text
from sense_hat import SenseHat

sense = SenseHat()

app = App(title="Home Nexus")

top_message = Text(app,"Home Interface",color="blue")

temp_humidity = sense.get_temperature_from_humidity()
temp_pressure = sense.get_temperature_from_pressure()
humidity = sense.get_humidity()
pressure = sense.get_pressure()

rounded_temp_humidity = round(temp_humidity, 2)

#temp_humidity_title = "Temerature from Humidity"

text_0 = Text(app, "Temperature (deg C)", color="blue",align="left")
text_1 = Text(app,  rounded_temp_humidity, color="blue",align="left") 
text_2 = Text(app, temp_humidity)



app.display()