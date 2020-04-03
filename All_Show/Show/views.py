# coding:utf-8
'''
Created on 2020/3/2
@author: Paul
@note: data
'''

from flask import Flask, jsonify, render_template, request, make_response
import json
from flask_cors import *
from All_Show.Show import showblue


@showblue.route('/', methods=['GET', 'POST'])
def INDEX():
    
    return render_template("index.html")


@showblue.route('/iSCSI_create', methods=['GET', 'POST'])
def iSCSI_CREATE():
    return render_template("iSCSI_create.html")


@showblue.route('/LINSTOR_create', methods=['GET', 'POST'])
def LINSTOR_CREATE():
    return render_template("LINSTOR_create.html")


@showblue.route('/show', methods=['GET', 'POST'])
def SHOW():
    return render_template("show.html")


# 第一阶段网页
@showblue.route('/Node', methods=['GET', 'POST'])
def Node():
    return render_template("Node.html")


# 第一阶段网页
@showblue.route('/Resource', methods=['GET', 'POST'])
def Resource():
    return render_template("Resource.html")


# 第一阶段网页
@showblue.route('/StoragePool', methods=['GET', 'POST'])
def StoragePool():
    return render_template("StoragePool.html")


# 第一阶段网页
@showblue.route('/iSCSI_Resource', methods=['GET', 'POST'])
def iSCSI_Resource():
    return render_template("iSCSI_Resource.html")

# 第一阶段网页
@showblue.route('/Configuration', methods=['GET', 'POST'])
def Configuration():
    return render_template("Configuration.html")
