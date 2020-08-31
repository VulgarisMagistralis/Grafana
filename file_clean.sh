#!/bin/bash

#remove empty lines
sed -i '/^[[:space:]]*$/d' $1

tail -n +2 "$1" > "$1.new" && mv "$1.new" "$1"
head -n -4 "$1" > "$1.new" && mv "$1.new" "$1"

exit 0











