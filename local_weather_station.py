from guizero import App, Text
from sense_hat import SenseHat

sense = SenseHat()

app = App(title="Home Nexus")

top_message = Text(app,"Home Interface",color="blue")

temp_humidity = sense.get_temperature_from_humidity()
temp_pressure = sense.get_temperature_from_pressure()
humidity = sense.get_humidity()
pressure = sense.get_pressure()






app.display()