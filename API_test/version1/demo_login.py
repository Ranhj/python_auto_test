# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-08-17 11:12
# className:  demo_login.py
#########################################################################
# 脚本说明：登录接口自动化测试脚本面向对象封装
# 版本：version1.0
# 登录接口地址：https"//lefeiwisdom-3pt-2t6a7-www.vip.51env.net/api/login/ios_login
# 测试数据：{"mobile": "17702055670", "user_status": 10}
#########################################################################
# 导入类库文件
import requests

# 定义接口地址
url = 'https://lefeiwisdom-3pt-2t6a7-www.vip.51env.net/api/login/ios_login'

# 定义接口参数
testdata = {"mobile": "17702055670", "user_status": 10}

# 发送接口请求并获取接口返回值
response = requests.post(url, json=testdata).json()     # 得到JSON格式的响应结果

# 进行接口返回结果比对，给出测试结论
print(response)

# 获取token
token = response['data']['token']
print(token)