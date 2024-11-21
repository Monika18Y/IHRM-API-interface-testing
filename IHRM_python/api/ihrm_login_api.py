"""
登录接口
"""
import requests


class IhrmLoginApi(object):
    @classmethod
    def login(cls, json_data):
        resp = requests.post(
            url="http://ihrm2-test.itheima.net/api/sys/login",
            headers={"Content-Type": "application/json"},
            json=json_data
        )
        return resp
