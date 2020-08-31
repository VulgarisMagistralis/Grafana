#   Weather update client
#   Connects SUB socket to tcp://localhost:5556
#   Collects weather updates and finds avg temp in zipcode
import sys
import zmq
#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
print("Collecting updates from weather server...")
socket.connect("tcp://localhost:5556")
zip_filter ="10141"
# Python 2 - ascii bytes to unicode str
zip_filter = zip_filter.decode('ascii')
socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)
# Process 5 updates
total_temp = 0
for update_nbr in range(5):
    string = socket.recv_string()
    print("receiving values...")
    zipcode, temperature, relhumidity = string.split()
    total_temp += int(temperature)

print("Average temperature for zipcode '%s' was %dF" % (
      zip_filter, total_temp / (update_nbr+1))
)
