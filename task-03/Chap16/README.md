# Working with CSV and JSON Files

## CSV Format Overview
- **CSV** stands for **Comma-Separated Values**.
- CSV files are **plaintext representations** of spreadsheets.
- They **lack features** like:
  - Data types.
  - Formatting.
  - Multiple worksheets.

## Using the `csv` Module
- The `csv` module simplifies reading and writing CSV files.
- A **reader object**:
  - Allows iteration over lines in a CSV file.
  - Data can be accessed as:
    - A list of lists.
    - Through a `for` loop for **memory efficiency**.

### Writing to CSV Files
- A **writer object** is created using `csv.writer()`.
- The `writerow()` method writes lists to the CSV file.
- Custom **delimiters** and **line terminators** can be specified.

### DictReader and DictWriter
- **DictReader** and **DictWriter** allow working with CSV files using dictionaries.
- They use the first row as keys for the dictionaries, simplifying data access.

---

## JSON Format Overview
- **JSON** stands for **JavaScript Object Notation**.
- It is a **human-readable data format**.
- Widely used in **web applications** and **APIs**.

## Using the `json` Module
- The `json` module provides functions for converting between JSON strings and Python values:
  - `json.loads()`: Converts JSON strings to Python objects.
  - `json.dumps()`: Converts Python objects to JSON strings.
- JSON supports basic data types:
  - Strings.
  - Integers.
  - Floats.
  - Booleans.
  - Lists.
  - Dictionaries.

## Accessing APIs with JSON
- APIs often return data in JSON format, enabling **programmatic access** to web services.
- Example applications:
  - Weather data retrieval.
  - Social media automation.

---

## Practical Applications

### Project Ideas
1. Automate the removal of headers from multiple CSV files.
2. Create a weather data fetching program using an API.
3. Develop an Excel-to-CSV converter for batch processing of files.

### Practice Questions and Projects
- **Questions** focus on:
  - Understanding CSV and JSON features and functions.
- **Suggested projects** encourage hands-on experience with:
  - File manipulation.
  - API interaction.
