#!/bin/bash
#run pcap file through tshark
#address for tshark build file
if [ $# -ne 3 ] ; then
        echo "Usage: <tshark_address> <pcap_file> <output_file>"
        exit 1
fi
run_shark="./run/tshark -r $2 -T fields -e cam.yawRateValue"
cd $1 && $run_shark > $3

exit 0


