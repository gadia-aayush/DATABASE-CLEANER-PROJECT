'''
SCRIPT-2 : Copied Data Clean & then Re-Filling the Original Table.
'''


#Importing Important Libraries
import MySQLdb
from datetime import datetime


startime=datetime.now()


#Creating a connection to database
conn=MySQLdb.connect(host='localhost',user='user',password='fill_as_per_requirement',db='graph_data')
cur=conn.cursor()


#Using Database
cur.execute('USE graph_data')


#Currencies total:
cur.execute('SELECT from_sym FROM avgprices_cleaner ORDER BY from_sym ASC,timestamp ASC')
currencies=list((map(list, set(cur.fetchall()))))


#Time List
time_day=['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00',]


for currency in currencies:
    cur.execute('SELECT utcdate FROM avgprices_cleaner WHERE from_sym=%s', (currency[0],  ))  #cuurency[0], 'comma dena is very very necessary'
    dates=list((map(list, set(cur.fetchall()))))
    for date in dates:
        cur.execute('SELECT utctime FROM avgprices_cleaner WHERE from_sym=%s AND utcdate=%s',(currency[0],date[0], ))  
        times=list((map(list, set(cur.fetchall()))))
        times.sort()
        for time in times:
            if time[0] in time_day:
                cur.execute('SELECT timestamp FROM avgprices_cleaner WHERE from_sym=%s AND utcdate=%s AND utctime=%s',(currency[0],date[0],time[0], ))
                timestamps=list((map(list, set(cur.fetchall()))))  #xlm wala problem fix....1 ms mein 2 input nahi...imply repeat ho raha hai
                timestamps.sort()         
                timestamp=timestamps[0][0]
                #timestamp always unique hai for each currency
                from_sym=currency[0]
            
                cur.execute('SELECT avg_price FROM avgprices_cleaner WHERE from_sym=%s AND timestamp=%s', (currency[0],timestamp))
                price_rough=list((map(list, cur.fetchall())))
                price=price_rough[0][0]
            
                cur.execute('SELECT to_sym FROM avgprices_cleaner WHERE from_sym=%s AND timestamp=%s', (currency[0],timestamp))
                tosym_rough=list((map(list, cur.fetchall())))
                to_sym=tosym_rough[0][0]
            
            
                print(timestamp,' ', currency[0],' ', price, ' ', to_sym, ' ', date, ' ', time)
                cur.execute('INSERT IGNORE INTO avgprices(timestamp,avg_price,from_sym,to_sym) VALUES (%s,%s,%s,%s)',(timestamp,price, from_sym, to_sym))
                          
                conn.commit()
            
            else:
                continue            

            
cur.execute('TRUNCATE TABLE avgprices_cleaner')
cur.execute('SELECT * FROM avgprices ORDER BY timestamp ASC')
cur.close()

endtime=datetime.now()
print(endtime-startime)




#[written by AAYUSH GADIA]
