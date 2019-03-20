
import os
import yaml

# 当前文件的路径  (D:/python-lib/ThirdLib)
filePath = os.path.dirname(__file__)
print(filePath)

#  获取当前文件的Realpath (D:\python-lib\ThirdLib)
fileNamePath = os.path.split(os.path.realpath(__file__))[0]
print(fileNamePath)

# yaml file
yaml_path = os.path.join(fileNamePath, 'test_config.yaml')


def read_yaml():
    with open(yaml_path, 'r', encoding='utf-8') as f:
        content = f.read()
    data = yaml.load(content) # data:<class 'dict'>
    print(data['server'])
    print(type(data['server']))
    print(data['server']['port'])
    print(data.get('server').get('port'))
    pass


def add_config():
    # 追加
    fw = open(yaml_path, 'a', encoding='utf-8')
    # 构建数据
    data = {
        "cookie1": {'domain': '.yiyao.cc', 'expiry': 1521558688.480118, 'httpOnly': False, 'name': '_ui_', 'path': '/',
                    'secure': False, 'value': 'HSX9fJjjCIImOJoPUkv/QA=='}}
    # 装载数据
    yaml.dump(data, fw)
    fw.close()


if __name__ == "__main__":
    read_yaml()
    add_config()

