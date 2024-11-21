import unittest
from htmltestreport import HTMLTestReport

from scripts.test_emp_add import TestEmpAdd
from scripts.test_ihrm_login import TestIhrmLogin

suite = unittest.TestSuite()

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestIhrmLogin))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestEmpAdd))

runner = HTMLTestReport("./report/ihrm.html", description="py3.12", title="IHRM测试报告")

runner.run(suite)