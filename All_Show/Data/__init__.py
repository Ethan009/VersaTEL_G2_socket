# coding:utf-8
'''
Created on 2020/1/5
@author: Paul
@note: data post
'''
from flask import Flask,Blueprint

datablue = Blueprint("datablue", __name__)

# from . import views
from All_Show.Data import views