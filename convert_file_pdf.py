from pdf2docx import Converter
import os

def convert_pdf_to_docx(pdf_file, docx_file):
    try:
        # Konversi PDF ke DOCX
        cv = Converter(pdf_file)
        cv.convert(docx_file, start=0, end=None)  # start=0, end=None artinya konversi seluruh halaman
        cv.close()
        
        print(f"Konversi selesai! File disimpan sebagai: {docx_file}")
    
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Input file PDF
pdf_file = input("Masukkan path file PDF: ")
docx_file = os.path.splitext(pdf_file)[0] + ".docx"

convert_pdf_to_docx(pdf_file, docx_file)
