from Base.Base import Base
import Page

class Login_Page(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, username, password):
        """登录"""
        # 输入用户名
        self.send_element(Page.login_name_id, username)
        # 输入密码
        self.send_element(Page.login_passwd_id, password)
        # 点击登录按钮
        self.click_element(Page.login_btn_id)

    def close_login_page(self):
        """关闭登录页面"""
        self.click_element(Page.login_close_btn_id)

    def if_login_btn(self):
        # 登录按钮是否存在， 存在返回True 不存在返回False
        try:
            self.search_element(Page.login_btn_id)
            return True
        except:
            return False
