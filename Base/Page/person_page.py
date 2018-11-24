from Base.Base import Base
import Page

class Person_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def get_mylike_data(self):
        """获取我的收藏文本"""
        return self.search_element(Page.my_like_id).text

    def click_setting_btn(self):
        """点击设置按钮"""
        self.click_element(Page.setting_btn_id)