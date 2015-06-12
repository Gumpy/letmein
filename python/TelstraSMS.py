# Tested with pythnon 3.4
import requests, json

number_to_sms = "" 
client_id = ""
secret = ""

r1 = requests.get("https://staging.api.telstra.com/v1/oauth/token?client_id={0}&client_secret={1}&grant_type=client_credentials&scope=SMS".format(client_id, secret))
token = r1.json()["access_token"]
headers = {'authorization': 'Bearer {0}'.format(token) , "Content-Type" : "application/json", "Accept" : "application/json"}
message = json.dumps({ "to" : number_to_sms , "body" : "Hello from the telsta API! :-)"})
r2 = requests.post("https://staging.api.telstra.com/v1/sms/messages", data=message, headers=headers)
print(r2.json())