#!/bin/bash

while read speed ; do
        echo $(./cm2km "$speed") >> $2
done < "$1"

exit 0

