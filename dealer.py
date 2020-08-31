import zmq
import time
import os
import sys
import json
from random import randrange
"""
	Sends JSON data every second 
	to Subscriber @ port 2002
"""
speed = 0; lat = 45.065834 ;lng =  7.658805
context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://127.0.0.1:85")
while True:
	print('Generating JSON\n')
	x = randrange(-2, 2)
	y = randrange(0,9)*0.0001 
	z = randrange(0,9)*0.0001
	speed+=x ; lat+=y ; lng+=z
	#create sample JSON
	data = {'_source':{'layers':{'etsi_its_geonetworking':{'cam':{'cam.CAM_element':{'cam.cam_element':{'cam.camParameters_element':{'cam.highFrequencyContainer_tree':{'cam.basicVehicleContainerHighFrequency_element':{'cam.speed_element':{'cam.time':time.time(),'cam.speedValue': speed,'cam.Lat':lat,'cam.Lng':lng}}}}}}}}}}}    
	# Prepare context & publisher
	topic="CAM"
	cam_data=" "+str(speed)+" "+str(lat)+" "+str(lng)
	publisher.send("sadsad")
	time.sleep(0.5)
publisher.close()
context.term()
target.close()