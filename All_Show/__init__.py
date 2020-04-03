# coding:utf-8
'''
Created on 2020/3/2
@author: Paul
@note: data post
'''

from flask import Flask, Blueprint

from Data import datablue
from Show import showblue
from Interaction import interaction_blue

app = Flask(__name__)

# 将蓝图注册到app
app.register_blueprint(datablue)
app.register_blueprint(showblue)
app.register_blueprint(interaction_blue)
