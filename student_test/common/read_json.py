import json

from student_test.config import BASE_DIR

# url = BASE_DIR + "\data\add_depart.json"
def build_data():
    try:
        # 读取json文件
        with open(BASE_DIR + r"/data/add_depart.json",'r',encoding='UTF-8') as f:
            build_list = json.load(f)
            built_data = []
            for data_dict in build_list:
                for data in data_dict.values():
                    # print(type(data))

                    req_data = data.get('req_data')
                    res_key = data.get('res_key')
                    res_value = data.get('res_value')
                    status_code = data.get('status_code')
                    built_data.append((req_data, res_key, res_value, status_code))
            return built_data
    except Exception as e:
        print(e)

def update_data():
    try:
        with open(BASE_DIR + r"/data/update_depart.json",'r',encoding='UTF-8') as f:
            build_list = json.load(f)
            built_data = []
            # print(build_list)
            print(type(build_list))
            for data_dict in build_list:
                for data in data_dict.values():
                    # print(type(data))
                    title = data.get("title")
                    dep_id = data.get('dep_id')
                    req_data = data.get('req_data')
                    res_key = data.get('res_key')
                    res_value = data.get('res_value')
                    status_code = data.get('status_code')
                    built_data.append((title,dep_id,req_data,res_key,res_value, status_code))
            return built_data
    except Exception as e:
        print(e)
# 读取delete_depart.json文件
def delete_data():
    try:
        with open(BASE_DIR + r"/data/delete_depart.json",'r',encoding='UTF-8') as f:
            build_list = json.load(f)
            built_data = []
            # print(build_list)
            print(type(build_list))
            for data_dict in build_list:
                for data in data_dict.values():
                    # print(type(data))
                    title = data.get("title")
                    dep_id = data.get('dep_id')
                    # req_data = data.get('req_data')
                    res_key = data.get('res_key')
                    res_value = data.get('res_value')
                    status_code = data.get('status_code')
                    built_data.append((title,dep_id,res_key,res_value, status_code))
            return built_data
    except Exception as e:
        print(e)
if __name__=="__main__":
    data =delete_data()
    # print(data)
    print(type(data))
    for d in data:
        print(d)


    # print(url)