import sys
import argparse
import subprocess

def convert_pdf_to_epub(input_file, output_file):
    # TODO: Check file extensions
    try:
        # Use ebook-convert command to convert PDF to EPUB
        subprocess.run(['ebook-convert', input_file, output_file])
        print(f"Conversion completed. Output saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_epub_to_mobi.py input.pdf output.epub")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_pdf_to_epub(input_file, output_file)
