import requests
url='http://admin:admin@localhost:3000/api/dashboards/import'
data='''{
  "dashboard": {}
  "folderId": 0,
  "overwrite": false
}'''
headers={"Content-Type": 'application/json'}
response = requests.post(url, data=data,headers=headers)
print(response)
print(response.status_code)
print (response.text)