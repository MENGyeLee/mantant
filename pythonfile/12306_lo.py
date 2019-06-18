import requests
import http.cookiejar as cookielib

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")

def isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    url = "https://kyfw.12306.cn/passport/web/login"
    login_code = session.get(url, headers=headers, allow_redirects=False).status_code
    if login_code == 200:
        return True
    else:
        return False
    
def login(secret, account):
    post_url = 'https://kyfw.12306.cn/passport/web/login'
    postdata = {
        'pwd': secret,
        'log': account,
        'rememberme' : 'true',
        'redirect_to': 'https://kyfw.12306.cn/passport/web/login',
        'testcookie' : 1,
    }
    try:
        # 不需要验证码直接登录成功
        login_page = session.post(post_url, data=postdata, headers=headers)
        login_code = login_page.text
        print(login_page.status_code)
        #print(login_code)
    except:
        pass
    session.cookies.save()
    
if __name__ == '__main__':
    agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    headers = {
        "Host": "www.santostang.com",
        "Origin":"https://kyfw.12306.cn/passport/web/login",
        "Referer":"https://kyfw.12306.cn/passport/web/login",
        'User-Agent': agent
    }
    if isLogin():
        print('您已经登录') 
    else:
        login('a12345', 'test')