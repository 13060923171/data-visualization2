from pyecharts.components import Image
from pyecharts.options import ComponentTitleOpts


def main_image():
    image = Image()
    img_src = (
        "女性角色.png"
    )
    image.add(
        src=img_src,
    )
    image.set_global_opts(
        title_opts=ComponentTitleOpts(title="女性在社会中所担当的主要角色")
    )
    return image
