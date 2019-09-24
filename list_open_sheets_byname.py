import smartsheet
import logging
import json
import pprint

# Set API access token
access_token = None

# initialize client
smart = smartsheet.Smartsheet(access_token)
# make sure we don't miss any errors
smart.errors_as_exceptions(True)
# log all calls
logging.basicConfig(filename='rwsheet.log', level=logging.INFO)

# put test commands here
workspace = smart.Workspaces.get_workspace(
    8881208101758852)

pyworkspace = json.loads(str(workspace))
b = pyworkspace.get('sheets', 0)

albert = {}

for n in range(len(b)):
    c = b[n]
    albert[str(c['name'])] = str(c['id'])

albert2 = sorted(albert)

for n in albert2:
    print(n + ': : ' + albert[n])


print('press Enter key to close')
input()
