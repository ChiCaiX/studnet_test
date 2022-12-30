import pytest

from student_test.common.HttpReq import ETReq
from student_test.common.db_funs import count_db, execute_db


class Test_selectDepartment(object):
    def setup_class(self):
        print("执行前，清楚数据库")
        self.url = "http://127.0.0.1:8099/api/departments/{}"
        # init_db()

    def teardown_class(self):
        print("执行后，清除数据库")
        # init_db()
    # 查询搜索学院信息
    def test_query_depart_001(self):
        resp = ETReq.get_id()
        res = resp.json()
        print(res)
        count = count_db()
        print(count)
        assert 200 == resp.status_code
        assert count == res.get('count')

    def test_query_depart_002(self):
        resp=ETReq.get_id(dep_id='T2001N')
        res = resp.json()
        print(res)
        assert 200 == resp.status_code
        assert 'T2001N'==res['dep_id']
    def test_query_depart_003(self):
        # T01为不存在
        resp = ETReq.get_id(dep_id='T011')
        res = resp.json()
        print(res)
        assert 404 == resp.status_code
        assert '未找到' in res['detail']

    # 学院查询（根据dep_id）
    def test_query_depart_004(self):
        #T01,T02两个都为不存在
        data = "T0911,T0811"
        resp = ETReq.get_list(list_name= "$dep_id_list",data =data)
        res = resp.json()
        count = execute_db("SELECT count(*) FROM departments WHERE dep_id='T0811'OR dep_id ='T0911'")[0][0]
        print(count)
        assert 200 == resp.status_code
        assert count == res.get('count')
    def test_query_depart_005(self):
        #T01,T02都存在
        data = "T091,T081"
        resp = ETReq.get_list(list_name= "$dep_id_list",data =data)
        res = resp.json()
        count = execute_db("SELECT count(*) FROM departments WHERE dep_id='T081'OR dep_id ='T091'")[0][0]
        print(count)
        assert 200 == resp.status_code
        assert count == res.get('count')
    def test_query_depart_005(self):
        #T01,T02都存在
        data = "T091,T0811"
        resp = ETReq.get_list(list_name= "$dep_id_list",data =data)
        res = resp.json()
        count = execute_db("SELECT count(*) FROM departments WHERE dep_id='T081'OR dep_id ='T0911'")[0][0]
        print(count)
        assert 200 == resp.status_code
        assert count == res.get('count')
    #学院查询（根据dep_name）
    def test_query_depart_006(self):
        #T01，T02:两个为不存在
        data ="T02学院,T08学院"
        resp = ETReq.get_list(list_name="$dep_name_list", data=data)
        res = resp.json()
        count = execute_db("SELECT count(*) FROM departments WHERE dep_name='T02学院'OR dep_name ='T08学院'")[0][0]
        print(count)
        assert 200 == resp.status_code
        assert count == res.get('count')
    #组合查询depname、mastername、slogan:为存在且格式正确；三个条件可随意组合或单个使用
    data =[
        ("T08学院",'','',),
        ('','T09Master',''),
        ('','','yysds'),
        ('','',''),
        ('T08学院$%^','T09Master','')
    ]
    @pytest.mark.parametrize('dep_name,master_name,slogan',data)
    def test_query_depart_0016(self,dep_name,master_name,slogan):
        # print(title)
        resp = ETReq.get(dep_name=dep_name,master_name=master_name,slogan=slogan)
        # res=resp.text()
        # print(resp)
        # print(resp.json())
        # print(resp.status_code)
        assert 200 == resp.status_code


