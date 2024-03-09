import os
import json

# 初始化poc
def Initialization_poc():
    # 标识 是否需要进行再次初始化
    Identification = ''
    for i in open('./lib/Initialization_n','r'):
        Identification = i
    # 初始化一个空列表来存储POC名称
    if Identification == "0":
        print('''\t\t🌸🌸🌸🌸🌸🌸\tpoc列表初始化开始\t🌸🌸🌸🌸🌸🌸
            ''')
        pocnames = []
        dir_path = './poc'
        # 初始化一个计数器
        index = 1
        for dirpath, dirnames, filenames in os.walk(dir_path):
            for filename in filenames:
                # 判断是否存在.py后缀且不包含__init__
                if filename.endswith('.py') and '__init__' not in filename:
                    # 获取不包含.py后缀的文件名
                    pocname = filename.replace('.py', '')
                    # 创建一个子列表，包含序号和POC名称
                    poc_entry = [index, pocname]
                    # 将子列表添加到主列表中
                    pocnames.append(poc_entry)
                    # 更新计数器
                    index += 1
        with open('./lib/pocnames.json', 'w', encoding='utf-8') as file:
            # 将列表转换为JSON格式并写入文件
            json.dump(pocnames, file, ensure_ascii=False, indent=4)
        Identification = '1'
        with open('./lib/Initialization_n', 'w', encoding='utf-8') as file:
            file.write(Identification)
    else:
        pass

def Reset_poc():
        Identification = '0'
        with open('./lib/Initialization_n', 'w', encoding='utf-8') as file:
            file.write(Identification)