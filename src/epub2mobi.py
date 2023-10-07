import subprocess
import sys

def convert_epub_to_mobi(input_file, output_file):
    try:
        # Use ebook-convert command to convert EPUB to MOBI
        subprocess.run(['ebook-convert', input_file, output_file])
        print(f"Conversion completed. Output saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_epub_to_mobi.py input.epub output.mobi")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_epub_to_mobi(input_file, output_file)
