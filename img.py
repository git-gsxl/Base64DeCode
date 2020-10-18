import base64
import requests
from jsonpath import jsonpath


def img_decode(en64_img, save_img=False, dic_words='words'):
    # todo 获取百度ai的access_token
    token_url = 'https://aip.baidubce.com' \
                '/oauth/2.0/token?grant_type=client_credentials&' \
                'client_id=GOMMIBuWOO8oWNfOI9fRjjHV&client_secret=VplG3PsATgoDww7MMzzdf3cB4GA1p6CN'
    response = requests.get(token_url)
    access_token = response.json().get('access_token')

    # todo 把图片base64值发给百度识别
    params = {'image': en64_img}
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=%s' % access_token
    response = requests.post(url, data=params)
    words = None
    if response:
        result = response.json()
        words = jsonpath(result, '$..%s' % dic_words)[0]     # todo 最终识别出来的字符
        if save_img:
            filename = words + '.jpg'                        # todo 将识别的字符保存在本地
            with open(filename, 'wb') as f:
                f.write(base64.b64decode(en64_img))
    return words


if __name__ == '__main__':
    import base64Code
    en64 = base64Code.encode_base64('PFfr.png')
    print(img_decode(en64, True))
