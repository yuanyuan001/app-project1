import sys, os, pytest
sys.path.append(os.getcwd())
from Base.page import Page
from Base.get_driver import get_driver
from Base.get_data import Get_Data
from selenium.common.exceptions import TimeoutException

def get_login_data():
    # 成功 [(),()]
    suc_list = []
    # 失败 [(),()]
    fal_list = []
    login_data = Get_Data().get_yaml_data("test_data.yml").get("Login_Data")
    for i in login_data.keys():
        if login_data.get(i).get("get_toast"):
            fal_list.append((i, login_data.get(i).get("phone"), login_data.get(i).get("passwd"),
                             login_data.get(i).get("get_toast"), login_data.get(i).get("expect_data")))
        else:
            suc_list.append((i, login_data.get(i).get("phone"), login_data.get(i).get("passwd"),
                             login_data.get(i).get("expect_data")))
    return {"suc": suc_list, "fal": fal_list}

class Test_Login:

    def setup_class(self):
        # 实例化统一入口类
        self.page_obj = Page(get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity"))
    def teardown_class(self):
        self.page_obj.driver.quit()
    @pytest.mark.parametrize("i, phone, passwd, expect_data", get_login_data().get("suc"))
    def abc_test_login_suc(self, i, phone, passwd, expect_data):
        """成功测试用例"""
        # 点击我
        self.page_obj.get_home_page_obj().click_my_btn()
        # 点击已有账号去登录
        self.page_obj.get_sign_page_obj().click_exits_account()
        # 执行登陆操作
        self.page_obj.get_login_page_obj().login(phone, passwd)
        try:
            # 取我的收藏
            my_like_text = self.page_obj.get_person_page().get_mylike_data()
            # 执行退出操作
            # 点击设置
            self.page_obj.get_person_page().click_setting_btn()
            # 点击退出
            self.page_obj.get_setting_page_obj().log_out()
            # 断言
            assert expect_data == my_like_text
        except TimeoutException:
            # 关闭登录页面
            self.page_obj.get_login_page_obj().close_login_page()
            assert False

    @pytest.mark.parametrize("i, phone, passwd, get_toast, expect_data", get_login_data().get("fal"))
    def test_login_fal(self, i, phone, passwd, get_toast, expect_data):
        """失败测试用例"""
        # 点击我
        self.page_obj.get_home_page_obj().click_my_btn()
        # 点击已有账号去登录
        self.page_obj.get_sign_page_obj().click_exits_account()
        # 执行登陆操作
        self.page_obj.get_login_page_obj().login(phone, passwd)
        try:
            # 获取toast
            toast_message = self.page_obj.get_login_page_obj().get_toast(get_toast)
            # 登录按钮是否存在
            if_login = self.page_obj.get_login_page_obj().if_login_btn()
            # 关闭页面
            self.page_obj.get_login_page_obj().close_login_page()
            # 断言
            assert toast_message == expect_data and if_login
        except TimeoutException:
            #执行退出操作
            # 点击设置
            self.page_obj.get_person_page().click_setting_btn()
            # 点击退出
            self.page_obj.get_setting_page_obj().log_out()
            # 断言
            assert False