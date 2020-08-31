#!/bin/bash

#curl -I -H "Authorization: Bearer eyJrIjoiR0x1Z0txWjlVbG56QmNGWHl0TUFWSWx6UDUyNnlYZDkiLCJuIjoiaW1wb3J0X3Rlc3QyIiwiaWQiOjF9" https://vulgaris.grafana.net/api/dashboards/db

#creating datasource
curl -X POST -H "Authorization: Bearer eyJrIjoianVnczRHekJPYTR6a3Y2R1AydDlvM0JxS1ZWWVNEbjkiLCJuIjoiaW1wb3J0X3Rlc3RfZGFzaCIsImlkIjoxfQ==" -H "Content-Type: application/json" -d '
{
  "name":"test_datasource_2",
  "type":"influxdb",
  "database":"CAMessageLog8",
  "url":"http://localhost:8086",
  "access":"browser",
  "user":"root",
  "password":"root",
  "basicAuth":true
}'  https://vulgaris.grafana.net/api/datasources


