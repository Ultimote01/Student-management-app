from PIL import Image, ImageTk,ImageDraw
from .helper import hexToDecimal

def create_transparent_image(width, height,colorv,opacity):
    # Create an RGBA image with a transparent background
    image = Image.new('RGBA', (width, height), (colorv[0], colorv[1], colorv[2], opacity))
    return image




def createTransparentImage(width,height,colorvalue,opacity):

    colorv=hexToDecimal(colorvalue)

    # Create a transparent image using PIL
    transparent_image = create_transparent_image(width,height,colorv,opacity)
    return ImageTk.PhotoImage(transparent_image)