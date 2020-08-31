#!/usr/bin/python
import os
import sys
import zmq
import time
import json
import subprocess
from collections import OrderedDict
from influxdb import InfluxDBClient

# Variable names
measurement_name = "CAMessage"
# Connecting to InfluxDB creating DB, delete if DB exists already  otherwise causes problems
dbClient = InfluxDBClient('localhost' , 8086 , 'root' , 'root' , 'CAMessageLog8')
dbClient.drop_database('CAMessageLog8')
dbClient.create_database('CAMessageLog8')
context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://127.0.0.1:2002")
subscriber.setsockopt(zmq.SUBSCRIBE,'')

# Listening the Publisher
while True:
	pcap_data = subscriber.recv_json()
	print("Received JSON")
	speed = json.dumps(pcap_data['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.speed_element']['cam.speedValue'] , indent = 4).strip("\"")
	datum = [{"measurement": measurement_name, "fields":{"Speed" : float(speed)}}]
	# After each successful iteration, object is written into to the InfluxDB.CAMessageLog database
	dbClient.write_points(datum)
