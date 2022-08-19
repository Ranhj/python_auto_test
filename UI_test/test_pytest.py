# *********************************************************
# 自动化测试脚本：自动化测试平台UI测试脚本V1.0
# 测试用例：3组
# 测试数据：常量
# 将脚本移植到pytest框架中
# *********************************************************
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
# *********************************************************
# 定义测试类
class Test_Django_login():
    # 测试初始化
    def setup_class(self):
        self.url = "http://testplt3.share.atstudy.com/admin/login/?next=/admin/"
        self.driver = webdriver.Chrome()

    # 测试用例1：密码为空
    def test_case1(self):
        self.driver.get(self.url)
        self.driver.find_element(By.NAME,'username').send_keys('webmaster')
        self.driver.find_element(By.NAME,'password').send_keys('')
        self.driver.find_element(By.XPATH,'//*[@id="login-form"]/div[3]/button').click()
        time.sleep(1)
        result=self.driver.find_element(By.CLASS_NAME,'el-message').text
        print(result)

    # 测试用例2：用户名密码错误
    def test_case2(self):
        time.sleep(2)
        self.driver.get(self.url)
        self.driver.find_element(By.NAME,'username').send_keys('web')
        self.driver.find_element(By.NAME,'password').send_keys('web')
        self.driver.find_element(By.XPATH,'//*[@id="login-form"]/div[3]/button').click()
        result=self.driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div').text
        print(result)

    # 测试用例3：用户名密码正确
    @pytest.mark.smoke
    def test_case3(self):
        time.sleep(2)
        self.driver.get(self.url)
        self.driver.find_element(By.NAME,'username').send_keys('webmaster')
        self.driver.find_element(By.NAME,'password').send_keys('atplt2021')
        self.driver.find_element(By.XPATH,'//*[@id="login-form"]/div[3]/button').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        result=self.driver.find_element(By.XPATH,'//*[@id="main"]/section/section/header/div/div[2]/div/button/span').text
        print(result)
        assert result=='admin'

    # 回收测试资源
    def teardown_class(self):
        self.driver.quit()
# if __name__ == '__main__':
#     pytest.main()