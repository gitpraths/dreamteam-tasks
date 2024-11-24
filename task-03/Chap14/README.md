This repository contains three distinct Python projects that interact with Google Sheets using the ezsheets library.
Below is a brief description of each project, including setup instructions and how to run the code.

Install the ezsheets library
pip install ezsheets

Downloading Google Forms Data

Converting Spreadsheets to Other Formats

Finding Mistakes in a Spreadsheet

General Running Instructions
For all three projects, you will need to set up Google API credentials to interact with Google Sheets through ezsheets. Follow these steps:

Go to the Google Developers Console (https://console.developers.google.com/).
Create a new project or select an existing one.
Enable the Google Sheets API for your project.
Create credentials (OAuth 2.0 client ID) for your application.
Download the JSON file with your credentials.
Set the GOOGLE_API_KEY environment variable to the path of your JSON file.
After setting up your credentials, you can run each project's script individually.
Make sure to replace placeholder values with your actual data, such as the spreadsheet ID and file paths.
