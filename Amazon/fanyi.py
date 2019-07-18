# coding=utf
"""
author=Hui_T
"""
import time

from googletrans import Translator

translator = Translator(service_urls=['translate.google.cn'])
# s = 'hello world 空'
# print(translator.translate(s,dest='zh-CN').text)

with open('./data/data.csv', 'r', encoding='utf8') as f, open('./data/data(翻译).csv', 'w', encoding='utf8')as f2:
    for line in f:
        print(line)
        res = translator.translate(line,dest="zh-CN").text
        time.sleep(1)
        f2.write(res)
        f2.write('\n')
        print(res)
