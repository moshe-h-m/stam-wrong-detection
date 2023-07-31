


# a program that gets a image and detects the range of each hebrew letter in the image
# Path: getRange.py
from PIL import Image, ImageDraw



def draw_Image(img):
    draw = ImageDraw.Draw(img)
    draw.line((0,0) + img.size, fill=128)
    draw.line((0,img.size[1], img.size[0], 0), fill=128)
    del draw
    img.show()

def get_Image(filename):
    img = Image.open(filename)
    #img.show()
    return img

def show_Image(img):
    print(f' size:{img.size}, format: {img.format}, mode: {img.mode} \n image displayed')
    img.show()



def get_all_images(param):
    return None