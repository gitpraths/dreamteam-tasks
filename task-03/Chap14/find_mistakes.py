import ezsheets

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet = ss[0]


for i, row in enumerate(sheet.getRows()):
    if len(row)!= len(sheet.getRow(1)):
        print(f"Row {i+1} has an inconsistent number of cells.")


for i, row in enumerate(sheet.getRows()):
    for j, cell in enumerate(row):
        try:
            float(cell)
        except ValueError:
            print(f"Cell ({i+1}, {j+1}) contains non-numeric data: {cell}")


for i, row in enumerate(sheet.getRows()):
    for j, cell in enumerate(row):
        if cell == "":
            print(f"Cell ({i+1}, {j+1}) is blank.")