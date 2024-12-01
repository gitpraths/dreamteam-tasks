import os
import sys
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.errors import PdfReadError


def decrypt_pdfs(folder, password):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith("_encrypted.pdf"):
                filepath = os.path.join(foldername, filename)

                try:
                    pdf_reader = PdfReader(filepath)

                    if pdf_reader.decrypt(password) == 0:
                        print(f"Wrong password for {filename}")
                        continue

                    pdf_writer = PdfWriter()

                    for page in pdf_reader.pages:
                        pdf_writer.add_page(page)

                    decrypted_filepath = filepath[:-14] + "_decrypted.pdf"
                    with open(decrypted_filepath, "wb") as output_file:
                        pdf_writer.write(output_file)

                    print(f"Decrypted {filename} successfully.")

                except (PdfReadError, OSError) as e:
                    print(f"Error decrypting {filename}: {str(e)}")
                except ValueError as e:
                    print(f"Invalid PDF format in {filename}: {str(e)}")
                except PermissionError as e:
                    print(f"Permission denied accessing {filename}: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdf_decryptor.py <folder> <password>")
        sys.exit(1)

    folder = sys.argv[1]
    password = sys.argv[2]

    if not os.path.exists(folder):
        print("Folder does not exist.")
        sys.exit(1)

    decrypt_pdfs(folder, password)
