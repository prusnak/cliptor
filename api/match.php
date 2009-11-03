<?php

@$type = $_GET['type'];
if ($type != 'json') $type = 'xml';

@$streamid = $_GET['streamid'];

$result = array();

if ( preg_match('/^[a-zA-Z0-9_-]{3,16}$/', $streamid) ) {
// TODO: fill $result from database
}

/*
// DEBUG
$entry['stream1'] = 'yt_oP8SrlbpJ5A';
$entry['stream2'] = 'yt_laIr_d0hFB8';
$entry['time1']   = 214.34;
$entry['time2']   = 12.98;
$entry['speed1']  = 1.03;
$entry['speed2']  = 0.97;
$entry['trans']   = 7.15;
$result[] = $entry;
*/

header("Content-Type: application/$type");

print ($type == 'xml') ? "<match>\n" : "[\n";

foreach ($result as $entry) {
  print ($type == 'xml') ? "  <entry>\n" : "{\n";
  foreach (array('stream1', 'stream2') as $i) {
      print ($type == 'xml') ? "    <$i>$entry[$i]</$i>\n" : "\"$i\": \"$entry[$i]\",\n";
  }
  foreach (array('time1', 'time2', 'speed1', 'speed2', 'trans') as $i) {
      print ($type == 'xml') ? "    <$i>$entry[$i]</$i>\n" : "\"$i\": $entry[$i],\n";
  }
  print ($type == 'xml') ? "  </entry>\n" : "},\n";
}

print ($type == 'xml') ? "</match>\n" : "]\n";

?>
