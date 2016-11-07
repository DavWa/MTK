import serial
import time
import sys, os
import paho.mqtt.client as mqtt
import json
client_id = ""

client = mqtt.Client(client_id=client_id)

user = ""
password = ""
client.username_pw_set(user, password)

client.connect("210.65.89.177")
topic = "mqtt-message"
s = None
def setup():
    global s

    s = serial.Serial("/dev/ttyS0", 57600)
def loop():
    s.write("1")
    msg = json.dumps({'Light': 'on'})
    client.publish(topic, payload = msg, retain = True)
    time.sleep(1)

    s.write("0")
    msg = json.dumps({'Light': 'off'})
    client.publish(topic, payload = msg, retain = True)
    time.sleep(5)

if __name__ == '__main__':
    setup()

while True:
    loop()
