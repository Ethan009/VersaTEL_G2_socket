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
    data = {}
    # 键值对
    if request.method == 'GET':
        data_all = request.args.items()
        print("data_all:", data_all)
        for i in data_all:
            data_one_dict = {i[0]:i[1]}
            data.update(data_one_dict)
        for i in  data.keys():
            if i in Host_create:
                str_cmd = "python3 vtel_iscsi.py iscsi host create %s %s -gui gui" % (data["Host_Name"], data["Host_iqn"])
                str_cmd = str_cmd.encode()
                CLI_result = vst.conn(str_cmd)
                break
            elif i in HostGroup_create:
                hostgroup = data['Host'].replace(',',' ')
                str_cmd = "python3 vtel_iscsi.py iscsi hostgroup create %s %s -gui gui" % (data["HostGroup_Name"], hostgroup)
                str_cmd = str_cmd.encode()
                CLI_result = vst.conn(str_cmd)
                break
            elif i in DiskGroup_create:
                diskgroup = data['Disk'].replace(',',' ')
                str_cmd = "python3 vtel_iscsi.py iscsi diskgroup create %s %s -gui gui" % (data["DiskGroup_Name"], diskgroup)
                str_cmd = str_cmd.encode()
                CLI_result = vst.conn(str_cmd)
                break
            elif i in Map_create:
                str_cmd = "python3 vtel_iscsi.py iscsi map create %s -hg %s -dg %s -gui gui" % (data["Map_Name"], data["Host_Group"], data["Disk_Group"])
                str_cmd = str_cmd.encode()
                CLI_result = vst.conn(str_cmd)
                break   
        return 'SUCCESS' if CLI_result == True else 'Failed'
    else:
        return "test"

    
@interaction_blue.route('/LINSTOR_message', methods=['GET'])
def LINSTOR_message():
    Node = ['Node_Name', 'IP', 'Node_Type_Test']
    Storage_pool = ['SP_Name', 'Node_One_Text', 'lvm_name', 'lv_Text']

    Resurce_auto = ['Resource_Name_two', 'size_two', 'select_two', 'Node_Num']
    data = {}
    if request.method == 'GET':
        data_all = request.args.items()
        for i in data_all:
            print(i);
           
            data_one_dict = {i[0]:i[1]}
            data.update(data_one_dict)
        for i in  data.keys():
            if i in Node:
                str_cmd = "python3 vtel.py stor n c %s -ip %s -nt %s -gui" % (data['Node_Name'], data['IP'], data['Node_Type_Test'])
                str_cmd = str_cmd.encode()
                CLI_result = vst.conn(str_cmd)
                break

            elif i in Storage_pool:
                str_cmd = "python3 vtel.py stor sp c %s -n %s %s %s -gui" % (data['SP_Name'], data['Node_One_Text'], data['lvm_name'], data['lv_Text'])
                str_cmd = str_cmd.encode()
                CLI_result = vst.conn(str_cmd)
                break
 
            elif i in Resurce_auto:
                str_cmd = "python3 vtel.py stor r c %s -s %s%s -a -num %d -gui" % (data['Resource_Name_two'], data['size_two'], data['select_two'], int(data['Node_Num']))
                str_cmd = str_cmd.encode()
                CLI_result = vst.conn(str_cmd)
                break

        return 'SUCCESS' if CLI_result == True else  CLI_result
            
    else:
        return "request failed"
