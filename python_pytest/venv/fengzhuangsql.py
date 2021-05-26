import pymysql
class Handsql:
    def __init__(self):
        self.conn=pymysql.connect(host='10.28.13.177',port=3066,user='root',password='smcdyanfa',db='smzc_new')

    def get_data(self):
        self.cur.execute(sql)
        
    def __close_cur(self):
        self.cur.close()
    def __clos_conn(self):
        self.conn.close()