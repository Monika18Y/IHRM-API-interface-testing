def assert_util(self, resp, status_code, status, msg):
    self.assertEqual(status_code, resp.status_code)
    self.assertEqual(status, resp.json()['code'])
    self.assertIn(msg, resp.json()['message'])