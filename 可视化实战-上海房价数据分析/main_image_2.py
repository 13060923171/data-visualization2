from pyecharts.components import Image
from pyecharts.options import ComponentTitleOpts

def main_image_2():
    image = Image()
    img_src = (
        "2.png"
    )
    image.add(
        src=img_src,
    )
    return image
