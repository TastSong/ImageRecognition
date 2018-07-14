import base64
import hashlib
import time
import random
import string
from urllib.parse import quote
import requests
import os


def curlmd5(src):
    m = hashlib.md5(src.encode('UTF-8'))
    return m.hexdigest().upper()


# 请求时间戳（秒级），用于防止请求重放（保证签名5分钟有效）
def get_params(base64_data):
    t = time.time()
    time_stamp = str(int(t))
    # 请求随机字符串，用于保证签名不可预测
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    # 应用标志，这里修改成自己的id和key
    app_id = '1107044144'
    app_key = '8461m2qsOhX7o4Hq'
    params = {'app_id': app_id,
              'image': base64_data,
              'time_stamp': time_stamp,
              'nonce_str': nonce_str,
              }
    sign_before = ''
    # 要对key排序再拼接
    for key in sorted(params):
        # 键值拼接过程value部分需要URL编码，URL编码算法用大写字母，例如%E8。quote默认大写。
        sign_before += '{}={}&'.format(key, quote(params[key], safe=''))
    # 将应用密钥以app_key为键名，拼接到字符串sign_before末尾
    sign_before += 'app_key={}'.format(app_key)
    # 对字符串sign_before进行MD5运算，得到接口请求签名
    sign = curlmd5(sign_before)
    params['sign'] = sign
    return params
#腾讯AI接口地址（通用OCR）
url = "https://api.ai.qq.com/fcgi-bin/ocr/ocr_generalocr"

#统计文件夹中有多少图片
imgFileNameF = 'C:/Users/10071/Desktop/Python/ImageRecognition/img'
imgNum = len([name for name in os.listdir(imgFileNameF) if os.path.isfile(os.path.join(imgFileNameF, name))])

#依次读入图片

for i in range(imgNum):
    imgFileName = './img/' + str(i) + '.jpg'
    print(imgFileName)
    #传送给腾讯AI接口
    with open(imgFileName, 'rb') as imgFile:
        image_data = imgFile.read()
    base64_data = base64.b64encode(image_data)
    params = get_params(base64_data)
    r = requests.post(url, data=params)
    item_list = r.json()['data']['item_list']

    #内容写入TXT
    with open('data.txt','a') as f:
        for s in item_list:
            f.write(s['itemstring'] + "\n")
            print(s['itemstring'])
    f.close()
    imgFile.close()