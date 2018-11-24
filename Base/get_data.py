import os, yaml

class Get_Data:
    def __init__(self):
        pass
    def get_yaml_data(self, file_name):
        """返回yaml文件数据"""
        with open("./Data"+ os.sep + file_name, "r") as f:
            return yaml.load(f)