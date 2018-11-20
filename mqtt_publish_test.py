# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

ip = "172.22.20.174"

publish.single("Compass","N", hostname=ip)
publish.single("Current","10.01", hostname=ip)
publish.single("Obsticle","True", hostname=ip)
publish.single("Trailer","True", hostname=ip)
publish.single("Speed","1", hostname=ip)

publish.single("Start","True", hostname=ip)
              
print("Done")
