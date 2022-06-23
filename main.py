from PIL import Image, ImageDraw, ImageFont
from rich import print
import string
import os


def create_im(sign):
    with Image.new('RGB', (100, 100)) as im:
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("/usr/share/fonts/liberation-mono/LiberationMono-Regular.ttf", size=100)
        draw.text((0, 0),sign, font=font)
        return im

def get_brightness(im):
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

if __name__ == "__main__":
    #signs = string.printable
    #for sign in signs:
        #im = create_im(sign)
        #brightness = get_brightness(im)
        #print(f"{sign}: {brightness:.2f}%")

    font = ImageFont.truetype("/usr/share/fonts/google-roboto/Roboto-Regular.ttf", size=100)
    signs = string.printable
    for sign in signs:
        print(sign, font.getsize(sign))
