#!/bin/bash

HOST="https://vulgaris.grafana.net"
KEY="eyJrIjoiVVN2d1V6NUtPVGlNQ1lnN3VLRHp5cmlnc0QyVDZrNEYiLCJuIjoicmVtb3RlX3Rlc3QiLCJpZCI6MX0="
DASH_DIR="/home/vulgaris/Documents/ETSI/scripts/dashboards"
if [ -d "$DASH_DIR" ]; then
    DASH_LIST=$(find "$DASH_DIR" -mindepth 1 -name \*.json)
    if [ -z "$DASH_LIST" ]; then
        exit 1
    else
        FILESTOTAL=$(echo "$DASH_LIST" | wc -l)
    fi
else
    exit 1
fi
for DASH_FILE in $DASH_LIST; do 
    $(cat "$DASH_FILE" | jq '. * {overwrite: false, dashboard: {id: null}}' | curl -s -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $KEY" "$HOST"/api/dashboards/db -d @-)
done