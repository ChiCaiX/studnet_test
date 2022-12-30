import json

import pytest

from student_test.common.HttpReq import ETReq
from student_test.common.db_funs import insert_db
from student_test.common.read_json import update_data
class Test_updateDepartment(object):
    # 前置条件
    # 前置
    def setup_class(self):
        print("执行前，清楚数据库")
        # init_db()
        insert_db()

    def teardown_class(self):
        print("执行后，清除数据库")
        insert_db()

    @pytest.mark.parametrize("title,dep_id,req_data,res_key,res_value, status_code", update_data())
    def test_update_department_001(self,title,dep_id,req_data,res_key,res_value, status_code):
        # print(f"dep_id={dep_id},data={data}")
        # print("yyds")
        print(title)
        resp = ETReq.put(dep_id=dep_id,data=req_data)
        res = json.loads(resp.text)
        print(res)
        # print(resp.status_code)
        assert resp.status_code == status_code
        # assert resp['dep_id']=='T2002N'
        # assert dep_id in res['dep_id']
        assert res_value in res[res_key]