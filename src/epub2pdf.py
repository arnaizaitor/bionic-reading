import argparse
import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

class Epub2PdfConverter:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def clean_html(self, html_content):
        # Use BeautifulSoup to parse and clean the HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Modify or remove problematic elements/attributes here if needed
        # For example, you can remove all 'id' attributes
        for tag in soup.find_all():
            del tag['id']

        # Remove or replace the 'class' attribute in all tags
        for tag in soup.find_all():
            if 'class' in tag.attrs:
                del tag['class']  # Remove the 'class' attribute

        # Remove the 'style' attribute in all tags
        for tag in soup.find_all():
            if 'style' in tag.attrs:
                del tag['style']  # Remove the 'style' attribute

        # TODO: Before removing all images, insert a page break before each image <br style="page-break-after:always">
        # Find and remove all <img> tags
        for img_tag in soup.find_all('img'):
            img_tag.extract()  # Remove the <img> tag

        # Find all <p> tags and add a <br/> tag after each one
        for paragraph_tag in soup.find_all('p'):
            br_tag1 = soup.new_tag('br')
            br_tag2 = soup.new_tag('br')
            paragraph_tag.insert_after(br_tag1)
            paragraph_tag.insert_after(br_tag2)

        # Return the cleaned HTML as a string
        return str(soup)

    def convert(self):
        print(f'Converting {self.input_file_path} to {self.output_file_path}...')

        # Open the EPUB file
        book = epub.read_epub(self.input_file_path)

        # Create a PDF document
        pdf_document = SimpleDocTemplate(self.output_file_path, pagesize=letter)

        # Create a list to hold the PDF content
        pdf_content = []

        # Define the styles for paragraphs
        styles = getSampleStyleSheet()
        normal_style = styles['Normal']

        # Iterate through the items in the EPUB book
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                # Extract the content and CSS from the EPUB item
                content = item.get_body_content()
                cleaned_html = self.clean_html(content)

                # Create a PDF paragraph with the cleaned HTML content
                paragraph = Paragraph(cleaned_html, normal_style)
                pdf_content.append(paragraph)
                pdf_content.append(Spacer(1, 12))  # Add spacing between paragraphs

        # Build the PDF document
        pdf_document.build(pdf_content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='path to the input epub file')
    parser.add_argument('--output', help='path to the output pdf file')
    args = parser.parse_args()
    # Retrieve input and output paths as args using argparse
    input_file_path = args.input
    output_file_path = args.output
    # then pass them to the converter
    converter = Epub2PdfConverter(input_file_path, output_file_path)
    converter.convert()
