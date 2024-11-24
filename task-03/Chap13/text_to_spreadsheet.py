import openpyxl
import os

def insert_text_file_contents(filename, text_files):
  
    wb = openpyxl.Workbook()
    ws = wb.active

    for i, file_path in enumerate(text_files, start=1):
      
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for j, line in enumerate(lines, start=1):
            ws.cell(row=j, column=i, value=line.strip())  # Remove newline character

    wb.save(filename)
    print(f"Contents of text files have been written to '{filename}'")

def main():
    text_files = ['file1.txt', 'file2.txt', 'file3.txt']

    output_filename = 'output_spreadsheet.xlsx'

    if not all(os.path.exists(file) for file in text_files):
        print("One or more text files do not exist.")
        return

    insert_text_file_contents(output_filename, text_files)

if __name__ == "__main__":
    main()