import pytest
import yaml


def read_yaml():
    """
    读取yaml文件
    :return:
    """
    with open('test_api.yaml', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data

# def write_yaml():
#   with open(str())


"""def read_yaml_login():
    
    读取登陆用户名和密码信息
    :return:
    
    with open('test_login.yaml', encoding='utf-8') as l:
        date = yaml.load(l, Loader=yaml.FullLoader)
        return date


if __name__ == '__main__':
    pytest.main(['-vs', 'yaml.util.py'])"""
