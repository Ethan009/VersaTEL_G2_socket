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
#import Process
from iscsi_json import JSON_Operation

message_get_ll = None

vg = {'lvm':[{"cityName":"Node1"}, {"cityName":"Node2"}, {"cityName":"Node3"}, {"cityName":"Node4"}],
      'thin_lvm': [{"cityName":"Node1"}, {"cityName":"Node2"}, {"cityName":"Node3"}, {"cityName":"Node4"}]     
             }

node = {'code': 0,
 'count': 1000,
 'data': [{'addr': u'10.203.2.89:3366(PLAIN)',
           'node': u'klay1',
           'node_type': u'COMBINED',
           'res_num': '8',
           'res_num_son': [{'device_name': u'/dev/drbd1000',
                            'res_name': u'apple',
                            'size': u'12MiB',
                            'status': u'UpToDate',
                            'stp_name': u'pool_hdd',
                            'used': u'InUse'},
                           {'device_name': u'/dev/drbd1001',
                            'res_name': u'banana',
                            'size': u'12MiB',
                            'status': u'UpToDate',
                            'stp_name': u'pool_hdd',
                            'used': u'InUse'},
                           {'device_name': u'/dev/drbd1005',
                            'res_name': u'ben',
                            'size': u'12MiB',
                            'status': u'UpToDate',
                            'stp_name': u'pool_hdd',
                            'used': u'InUse'},
                           {'device_name': u'/dev/drbd1003',
                            'res_name': u'fred',
                            'size': u'12MiB',
                            'status': u'UpToDate',
                            'stp_name': u'pool_hdd',
                            'used': u'InUse'},
                           {'device_name': u'/dev/drbd1002',
                            'res_name': u'linstordb',
                            'size': u'252MiB',
                            'status': u'UpToDate',
                            'stp_name': u'pool_hdd',
                            'used': u'InUse'},
                           {'device_name': u'/dev/drbd1006',
                            'res_name': u'seven',
                            'size': u'12MiB',
                            'status': u'UpToDate',
                            'stp_name': u'pool_hdd',
                            'used': u'InUse'},
                           {'device_name': u'/dev/drbd1009',
                            'res_name': u'ssss',
                            'size': u'12MiB',
                            'status': u'UpToDate',
                            'stp_name': u'pool_hdd',
                            'used': u'Unused'},
                           {'device_name': u'/dev/drbd1004',
                            'res_name': u'test',
                            'size': u'10.00GiB',
                            'status': u'UpToDate',
                            'stp_name': u'pool_hdd',
                            'used': u'InUse'}],
           'status': u'UpToDate',
           'stp_num': '3'},
          {'addr': u'10.203.2.90:3366(PLAIN)',
           'node': u'klay2',
           'node_type': u'COMBINED',
           'res_num': '7',
           'res_num_son': [{'device_name': u'/dev/drbd1001',
                            'res_name': u'banana',
                            'size': u'12MiB',
                            'status': u'UpToDate',
                            'stp_name': u'pool_hdd',
                            'used': u'Unused'},
                           {'device_name': u'/dev/drbd1005',
                            'res_name': u'ben',
                            'size': u'12MiB',
                            'status': u'UpToDate',
                            'stp_name': u'pool_hdd',
                            'used': u'Unused'},
                           {'device_name': u'/dev/drbd1008',
                            'res_name': u'ddfl',
                            'size': u'',
                            'status': u'Diskless',
                            'stp_name': u'DfltDisklessStorPool',
                            'used': u'Unused'},
                           {'device_name': u'/dev/drbd1003',
                            'res_name': u'fred',
                            'size': u'12MiB',
                            'status': u'UpToDate',
                            'stp_name': u'pool_hdd',
                            'used': u'Unused'},
                           {'device_name': u'/dev/drbd1002',
                            'res_name': u'linstordb',
                            'size': u'252MiB',
                            'status': u'UpToDate',
                            'stp_name': u'pool_hdd',
                            'used': u'Unused'},
                           {'device_name': u'/dev/drbd1006',
                            'res_name': u'seven',
                            'size': u'12MiB',
                            'status': u'UpToDate',
                            'stp_name': u'pool_hdd',
                            'used': u'Unused'},
                           {'device_name': u'/dev/drbd1004',
                            'res_name': u'test',
                            'size': u'10.00GiB',
                            'status': u'UpToDate',
                            'stp_name': u'pool_hdd',
                            'used': u'Unused'}],
           'status': u'UpToDate',
           'stp_num': '1'}],
 'msg': ''}

