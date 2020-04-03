# coding:utf-8
'''
Created on 2020/1/5
@author: Paul
'''
{"Disk": 
      {"DiskA": "/dev/000000",
       "DiskB": "/dev/000000",
       "DiskC": "/dev/000000",
       "DiskD": "/dev/000000",
  "DiskGroup": {
             "DiskGroup1": ["DiskA", "DiskB"],
              "DiskGroup2": ["DiskC", "DiskD"], "tdg": ["td"]},
  "Host": {"HostA": "iqn.xxxx",
               "HostB": "iqn.xxxx",
               "HostC": "iqn.xxxx",
               "HostD": "iqn.xxxx",
               "HostE": "onsin",
               "hostzane": "iqnname",
               "dog": "isdog", "th": 
               "testhost", "h1": "h11111"},
  "HostGroup": {"HostGroup1": ["HostA", "HostB"],
                  "HostGroup2": ["HostC", "HostD"], "thg": ["th"]},
  "Map": {"Map2": ["HostGroup2", "DiskGroup2"],
          "m111": ["HostGroup1", "DiskGroup1"],
          "tmp": ["thg", "tdg"]},
  "Target": {"Target1": "iqn.xxx",
               "Target2": "iqn.xxx",
                "Target3": "iqn.xxx",
                "Target4": "iqn.xxx"},


