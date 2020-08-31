from influxdb import InfluxDBClient

#worked

loginEvents = [{"measurement":"UserLogins",

        "tags": {

            "Area": "North America",

            "Location": "New York City",

            "ClientIP": "192.168.0.256"

        },

        "fields":

        {

        "SessionDuration":1.2

        }

        },



        {"measurement":"UserLogins",

          "tags": {

            "Area": "South America",

            "Location": "Lima",

            "ClientIP": "192.168.1.256"

        },

        "fields":

        {

        "SessionDuration":2.0

        }

        }

        ]



dbClient = InfluxDBClient('localhost', 8086, 'root', 'root', 'AccessHistory')



# Write the time series data points into database - user login details

dbClient.create_database('AccessHistory')

dbClient.write_points(loginEvents)



# Query the IPs from logins have been made !!!!!!!!!!!!!!! need to define more

#loginRecords = dbClient.query('select * from UserLogins;')
southLogs = dbClient.query('select SessionDuration, Location from UserLogins ;')


# Print the time series query results
print(southLogs)
#print(loginRecords)