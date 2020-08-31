<!DOCTYPE html>
<html>
	<meta charset='utf-8'/>
	<head profile="http://gmpg.org/xfn/11">
		<link rel="stylesheet" type="text/css" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css"/>
		<script src="https://d3js.org/d3.v5.min.js"></script>
		<script src=" https://cdn.plot.ly/plotly-latest.min.js"></script>
		<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0/dist/Chart.min.js"></script>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
		<script type='text/javascript' src='http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js'></script>
		<script src=" leaflet-heat.js"></script>
	</head>
	<body>
		<form id="form1" runat="server"></form>
		<div style="margin:20px auto;width: 500px;"></div>
		
		<table id="jsonTable" border="1" style="border-collapse:collapse;" cellpadding="5"></table>
		<script type="text/javascript"> //table
			function addAllColumnHeaders(myList){
				var columnSet = [];
				var headerTr$ = $('<tr/>');
				for(var i = 0; i < myList.length; i++){
					var rowHash = myList[i];
					for(var key in rowHash){
						if($.inArray(key, columnSet) == -1){
							columnSet.push(key);
							headerTr$.append($('<th/>').html(key));
						}
					}
				}
				$("#jsonTable").append(headerTr$);
				return columnSet;
			}
			$.getJSON("cam2js.json", function (data){
				var columns = addAllColumnHeaders(data); 
				for(var i = 0; i < data.length; i++){
					var row$ = $('<tr/>');
					for(var colIndex = 0; colIndex < columns.length; colIndex++){
						var cellValue = data[i][columns[colIndex]];
						if(cellValue == null) cellValue = ""; 
						row$.append($('<td/>').html(cellValue));
					}
					$("#jsonTable").append(row$);
				}
			});
		</script>
		<script>
		  $(document).ready(function() {

$.ajax({

    url: "cam2js.json",
    dataType: "JSON",
    type: "POST",
    cache: false,
    success: function(pieData) {
            var ctx = $("#chart-area").get(0).getContext("2d");
            new Chart(ctx).Pie(pieData);
    }
   });  });
		
		</script>
	</body>
</html>