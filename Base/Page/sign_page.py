from Base.Base import Base
import Page

class Sign_page(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_exits_account(self):
        """点击已有账户 去登录"""
        self.click_element(Page.exits_account_btn_id)