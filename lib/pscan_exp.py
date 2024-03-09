from poc.ARL import *
import json

def exp_start(args):
    # ANSI转义序列，用于设置文本颜色
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RESET = '\033[0m'  # 用于重置颜色到默认

    poc_name = args.poc
    with open('./lib/pocnames.json', 'r', encoding='utf-8') as file:
        # 解码JSON文件内容为Python对象（列表）
        pocnames = json.load(file)
    for i in range(len(pocnames)):
        if str(pocnames[i][0]) == str(poc_name) or str(pocnames[i][1]) == str(poc_name):
                run_arl(args)
