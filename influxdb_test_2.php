<!DOCTYPE html>
<html>
	<meta charset='utf-8'/>
	<head profile="http://gmpg.org/xfn/11">
		<link rel="stylesheet" type="text/css" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css"/>      
		<script type='text/javascript' src='http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js'></script>
		<script src=" leaflet-heat.js" ></script>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	</head>
	<body>
	<div id="map" style="height: 440px; border: 1px solid #AAA;"></div>
		<div id ="scontent"></div>
		<script>
        var time = 0;
        setInterval(function() {
            $.ajax({
                type: "POST",
                data: {time : time},
                url: "fetch_data.php",
                success: function (data) {
                    var result = $.parseJSON(data)
                    if (result.content) {
						var line = result.content; 
						$.ajax({
							url:'influxdb_test_2.php',
							type:"POST",
							dataType:'json',
							data: data,
							success: function(data1){
								console.log(data1);
							}
						});
						//$('#scontent').append('<br>' + line);
					}
                }
            });
        }, 1000);
			<?
			 $var = $_POST['speed'];
			var_dump( "afdafdsf");
			//doenst work
			?>
			var data_t=[];
			var data_s=[];
			var points=[];
			var map = L.map( 'map').setView(points[0],15);
			L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
				attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
			}).addTo(map);
			var polyLine = L.polyline(points,{color: 'lime'}).addTo(map);
			var points_heated = [];
		</script>
	</body>
</html>