# coding:utf-8
'''
Created on 2020/3/2
@author: Paul
@note: data
'''

from flask import Flask, jsonify, render_template, request, make_response,views
from versatelG2.Data import datablue
import VersaTELSocket as vst
import json
from flask_cors import *
import Process
message_get_ll = None
global lvm 
global sp
global node_create
global node_num


def data(data_two_lict):
    response = make_response(jsonify(data_two_lict))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


class nodeView(views.MethodView):
    def get(self):
        pc = Process.Process_data()
        data_two_lict = pc.process_data_node()
        return data(data_two_lict)
    
class resourceView(views.MethodView):  
    def get(self):
        pc = Process.Process_data()
        data_three_lict = pc.process_data_resource()
        return data(data_two_lict)
    
    
