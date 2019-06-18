import requests
from lxml import etree
import MySQLdb


con= MySQLdb.connect(host='localhost',user='root',password='root',db='test',charset="utf8")
cursor=con.cursor()
cursor.execute("create table test(No varchar(32) ,content char(255))")

#静态网页抓取：request爬虫实践：top250电影数据
def get_page(start_num):
    url='https://movie.douban.com/top250?start=%s&filter=' %start_num
    print(url)

    response=requests.get(url)
    tree=etree.HTML(response.text)
    title=tree.xpath('//span[@class="title"][1]/text()')
    return title

def get_all_page(start,end):
    result=[]
    for i in range(start,end-start):
        title_list=get_page(i*25)
        result+=title_list
        print(result)
    return result

if __name__=="__main__":
    result=get_all_page(0,10)
    
    for i in range(len(result)):
        cursor.execute("INSERT INTO movies(id,content) values(%d,'%s')" %(i+1,result[i]))
    cursor.close()
    con.commit()
    con.close()

