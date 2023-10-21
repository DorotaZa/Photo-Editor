from PIL import Image, ImageEnhance, ImageFilter
import os

path = './images'
pathOut = '/editedImages'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.BLUR).rotate(-90)

    edit = img.filter(ImageEnhance.BLUR).rotate(-90)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
