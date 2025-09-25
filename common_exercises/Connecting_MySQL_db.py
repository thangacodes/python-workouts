##### How to connect MySQL database using Python Script ##################

import mysql.connector
testdb = mysql.connector.connect(user='root',passwd='Covacin@123',host='localhost',database='python')
cur = testdb.cursor()
cur.execute("insert into sampletable values ('thanga','149'),('mani','789');")
testdb.commit()  ## In database commit is equal to save
cur.execute("select * from sampletable;")
Table= cur.fetchall()
print(Table)
testdb.close()

Please note:This script is use to connect locally installed MySQL db in our laptop or desktop. Look at the hostname.

