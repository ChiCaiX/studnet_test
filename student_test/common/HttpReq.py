import json

import requests

from student_test.common.logger import write_log
from student_test.config import URL

class HttpReq(object):
    def __init__(self):
        self.headers = {"Content-Type": "application/json",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
                        }
        self.add_url = URL
        self.update_url = "http://172.16.88.36:8099/api/departments/{}/"
        self.delete_url = "http://172.16.88.36:8099/api/departments/{}/"
        self.select_url ="http://172.16.88.36:8099/api/departments/{}"



    def post_add(self,data,cookies=None):
        try:
            resp = requests.post(self.add_url, headers=self.headers, data=json.dumps(data))
            return resp
        except Exception as e:
            write_log.error("Post请求失败{}".format(e))
    # 查询学院
    # 1. 根据id来查询学院
    def get_id(self,url='',dep_id="",cookies=None):
        """

        :param url: api路径
        :param ids: dep_Id,如果dep_id为空，则查询安全部id
        :param data:
        :param cookies:
        :return:
        """
        try:
            self.query_url=self.select_url.format(dep_id)
            print(self.query_url)
            resp = requests.get(self.query_url,headers=self.headers, cookies=cookies)
            return resp
        except Exception as e:
            write_log.error("GET请求失败{}".format(e))
   # 根据列表查询
    def get_list(self,list_name,data):
        """

        :param url: api路径
        :param list_name: 列表名称：id列表，校长名称列表，口号列表
        :param data:列表数据
        :return:返回查询的数据
        """
        try:
            path ="?{}={}".format(list_name,data)
            self.url = self.select_url.format(path)
            print(self.url)
            resp = requests.get(self.url,headers=self.headers)
            return resp
        except Exception as e:
            write_log.error("GET请求失败{}".format(e))

    def get(self,dep_name='',master_name='',slogan='',cookies=None):
        data ={
           "dep_name":dep_name,
            "master_name":master_name,
            "slogan":slogan

        }
        try:
            resp=requests.get("http://127.0.0.1:8099/api/departments/",params=data,headers=self.headers)
            return resp
        except Exception as e:
            write_log.error("GET请求失败{}".format(e))

    #PUT
    # 更新学院信息
    def put(self, dep_id,data, cookies=None):
        try:
            self.ud_url = self.update_url.format(dep_id)
            # print(self.update_url)
            # print(self.ud_url)
            resp = requests.put(self.ud_url,data=json.dumps(data), headers=self.headers,
                                cookies=cookies)
            return resp
        except Exception as e :
            write_log.error("PUT请求失败{}".format(e))
    #DELETE
    # 删除学院信息
    def delete(self, dep_id='', data='', cookies=None):

        try:
            self.del_url = self.delete_url.format(dep_id)

            resp = requests.delete(self.del_url, data=data, headers=self.headers, cookies=cookies)
            return resp
        except Exception as e:
            print(e)


ETReq = HttpReq()