import smartsheet
import logging
import pprint

# Set API access token
access_token = None

sheet_columns = {}    # a place to map project column names to column IDs

# initialize client
ss_client = smartsheet.Smartsheet(access_token)
# make sure we don't miss any errors
ss_client.errors_as_exceptions(True)
# log all calls
logging.basicConfig(filename='rwsheet.log', level=logging.INFO)

# select the sheet
print('What is the sheet we are working on? (Sheet ID)')
this_sheet = input()

# get sheet
sheet = ss_client.Sheets.get_sheet(this_sheet)

# create column map for the sheet
for column in sheet.columns:
    sheet_columns[column.title] = column.id

# print the sheet columns
pprint.pprint(sheet_columns)

print('press Enter key to close')
input()

### select the columns
##print('What column? (column ID)')
##this_column = input()
##
### get the column
##column = ss_client.Sheets.get_column(
##    this_sheet,
##    this_column)
##
### tell me pertinent facts about the column
##print('The column width is')
##print(column.width)
##print('The column index is')
##print(column.index)
##
### set new column width
##print('How wide should it be?')
##this_wide = input()
##
### update column
##column_spec = smartsheet.models.Column({
##    'width': int(this_wide)
##})
##
##response = ss_client.Sheets.update_column(
##    this_sheet,
##    this_column,
##    column_spec)
##
##updated_column = response.result
##
### Finish it
##print('We made it this far.')
##print('Good Job.')
##

