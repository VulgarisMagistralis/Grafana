#!/bin/bash
HOST="https://vulgaris.grafana.net"
KEY="eyJrIjoiR0x1Z0txWjlVbG56QmNGWHl0TUFWSWx6UDUyNnlYZDkiLCJuIjoiaW1wb3J0X3Rlc3QyIiwiaWQiOjF9"
DASH_DIR="/home/path/Documents/ETSI/scripts/dashboards"


response=$(curl -v -X POST --insecure -H "Authorization: Bearer eyJrIjoiR0x1Z0txWjlVbG56QmNGWHl0TUFWSWx6UDUyNnlYZDkiLCJuIjoiaW1wb3J0X3Rlc3QyIiwiaWQiOjF9" -H "Content-Type: application/json" -d '{
    "dashboard": {
      "id": null,
      "title": "Production Overview",
      "tags": [ "templated" ],
      "timezone": "browser",
      "rows": [
        {
        }
      ],
      "schemaVersion": 6,
      "version": 0
    },
    "overwrite": false
  }' https://vulgaris.grafana.net/api/dashboards/db)  
  echo "".$response