# coding:utf-8
'''
Created on 2020/3/2
@author: Paul
@note: data
'''

from flask import Flask, jsonify, render_template, request, make_response
from All_Show.Data import datablue

import json
from flask_cors import *
import Process
from iscsi_json import JSON_Operation

message_get_ll = None
global lvm

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
    configuration = JSON_Operation().read_data_json()
    response = make_response(jsonify(configuration))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@datablue.route('/socket', methods=['GET', 'POST'])  # 路由
def data_test():
    global lvm
    pc = Process.Process_data()
    print(pc.get_option_lvm())
    lvm = pc.get_option_lvm()
    #print(pc.get_option_sp())#FOR create resource
    
    return "response"


@datablue.route('/lvm', methods=['GET', 'POST'])  # 路由
def lvm():
    global lvm
    print(lvm);
    response = make_response(jsonify(lvm))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@datablue.route('/testthree', methods=['GET', 'POST'])  # 路由
def data_test_three():
    data_test_three = [{'NodeName': 'Node1',
                    'Spool': [{'device_name': '1'},
                             {'device_name': '2'},
                             {'device_name': '3'},
                             {'device_name': '4'}]
                  },
                  {'NodeName': 'Node2',
                  'Spool': [{'device_name': '5'},
                            { 'device_name': '6'},
                             {'device_name': '7'},
                             {'device_name': '8'}]
                }]
    
    #     data_test_three = {
#                     'Node1': {'device_name': '1',
#                               'device_name': '2',
#                               'device_name': '3',
#                               'device_name': '4',
#                               'device_name': '5'},
#                     'Node2': {'device_name': '5',
#                             'device_name': '6',
#                              'device_name': '7',
#                              'device_name': '8'}}
    
    
    
    response = make_response(jsonify(data_test_three))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

##############################
# -------------------------


@datablue.route('/data_iqn_alias_all', methods=['GET', 'POST'])  # 路由
def iqn_alias_all1():
    iqn_alias_all = "111"
    response = make_response(jsonify(iqn_alias_all))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@datablue.route('/data_target_alias_all', methods=['GET', 'POST'])  # 路由
def target_alias_all1():
    target_alias_all = "sss"
    response = make_response(jsonify(target_alias_all))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@datablue.route('/data_ig_all', methods=['GET', 'POST'])  # 路由
def ig_all1():
    ig_all = "sss"
    response = make_response(jsonify(ig_all))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response
# ----------------------------------

