from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from PIL import Image
import glob
# List of png images
images = sorted(glob.glob('*.png'))#[0:2]




from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from PIL import Image

# List of png images
# images = ["image1.png", "image2.png", "image3.png"]

# Set the width and height of the PDF
pdf_width, pdf_height = landscape(letter)

c = canvas.Canvas("output.pdf", pagesize=(pdf_width, pdf_height))

for image in images:
    img = Image.open(image)
    # Get the dimensions of the image
    img_width, img_height = img.size
    # Calculate the scale ratios for width and height
    width_ratio = pdf_width / img_width
    height_ratio = pdf_height / img_height
    # Use the smaller ratio to ensure the entire image fits on the canvas
    scale_ratio = min(width_ratio, height_ratio)
    # Calculate the scaled dimensions
    scaled_width = img_width * scale_ratio
    scaled_height = img_height * scale_ratio
    # Calculate the position to center the image on the canvas
    x_pos = (pdf_width - scaled_width) / 2
    y_pos = pdf_height  - (pdf_height - scaled_height) / 2 - scaled_height
    # Draw the image on the canvas, scaled and centered
    # c.drawImage(image, x_pos, y_pos, width=scaled_width, height=scaled_height)
    c.drawImage(image, 0, 160, width=scaled_width, height=scaled_height)
    c.showPage()

c.save()