#!/usr/bin/python
import json
from collections import OrderedDict
from influxdb import InfluxDBClient
# opening JSON file ,created by wireshark, to load a local json object
with open("roc_pcap.json") as json_file:
    pcap_data = json.load(json_file)
# variable names for temporary storage, from JSON to InfluxDB
measurement_name = "CAMessage" ; st_ID=0 ; latt=0 ; long=0 ; alti=0 ; curve=0 ; longA=0 ; speed=0 ; timeE=0 ; timeV=0 ; laneP=[] ; lane_pos=0 ; lenV=0 ; yawR=0 ; dDir=0 ; Vtype=0 ; j=0
# connecting to InfluxDB creating DB, delete if DB exists already  otherwise causes problems
dbClient = InfluxDBClient('localhost' , 8086 , 'root' , 'root' , 'CAMessageLog')
dbClient.drop_database('CAMessageLog')
dbClient.create_database('CAMessageLog')
# Getting necessary fields from local json object, to individual variables for performing operations easily on them
for j in range(len(pcap_data)):
    timeE= json.dumps(pcap_data[j]['_source']['layers']['frame']['frame.time_epoch'] , indent = 4)
    st_ID= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.header_element']['cam.stationID'], indent = 4)
    timeV= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.generationDeltaTime'] , indent = 4)
    Vtype= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.basicContainer_element']['cam.stationType'] , indent = 4)
    latt = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.basicContainer_element']['cam.referencePosition_element']['cam.latitude'] , indent = 4)
    long = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.basicContainer_element']['cam.referencePosition_element']['cam.longitude'] , indent = 4)
    dDir = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.driveDirection'] , indent = 4)
    alti = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.basicContainer_element']['cam.referencePosition_element']['cam.altitude_element']['cam.altitudeValue'] , indent = 4)
    laneP= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element'].get('cam.yawRate_element'), indent = 4)
    speed= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.speed_element']['cam.speedValue'] , indent = 4)
    curve= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.curvature_element']['cam.curvatureValue'] , indent = 4)
    lenV = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.vehicleLength_element']['cam.vehicleLengthValue'] , indent = 4)
    longA= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.longitudinalAcceleration_element']['cam.longitudinalAccelerationValue'] , indent = 4)
    timeE = timeE.strip("\"")
    timeE = timeE.replace(".",'')
    # Enumeration in front of the new json object fileds allows us to have ordered columns on both DB and Grafana Tables as we want
    # .strip() is used to eliminate ' " ' because python dumps data as string but we need numerical values for operations
    datum = [{"measurement": measurement_name,
                      "fields":{"1_ID" : float(st_ID.strip("\"")),
                                            "6_Speed" : float(speed.strip("\"")) * 0.036,
                                            "4_Longitude":float(long.strip("\""))/(10**7),
                                            "3_Latitude" : float(latt.strip("\""))/(10**7),
                                            "5_Altitude" : float(alti.strip("\"")) / 100,
                                            "2_GenerationTime" : float(timeV.strip("\"")),
                                            "7_LongitudinalAcc":float(longA.strip("\""))/100,
                                            "8_Curve" : float(curve.strip("\"")),
                                            "9_VehicleLength" : float(lenV.strip("\"")),
                                            "99_DriveDir" : float(dDir.strip("\"")),
                                            "99_StationType" : Vtype.strip("\"")
                                       },
                      "time" : int(timeE)
                     }]
    # After each filled iteration, object is written into to the InfluxDB.CAMessageLog database
    # Better version might be adding everything at the end of writing all the single instances but doing so caused some problems on my test
    dbClient.write_points(datum)
    j+=1
