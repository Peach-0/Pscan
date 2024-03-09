import os
import json

def search_poc(args):
    # ANSI转义序列，用于设置文本颜色
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RESET = '\033[0m'  # 用于重置颜色到默认

    search_name = args.search
    with open('./lib/pocnames.json', 'r', encoding='utf-8') as file:
        # 解码JSON文件内容为Python对象（列表）
        pocnames = json.load(file)
    for i in range(len(pocnames)):
        if search_name in pocnames[i][1]:
            aaa = str(pocnames[i])
            print(aaa.replace(']','').replace(',','').replace('\'','').replace(' ','] -- ').replace(search_name,RED+search_name+RESET))