resource = {'code': 0,
 'count': 1000,
 'data': [{'device_name': u'/dev/drbd1000',
           'mirror_way': 1,
           'mirror_way_son': [{'drbd_role': u'primary',
                               'node_name': u'klay1',
                               'status': u'UpToDate',
                               'stp_name': u'pool_hdd'}],
           'resource': u'apple',
           'size': u'12MiB',
           'used': u'InUse'},
          {'device_name': u'/dev/drbd1001',
           'mirror_way': 2,
           'mirror_way_son': [{'drbd_role': u'primary',
                               'node_name': u'klay1',
                               'status': u'UpToDate',
                               'stp_name': u'pool_hdd'},
                              {'drbd_role': u'secondary',
                               'node_name': u'klay2',
                               'status': u'UpToDate',
                               'stp_name': u'pool_hdd'}],
           'resource': u'banana',
           'size': u'12MiB',
           'used': u'InUse'},
          {'device_name': u'/dev/drbd1005',
           'mirror_way': 2,
           'mirror_way_son': [{'drbd_role': u'primary',
                               'node_name': u'klay1',
                               'status': u'UpToDate',
                               'stp_name': u'pool_hdd'},
                              {'drbd_role': u'secondary',
                               'node_name': u'klay2',
                               'status': u'UpToDate',
                               'stp_name': u'pool_hdd'}],
           'resource': u'ben',
           'size': u'12MiB',
           'used': u'InUse'},
          {'device_name': u'/dev/drbd1003',
           'mirror_way': 2,
           'mirror_way_son': [{'drbd_role': u'primary',
                               'node_name': u'klay1',
                               'status': u'UpToDate',
                               'stp_name': u'pool_hdd'},
                              {'drbd_role': u'secondary',
                               'node_name': u'klay2',
                               'status': u'UpToDate',
                               'stp_name': u'pool_hdd'}],
           'resource': u'fred',
           'size': u'12MiB',
           'used': u'InUse'},
          {'device_name': u'/dev/drbd1002',
           'mirror_way': 2,
           'mirror_way_son': [{'drbd_role': u'primary',
                               'node_name': u'klay1',
                               'status': u'UpToDate',
                               'stp_name': u'pool_hdd'},
                              {'drbd_role': u'secondary',
                               'node_name': u'klay2',
                               'status': u'UpToDate',
                               'stp_name': u'pool_hdd'}],
           'resource': u'linstordb',
           'size': u'252MiB',
           'used': u'InUse'},
          {'device_name': u'/dev/drbd1006',
           'mirror_way': 2,
           'mirror_way_son': [{'drbd_role': u'primary',
                               'node_name': u'klay1',
                               'status': u'UpToDate',
                               'stp_name': u'pool_hdd'},
                              {'drbd_role': u'secondary',
                               'node_name': u'klay2',
                               'status': u'UpToDate',
                               'stp_name': u'pool_hdd'}],
           'resource': u'seven',
           'size': u'12MiB',
           'used': u'InUse'},
          {'device_name': u'/dev/drbd1009',
           'mirror_way': 1,
           'mirror_way_son': [{'drbd_role': u'secondary',
                               'node_name': u'klay1',
                               'status': u'UpToDate',
                               'stp_name': u'pool_hdd'}],
           'resource': u'ssss',
           'size': u'12MiB',
           'used': u'Unused'},
          {'device_name': u'/dev/drbd1004',
           'mirror_way': 2,
           'mirror_way_son': [{'drbd_role': u'primary',
                               'node_name': u'klay1',
                               'status': u'UpToDate',
                               'stp_name': u'pool_hdd'},
                              {'drbd_role': u'secondary',
                               'node_name': u'klay2',
                               'status': u'UpToDate',
                               'stp_name': u'pool_hdd'}],
           'resource': u'test',
           'size': u'10.00GiB',
           'used': u'InUse'}],
 'msg': ''}

