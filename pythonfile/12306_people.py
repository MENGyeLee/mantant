import requests
import re
import os
from PIL import Image

def get_si_code():
    # si_code 是一个动态变化的参数
    index_url = 'http://www.santostang.com/wp-login.php?action=register'
    # 获取注册时需要用到的 si_code
    index_page = session.get(index_url, headers=headers)
    html = index_page.text
    pattern = r'name="si_code_reg" type="hidden"  value="(.*?)"'
    # 这里用re.search方法找到si_code
    si_code = re.search(pattern, html).group(1)
    return si_code

def get_captcha(si_code):
    captcha_url = "http://www.santostang.com/wp-content/plugins/si-captcha-for-wordpress/captcha/securimage_show.php?si_sm_captcha=1&si_form_id=reg" + si_code
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input("please input the captcha\n>")
    return captcha

def register(account, email,si_code):      
    post_url = 'http://www.santostang.com/wp-login.php?action=register'
    postdata = {
        'user_login': account,
        'user_email': email,
        'si_code_reg': si_code,
        'redirect_to': '',
        }
    # 调用get_captcha函数，获取验证码数字
    postdata["captcha"] = get_captcha(si_code)  
    # 提交POST请求，进行注册
    register_page = session.post(post_url, data=postdata, headers=headers)
    # 若输出打印结果为200，则表示注册成功
    print(register_page.status_code)


if __name__ == '__main__':
    agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    headers = {
        "Host": "www.santostang.com",
        "Origin":"https://kyfw.12306.cn",
        "Referer":"https://kyfw.12306.cn/passport/web/login",
        'User-Agent': agent
    }
    session = requests.session()
    #获取我们需要的验证码匹配码
    si_code = get_si_code()
    # 调用注册函数进行注册
    account = '15669770297'
    email = 'a12345@qq.com'
    register(account, email, si_code)