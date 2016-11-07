import paho.mqtt.client as mqtt
import random
import time, json
import requests
from time import gmtime, strftime

def random_temp():
    a = random.randint(21,27)
    payload = json.dumps({"temperature": a})
    return "temperature/"+strftime("%Y-%m-%d_%H:%M:%S", gmtime()), payload

client_id = ""
client = mqtt.Client(client_id=client_id)

user = ""
password = ""
client.username_pw_set(user, password)
client.connect("210.65.89.177")
hum = -1

while True:
    topic, data = random_temp()

    client.publish("temperature", payload=data, retain=True)
#    client.publish(topic, payload=data, retain=True)
    time.sleep(5)
