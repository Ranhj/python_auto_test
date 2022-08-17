# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-08-17 16:03
# className:  demo_token_assert.py
######################################################
# 脚本说明：登录接口+更新接口联调
# 传入参数token+assert断言
# 版本：version1.0
#######################################################

# 导入类库文件
import requests

# 封装登录接口
def demo_login():
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
    return token    # 下一个方法要使用到这个token时，就return token


# 封装修改接口
def demo_update(token1):     # 传入token
    # 定义url
    url = "https://lefeiwisdom-3pt-2t6a7-www.vip.51env.net/api/reader/update_userinfo"

    # 定义接口传参
    testdata = {"nickname": "test5", "avatar": "", "signature": "test5"}

    # 定义token参数
    headdata = {"token": token1}     # 传入token，此处的token参数名（token1）必须与定义本方法时传入的token参数名一致，就是外部不管他，但是方法内部必须参数名一致

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


if __name__ == '__main__':
    token = demo_login()
    demo_update(token)