<!DOCTYPE html>
<html>
		<meta charset='utf-8' />
<body>
	<div>  </div>
<script>
	var j;
	var size=
	<?
		$i=0;
		$filename  = "deg_coor.txt";
		$pairs = file($filename, FILE_IGNORE_NEW_LINES); 
		 echo sizeof($pairs);
	?>;
	
		for(j = 0; j < size; j++){
				<? $coors = explode(" ",$pairs[$i++]); ?>
				document.write( <? echo $coors[0];?>);
		}
</script>
</body>
</html>








