import requests
import time

endpoint = "https://filfox.info/api/v1/address/f05/messages?pageSize=100&page={}".format

revenue = 0

for i in range(10000):
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
        

    for msg in messages:
        day = time.strftime('%d', time.localtime(msg["timestamp"]))
        if day == 19:
            print("I am at 19")
            print(revenue)
            break

        if day == 20:
            revenue += (msg["value"] / (10 ** 18))
