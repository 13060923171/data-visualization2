from pyecharts.components import Image
from pyecharts.options import ComponentTitleOpts

def main_image_3():
    image = Image()
    img_src = (
        "3.png"
    )
    image.add(
        src=img_src,
    )
    return image
