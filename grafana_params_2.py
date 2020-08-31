#!/usr/bin/python
import os
import sys
import zmq
import time
import json
import socket
import commands
import requests
import subprocess
import default_panel
from collections import OrderedDict
from influxdb import InfluxDBClient

def query_interpreter(table, field):
	print"Building Query on ",field
	query = "SELECT "+field+" FROM "+table
	return query;

if(len(sys.argv) < 5):
	print"Usage:\n",sys.argv[0],"<Datasource> <Graph Type> <Field> <Min Range> <Max Range> <Table Name> <Port to Cconnect>"
	sys.exit(1)
#python grafana_params_2.py ZMQ_1 graph Speed -200 200 CAMessage tcp://127.0.0.1:85

# variables
database_name='CAMessageLog9'
port_to_listen = sys.argv[7] #"tcp://127.0.0.1:85" #var
headers = { #Company credentials?
	'Authorization': 'Bearer eyJrIjoiVVN2d1V6NUtPVGlNQ1lnN3VLRHp5cmlnc0QyVDZrNEYiLCJuIjoicmVtb3RlX3Rlc3QiLCJpZCI6MX0=',
	'Content-Type': 'application/json',
}
#seperate with exec or fork
datasource = '\n{\n  "name":"'+sys.argv[1]+'",\n  "type":"influxdb",\n  "database":"'+database_name+'",\n  "url":"http://localhost:8086",\n  "access":"browser",\n  "user":"root",\n  "password":"root",\n  "basicAuth":true\n}'
# Create Datasource - !!!!!!!!!!1
response = requests.post('https://vulgaris.grafana.net/api/datasources', headers=headers, data=datasource)
# Connecting to InfluxDB creating DB, delete if DB exists already
dbClient = InfluxDBClient('localhost' , 8086 , 'root' , 'root' , database_name)
dbClient.drop_database(database_name)
dbClient.create_database(database_name)
# start listening station
context_json_py = zmq.Context()
subscriber = context_json_py.socket(zmq.SUB)
subscriber.connect(port_to_listen)
subscriber.setsockopt(zmq.SUBSCRIBE,'')
# forking to listen while running grafana
process = os.fork()
if process > 0:
	while True:
		pcap_data = subscriber.recv_json()
		print("Received JSON")
		tim = time.time()
		speed = json.dumps(pcap_data['CAM']['cam']['camParameters']['highFrequencyContainer']['basicVehicleContainerHighFrequency']['speed']['speedValue'] , indent = 4).strip("\"")
		lat = json.dumps(pcap_data['CAM']['cam']['camParameters']['basicContainer']['referencePosition']['latitude'] , indent = 4).strip("\"")
		lng = json.dumps(pcap_data['CAM']['cam']['camParameters']['basicContainer']['referencePosition']['longitude'] , indent = 4).strip("\"")
		datum = [{"measurement": sys.argv[6], "fields":{sys.argv[3] : float(speed)}}]
		# After each successful catch, object is written into to the database
		dbClient.write_points(datum)
else:
	# Generate Query
	query = query_interpreter(sys.argv[6],sys.argv[3])
	# Generic panel
	panel = default_panel.main(sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],query)
	# Import to Grafana & open Grafana on browser
	subprocess.call("./panel_import.sh")
