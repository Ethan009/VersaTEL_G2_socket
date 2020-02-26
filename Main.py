# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request, make_response
import json
from flask_cors import *
import Process


app = Flask(__name__)  # 实例化app对象
CORS(app, resources=r'/*')  
message_get_ll = None

@app.route('/data_two', methods=['GET', 'POST'])  # 路由
def data_two():

    pc = Process.Process_data()
    data_two_lict = pc.process_data_node()
    response = make_response(jsonify(data_two_lict))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@app.route('/data_three', methods=['GET', 'POST'])  # 路由
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


@app.route('/data_four', methods=['GET', 'POST'])  # 路由
def data_four():
    pc = Process.Process_data()
    data_four_lict = pc.process_data_stp()
    response = make_response(jsonify(data_four_lict))
    # 这里是解决Flask文件数据跨域问题，重要包导入 pip install flask_cors
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response


@app.route('/', methods=['GET', 'POST'])
def INDEX():
    return render_template("index.html")

@app.route('/show', methods=['GET', 'POST'])
def SHOW():
        return render_template("show.html")
    
#第一阶段网页
@app.route('/Node', methods=['GET', 'POST'])
def Node():
        return render_template("Node.html")

#第一阶段网页
@app.route('/Resource', methods=['GET', 'POST'])
def Resource():
        return render_template("Resource.html")

#第一阶段网页
@app.route('/StoragePool', methods=['GET', 'POST'])
def StoragePool():
        return render_template("StoragePool.html")

#第一阶段网页
@app.route('/iSCSI_Resource', methods=['GET', 'POST'])
def iSCSI_Resource():
        return render_template("iSCSI_Resource.html")
  
  
if __name__ == '__main__':
  app.run(host='0.0.0.0',  # 任何ip都可以访问
      port=7777,  # 端口
      debug=True
      )
