# Create a new spreadsheet or upload an existing file:

import ezsheets
ss = ezsheets.createSpreadsheet('My Spreadsheet')
ezsheets.upload('example.xlsx')

# List all spreadsheets in your Google account
ezsheets.listSpreadsheets()

# Spreadsheet Attributes
# Key attributes of a spreadsheet include:
# - title: The spreadsheet's name.
# - spreadsheetId: Unique ID of the spreadsheet.
# - url: Direct link to the spreadsheet.
# - sheetTitles: A list of all sheet titles.
# - sheets: A list of sheet objects.

# Access or modify cell data:
sheet = ss[0]  # Access the first sheet
print(sheet['A1'])  # Read cell A1
sheet['A1'] = 'Hello, World!'  # Write to cell A1

# Read or write entire rows and columns efficiently:
print(sheet.getRow(1))  # Get the first row
sheet.updateRow(1, ['Name', 'Age', 'Location'])  # Update the first row
# Creating and Deleting Sheets
# Add a new sheet:
ss.createSheet('New Sheet')
# Delete or clear a sheet:
ss[1].delete()  # Delete the second sheet
ss[0].clear()  # Clear all data in the first sheet