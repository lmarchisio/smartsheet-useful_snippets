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

# note that this differs slightly from list_users.py as a workspace is not iterable where a list of users is
workspace = smart.Workspaces.get_workspace(
    8881208101758852)

pyworkspace = json.loads(str(workspace))
b = pyworkspace.get('sheets', 0)

for n in range(len(b)):
    c = b[n]
    print(str(c['name']) + ': ' + str(c['id']))
    print(c['permalink'])
    print()

# uncomment below to print all sheet data
#pprint.pprint(pyworkspace['sheets'])

# uncomment below to print all data
#pprint.pprint(pyworkspace)

print(len(pyworkspace))
