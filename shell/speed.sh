#!/bin/bash

#pulls speed var
#identify & pull speed
#tshark addr -pcap file - out file
run_shark="./run/tshark -r $2 -T fields -e cam.speedValue cam.stationID != 3907"
cd $1 && $run_shark > $3

exit 0



