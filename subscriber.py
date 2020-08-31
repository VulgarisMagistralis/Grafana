import zmq
import os
import time
import sys
import subprocess
"""
	Receives JSON file from Publisher, task;
	filter the data and load to InfluxDB
"""
while True:
	context = zmq.Context()
	subscriber = context.socket(zmq.SUB)
	subscriber.connect("tcp://127.0.0.1:2002")
	subscriber.setsockopt(zmq.SUBSCRIBE,'')
	msg = subscriber.recv(313344) # is this enough?
	if msg:
		print('open\n')
		#subprocess.Popen("filter4sub.py json")
		print(msg)
		print('close\n')
	time.sleep(5)
