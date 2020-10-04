import pymysql

MYSQL_CONN = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'qkrtpdnd123@',
    db = 'cafeteria_db',
    charset = 'utf8'
)



def conn_mysqldb():
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN

#테이블 생성
def make_table(school_name):
    cursor = MYSQL_CONN.cursor()
    sql = """
    CREATE TABLE {0}(
        ID INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
        DATE VARCHAR(45) NOT NULL,
        MENU1 VARCHAR(45),
        MENU2 VARCHAR(45),
        MENU3 VARCHAR(45),
        MENU4 VARCHAR(45),
        MENU5 VARCHAR(45),
        MENU6 VARCHAR(45),
        MENU7 VARCHAR(45),
        MENU8 VARCHAR(45),
        MENU9 VARCHAR(45),
        MENU10 VARCHAR(45)
        )
    """.format(school_name)
    return cursor.execute(sql)

#테이블 삭제
def drop_table(school_name):
    cursor = MYSQL_CONN.cursor()
    sql = "DROP TABLE {0}".format(school_name)
    return cursor.execute(sql)

#테이블 조회
def show_table():
    if __name__ == '__main__':
        cursor = MYSQL_CONN.cursor()
        sql = "SHOW TABLEs"
        return cursor.execute(sql)

def delete_data(school_name):
    cursor = MYSQL_CONN.cursor()
    sql = 'TRUNCATE {0}'.format(school_name)
    return cursor.execute(sql)

def data_upload(school_name,date):
    cursor = MYSQL_CONN.cursor()
    sql = "SELECT DATE, MENU1, MENU2, MENU3, MENU4, MENU5, MENU6, MENU7, MENU8, MENU9, MENU10 FROM {0}".format(school_name)
    cursor.execute(sql)
    results = cursor.fetchall()
    for result in results:
        if result[0] == date:
            return result


#print(data_upload('solbat','20200103'))


