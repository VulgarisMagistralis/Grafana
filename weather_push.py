#   Weather update server
#   Binds PUB socket to tcp://*:5556
#   Publishes random weather updates
import zmq
import time
from random import randrange
context = zmq.Context()
socket = context.socket(zmq.PUB)
print("Weather server binded.")
socket.bind("tcp://*:5556")
while True:
    zipcode = 10141
    temperature = randrange(-80, 135)
    relhumidity = randrange(10, 60)
    socket.send_string("%i %i %i" % (zipcode, temperature, relhumidity))
    time.sleep(1)
    print("Data generated %i %i %i..."%(zipcode, temperature, relhumidity))