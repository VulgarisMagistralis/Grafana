import json
import Geohash
from collections import OrderedDict
from influxdb import InfluxDBClient
'''
#time in ns
def create_json(speed,lat,lng,time):
	geo_h = Geohash.encode(lat,lng)
	datum=[{
		"name": "SpeedStats",
		"tags": {
			"geohash":geo_h,
		}
		"columns":[
			"time",
			"metric"
		]
		"values":[
			time,
			speed
		]
	}]
'''
with open("3907.json") as json_file:
    pcap_data = json.load(json_file)
ms="SpeedStats" ; tag=0
dbClient = InfluxDBClient('localhost' , 8086 , 'root' , 'root' , 'MAP_TEST')
dbClient.drop_database('MAP_TEST')
dbClient.create_database('MAP_TEST')
def has_gn_fields(json_data):
    return 'cam.CAM_element' in json_data
for j in range(len(pcap_data)) :
	if has_gn_fields(str(pcap_data[j])):
		tim =(json.dumps(pcap_data[j]['_source']['layers']['frame']['frame.time_epoch'] , indent = 4)).strip("\"").replace(".","")
		lat = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.basicContainer_element']['cam.referencePosition_element']['cam.latitude'] , indent = 4).strip("\"")
		lng = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.basicContainer_element']['cam.referencePosition_element']['cam.longitude'] , indent = 4).strip("\"")
		speed=json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.speed_element']['cam.speedValue'] , indent = 4).strip("\"")
		geo_h=Geohash.encode(float(lat)/(10**7),float(lng)/(10**7))
		datum =[{
			"measurement": ms,
			"tags":{
				"point_tag":tag
			},
			"fields":{
				"Speed":float(speed),
				"Latitude":float(lat)/(10**7),
				"Longitude":float(lng)/(10**7),
				"Geohash":geo_h
			},
			"time":int(tim)
		}]
		tag+=1
		dbClient.write_points(datum)
