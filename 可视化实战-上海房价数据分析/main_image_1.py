from pyecharts.components import Image
from pyecharts.options import ComponentTitleOpts

def main_image_1():
    image = Image()
    img_src = (
        "1.png"
    )
    image.add(
        src=img_src,
    )
    return image
