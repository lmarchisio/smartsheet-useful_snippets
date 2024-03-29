import smartsheet
import logging
import json

# Set API access token
access_token = None

# initialize client
smart = smartsheet.Smartsheet(access_token)
# make sure we don't miss any errors
smart.errors_as_exceptions(True)
# log all calls
logging.basicConfig(filename='rwsheet.log', level=logging.INFO)

response = smart.Users.list_users(include_all=True)
users = response.data

for user in users:
    pyuser = json.loads(str(user))
    print(str(pyuser['id']) + ": " + str(pyuser['name']))

print('press Enter key to close')
input()
