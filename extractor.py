'''
SCRIPT-1 : Original Table data extract & delete
'''


#Importing Libraries
import MySQLdb  
from datetime import datetime


startime=datetime.now()


#Creating a connection to database
conn=MySQLdb.connect(host='localhost',user='user',password='fill_as_per_requirement',db='graph_data')
#make changes to database user, password & db name.....a

cur=conn.cursor()



#Using Database
cur.execute('USE graph_data')

#Creating a Table and feeding all values in it....
cur.execute('CREATE TABLE IF NOT EXISTS avgprices_cleaner(timestamp BIGINT(30) UNIQUE,avg_price TEXT, from_sym TEXT, to_sym TEXT,utcdate TEXT , utctime TEXT)')


cur.execute('SELECT * FROM avgprices') 
rows=cur.fetchall()

for row in rows:
    timestamp=row[0]
    unixtime=int((timestamp/1000))
    utcdate=datetime.utcfromtimestamp(unixtime).strftime('%d-%m-%Y')
    utctime=datetime.utcfromtimestamp(unixtime).strftime('%H:%M')
    from_sym=row[1]
    to_sym=row[2]  
    avg_price=row[3]
    
    cur.execute("INSERT IGNORE INTO avgprices_cleaner(timestamp,utcdate,utctime,from_sym,to_sym,avg_price)\
        VALUES (%s,%s,%s,%s,%s,%s)",(timestamp,utcdate,utctime,from_sym,to_sym,avg_price))

    conn.commit()  #very important step


cur.execute('TRUNCATE TABLE avgprices')
cur.close()

endtime=datetime.now()
print(endtime-startime)





#[written by AAYUSH GADIA]
