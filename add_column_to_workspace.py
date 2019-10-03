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

# get workspace
workspace = smart.Workspaces.get_workspace(
    8881208101758852)

# make the workspace into a string and translate from JSON into Python
pyworkspace = json.loads(str(workspace))

# get just the sheet data from the workspace, return 0 if no sheet data exists
sheets = pyworkspace.get('sheets', 0)

for sheet in sheets:
    # check to make sure the sheet doesn't already have a column with this name
    worksheet = smart.Sheets.get_sheet(sheet['id'])
    work_column = True
    print('checking sheet ' + str(worksheet.name) + ': ' + str(worksheet.id))
    for column in worksheet.columns:
        if column.title == 'Modified by':
            work_column = False
            break

    print(work_column)

    # if a column by that name did not already exist, make the column
    if work_column == True:
        print('adding new column')
        column = smartsheet.models.Column({
            'title': 'Modified by',
            'type': 'CONTACT_LIST',
            'systemColumnType': 'MODIFIED_BY',
            'index': len(sheet.columns)+1,
            'hidden': True
        })

        new_columns = smart.Sheets.add_columns(
            worksheet.id,
            [column])

