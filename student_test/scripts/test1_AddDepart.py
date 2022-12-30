import json

import pytest
import requests

from student_test.common.HttpReq import ETReq
from student_test.common.db_funs import init_db
from student_test.config import URL
from student_test.common.read_json import build_data
#

class Test_AddDepartment(object):
    # 前置
    def setup_class(self):
        print("执行前，清楚数据库")
        init_db()

    def teardown_class(self):
        print("执行后，清除数据库")
        init_db()
    @pytest.mark.parametrize('req_data,req_key,req_value,status_code', build_data())
    def test_add_department(self,req_data,req_key,req_value,status_code):

        resp = ETReq.post_add(req_data)
        res = json.loads(resp.text)
        assert status_code == resp.status_code
        if res.get('create_success'):
            assert res[req_key]['count'] == req_value
        else:
            assert res[req_key][0] == req_value


if __name__=="__main__":
    # -s 表示支持控制台打印，如果不加，print 不会出现任何内容
    pytest.main(["-s", "test1_AddDepart.py"])
    # print("test")