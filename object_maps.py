# sheet map
response = ss_client.Sheets.list_sheets(include_all=True)
sheets = response.data

for sheet in sheets:
    map_of_sheets[sheet.name] = sheet.id

# column map
sheet = ss_client.Sheets.get_sheet(map_of_sheets[this_project])

for column in sheet.columns:
    project_columns[column.title] = column.id

# row map
sheet = ss_client.Sheets.get_sheet(map_of_sheets[this_project])

for row in sheet.rows:
    project_rows[row.row_number] = row.id
