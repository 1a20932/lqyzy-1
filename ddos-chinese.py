import requests
import random
import easygui
import requests #引入库


#开始进入Python的世界
# 输入url
URL = input('URL:')
print('由刘钦宇制作')
print('=========================================================================================')
print('[刘钦宇制作]不支持打开google,易报错')
print('=========================================================================================')
for __count in range(9999999):
    for __count in range(99999999):
        try:
            response = requests.get(URL)
            print('正常', random.randint(1, 100))
            print('=========================================================================================')
        except :
            # 警告
            print('404')
            print('=========================================================================================')
            easygui.msgbox('404', '404', 'Ok')
# 提示
print('完成！')
# 提示
easygui.msgbox('完成')