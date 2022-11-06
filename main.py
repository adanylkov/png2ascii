from PIL import Image, ImageDraw, ImageFont
from rich import print
import string
import os
import pickle

font = ImageFont.truetype("Roboto-Regular.ttf", size=100)
with open("char_brightness.json", mode="rb") as file:
    signs_brightness = pickle.load(file)
    signs_brightness[0] = ' '
signs_brightness = {
        0: ' ',
        5: '.',
        10: ',',
        20: 'x',
        35: '1',
        55: 'X',
        65: 'q',
        85: '@',
        }
    

def create_im(sign):
    width, heigth = font.getsize(sign)
    with Image.new('RGB', (width, heigth)) as im:
        draw = ImageDraw.Draw(im)
        draw.text((0, 0),sign, font=font)
        return im

def get_char_brightness(im):
    px = im.load()
    width, heigth = im.size
    colors = dict()
    if px:
        for y in range(heigth):
            for x in range(width):
                color = px[x, y]
                count = colors.get(color, 0)
                colors[color] = count + 1

    black_pixels = colors.get((0, 0, 0), 0)
    brightness = 100 - black_pixels / (width * heigth) * 100
    return brightness

def create_ascii_picture(file_name):

    ascii_array = []
    im = Image.open(file_name)
    im = im.resize((50,50))
    width, heigth = im.size
    im = im.resize((width, round(heigth * 0.6)))
    width, heigth = im.size
    px = im.load()
    if px:
        for y in range(heigth):
            row = []
            for x in range(width):
                pixel = px[x, y]
                pixel_brightness = get_pixel_brightness(pixel)
                row.append((get_nearest_char(pixel_brightness)))
            ascii_array.append(row)
    #print(len(ascii_array))
    for line in ascii_array:
        print(''.join(line))

def get_pixel_brightness(pixel):
    r, g, b, _ = pixel
    return (r / 2.55 + g / 2.55 + b / 2.55) / 3

def get_nearest_char(pixel_brightness):
    n = min(signs_brightness, key=lambda x:abs(x-pixel_brightness))
    return signs_brightness[n]

if __name__ == "__main__":
    #signs_brightness = {}
    #signs = string.printable
    #for sign in signs:
        #im = create_im(sign)
        #brightness = get_char_brightness(im)
        #signs_brightness[sign] = brightness
    #with open("char_brightness.json", mode="wb") as file:
        #pickle.dump(signs_brightness, file)
    #with open("char_brightness.json", mode="rb") as file:
        #signs_brightness = pickle.load(file)
        #print(signs_brightness)
    create_ascii_picture("test.png")
