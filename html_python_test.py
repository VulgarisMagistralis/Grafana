#!/usr/bin/env python

import cgi
import os
import sys
import zmq
import time
import json
import commands
import requests
import subprocess
import default_panel
from collections import OrderedDict

context_json_py = zmq.Context()
subscriber = context_json_py.socket(zmq.SUB)
subscriber.connect("tcp://127.0.0.1:2004")
subscriber.setsockopt(zmq.SUBSCRIBE,'')
 
print "Content-type: text/html"
print

print """
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
			integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
			crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
   			integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
   			crossorigin=""></script>
       <script src=" leaflet-heat.js" ></script>
        <script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0/dist/Chart.min.js"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
        <title>Real Time Updating Map</title>
    </head>
    <body style="background-color: black;">
        <div id = "map" style="height: 440px; border: 1px solid #AAA;"></div>
	<script>
		//Creating a Layers for the markers and Polylines and Creating the Main map
		var markerLayer = new L.layerGroup();
		var polylineLayer = new L.layerGroup();
		var map = L.map('map').setView([45.06,7.65],15);
			L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
				attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
			}).addTo(map);
		var overlays = {
			"Marker Layer" : markerLayer,
			"Path Layer" : polylineLayer
		};
		L.control.layers(overlays).addTo(map);
	</script>
	<script type="text/javascript">
		// This script is to simmulate a dataset 
		var j = 0;
		var lat = 6.88869;
		var lon = 79.85878;
		var speedflag = "false";
		function myLoop() {
			setTimeout(function() {
				lat = lat + 0.0001;
				lon = lon + 0.0001;
				lat2 = lat + 0.0001;
				lon2 = lon + 0.0002;
				var id = Math.floor((Math.random() * 2) + 1);
				mapUpdater("" + id, lat, lon);
				j++;
				if (j < 10000) {
					myLoop();
				}
			}, 50)
		}
		myLoop();
	</script>
	<script type="text/javascript">
		//Main Map Related Scripts
		var idList = [];
        var id_1 = 1;
		function mapUpdater(id, lat, lon) {
			var proxi = true;
			var len = null;
			var poly = null;
			var mark = null;
			//If the list doesn't contain anything Adding The Markers and PolyLines
			if (idList.length == 0) {
				mark = L.marker([ lat, lon ]).bindPopup("Vehicle ID : " + id, {
					autoPan : false
				});
				markerLayer.addLayer(mark);
				poly = L.polyline([], {
					color : 'pink'
				});
				polylineLayer.addLayer(poly).addTo(map);
				idList.push([ id, mark, poly, false ]);
				return;
			}
			for (var i = idList.length; i > 0; i--) {
				if (id == idList[i - 1][0]) {
					len = i - 1;
					break;
				}
				// If the ID is not in the list initiate new entry
				else if ((i - 1) == 0) {
					mark = L.marker([ lat, lon ]).bindPopup(
							"Vehicle ID : " + id, {
								autoPan : false
							});
					markerLayer.addLayer(mark);
					poly = L.polyline([], {
						color : 'pink'
					});
					polylineLayer.addLayer(poly).addTo(map);
					len = idList.length - 1;
					idList.push([ id, mark, poly, false ]);
					//idListArea.value += id + ", ";
					return;
				}
			}
			if (idList[len][3] == true) {
				idList[i - 1][2].addLatLng([ lat, lon ]);
				poly = L.polyline([], {
					color : 'Pink'
				});
				polylineLayer.addLayer(poly).addTo(map);
				idList[len][2] = poly;
				idList[len][3] = false;
			}
			idList[len][1].setLatLng([ lat, lon ]).update(); // updating the marker
			// Drawing the Path if the check box is checked
			idList[len][2].addLatLng([ lat, lon ]); // updating the poly-line
			// Maintaining the focus on a selected device
			map.panTo([ lat, lon ], {duration : 0.5})
		}
		//Function to maintain focuss on a device
		function followID() {
			var id = document.getElementById("followID").value;
			if (id != "") {
				for (var i = idList.length; i > 0; i--) {
					if (idList[i - 1][0] == id) {
						idList[i - 1][1].openPopup();
						break;
					}
				}
			}
		}
	</script>

</body>
</html>
""" 