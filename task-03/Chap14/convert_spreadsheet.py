import ezsheets

file_path = 'myfile.xlsx'
ss = ezsheets.upload(file_path)

print(f"Spreadsheet uploaded to Google Sheets: {ss.title}")

ss.downloadAsExcel('myfile.xlsx')
print("Downloaded as Excel (.xlsx): myfile.xlsx")

ss.downloadAsODS('myfile.ods')
print("Downloaded as OpenDocument Spreadsheet (.ods): myfile.ods")

ss.downloadAsCSV('mytest.csv', sheetId=0)
print("Downloaded as CSV from the first sheet: mytest.csv")

ss.downloadAsTSV('myfile.tsv', sheetId=0)
print("Downloaded as TSV from the first sheet: myfile.tsv")

ss.downloadAsPDF('testmyfile.pdf')
print("Downloaded as PDF: testmyfile.pdf")

ss.downloadAsHTML('myfile.html')
print("Downloaded as HTML: myfile.html")