#!/usr/bin/python
import json

with open("out.json") as json_file:
    pcap_data = json.load(json_file)
i="{}"
j=0
while i is not None:
    i = json.dumps(pcap_data[j]['_source']['layers']['etsi_its_geonetworking']['cam'],indent=4)
    print(i)
    j+=1