pool = {'code': 0,
 'count': 1000,
 'data': [{'driver': u'LVM',
           'free_size': u'19.68GiB',
           'node_name': u'klay1',
           'pool_name': u'linstor1',
           'res_name_son': [{'device_name': u'/dev/drbd1000',
                             'res_name': u'apple',
                             'size': u'12MiB',
                             'status': u'UpToDate',
                             'used': u'InUse'},
                            {'device_name': u'/dev/drbd1001',
                             'res_name': u'banana',
                             'size': u'12MiB',
                             'status': u'UpToDate',
                             'used': u'InUse'},
                            {'device_name': u'/dev/drbd1005',
                             'res_name': u'ben',
                             'size': u'12MiB',
                             'status': u'UpToDate',
                             'used': u'InUse'},
                            {'device_name': u'/dev/drbd1003',
                             'res_name': u'fred',
                             'size': u'12MiB',
                             'status': u'UpToDate',
                             'used': u'InUse'},
                            {'device_name': u'/dev/drbd1002',
                             'res_name': u'linstordb',
                             'size': u'252MiB',
                             'status': u'UpToDate',
                             'used': u'InUse'},
                            {'device_name': u'/dev/drbd1006',
                             'res_name': u'seven',
                             'size': u'12MiB',
                             'status': u'UpToDate',
                             'used': u'InUse'},
                            {'device_name': u'/dev/drbd1009',
                             'res_name': u'ssss',
                             'size': u'12MiB',
                             'status': u'UpToDate',
                             'used': u'Unused'},
                            {'device_name': u'/dev/drbd1004',
                             'res_name': u'test',
                             'size': u'10.00GiB',
                             'status': u'UpToDate',
                             'used': u'InUse'}],
           'res_num': '8',
           'snapshots': u'False',
           'status': u'UpToDate',
           'stp_name': u'pool_hdd',
           'total_size': u'29.99GiB'},
          {'driver': u'LVM',
           'free_size': u'9.70GiB',
           'node_name': u'klay2',
           'pool_name': u'linstor2',
           'res_name_son': [{'device_name': u'/dev/drbd1001',
                             'res_name': u'banana',
                             'size': u'12MiB',
                             'status': u'UpToDate',
                             'used': u'Unused'},
                            {'device_name': u'/dev/drbd1005',
                             'res_name': u'ben',
                             'size': u'12MiB',
                             'status': u'UpToDate',
                             'used': u'Unused'},
                            {'device_name': u'/dev/drbd1003',
                             'res_name': u'fred',
                             'size': u'12MiB',
                             'status': u'UpToDate',
                             'used': u'Unused'},
                            {'device_name': u'/dev/drbd1002',
                             'res_name': u'linstordb',
                             'size': u'252MiB',
                             'status': u'UpToDate',
                             'used': u'Unused'},
                            {'device_name': u'/dev/drbd1006',
                             'res_name': u'seven',
                             'size': u'12MiB',
                             'status': u'UpToDate',
                             'used': u'Unused'},
                            {'device_name': u'/dev/drbd1004',
                             'res_name': u'test',
                             'size': u'10.00GiB',
                             'status': u'UpToDate',
                             'used': u'Unused'}],
           'res_num': '6',
           'snapshots': u'False',
           'status': u'UpToDate',
           'stp_name': u'pool_hdd',
           'total_size': u'20.00GiB'},
          {'driver': u'LVM_THIN',
           'free_size': u'2.49GiB',
           'node_name': u'klay1',
           'pool_name': u'vg1/lvol1',
           'res_name_son': [],
           'res_num': '0',
           'snapshots': u'True',
           'status': u'Ok',
           'stp_name': u'poollvt',
           'total_size': u'2.49GiB'},
          {'driver': u'LVM',
           'free_size': u'2.25GiB',
           'node_name': u'klay1',
           'pool_name': u'vg1',
           'res_name_son': [],
           'res_num': '0',
           'snapshots': u'False',
           'status': u'Ok',
           'stp_name': u'poolvg1',
           'total_size': u'5.00GiB'}],
 'msg': ''}
##########
# configuration = {"Disk": {"DiskA": "/dev/000000",
#                       "DiskB": "/dev/000000",
#                       "DiskC": "/dev/000000",
#                       "DiskD": "/dev/000000",
#                       "td": "testdisk"},
#             "DiskGroup": {"DiskGroup1": ["DiskA", "DiskB"],
#                           "DiskGroup2": ["DiskC", "DiskD"], "tdg": ["td"]},
#   "Host": {"HostA": "iqn.xxxx",
#                "HostB": "iqn.xxxx",
#                "HostC": "iqn.xxxx",
#                "HostD": "iqn.xxxx",
#                "HostE": "onsin",
#                "hostzane": "iqnname",
#                "dog": "isdog", "th": 
#                "testhost", "h1": "h11111"},
#   "HostGroup": {"HostGroup1": ["HostA", "HostB"],
#                   "HostGroup2": ["HostC", "HostD"], "thg": ["th"]},
#   "Map": {"Map2": ["HostGroup2,HostGroup1", "DiskGroup2"],
#           "m111": ["HostGroup1", "DiskGroup1"],
#           "tmp": ["thg", "tdg"]}
#     }


@datablue.route('/node', methods=['GET', 'POST'])  # 路由
def data_two():
# 
#     pc = Process.Process_data()
#     data_two_lict = pc.process_data_node()
    
    response = make_response(jsonify(node))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@datablue.route('/resource', methods=['GET', 'POST'])  # 路由
def data_three():
    # import LINSTORDB as db
#     pc = Process.Process_data()
#     data_three_lict = pc.process_data_resource()
    response = make_response(jsonify(resource))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@datablue.route('/storagepool', methods=['GET', 'POST'])  # 路由
def data_four():
#     pc = Process.Process_data()
#     data_four_lict = pc.process_data_stp()
    response = make_response(jsonify(pool))
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


@datablue.route('/test', methods=['GET', 'POST'])  # 路由
def data_test():
    response = make_response(jsonify(vg))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@datablue.route('/testtwo', methods=['GET', 'POST'])  # 路由
def data_test_two():
    data_test_lict = [{"cityName":"Node_one"}, {"cityName":"Node_two"}, {"cityName":"Node_three"}, {"cityName":"Node_four"}]
    response = make_response(jsonify(data_test_lict))
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

