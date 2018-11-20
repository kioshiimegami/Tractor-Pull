# MQTT Client demo from Core-Electrons
# Modified by Jennifer McNeil
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
 
import paho.mqtt.client as mqtt
import threading
import sys

ip = "172.22.20.174"

def on_connect(client, userdata, flags, rc):
     
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Compass")
    client.subscribe("Current")
    client.subscribe("Obsticle")
    client.subscribe("Trailer")
    client.subscribe("Speed")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print()
    print (msg.topic)
    print( msg.payload.decode() )
    
    if msg.topic == "Speed":
        #payload either 0, 1, or 2
        SPEED = msg.payload.decode()
        print(SPEED)
        
    if msg.topic == "Current":
        CURRENTVALUE = msg.payload.decode()
        print(CURRENTVALUE)
        
    if msg.topic == "Compass":
        DIRECTION = msg.payload.decode()
        print(DIRECTION)

    if msg.topic == "Obsticle":
        #payload either TRUE or FALSE
        OBSTICLE = msg.payload.decode()
        print(OBSTICLE)

    if msg.topic == "Trailer":
        #payload either TRUE or FALSE
        TRAILER = msg.payload.decode()
        print(TRAILER)

#def client_subscription():
    #lock.acquire()
    
 #   client = mqtt.Client()
  #  client.on_connect = on_connect
   # client.on_message = on_message
 
    #client.connect(ip, 1883, 60)
    #client.loop_forever()
    
    #lock.release()

#tclient_sub = threading.Thread(target=client_subscription)
#tclient_sub.start()

#client_subscription ()  


#Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(ip, 1883, 60)
 
# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions
client.loop_forever()
