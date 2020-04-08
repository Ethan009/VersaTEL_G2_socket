# coding:utf-8
'''
Created on 2020/3/2
@author: Paul
@note: data
'''

from flask import Flask, jsonify, render_template, request, make_response
from All_Show.Data import datablue
import VersaTELSocket as vst
import json
from flask_cors import *
import Process
from iscsi_json import JSON_Operation

message_get_ll = None
global lvm 
global sp
global node_create
global node_num


@datablue.route('/node', methods=['GET', 'POST'])  # 路由
def data_two():
# 
    pc = Process.Process_data()
    data_two_lict = pc.process_data_node()
    
    response = make_response(jsonify(data_two_lict))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@datablue.route('/resource', methods=['GET', 'POST'])  # 路由
def data_three():
    # import LINSTORDB as db
    pc = Process.Process_data()
    data_three_lict = pc.process_data_resource()
    response = make_response(jsonify(data_three_lict))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@datablue.route('/storagepool', methods=['GET', 'POST'])  # 路由
def data_four():
    pc = Process.Process_data()
    data_four_lict = pc.process_data_stp()
    response = make_response(jsonify(data_four_lict))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@datablue.route('/configuration_data', methods=['GET', 'POST'])  # 路由
def data_configuration():
    
    str_cmd = "python3 vtel_iscsi.py iscsi show js" 
    str_cmd = str_cmd.encode()
    CLI_result = vst.conn(str_cmd)
    print("CLI_result:",CLI_result)
    response = make_response(jsonify(CLI_result))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@datablue.route('/socket', methods=['GET', 'POST'])  # 路由
def data_test():
    global lvm
    global node_create
    global sp
    global node_num
    pc = Process.Process_data()
   # print('1:',pc.get_option_lvm())
    lvm = pc.get_option_lvm()
    node_create = pc.get_option_node()
    # print("node_create:",node_create);
    sp = pc.get_option_sp()
    # print("sp:",sp)
    # node_num = pc.get_option_nodenum()
    # print(pc.get_option_sp())#FOR create resource
    node_num = pc.get_option_nodenum()
    return "response"


@datablue.route('/lvm', methods=['GET', 'POST'])  # 路由
def lvm():
    global lvm
    response = make_response(jsonify(lvm))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@datablue.route('/sp', methods=['GET', 'POST'])  # 路由
def sp():
    # global node
    global sp
    response = make_response(jsonify(sp))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@datablue.route('/node_create', methods=['GET', 'POST'])  # 路由
def node_create():
    global node_create
    response = make_response(jsonify(node_create))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@datablue.route('/node_num', methods=['GET', 'POST'])  # 路由
def node_num():
    global node_num
    response = make_response(jsonify(node_num))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

##############################
#

