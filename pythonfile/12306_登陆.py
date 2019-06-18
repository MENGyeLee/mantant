import re
import requests
import base64
import time
import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class check_login():
    def getImg(self):
        headers = {'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }
        Xq_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image64'    #生成验证码的url
        Xq_parmas = {
            "login_site": "E",
            "module": "login",
            "rand": "sjrand",
            "15669770297":"",
            "callback": "jQuery19109087628126888729_15669770297",
            "_": "15669770297",
        }
        sess=requests.session()
        response=sess.get(url=Xq_url,params=Xq_parmas,headers=headers).text
        image_bs64=re.findall('"image":"(.*?)",',response)[0]
        image=base64.b64decode(image_bs64)
        with open('image.jpg','wb') as f:
            f.write(image)
        self.sess=sess

    def check_result(self):
        Xq_url1='http://littlebigluo.qicp.net:47720/'
        sess1=requests.session()
        response1=sess1.post(url=Xq_url1,data={"type":"1"},files={'pic_xxfile':open('Yz_image.jpg','rb')})
        result=[]
        try:
            for i in re.findall("<B>(.*)</B>",response1.text)[0].split(" "):
	            result.append(int(i))
        except:
            print("该验证网站繁忙")
        coord_data ={
            "1":"40,40","2":"120,40", "3":"180,40", "4":"250,40","5":"40,100", "6":"120,100", "7":"180,100", "8":"250,100",
            }
        answerlist = []
        print('选中图片为:',result)
        for i in result:
            answerlist.append(coord_data[str(i)])
        print('坐标为：' + ';'.join(answerlist))
        answer = ','.join(answerlist)
        self.answer=answer


    # def cookie(self):

    #     Login_url="https://kyfw.12306.cn/otn/resources/login.html"

    #     chromedriver="D:/平时文件/爬虫/12306登录/test/chromedriver.exe"

    #     os.environ["webdriver.chrome.driver"]=chromedriver

    #     self.driver=webdriver.Chrome(chromedriver)

    #     print("正在打开网页...")

    #     self.driver.get(Login_url)

    #     account=self.driver.find_element_by_class_name("login-hd-account active")

    #     account.click()

    #     userName=self.driver.find_element_by_id("J-userName")

    #     userName.send_keys("qch947769566")

    #     password=self.driver.find_element_by_id("J-password")

    #     password.send_keys("0qiu1chao2hai3")



    def login(self):
        check_url="https://kyfw.12306.cn/passport/captcha/captcha-check"    #验证验证码的url
        Sy_url="https://kyfw.12306.cn/passport/web/login"    #登录的url

        check_headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        }

        Sy_headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin':'https://kyfw.12306.cn',
            'Referer':'https://kyfw.12306.cn/otn/resources/login.html',
            'Accept':'application/json, text/javascript, */*; q=0.01',

        }

        

        username = input('请输入用户名：')
        password = input('请输入密码：')

        log_data = {
            "username": username,
            "password": password,
            "appid": "otn",
            #"answer": self.answer,
        }
        #Yz_url
        log_parmas = {
            "callback": "jQuery19105010300528763358_1559733968819",
            "answer":self.answer, 
            "rand": "sjrand",
            "login_site": "E",
            "_": "15669770297",          
        }
        #发送图片验证请求
        response2=self.sess.get(url=check_url,params=log_parmas,headers=check_headers).text
        #获得图片验证信息
        print(re.findall('"result_message":"(.*?)"',response2))

        #增加cookies
        self.sess.cookies.update({
            'RAIL_EXPIRATION':'15669770297',
            'RAIL_DEVICEID':'p3xGaEyfGCtCN3Q1YYWImAt9vwLj1LB4oZltVN07EBp_UARZbREL1HzlVDd2B1_HL980K1Pl__t1bGWfXfNGt6zbaoppKNeFwxcBq-BXZ1dxgsQMVLJ8S_IR6k13aAaoH2A99dz55yCS97mNTJTXmNsAqXIhOk0p',
        })

        response3=self.sess.post(url=Sy_url,data=log_data,headers=Sy_headers)
        #返回编码后的数据
        response3.encoding='utf-8'
        print(re.findall('"result_message":"(.*?)"',response3.text))





    def load(self):
        self.getImg()
        time.sleep(3)
        self.check_result()
        time.sleep(10)
        self.login()
        time.sleep(10)

if __name__=="__main__":
    test=check_login()
    test.load()