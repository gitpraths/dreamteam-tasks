import os
import sys
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.errors import PdfReadError


def encrypt_pdfs(folder, password):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(".pdf") and not filename.endswith("_encrypted.pdf"):
                filepath = os.path.join(foldername, filename)

                try:
                    pdf_reader = PdfReader(filepath)
                    pdf_writer = PdfWriter()

                    for page in pdf_reader.pages:
                        pdf_writer.add_page(page)

                    pdf_writer.encrypt(password)
                    encrypted_filepath = filepath[:-4] + "_encrypted.pdf"

                    with open(encrypted_filepath, "wb") as output_file:
                        pdf_writer.write(output_file)

                    try:
                        verify_reader = PdfReader(encrypted_filepath)
                        verify_reader.decrypt(password)
                        os.remove(filepath)
                        print(f"Encrypted {filename} successfully.")
                    except (PdfReadError, OSError) as e:
                        print(
                            f"Encryption verification failed for {filename}: {str(e)}"
                        )
                        try:
                            os.remove(encrypted_filepath)
                        except OSError as e:
                            print(f"Error removing failed encrypted file: {str(e)}")

                except (PdfReadError, OSError, ValueError) as e:
                    print(f"Error encrypting {filename}: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdf_encryptor.py <folder> <password>")
        sys.exit(1)

    folder = sys.argv[1]
    password = sys.argv[2]

    if not os.path.exists(folder):
        print("Folder does not exist.")
        sys.exit(1)

    encrypt_pdfs(folder, password)
