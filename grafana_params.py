import sys
import subprocess
import default_panel 
def query_interpreter(table, field):
	print"Building Query on ",field
	query = "SELECT "+field+" FROM "+table
	return query;
if(len(sys.argv) < 5):
	print"Usage:\n",sys.argv[0],"<Datasource> <Graph Type> <Field> <Min Range> <Max Range> <Table Name>"
	#print"For help ",sys.argv[0]," -help"
	sys.exit(1)
# Generate Query
query = query_interpreter(sys.argv[6],sys.argv[3])
# Generic panel
panel = default_panel.main(sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],query)
# Import to Grafana & open Grafana on browser
subprocess.call("./import_dashboard.sh")