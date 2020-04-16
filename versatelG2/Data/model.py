# coding:utf-8
'''
Created on 2020/3/2
@author: Paul
@note: data
'''

from flask import Flask, jsonify, render_template, request, make_response,views
import VersaTELSocket as vst
import json
from flask_cors import *
import Process


def data(datadict):
    response = make_response(jsonify(datadict))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

class nodeView(views.MethodView):
    def get(self):
        pc = Process.Process_data()
        nodedict = pc.process_data_node()
        return data(nodedict)
    
class resourceView(views.MethodView):  
    def get(self):
        pc = Process.Process_data()
        resourcedict = pc.process_data_resource()
        return data(resourcedict)
    
class storagepoolView(views.MethodView):  
    def get(self):
        pc = Process.Process_data()
        spdict = pc.process_data_stp()
        return data(spdict)
    
class iSCSIView(views.MethodView):  
    def get(self):
        str_cmd = "python3 vtel_iscsi.py iscsi show js" 
        str_cmd = str_cmd.encode()
        CLI_result = vst.conn(str_cmd)
        return data(CLI_result)

datalist=[]
class LINSTORView(views.MethodView):
    def get(self):
        pc = Process.Process_data()
        lvm = pc.get_option_lvm()
        sp = pc.get_option_sp()
        node_create = pc.get_option_node()
        node_num = pc.get_option_nodenum()
        datalist = [lvm,sp,node_create,node_num]
        return 'Test'

class lvmView(views.MethodView):  
    def get(self):
        return data(datalist[0])
 
class spView(views.MethodView):  
    def get(self):
        return data(datalist[1])
    
class nodecreateView(views.MethodView):  
    def get(self):
        return data(datalist[2])

class nodenumView(views.MethodView):  
    def get(self):
        return data(datalist[3])
   
    
