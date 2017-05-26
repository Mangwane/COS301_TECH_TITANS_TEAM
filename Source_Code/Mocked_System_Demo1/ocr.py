#!/usr/bin/python
import sys
import base64
import requests
import json

print ("----------------------------------------------------------------------------------")
print ("------------------------------SCANNING INPUT--------------------------------------")
file_path = sys.argv[1]
image_uri = "data:image/jpeg;base64," + base64.b64encode(open(file_path, "rb").read())
r = requests.post("https://api.mathpix.com/v3/latex",
    data=json.dumps({'url': image_uri}),
    headers={"app_id": "lsg", "app_key": "851562083f16c98fe08e7c3b918066ba",
        "Content-type": "application/json"})
result = json.loads(r.text)
print json.dumps(result, indent=4, sort_keys=True)

print ("----------------------------------------------------------------------------------")
print ("------------------------------SCANNING MEMO---------------------------------------")

file_memo = "Memo/memo.jpg"
image_uri = "data:image/jpeg;base64," + base64.b64encode(open(file_memo, "rb").read())
r = requests.post("https://api.mathpix.com/v3/latex",
    data=json.dumps({'url': image_uri}),
    headers={"app_id": "lsg", "app_key": "851562083f16c98fe08e7c3b918066ba",
        "Content-type": "application/json"})
memo = json.loads(r.text)
print json.dumps(memo, indent=4, sort_keys=True)

print ("----------------------------------------------------------------------------------")
print ("--------------------------COMPARING INPUT AGAINST MEMO----------------------------")

print ("User input - ", result.get('latex'))
print ("Memo input - ", memo.get('latex'))

print ("----------------------------------------------------------------------------------")
print ("-------------------------------OUTPUTING RESULTS----------------------------------")

if (result.get('latex') == memo.get('latex')):
    print ("Answer is correct! 1 mark awarded!")
else:
    print ("Answer is incorrect! 0 mark awarded!")
