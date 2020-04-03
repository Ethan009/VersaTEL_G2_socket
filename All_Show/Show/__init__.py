# coding:utf-8

'''
Created on 2020/3/2
@author: Paul
@note: data
'''

from flask import Flask,Blueprint

showblue = Blueprint("showblue", __name__)

from All_Show.Show import views