import paho.mqtt.client as mqtt
import random
import time, json
import requests
from time import gmtime, strftime


def random_humidity(b):
    if (b == -1):
        b = random.randint(0,100)


    if ((b <= 97) & (b >= 3)):
        a = random.randint(b-3, b+3)
    elif b > 97:
        a = random.randint(b-3, 100)
    else:
        a = random.randint(0, b+3)

    return "humidity", a

client_id = ""
client = mqtt.Client(client_id=client_id)

user = ""
password = ""
client.username_pw_set(user, password)
client.connect("210.65.89.177")
hum = -1
topic, data = random_humidity(hum)
payload = json.dumps({"humidity": data})

while True:
    client.publish(topic, payload=payload, retain=True)
    topic, data = random_humidity(data)
    payload = json.dumps({"humidity": data})

    time.sleep(2)
