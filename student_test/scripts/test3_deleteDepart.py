import pytest

from student_test.common.HttpReq import ETReq
from student_test.common.read_json import delete_data


class Test_deleteDepartment(object):
    def setup_class(self):
        print("执行前，清楚数据库")
        # init_db()

    def teardown_class(self):
        print("执行后，清除数据库")
        # init_db()
    @pytest.mark.parametrize("title,dep_id,res_key,res_value, status_code",delete_data())
    def test_delete_department_001(self,title,dep_id,res_key,res_value, status_code):
        print(title)
        resp = ETReq.delete(dep_id)
        assert status_code == resp.status_code
        if resp.text:
            assert res_value == resp.json()[res_key]
        else:
            assert res_value == resp.text
