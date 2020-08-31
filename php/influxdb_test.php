<!DOCTYPE html>
<html>
	<meta charset='utf-8'/>
	<head profile="http://gmpg.org/xfn/11">
		<link rel="stylesheet" type="text/css" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css"/>      
		<script type='text/javascript' src='http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js'></script>
		<script src=" leaflet-heat.js" ></script>
		<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0/dist/Chart.min.js"></script>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	</head>
	<body>
	<div id="map" style="height: 440px; border: 1px solid #AAA;"></div>
		<?php
	include('/home/path/Documents/ETSI/scripts/php/vendor/autoload.php');
	use InfluxDB\Client;
	use InfluxDB\Point;
	use InfluxDB\Query\Builder;
	$host="127.0.0.1";
	$port="8086";
	$client = new Client($host,$port);
	$database = $client->selectDB('MAP_TEST');
	$result_2 = $database->getQueryBuilder()
		->select('Speed,Latitude,Longitude')
		->from('SpeedStats')
		->getResultSet()
		->getPoints();
?>
		<script>
			var data_t=[];
			var data_s=[];
			var points=[];
			
			<?php
				for($i = 0; $i < count($result_2); $i++){
					$result_3 = implode(",",$result_2[$i]);
					$result_4 = explode(',',$result_3);
					echo "data_s.push(" . $result_4[1] . ");";
					echo "points.push([" . $result_4[2] . "," . $result_4[3]. "]);";
				} 
			?>
			//loop doesnt work map is fine
			var map = L.map( 'map').setView(points[0],15);
			L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
				attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
			}).addTo(map);
			var polyLine = L.polyline(points,{color: 'lime'}).addTo(map);
			var points_heated = [];
		</script>
	</body>
</html>