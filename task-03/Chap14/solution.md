## Introduction to Google Sheets and EZSheets
- Google Sheets is a free, web-based spreadsheet application accessible to anyone with a Google account.
- EZSheets is a third-party module that simplifies interactions with Google Sheets, making common tasks easier than using the official API.

## Installing and Setting Up EZSheets
- Install EZSheets using the command: pip install --user ezsheets.
- The installation also includes necessary modules for API requests.
### Obtaining Credentials and Token Files:
- Enable Google Sheets and Google Drive APIs via specific URLs.
- Download and rename the credentials file to credentials-sheets.json.
- After importing EZSheets for the first time, a browser window will prompt for Google account login to generate token files.
## Spreadsheet and Sheet Objects
- A Spreadsheet can contain multiple Sheets, each with rows and columns of data.
### Creating, Uploading, and Listing Spreadsheets:
- Create a new Spreadsheet or upload existing files using EZSheets functions.
- Use the listSpreadsheets() function to view all spreadsheets in your account.
### Spreadsheet Attributes:
- Attributes include title, spreadsheetId, url, sheetTitles, and sheets, which can be manipulated programmatically.
## Data Manipulation in Sheets
### Reading and Writing Data:
- Use square brackets to access and modify cell data.
- EZSheets provides methods for reading and writing entire rows and columns efficiently.
### Creating and Deleting Sheets:
- New sheets can be added or deleted using createSheet() and delete() methods.
- The clear() method can be used to empty a sheet without deleting it.
## Working with Google Sheets Quotas
- Google Sheets has limits on read and write operations, which can affect performance.
- Users can create a limited number of spreadsheets and perform a set number of requests within a time frame.
- EZSheets can handle quota exceptions automatically, but users can also manage these exceptions manually.