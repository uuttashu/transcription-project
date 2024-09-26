#!/usr/bin/env python3

from PIL import Image
import pytesseract
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def read_text_from_image(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Use pytesseract to recognize text from the image
    text = pytesseract.image_to_string(image)

    return text

def save_text_to_pdf(text, pdf_filename):
    # Create a PDF file
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    
    # Set font and size for the text
    c.setFont("Helvetica", 16)

    # Split text into lines
    lines = text.split('\n')

    # Start position for writing text
    x = 100
    y = 750

    # Write each line of text to the PDF
    for line in lines:
        c.drawString(x, y, line)
        y -= 15  # Move to the next line
        if y < 50:
            c.showPage()  # If close to the bottom, start a new page
            y = 750  # Reset y position for the new page

    # Save the PDF file
    c.save()

    print(f"Text saved to {pdf_filename}")

def process_images_in_folder(folder_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            # Read text from the image
            image_path = os.path.join(folder_path, filename)
            text = read_text_from_image(image_path)

            # Create a PDF file with the same name as the image in the output folder
            pdf_filename = os.path.join(output_folder, os.path.splitext(filename)[0] + ".pdf")

            # Save the text to a PDF file
            save_text_to_pdf(text, pdf_filename)

def main():
    # Path to the folder containing images
    folder_path = "/home/vboxuser/Downloads"  # Change this to your folder path

    # Path to the output folder for PDF files
    output_folder = "/home/vboxuser"  # Change this to your output folder path

    # Process all images in the folder
    process_images_in_folder(folder_path, output_folder)

if _name_ == "_main_":
    main()
