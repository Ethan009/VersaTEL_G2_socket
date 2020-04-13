#coding:utf-8
import sqlite3
import VersaTELSocket as vst

class LINSTORDB():

    def __init__(self):
        self.con = sqlite3.connect(':memory:',check_same_thread=False)
        self.cur = self.con.cursor()
        self.drop_tb()
        b = vst.conn(b'python3 vtel.py stor gui -db')
        self.cur.executescript(b)

    def drop_tb(self):
        drp_storagepooltb_sql = "drop table if exists storagepooltb"
        drp_resourcetb_sql = "drop table if exists resourcetb"
        drp_nodetb_sql = "drop table if exists nodetb"
        self.cur.execute(drp_storagepooltb_sql)
        self.cur.execute(drp_resourcetb_sql)
        self.cur.execute(drp_nodetb_sql)
        self.con.commit()
