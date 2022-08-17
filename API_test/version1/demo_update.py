# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-08-17 15:37
# className:  demo_update.py
######################################################
# 脚本说明：更新用户信息接口
# 登录接口地址：https://lefeiwisdom-3pt-2t6a7-www.vip.51env.net/api/reader/update_userinfo
# 测试数据：{"nickname": "test3", "avatar": "", "signature": "test3"}
# 版本：version1.0  token使用常量+assert断言
#######################################################
# 导库
import requests

# 定义url
url = "https://lefeiwisdom-3pt-2t6a7-www.vip.51env.net/api/reader/update_userinfo"

# 定义接口传参
testdata = {"nickname": "test2", "avatar": "", "signature": "test2"}

# 定义token参数
headdata = {"token": "93dad1b4-f60a-4689-a735-e3d1a08bd206"}

# 发送请求接收返回值
response = requests.post(url, json=testdata, headers=headdata).json()

# 比对结果，给出测试结论
print(response['msg'])

# 检查点
# 用if else 判断，很麻烦
# if response['msg'] == '修改成功!':
#     print('修改用户接口测试通过')
# else:
#     print('修改用户接口测试失败')

# 用assert断言，简洁明了
assert response['msg'] == '修改成功!'