#!/bin/bash

#main script
#tshark_adr - pcap file - path for scripts
#set up files
speed_c="$3/speed_cm.txt"
speed_k="$3/speed_km.txt"
raw_coor="$3/raw_coor.txt"
clean_coor="$3/clean_coor.txt"
raw_alt="$3/raw_altitude.txt"
clean_alt="$3/clean_altitude.txt"
raw_acc_lng="$3/raw_long_acc.txt"
curv="$3/curvature.txt"
yaw="$3/yaw.txt"
#identify & pull coordinates
sh ./pcap2latt.sh $1 $2 $raw_coor && sh ./file_clean.sh $raw_coor && sh ./coor.sh $raw_coor $clean_coor
sh ./pcap2alt.sh $1 $2 $raw_alt && sh ./file_clean.sh $raw_alt #&& sh ./coor.sh $raw_alt $clean_alt
sh ./pcap2acc.sh $1 $2 $raw_acc_lng && sh ./file_clean.sh $raw_acc_lng
sh ./pcap2curv.sh $1 $2 $curv && sh ./file_clean.sh $curv
sh ./pcap2yaw.sh $1 $2 $yaw && sh ./file_clean.sh $yaw
#altitude conversion?
#cm2km float
sh ./speed.sh $1 $2 $speed_c && sh ./file_clean.sh $speed_c #&& sh ./cm2km.sh $speed_c $speed_k

exit 0


