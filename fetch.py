import requests
import time
import csv

endpoint = "https://filfox.info/api/v1/address/f05/messages?pageSize=100&page={}".format

field_names= ['cid', 'height', 'timestamp', 'from', 'to', 'nonce', 'value', 'method', 'receipt']

for i in range(3500, 10000):
    print("i = {}".format(i))
    response = dict(requests.get(endpoint(i)).json())
    try:
        messages = response["messages"]
    except Exception as e:
        print(e)
        print("Sleeping for 61 sec")
        time.sleep(61)

        response = dict(requests.get(endpoint(i)).json())
        messages = response["messages"]
        
    with open('response_{}.csv'.format(i), 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(messages)
