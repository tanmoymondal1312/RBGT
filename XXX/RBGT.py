from rembg import remove
from PIL import Image
import numpy as np
import os
import uuid

def remove_background(image_name):
    # Construct the full path to the input image using the provided image name
    input_img_path = r"C:\DJANGOOOOOOOOOOOOOO\MY PORTFOLIO WITH DJANGO TEMPLATES\RBGT\media\images\\" + image_name

    # Open the input image using PIL
    img = Image.open(input_img_path)

    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Remove the background using the rembg library
    result = remove(img_array)

    # Generate a unique name starting with "rbgt"
    unique_name = "rbgt" + str(uuid.uuid4())[:8]

    # Construct the full path to the output image in the 'bg_removed_images' folder
    output_folder = r"C:\DJANGOOOOOOOOOOOOOO\MY PORTFOLIO WITH DJANGO TEMPLATES\RBGT\media\bg_removed_images"
    output_img_path = os.path.join(output_folder, f"{unique_name}.png")

    # Create a PIL image from the resulting NumPy array
    processed_image = Image.fromarray(result)

    # Save the processed image with a unique name in the specified folder
    processed_image.save(output_img_path)

