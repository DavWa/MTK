import paho.mqtt.client as mqtt
import random
import time, json
import requests
from time import gmtime, strftime


def random_pressure(b):
    if (b == -1):
        b = 995

    a = random.randint(b-2, b+2)
    return "pressure", a

client_id = ""
client = mqtt.Client(client_id=client_id)

user = ""
password = ""
client.username_pw_set(user, password)
client.connect("210.65.89.177")
pre = -1
topic, data = random_pressure(pre)
payload = json.dumps({"pressure": data})
while True:
    client.publish(topic, payload=payload, retain=True)
    topic, data = random_pressure(data)
    payload = json.dumps({"pressure": data})
    time.sleep(5)
