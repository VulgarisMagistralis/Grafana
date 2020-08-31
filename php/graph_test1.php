<!DOCTYPE html>
<html>
	<meta charset='utf-8'/>
   	<head profile="http://gmpg.org/xfn/11">
    	<link rel="stylesheet" type="text/css" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css"/>      
      	<script type='text/javascript' src='http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js'></script>
		<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0/dist/Chart.min.js"></script>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	</head>
   	<body>
		<div id="map" style="height: 440px"></div>
		<canvas id="myChart" width="400" height="400"></canvas>
		<canvas id="canvas" width="400" height="400"></canvas>
		<?php
			$i;
			$filename  = "clean_coor.txt";
			$file_speed  = "speed_cm.txt";
			$file_time = "time.txt";
			$speed_data = file($file_speed, FILE_IGNORE_NEW_LINES);
			$time_data = file($file_time, FILE_IGNORE_NEW_LINES);
			$pairs = file($filename, FILE_IGNORE_NEW_LINES);
		?>

<script>
	var data_t=[];
	var data_s=[];
	<?
		for($i = 0; $i < sizeof($speed_data); $i+=50){
			echo "data_s.push(" .$speed_data[$i]. ");";
			echo "data_t.push(" .$time_data[$i]. ");";
		}
	?>
 var data = {
    labels: data_t,
    datasets: [
      {
        label: "Speed of the vehicle",
        data: data_s,
        backgroundColor: "blue",
        borderColor: "lightblue",
        fill: false,
        lineTension: 0,
        radius: 5
      }
    ]
  };
	var options = {
  responsive: true,
  title: {
    display: true,
    position: "top",
    text: "Speed for 3907",
    fontSize: 18,
    fontColor: "#111"
  },
 scales: {
        xAxes:  [{
          display: true,
          scaleLabel: {
            display: true,
            labelString: 'Time'
          }
        }] ,
        yAxes: [{
          display: true,
          scaleLabel: {
            display: true,
            labelString: 'Speed [cm / s]'
          }
        } ]
      },
  legend: {
    display: true,
    position: "bottom",
    labels: {
      fontColor: "#333",
      fontSize: 16
    }
  }
};
	var ctx = $("#myChart");
	var chart = new Chart(ctx, {
    type: "line",
    data: data,
    options: options
  });
			//file
			var j;
			var points =[];
			<?
			$j=0;
				for($j = 0; $j < sizeof($pairs); $j++){
					$coors = explode(" ",$pairs[$j]);
					echo "points.push([" .$coors[0]." ,".$coors[1]."]);";
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