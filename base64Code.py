import base64
import re


def encode_base64(file, code=True):
    with open(file, 'rb') as f:
        img_data = f.read()
        base64_img = base64.b64encode(img_data)
        base64_str = 'data:image/jpeg;base64,' + str(base64_img, 'utf-8')
        if code:
            return str(base64_img, 'utf-8')
        else:
            return base64_str


def decode_base64(base64_img, save_img=False):
    re_img = re.findall('data:image/jpeg;base64,(.+?)$', base64_img)[0]
    img = base64.b64decode(re_img)
    if save_img:
        with open('base64.jpg', 'wb') as f:
            f.write(img)
    return img


if __name__ == '__main__':
    en_base64 = encode_base64('PFfr.png')
    print(en_base64)

