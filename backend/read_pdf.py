import sys
import PyPDF2

def extract_pdf_info(file_path):
    print(f"Reading {file_path}")
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            print(f"Number of Pages: {len(reader.pages)}")
            for i, page in enumerate(reader.pages):
                print(f"--- Page {i+1} ---")
                print(page.extract_text())
                # Read all pages
    except Exception as e:
        print(f"Error reading PDF: {e}")

if __name__ == "__main__":
    extract_pdf_info(sys.argv[1])
