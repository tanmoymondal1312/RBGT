from rembg import remove
from PIL import Image
import numpy as np
import os
import uuid
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def remove_background(image_name):
    input_img_path = r"C:\DJANGOOOOOOOOOOOOOO\MY PORTFOLIO WITH DJANGO TEMPLATES\RBGT\media\images\\" + image_name
    img = Image.open(input_img_path)
    img_array = np.array(img)
    result = remove(img_array)
    unique_name = "rbgt" + str(uuid.uuid4())[:8]
    output_folder = r"C:\DJANGOOOOOOOOOOOOOO\MY PORTFOLIO WITH DJANGO TEMPLATES\RBGT\media\bg_removed_images"
    output_img_path = os.path.join(output_folder, f"{unique_name}.png")
    with default_storage.open(output_img_path, 'wb') as file:
        processed_image = Image.fromarray(result)
        processed_image.save(file, format='PNG')
    return output_img_path
