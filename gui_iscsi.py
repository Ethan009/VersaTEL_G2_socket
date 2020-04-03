#coding=utf-8
import subprocess

class gui_iscsi():

	def cmd(self,l):
		if isinstance(l,list):
			# print(l)
			strl = ' '.join(l)
			print("python3 vtel_iscsi.py iscsi " + strl)
			# subiscsi = subprocess.call("python3 vtel_iscsi.py iscsi " + a + " " + b + " " + c + " " + d, shell=True)
			# print(subiscsi)
		# return subiscsi
		else:
			print("传递的参数需要是一个列表")

	def cmda(self,a,b,c,d):
		subiscsi = subprocess.call("python3 vtel_iscsi.py iscsi " + a + " " + b + " " + c + " " + d, shell=True)
		print(subiscsi)
		return subiscsi


if __name__ == '__main__':
	gui = gui_iscsi()
	print("create 例子：")
	gui.cmd(['host','create','hostname1','iqn.xx1'])
	gui.cmd(['hostgroup','create','hostgroupname1','hostname1','hostname2','hostname3'])
	gui.cmd(['diskgroup','create','diskgroupname1','diskname1','diskname2'])
	gui.cmd(['map','create','mapname1','-hg','hostgroupname1','-dg','diskgroupname1'])
	print("delete 例子：")
	gui.cmd(['host','delete','hostname1'])
	gui.cmd(['hostgroup','delete','hostgroupname1'])
	gui.cmd(['diskgroup','delete','diskgroupname1'])
	gui.cmd(['map','delete','mapname1'])

