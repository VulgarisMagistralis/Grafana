#!/usr/bin/python
import json
from collections import OrderedDict
from influxdb import InfluxDBClient
# opening JSON file ,created by wireshark, to load a local json object
with open("roc_pcap.json") as json_file:
    pcap_data = json.load(json_file)
# variable names for temporary storage, from JSON to filtered JSON
st_ID=0 ; latt=0 ; long=0 ; alti=0 ; curve=0 ; longA=0 ; speed=0 ; timeE=0 ; timeV=0 ; laneP=[] ; lane_pos=0 ; lenV=0 ; yawR=0 ; dDir=0 ; Vtype=0 ; count=0 ; j=0 ; cams=[];
# Some messages have missing fields, a function to check presence of geonetworking fields
def has_gn_fields(json_data):
    return 'cam.CAM_element' in json_data
# Getting necessary fields from local json object, to individual variables for performing operations easily on them
for j in range(len(pcap_data)) :
    # field check, jump message if it is missing gn fields
    if has_gn_fields(str(pcap_data[j])):
        timeE= json.dumps(pcap_data[j]['_source']['layers']['frame']['frame.time_epoch'] , indent = 4).strip("\"").replace(".","")
        st_ID= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.header_element']['cam.stationID'] , indent = 4).strip("\"")
        timeV= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.generationDeltaTime'] , indent = 4).strip("\"")
        Vtype= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.basicContainer_element']['cam.stationType'] , indent = 4).strip("\"")
        latt = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.basicContainer_element']['cam.referencePosition_element']['cam.latitude'] , indent = 4).strip("\"")
        long = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.basicContainer_element']['cam.referencePosition_element']['cam.longitude'] , indent = 4).strip("\"")
        dDir = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.driveDirection'] , indent = 4).strip("\"")
        alti = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.basicContainer_element']['cam.referencePosition_element']['cam.altitude_element']['cam.altitudeValue'] , indent = 4).strip("\"")
        speed= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.speed_element']['cam.speedValue'] , indent = 4).strip("\"")
        curve= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.curvature_element']['cam.curvatureValue'] , indent = 4).strip("\"")
        lenV = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.vehicleLength_element']['cam.vehicleLengthValue'] , indent = 4).strip("\"")
        longA= json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam']['cam.CAM_element']['cam.cam_element']['cam.camParameters_element']['cam.highFrequencyContainer_tree']['cam.basicVehicleContainerHighFrequency_element']['cam.longitudinalAcceleration_element']['cam.longitudinalAccelerationValue'] , indent = 4).strip("\"")
        # loading a local json object to push into json set
        datum = {
                                "Info": "CAM",
                                "ID" : int(st_ID),
                                "Speed" : float(speed) * 0.001,
                                "Longitude": float(long)/(10**7),
                                "Latitude" : float(latt)/(10**7),
                                "Altitude" : float(alti),
                                "GenerationTime" : timeV,
                                "LongitudinalAcc":float(longA)/100,
                                #"Curve" : float(curve),
                                #"VehicleLength" : lenV,
                                #"DriveDir" : dDir,
                                #"StationType" : Vtype,
                                "Time" : int(timeE)
                        }
        cams.append(datum)
    else :
        count+=1
    j+=1
# writing json set to file
with open('cam2js.json','w') as file:
    json.dump(cams,file,indent=4)
# some info on file
print("Number of Messages w/o gn fields: " + str(count))
print("Total number of Messages: " + str(j-1))
