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

bob = {}

for n in range(len(b)):
    c = b[n]
    bob[str(c['id'])] = str(c['name'])

bob2 = sorted(bob)

for n in bob2:
    print(n + ': : ' + bob[n])

print('press Enter key to close')
input()
