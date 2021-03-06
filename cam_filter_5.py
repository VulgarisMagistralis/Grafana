#!/usr/bin/python
import json
from collections import OrderedDict
from influxdb import InfluxDBClient
#roc_braccini_solophy3
# opening JSON file ,created by wireshark, to load a local json object
with open("braccini_solophy_2.json") as json_file:
    pcap_data = json.load(json_file)
# variable names for temporary storage, from JSON to InfluxDB
measurement_name = "CAMessage" ; st_ID=0 ; latt=0 ; long=0 ; alti=0 ; curve=0 ; longA=0 ; speed=0 ; timeE=0 ; timeV=0 ; laneP=0 ; lenV=0 ; yawR=0 ; dDir=0 ; Vtype=0 ; count=0 ; j=0 ;
# connecting to InfluxDB creating DB, delete if DB exists already  otherwise causes problems
dbClient = InfluxDBClient('localhost' , 8086 , 'root' , 'root' , 'CAMessageLog5')
dbClient.drop_database('CAMessageLog4')
dbClient.create_database('CAMessageLog4')
# Some messages have missing fields, a function to check presence of geonetworking fields
def has_gn_fields(json_data):
    return 'cam.CAM_element' in json_data
# Getting necessary fields from local json object, to individual variables for performing operations easily on them
for j in range(len(pcap_data)) :
    # field check, jump message if it is missing gn fields
    if has_gn_fields(str(pcap_data[j])):
        timeE = (json.dumps(pcap_data[j]['_source']['layers']['frame']['frame.time_epoch'] , indent = 4)).strip("\"").replace(".","")
        st_ID= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.header_element']['cam.stationID'] , indent = 4).strip("\"")
        timeV= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.generationDeltaTime'] , indent = 4).strip("\"")
        Vtype= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.basicContainer_element']['cam.stationType'] , indent = 4).strip("\"")
        latt = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.basicContainer_element']['cam.referencePosition_element']['cam.latitude'] , indent = 4).strip("\"")
        long = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.basicContainer_element']['cam.referencePosition_element']['cam.longitude'] , indent = 4).strip("\"")
        laneP= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.lanePosition'] , indent = 4).strip("\"")
        dDir = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.driveDirection'] , indent = 4).strip("\"")
        alti = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.basicContainer_element']['cam.referencePosition_element']['cam.altitude_element']['cam.altitudeValue'] , indent = 4).strip("\"")
        speed= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.speed_element']['cam.speedValue'] , indent = 4).strip("\"")
        yawR = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.yawRate_element']['cam.yawRateValue'] , indent = 4).strip("\"")
        curve= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.curvature_element']['cam.curvatureValue'] , indent = 4).strip("\"")
        lenV = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.vehicleLength_element']['cam.vehicleLengthValue'] , indent = 4).strip("\"")
        longA= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.longitudinalAcceleration_element']['cam.longitudinalAccelerationValue'] , indent = 4).strip("\"")
        # Enumeration in front of the new json object fileds allows us to have ordered columns on both DB and Grafana Tables as we want
        datum = [{
                                "measurement": measurement_name,
                                "fields":{
                                        "1_ID" : int(st_ID),
                                        "6_Speed" : float(speed) * 0.001,
                                        "4_Longitude": float(long)/(10**7),
                                        "3_Latitude" : float(latt)/(10**7),
                                        "5_Altitude" : float(alti),
                                        "2_GenerationTime" : float(timeV),
                                        "7_LongitudinalAcc":float(longA)/100,
                                        "8_Curve" : float(curve),
                                        "9_VehicleLength" : lenV,
                                        "99_DriveDir" : dDir,
                                        "99_StationType" : Vtype,
                                        "YawRate" : float(yawR)/10000
                                },
                                "time" : int(timeE)
                        }]
        # After each successful iteration, object is written into to the InfluxDB.CAMessageLog database
        # Better version might be adding everything at the end of writing all the single instances but doing so caused some problems on my test
        dbClient.write_points(datum)
    else :
        count+=1
    j+=1
print("Number of Messages w/o gn fields: " + str(count))
print("Total number of Messages: " + str(j-1))
