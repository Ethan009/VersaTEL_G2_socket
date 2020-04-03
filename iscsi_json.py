# -*- coding: utf-8 -*-
import json

class JSON_Operation:

    def __init__(self):
        self.read_data = self.read_data_json()

    def read_data_json(self):
        rdata = open("iSCSI_Data.json")
        read_json_dict = json.load(rdata)
        rdata.close
        return read_json_dict

    #创建Host、Disk、Target、HostGroup、DiskGroup,Map
    def creat_data(self,first_key,data_key,data_value):
        self.read_data[first_key].update({data_key:data_value})
        with open('i.json', "w") as fw:
            json.dump(self.read_data, fw)

    #删除Host、Disk、Target，HostGroup、DiskGroup,Map
    def delete_data(self,first_key,data_key):
        self.read_data[first_key].pop(data_key)
        with open('i.json', "w") as fw:
            json.dump(self.read_data, fw)

    #获取Host,Disk、Target，HostGroup、DiskGroup,Map的信息
    def get_data(self,first_key):
        all_data = self.read_data[first_key]
        return all_data

    #检查key值是否存在
    def check_key(self,first_key,data_key):
    	if data_key in self.read_data[first_key]:
    		return True
    	else:
    		return False

    #检查value值是否存在
    def check_value(self,first_key,data_value):
    	for key in self.read_data[first_key]:
    		if data_value in self.read_data[first_key][key]:
    			return True
    	return False

        