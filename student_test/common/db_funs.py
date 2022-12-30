from student_test.common.logger import write_log
from student_test.config import PROJECT_DIR
import sqlite3
URL = "D:\student_test\student_env\studentManagementSystem\db.sqlite3"

def execute_db(sql):


    """
    连接接口项目sqlite数据库，并执行sql语句
    :param sql: sql语句
    :return:
    """
    try:
        conn = sqlite3.connect("{0}\\studentManagementSystem\\db.sqlite3".format(PROJECT_DIR))
        # conn = sqlite3.connect(r"D:\chicaixiang\auto-test\Interface test\student\student_env\studentManagementSystem\db.sqlite3")
        # 新建游标
        cursor = conn.cursor()
        # 执行sql
        cursor.execute(sql)
        # 如果是查询
        if sql.split()[0].lower() =='select':
            # 返回所有数据
            return cursor.fetchall()
        else:
            conn.commit()
            return cursor.rowcount
    except sqlite3.OperationalError as e:
        write_log.error("数据连接，执行难失败：{}".format(e))
    except Exception as e:
        conn.rollback()
        write_log.error("SQL提交错误:{}".format(e))
    finally:
        cursor.close()
        conn.close()


# 查询数据中数量




def init_db():
    """
    初始化数据库，删除掉departments的所有数据
    :return:
    """
    execute_db("delete from departments ;")

    # print(execute_db(sql))
# 查询list_data的数据
def count_db():
    sql = "SELECT COUNT(*) from departments"
    count = execute_db(sql)[0][0]
    return count
# 插入测试数据
def insert_db():
    init_db()
    sql ="INSERT INTO departments (dep_id,dep_name,master_name,slogan) VALUES" \
         "('T2001N','Test201学院','Master201','Slogan201')," \
         "('T2002N','Test202学院','Master202','')," \
         "('T2003N','Test203学院','Master203','')," \
         "('T2004N','Test204学院','Master204','')," \
         "('T2005N','Test205学院','Master205','Slogan205')," \
         "('T2006N','Test206学院','Master206','Slogan206')," \
         "('T2007N','Test207学院','Master207','Slogan207')," \
         "('T2008N','Test208学院','Master208','Slogan208')," \
         " ('T2009N','Test209学院','Master291','Slogan209')," \
         "('T2010N','Test210学院','Master210','Slogan210')"
    execute_db(sql)
if __name__ == '__main__':
    init_db()
    # query_db("dep_id","T02","T03")
    # count_db()
    # insert_db()
    print("{0}\\studentManagementSystem\\db.sqlite3".format(PROJECT_DIR))
