<?
$file = 'data_stream.txt';
$result = array();
$data['time']    = filemtime($file);
$data['content'] = $_POST['time'] < $data['time']
    ? file_get_contents($file)
    : false;

echo json_encode($data);

?>