"""
员工管理模块 接口对象层
"""
import requests


class IhrmEmpCURD(object):

    # 添加员工
    @classmethod
    def add_emp(cls, header, json_data):
        resp = requests.post(
            url="http://ihrm2-test.itheima.net/api/sys/user",
            headers=header,
            json=json_data
        )
        return resp

    # 查询员工
    @classmethod
    def query_emp(cls, emp_id, header):
        resp = requests.get(
            url="http://ihrm2-test.itheima.net/api/sys/user" + emp_id,
            headers=header
        )
        return resp

    # 修改员工
    @classmethod
    def modify_emp(cls, emp_id, header, modify_data):
        resp = requests.put(
            url="http://ihrm2-test.itheima.net/api/sys/user" + emp_id,
            headers=header,
            json=modify_data
        )
        return resp

    # 删除员工
    @classmethod
    def delete_emp(cls, emp_id, header):
        resp = requests.delete(
            url="http://ihrm2-test.itheima.net/api/sys/user" + emp_id,
            headers=header
        )
        return resp

