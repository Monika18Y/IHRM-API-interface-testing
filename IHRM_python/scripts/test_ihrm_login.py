import unittest

from api.ihrm_login_api import IhrmLoginApi
from common.assert_util import assert_util
from common.read_json_util import read_json_data
from config import BASE_DIR

from parameterized import parameterized


class TestIhrmLogin(unittest.TestCase):
    path_filename = BASE_DIR + "/data/ihrm_login.json"

    @parameterized.expand(read_json_data(path_filename))
    def test_login(self, desc, user_data, status_code, status, msg):
        res = IhrmLoginApi.login(user_data)
        print(f"测试用例：{desc}，返回结果：{res.json()}")
        assert_util(self, res, status_code, status, msg)
