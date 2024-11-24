import ezsheets

spreadsheet_id = "https://docs.google.com/spreadsheets/d/18oz6DD45x7s-4tj37cx84-iQ9oU32mU6Q0yGBkgwa88/edit?gid=0#gid=0"
ss = ezsheets.Spreadsheet(spreadsheet_id)

sheet = ss[0]

email_column_index = 2
email_addresses = []

for row in sheet.getRows(startRow=2):
    if row[email_column_index - 1]:
        email_addresses.append(row[email_column_index - 1])

print("Email addresses collected from the Google Form responses:")
for email in email_addresses:
    print(email)
