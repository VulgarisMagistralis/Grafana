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
		<canvas id="canvas" width="400" height="400"></canvas>
		<div> </div>
		<?php
			$i;
			$filename  = "clean_coor.txt";
			$pairs = file($filename, FILE_IGNORE_NEW_LINES);
		?>
		<script>
			var j; <? $i = 0; ?>
			var points =[];
			for(j = 0; j < <? echo sizeof($pairs); ?>; j++)
				<? $coors = explode(" ",$pairs[$i++]); ?>
				points.push( [<? echo $coors[0]; ?>,<? echo $coors[1]; ?>] );
			var points_json = JSON.stringify(points);
  // Get the context of the canvas element we want to select
  var ctx = document.getElementById("canvas").getContext("2d");

  // Instantiate a new chart using 'data' (defined below)
			
        var data = {
            labels :["January","February","March","April","May","June","July"],datasets : [
                {
                    fillColor : "rgba(220,280,220,0.5)",
                    strokeColor : "rgba(220,220,220,1)",
                    data : [65,59,90,81,56,55,40]

                },
                {
                    fillColor : "rgba(151,187,205,0.5)",
                    strokeColor : "rgba(151,187,205,1)",
                    data : [28,48,40,19,96,27,100]
                }
            ]
        };
	  	var myChart = new Chart(ctx).Line(data);

		</script>
   </body>
</html>