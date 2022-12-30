#_*_encoding:utf-8
# 1.导包
import os
# 2. 配置cmd执行下命令（生成allure执行命令）
run_cmd ="allure generate ./temp -o ./new_report --clean "
# 通过os.system命令运行终端命令
os.system(run_cmd)