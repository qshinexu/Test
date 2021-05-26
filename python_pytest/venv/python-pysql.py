import pymysql
conn = pymysql.connect(host='10.28.13.177',port=3306,user='root',password='smcdyanfa',db='smzc_new')
cur=conn.cursor()#打开白板
sql='select * from subscriber'
cur.execute(sql)#执行sql
result= cur.fetchall()#把返回的结果返回到白板
print(result)
cur.close()
