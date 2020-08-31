<!DOCTYPE html>
<html>
	<meta charset='utf-8' />
   	<head profile="http://gmpg.org/xfn/11">
    	<link rel="stylesheet" type="text/css" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css"/>      
      	<script type='text/javascript' src='http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js'></script>
    	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
		<script src="/home/path/Documents/ETSI/scripts/bower.json"></script>
		
	</head>
   	<body>
      	<div id="map" style="height: 440px"></div>
		<div></div>
		<?php
			$filename  = "clean_coor.txt";
			$pairs = file($filename, FILE_IGNORE_NEW_LINES);
		?>
		<script>
			//file
			var j;
			var points =[];
			<?
			$j=0;
				for($j = 0; $j < sizeof($pairs); $j++){
					$coors = explode(" ",$pairs[$j]);
					echo "points.push([" .$coors[0]." ,".$coors[1]."]);";
					echo "document.write(".$j.");";
				}
			?>
			//map
			var map = L.map( 'map').setView(points[0], 19);
   			L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    			attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    			subdomains: ['a','b','c'],
				maxZoom: 30,
				minZoom: 4
			}).addTo( map );
//			let polyLine = new L.polyline.antPath(points,{color: 'lime'}).addTo(map);
			var polyLine = L.polyline(points,{color: 'lime'}).addTo(map);
		</script>
   </body>
</html>