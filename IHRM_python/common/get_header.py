import requests


def get_header():
    url = "https://ihrm2-test.itheima.net/api/sys/login"
    data = {"mobile": "13800000002", "password": "888itcast.CN764%..."}
    resp = requests.post(url=url, json=data)
    token = "Bearer " + resp.json()['data']
    header = {"Content-Type": "application/json",
              "Authorization": token}
    return header
