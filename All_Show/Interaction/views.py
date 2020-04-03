# coding:utf-8

from flask import Flask, jsonify, render_template, request, make_response, Blueprint
from All_Show.Interaction import interaction_blue
import VersaTELSocket as vst
import json
from flask_cors import *

import sys

sys.path.append("../")
from All_Show import Models


@interaction_blue.route('/send_message', methods=['GET'])
def send_message():
    Host_create = ['Host_Name', 'Host_iqn']
    HostGroup_create = ['HostGroup_Name', 'Host']
    DiskGroup_create = ['DiskGroup_Name', 'Disk']
    Map_create = ['Map_Name', 'Disk_Group', 'Host_Group']
    data_dict = {}
    # 键值对
    if request.method == 'GET':
        data_all = request.args.items()
        print("data_all:", data_all)
        for i in data_all:
            data_one_dict = {i[0]:i[1]}
            data_dict.update(data_one_dict)
        print(data_dict)
        return "tesy"
    else:
        return "test"
        pass

    
@interaction_blue.route('/LINSTOR_message', methods=['GET'])
def LINSTOR_message():
    Node = ['Node_Name', 'IP', 'Node_Type']
    Storage_pool = ['SP_Name', 'Node_One_Text', 'lvm_name','lv_Text']
    
    if request.method == 'GET':
        data_all = request.args.items()
        print("data_all:", data_all)
    for i in data_all:
            data_one_dict = {i[0]:i[1]}
            data_dict.update(data_one_dict)
    for i in  data_dict:
        if i in Node:
            break
        if i in Storage_pool:
            print(data_dict.values()[0])
            print(data_dict.values()[1])
            print(data_dict.values()[2])
            print(data_dict.values()[3])
            
            #str_cmd = "python3 vtel.py stor sp c %s -n %s %s %s"%(sp,node,'-lvm','vg1')
            #sessage = vst.conn(str_cmd)
            
        return sessage
    else:
        return "test"
