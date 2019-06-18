import requests
import config

person=requests.session()
login_url='https://kyfw.12306.cn.otn/login/init'

login_response=person.get(login_url)

captcha_url='https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.785280601210562'

captcha_response=person.get(captcha_url)
captcha_content=captcha_response.content

fb=open('captcha.jpg','wb')
fb.write(captcha_content)
fb.close

check_url='https://kyfw.12306.cn/passport/captcha/captcha-check'
data={
    'answer':input('请输入验证码坐标》》》:'),
    'login_site':'E',
    'rand':'sjrand'
}
check_response=person.post(check_url,data=data)
res=check_response.json()
if not res['result_code']=='4':
    exit('验证码校验失败')

login_url='https://kyfw.12306.cn/passport/web/login'
login_data={
    'username': config.username,
    'password': config.password,
    'appid':'otn'
}
login_res=person.post(login_url,data=login_url)
if login_res.json()['result_code']!=0:
    exit('用户名密码错误')
    
token_url='https://kyfw.12306.cn/passport/web/auth/uamtk'
token_data={
    'appid':'otn',
}
token_response=person.post(token_url,data=token_data)
token_res=token_response.json()

auth_url='https://kyfw.12306.cn/otn/uamauthclient'
auth_data={
    'tk':token_res['newapptk']
}

auth_response=person.post(auth_url,data=auth_data)
print(auth_response.text)