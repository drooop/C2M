import os
import qrcode
from PIL import Image


def make_qrcode(data: object, save_path: object = 'src/default.png', border: object = 5, image_size: object = (1080, 1080), icon_path: object = '', factor: object = 3) -> object:
    # 生成二维码主体
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H, border=border)
    qr.add_data(data)  # 向二维码写入数据
    qr.make()
    qrcode_image = qr.make_image().resize(
        image_size, Image.ANTIALIAS).convert('RGBA')

    if icon_path:  # 在二维码中间贴上图标
        icon_size = int(image_size[0] / factor), int(image_size[1] / factor)
        icon = Image.open(icon_path).resize(
            icon_size, Image.ANTIALIAS).convert('RGBA')
        icon_margin = int(
            (image_size[0] - icon_size[0]) / 2), int((image_size[1] - icon_size[1]) / 2)
        mask = Image.new('RGBA', icon_size, color='white')
        qrcode_image.paste(mask, icon_margin, mask)
        qrcode_image.paste(icon, icon_margin, icon)

    # 保存二维码为文件
    if not os.path.isdir(os.path.dirname(save_path)):
        os.makedirs(os.path.dirname(save_path))
    qrcode_image.save(save_path)

    # 展示二维码图像
    qrcode_image.show()


if __name__ == '__main__':
    url = 'http://c2m.tq.yhlcps.com/#/super/eaac28c5-15e5-4486-b37e-e2281a7e31a6'
    make_qrcode(data=url, save_path='src/qr_telecom.png',
                icon_path='src/logo_china_telecom_with_border.png')
