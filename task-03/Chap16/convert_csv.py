import os
import csv
import openpyxl

def excel_to_csv():
    for excel_file in os.listdir("."):
        if excel_file.endswith(".xlsx") or excel_file.endswith(".xlsm"):
            base_filename = os.path.splitext(excel_file)[0]

            wb = openpyxl.load_workbook(excel_file)

            for sheet in wb.sheetnames:
                ws = wb[sheet]

                csv_filename = f"{base_filename}_{sheet}.csv"

                with open(csv_filename, "w", newline="") as csv_file:
                    csv_writer = csv.writer(csv_file)

                    for row in ws.rows:
                        csv_writer.writerow([cell.value for cell in row])

                print(f"Converted {excel_file} - {sheet} to {csv_filename}")
                
if __name__ == "__main__":
    excel_to_csv()
