# coding=utf
"""
author=Hui_T
"""
from googletrans import Translator

#实例化
translator = Translator(service_urls=['translate.google.cn'])

title = 'Today is a gooday'

title_alternative = translator.translate(title, dest='zh-CN').text

print(title_alternative )