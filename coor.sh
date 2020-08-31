#!/bin/bash

while read coors ; do
	echo $(./int2deg2 "$coors") >> $2
done < "$1"
exit 0
