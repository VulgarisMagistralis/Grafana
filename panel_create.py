#!usr/bin/env python
import json
import sys
import string
import random
import webbrowser

# generate user id for panel
def randomStringDigits(stringLength=6):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
# variables
false = False 
true = True
null=""
uid=randomStringDigits(9)

def main(extra,db,graph_t,field,min_r,max_r,query):
	x ={
		"dashboard":{
		"annotations": {
			"list": [
			  {
				"builtIn": 1,
				"datasource": "-- Grafana --",
				"enable": true,
				"hide": true,
				"iconColor": "rgba(0, 211, 255, 1)",
				"name": "Annotations & Alerts",
				"type": "dashboard"
			  }
			]
		  },
		  "editable": true,
		  "gnetId": null,
		  "graphTooltip": 0,
		  "id": 3,
		  "links": [],
		  "panels": [
			{
			  "aliasColors": {},
			  "bars": false,
			  "dashLength": 10,
			  "dashes": false,
			  "datasource": db,
			  "fill": 1,
			  "fillGradient": 10,
			  "gridPos": {
				"h": 14,
				"w": 21,
				"x": 0,
				"y": 0
			  },
			  "id": 2,
			  "legend": {
				"avg": false,
				"current": false,
				"max": false,
				"min": false,
				"show": true,
				"total": false,
				"values": false
			  },
			  "lines": true,
			  "linewidth": 1,
			  "nullPointMode": "null",
			  "options": {
				"dataLinks": []
			  },
			  "percentage": false,
			  "pointradius": 2,
			  "points": false,
			  "renderer": "flot",
			  "seriesOverrides": [],
			  "spaceLength": 10,
			  "stack": false,
			  "steppedLine": false,
			  "targets": [
				{
				  "groupBy": [
					{
					  "params": [
						"$__interval"
					  ],
					  "type": "time"
					},
					{
					  "params": [
						"null"
					  ],
					  "type": "fill"
					}
				  ],
				  "orderByTime": "ASC",
				  "policy": "default",
				  "query": query,
				  "rawQuery": true,
				  "refId": "A",
				  "resultFormat": "time_series",
				  "select": [
					[
					  {
						"params": [
						  "value"
						],
						"type": "field"
					  },
					  {
						"params": [],
						"type": "mean"
					  }
					]
				  ],
				  "tags": []
				}
			  ],
			  "thresholds": [],
			  "timeFrom": null,
			  "timeRegions": [],
			  "timeShift": null,
			  "title": field,
			  "tooltip": {
				"shared": true,
				"sort": 0,
				"value_type": "individual"
			  },
			  "type": graph_t,
			  "xaxis": {
				"buckets": null,
				"mode": "time",
				"name": null,
				"show": true,
				"values": []
			  },
			  "yaxes": [
				{
				  "format": "short",
				  "label": field,
				  "logBase": 1,
				  "max": max_r,
				  "min": min_r,
				  "show": true
				},
				{
				  "format": "short",
				  "label": null,
				  "logBase": 1,
				  "max": null,
				  "min": null,
				  "show": true
				}
			  ],
			  "yaxis": {
				"align": false,
				"alignLevel": null
			  }
			}
		  ],
		  "refresh": "100ms",
		  "schemaVersion": "",
		  "style": "dark",
		  "tags": [],
		  "templating": {
			"list": []
		  },
		  "time": {
			"from": "now-5m",
			"to": "now"
		  },
		  "timepicker": {
			"refresh_intervals": [
			  "100ms",
			  "1s",
			  "5s",
			  "10s",
			  "30s",
			  "1m",
			  "5m",
			  "15m",
			  "30m",
			  "1h",
			  "2h",
			  "1d"
			]
		  },
		  "timezone": "",
		  "title": "zmq_2",
		  "uid": uid,
		  "version": null
		}
	}
	y=0
	with open("dashboards/import_test_1.json", "w") as write_file:
		json.dump(x, write_file)
	url="http://vulgaris.grafana.net/d/"+uid+"/"+db+"?orgId=1"
	webbrowser.open(url,new=2)
	return y;
if __name__ == '__main__':
	main(sys.argv)