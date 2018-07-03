#coding=utf-8
import hashlib
from urllib import parse
import random
import requests

"""
language
auto 自动检测
zh  中文
en  英语
yue 粤语
wyw 文言文
jp  日语
kor 韩语
fra 法语
spa 西班牙语
th  泰语
ara 阿拉伯语
ru  俄语
pt  葡萄牙语
de  德语
it  意大利语
el  希腊语
nl  荷兰语
pl  波兰语
bul 保加利亚语
est 爱沙尼亚语
dan 丹麦语
fin 芬兰语
cs  捷克语
rom 罗马尼亚语
slo 斯洛文尼亚语
swe 瑞典语
hu  匈牙利语
cht 繁体中文
vie 越南语
"""

class baiduTranslate(object):

    def __init__(self, from_lang, to_lang):
        self.appid = ''
        self.secretKey = ''
        self.host = 'http://api.fanyi.baidu.com/api/trans/vip/translate?appid={appid}&q={query}&from={from_lang}&to={to_lang}&salt={salt}&sign={sign}'
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.salt = random.randint(32768, 65536)


    def run(self, query):
        sign = self.appid + query + str(self.salt) + self.secretKey
        m1 = hashlib.md5()
        m1.update(sign.encode(encoding='utf-8'))
        sign = m1.hexdigest()
        post_url = self.host.format(
            appid=self.appid,
            query=query,
            from_lang=self.from_lang,
            to_lang=self.to_lang,
            salt=self.salt,
            sign=sign
        )
        try:
            respose = requests.post(post_url)
            res = eval(respose.content)
            return {'is_error':False, 'data': res['trans_result']}
        except Exception as e:
            print(e)
            return {'is_error': True, 'data':None}


if __name__ == '__main__':
    transale = baiduTranslate('en', 'zh')

    print(transale.run('I am the best!\nOK,I will be back later!\nNOxuuessf'))