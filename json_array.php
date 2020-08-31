<?

$result_3 = implode(",",$result_2[]);

$result_4 = explode(',',$result_3);

echo "data_s.push(" . $result_4[1] . ");";

echo "points.push([" . $result_4[2] . "," . $result_4[3]. "]);";
?>