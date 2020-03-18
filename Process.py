#coding:utf-8
from VersaTEL_G2_socket import LinstorDB as db
import sqlite3


class Process_data():
    def __init__(self):
        self.linstor_db = db.LINSTORDB()
        # self.CRM = db.PacemakerDB()

    def process_data_node(self):
        cur = self.linstor_db.cur
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