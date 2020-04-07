#coding:utf-8
import LinstorDB as db
import sqlite3


class Process_data():
    def __init__(self):
        self.linstor_db = db.LINSTORDB()
        self.cur = self.linstor_db.cur
        # self.CRM = db.PacemakerDB()

    def process_data_node(self):
        # cur = self.linstor_db.cur
        cur = self.cur
        date = []
        def _count_node():
            select_sql = "select count(Node) from nodetb"
            cur.execute(select_sql)
            date_set = cur.fetchone()
            return list(date_set)

        def _select_nodetb(n):
            select_sql = "select Node,NodeType,Addresses,State from nodetb where id = ?"  # sql语言：进行查询操作
            cur.execute(select_sql, str(n))
            date_set = cur.fetchone()
            return list(date_set)

        def _select_res_num(n):
            select_sql = "SELECT COUNT(Resource) FROM resourcetb WHERE Node IN (SELECT Node FROM nodetb WHERE id = ?)"
            cur.execute(select_sql, str(n))
            date_set = cur.fetchone()
            return list(date_set)

        def _select_stp_num(n):
            select_sql = "SELECT COUNT(Node) FROM storagepooltb WHERE Node IN (SELECT Node FROM nodetb WHERE id = ?)"
            cur.execute(select_sql, str(n))
            date_set = cur.fetchone()
            return list(date_set)

        def _select_resourcetb(n):
            select_sql = "SELECT Resource,StoragePool,Allocated,DeviceName,InUse,State FROM resourcetb WHERE Node IN ((SELECT Node FROM nodetb WHERE id = ?))"
            cur.execute(select_sql, (str(n)))
            date_set = cur.fetchall()
            return list(date_set)

        for i in range(1, (_count_node()[0] + 1)):  # 从1开始循环到给定的整数，有没有更好的办法
            node, nodetype, addr, status = _select_nodetb(i)
            res_num = _select_res_num(i)[0]
            stp_num = _select_stp_num(i)[0]
            list_resdict = []
            for res in _select_resourcetb(i):
                res_name, stp_name, size, device_name, used, status = res
                dic = {"res_name": res_name, "stp_name": stp_name, "size": size, "device_name": device_name,
                       "used": used, "status": status}
                list_resdict.append(dic)
            # for #返回res_num 对应的几个resource信息，
            date_ = {"node": node,
                     "node_type": nodetype,
                     "res_num": str(res_num),
                     "stp_num": str(stp_num),
                     "addr": addr,
                     "status": status,
                     "res_num_son": list_resdict}
            date.append(date_)
        dict = {"code": 0, "msg": "", "count": 1000, "data": date}
        cur.close()
        return dict

    def process_data_resource(self):
        #linstor_db = Linst_db()
        cur = self.linstor_db.cur
        date = []

        def _get_resource():
            res = []
            select_sql1 = "SELECT distinct Resource,Allocated,DeviceName,InUse FROM resourcetb "
            cur.execute(select_sql1)
            res_all = cur.fetchall()

            select_sql2 = "SELECT distinct Resource,Allocated,DeviceName,InUse FROM resourcetb WHERE InUse = 'InUse'"
            cur.execute(select_sql2)
            in_use = cur.fetchall()

            for i in in_use:
                res.append(i[0])

            for i in res_all:
                if i[0] in res and i[3] == 'Unused':
                    res_all.remove(i)
            return res_all

        def _get_mirro_way(rn):
            select_sql = "SELECT COUNT(Resource) FROM resourcetb WHERE Resource = '" + rn + "'"
            cur.execute(select_sql)
            data_set = cur.fetchone()
            return list(data_set)

        def _get_mirror_way_son(rn):
            select_sql = "SELECT Node,StoragePool,InUse,State FROM resourcetb WHERE Resource = '" + rn + "'"
            cur.execute(select_sql)
            data_set = cur.fetchall()
            return list(data_set)

        for i in _get_resource():
            if i[1]:
                resource, size, device_name, used = i
                mirror_way = _get_mirro_way(str(i[0]))[0]  # i[0] = 'apple'
                list_resdict = []
                for res_one in _get_mirror_way_son(str(i[0])):
                    node_name, stp_name, drbd_role, status = list(res_one)
                    if drbd_role == u'InUse':
                        drbd_role = u'primary'
                    elif drbd_role == u'Unused':
                        drbd_role = u'secondary'
                    dic = {"node_name": node_name, "stp_name": stp_name, "drbd_role": drbd_role, "status": status, }
                    list_resdict.append(dic)
                date_one = {"resource": resource,
                            "mirror_way": mirror_way,
                            "size": size,
                            "device_name": device_name,
                            "used": used,
                            "mirror_way_son": list_resdict}
                date.append(date_one)
        dict = {"code": 0, "msg": "", "count": 1000, "data": date}
        cur.close()
        return dict

    def process_data_stp(self):
        #linstor_db = Linst_db()
        cur = self.linstor_db.cur
        date = []

        # 查询storagepooltb全部信息
        def _select_storagepooltb():
            # StoragePool | Node     | Driver | PoolName | FreeCapacity | TotalCapacity | SupportsSnapshots | State
            select_sql = '''SELECT 
            StoragePool,
            Node,
            Driver,
            PoolName,
            FreeCapacity,
            TotalCapacity,
            SupportsSnapshots,
            State 
            FROM storagepooltb
            '''
            cur.execute(select_sql)
            data_set = cur.fetchall()
            return list(data_set)

        def _res_sum(node, stp):
            select_sql = "SELECT COUNT(DISTINCT Resource) FROM resourcetb WHERE Node = '{}' AND StoragePool = '{}'".format(
                node, stp)
            cur.execute(select_sql)
            num = cur.fetchone()
            return num[0]

        def _res(node, stp):
            select_sql = "SELECT Resource,Allocated,DeviceName,InUse,State FROM resourcetb WHERE Node = '{}' AND StoragePool = '{}'".format(node, stp)
            cur.execute(select_sql)
            date_set = cur.fetchall()
            return list(date_set)


        for i in _select_storagepooltb():
            stp_name, node_name, driver, pool_name, free_size, total_size, snapshots, status = i
            res_num = _res_sum(str(node_name), str(stp_name))
            list_resdict = []
            for res in _res(str(node_name), str(stp_name)):
                res_name, size, device_name, used, status = res
                # Resource,Allocated,DeviceName,InUse,State FROM resourcetb where  StoragePool
                dic = {"res_name": res_name, "size": size, "device_name": device_name, "used": used, "status": status}
                list_resdict.append(dic)

            # 返回res_num 对应的几个resource信息，
            date_ = {"stp_name": stp_name,
                     "node_name": node_name,
                     "res_num": str(res_num),
                     "driver": driver,
                     "pool_name": pool_name,
                     "free_size": free_size,
                     "total_size": total_size,
                     "snapshots": snapshots,
                     "status": status,
                     "res_name_son": list_resdict}
            date.append(date_)
        dict = {"code": 0, "msg": "", "count": 1000, "data": date}
        cur.close()
        return dict

        # 获取表单行数据的通用方法

    def sql_fetch_one(self, sql):
        cur = self.cur
        cur.execute(sql)
        date_set = cur.fetchone()
        return date_set

        # 获取表全部数据的通用方法

    def sql_fetch_all(self, sql):
        cur = self.cur
        cur.execute(sql)
        date_set = cur.fetchall()
        return list(date_set)

    '''[{"cityName":"Node1"}, {"cityName":"Node2"}, {"cityName":"Node3"}, {"cityName":"Node4"}]
    '''

    def get_online_node(self):
        select_sql = "SELECT Node FROM nodetb WHERE State = 'Online'"
        return self.sql_fetch_all(select_sql)

    def get_ok_sp(self, node):
        select_sql = "SELECT Storagepool FROM storagepooltb WHERE Node = \'%s\' " \
                     "and FreeCapacity is not null and State = 'Ok'" % node
        return self.sql_fetch_all(select_sql)

    def get_node_num(self):
        select_sql = "SELECT COUNT(Node) FROM nodetb"
        return self.sql_fetch_one(select_sql)

    def get_vg(self):
        select_sql = "SELECT VG FROM vgtb"
        return self.sql_fetch_all(select_sql)

    def get_thinlv(self):
        select_sql = "SELECT LV FROM thinlvtb"
        return self.sql_fetch_all(select_sql)


    def get_option_node(self):
        list_node = self.get_online_node()  # E.g:[('klay1',), ('klay2',)]
        list_result = []
        for node in list_node:
            dict_one = {'key_node': node[0]}
            list_result.append(dict_one)
        return list_result

    """
     data_test_three = [{'NodeName': 'Node1',
                        'Spool': [{'device_name': '1'},
                                 {'device_name': '2'},
                                 {'device_name': '3'},
                                 {'device_name': '4'}]
                      },
                      {'NodeName': 'Node2',
                      'Spool': [{'device_name': '5'},
                                { 'device_name': '6'},
                                 {'device_name': '7'},
                                 {'device_name': '8'}]
                    }]
    """

    def get_option_sp(self):
        list_node = self.get_online_node()
        list_result = []
        for node in list_node:
            list_sp = self.get_ok_sp(node[0])
            list_result_sp = []
            for sp in list_sp:
                dict_sp = {'key_sp': sp[0]}
                list_result_sp.append(dict_sp)
            dict_one = {'NodeName': node[0], 'Spool': list_result_sp}
            list_result.append(dict_one)
        return list_result

    def get_option_lvm(self):
        vg = self.get_vg()
        thinlv = self.get_thinlv()

        list_vg = []
        list_thinlv = []
        for vg_one in vg:
            dict_vg = {"cityName": vg_one[0]}
            list_vg.append(dict_vg)

        for thinlv_one in thinlv:
            dict_thinlv = {"cityName": thinlv_one[0]}
            list_thinlv.append(dict_thinlv)

        dict_all = {"lvm": list_vg, "thin_lvm": list_thinlv}
        print(dict_all)
        return dict_all
    
    def get_option_nodenum(self):
        num_node = int(self.get_node_num()[0]) + 1
        list_result = []
        for i in range(1,num_node):
            dict_one = {'key_nodenum':i}
            list_result.append(dict_one)
        return list_result
