<!DOCTYPE html>
<html>
	<meta charset='utf-8' />
   	<head profile="http://gmpg.org/xfn/11">
    	<link rel="stylesheet" type="text/css" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css"/>      
      	<script type='text/javascript' src='http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js'></script>
    	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	</head>
   	<body>
      	<div id="map" style="height: 440px"></div>
		<div></div>
		<?php
			$i;
			$filename  = "deg_coor.txt";
			$pairs = file($filename, FILE_IGNORE_NEW_LINES);
		?>
		<script>
			//file
			var j; <? $i = 0; ?>
			var points =[];
			for(j = 0; j < <? echo sizeof($pairs); ?>; j++){
				<? $coors = explode(" ",$pairs[$i++]); ?>
				points.push( [<? echo $coors[0]; ?>,<? echo $coors[1]; ?>] );
			}
			//EOF
			var map = L.map( 'map').setView(points[0], 13);
   			L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    			attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    			subdomains: ['a','b','c']
			}).addTo( map );
//			var poly = L.polyline(points,{color: 'black'}).addTo(map);
			var GJ={
					"type": "Point" ,
					"coordinates": [45.6,7.65]
			};
			L.geoJSON(GJ).addTo(map);
		</script>
		
   </body>
</html>