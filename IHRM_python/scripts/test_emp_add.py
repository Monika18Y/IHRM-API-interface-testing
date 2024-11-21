import unittest
from parameterized import parameterized

from api.ihrm_emp_curd import IhrmEmpCURD
from common.assert_util import assert_util
from common.db_util import DBUtil
from common.get_header import get_header
from common.read_json_util import read_json_data
from config import TEL, BASE_DIR


class TestEmpAdd(unittest.TestCase):

    header = None
    path_filename = BASE_DIR + "/data/add_emp.json"

    @classmethod
    def setUpClass(cls):
        cls.header = get_header()

    def setUp(self):
        DBUtil.uid_db(f"delete from bs_user where mobile = '{TEL}'")

    def tearDown(self):
        DBUtil.uid_db(f"delete from bs_user where mobile = '{TEL}'")

    # 通用方法
    @parameterized.expand(read_json_data(path_filename))
    def test_add_emp(self, desc, json_data, status_code, status, msg):
        resp = IhrmEmpCURD.add_emp(self.header, json_data)
        print(f"测试用例：{desc}，返回结果：{resp.json()}")
        assert_util(self, resp, status_code, status, msg)
