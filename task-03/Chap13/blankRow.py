import sys
import openpyxl

def insert_empty_rows(workbook_filename, starting_row, number_of_rows_to_insert):
    workbook = openpyxl.load_workbook(workbook_filename)
    worksheet = workbook.active
    
    for _ in range(number_of_rows_to_insert):
        worksheet.insert_rows(starting_row, amount=1)
    
    workbook.save(workbook_filename)
    print(f'{number_of_rows_to_insert} empty rows have been inserted starting at row {starting_row}.')

def main():
    if len(sys.argv) != 4:
        print("Usage: python blankRowInserter.py STARTING_ROW NUMBER_OF_ROWS WORKBOOK_FILENAME", file=sys.stderr)
        sys.exit(1)
    
    try:
        starting_row = int(sys.argv[1])
        number_of_rows_to_insert = int(sys.argv[2])
        workbook_filename = sys.argv[3]
        
        if starting_row < 1 or number_of_rows_to_insert < 1:
            print("The starting row and number of rows to insert must be positive integers.", file=sys.stderr)
            sys.exit(1)
        
        insert_empty_rows(workbook_filename, starting_row, number_of_rows_to_insert)
        
    except ValueError:
        print("Error: One or more provided arguments are not valid integers.", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: The file '{workbook_filename}' does not exist.", file=sys.stderr)
        sys.exit(1)
    except openpyxl.utils.exceptions.InvalidFileException:
        print(f"Error: The file '{workbook_filename}' is not a valid Excel file.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()