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
				points.push( [parseFloat(<? echo $coors[0]; ?>), parseFloat(<? echo $coors[1]; ?>)] );
			}
			//EOF
			var map = L.map( 'map', {
    			center: points[0],
    			minZoom: 2,
    			zoom: 15});
   			L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    			attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    			subdomains: ['a','b','c']
			}).addTo( map );
			//mark coordinates to map

			var poly = L.polyline(points,{color: 'black'}).addTo(map);
			map.fitBounds(poly.getBounds());
/*			for(var x in points){
				console.log(points[x]);
			}*/
		</script>
		
   </body>
</html>