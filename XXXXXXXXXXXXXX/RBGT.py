from rembg import remove
from PIL import Image
import numpy as np

img = Image.open("C:\DJANGOOOOOOOOOOOOOO\\MY PORTFOLIO WITH DJANGO TEMPLATES\\RBGT\\media\\images\\{}")
img_array = np.array(img)
result = remove(img_array)
R = Image.fromarray(result)
R.save("img2.png")
