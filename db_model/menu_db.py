from mysql import conn_mysqldb,make_table
from bs4 import BeautifulSoup
import requests
def caf_scrapping(url,school_name):
        dates = []
        months = []
        #url = "http://school.cbe.go.kr/gaesin-e/MABADAHAE/"

        for i in range(1,32):
                date = str(i)
                if len(date) == 1:
                        date = '0'+date
                dates.append(date)

        for i in range(1,11):
                month = str(i)
                if len(month) == 1:
                        month = '0'+month
                months.append(month)

        for month in months:
                for date in dates:
                        res = requests.get(url+'list?ymd=2020'+month+date)
                        res.raise_for_status()
                        soup = BeautifulSoup(res.text,"lxml")
                        datetime = '2020'+month+date
                        items = soup.select('#usm-content-body-id > ul.tch-lnc-list > li.tch-lnc-wrap > dl > dd.tch-lnc > ul > li')

                        menus = []

                        for item in items:
                                menus.append(item.text)


                        for i in range(10-len(menus)):
                                menus.append('없음')

                        mysql_db = conn_mysqldb()
                        cursor = mysql_db.cursor()
                        sql = """INSERT INTO %s (DATE, MENU1, MENU2, MENU3, MENU4, MENU5, MENU6, MENU7, MENU8, MENU9, MENU10) 
                                VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (school_name,datetime, menus[0], menus[1], menus[2], menus[3], menus[4], menus[5], menus[6],menus[7],menus[8],menus[9])

                        cursor.execute(sql)
                        mysql_db.commit()
        return print('크롤링 완료')

make_table('solbat')
caf_scrapping("http://school.cbe.go.kr/solbat-e/M010303/","solbat")


