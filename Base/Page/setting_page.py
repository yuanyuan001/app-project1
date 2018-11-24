from Base.Base import Base
import Page

class Setting_Page(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def log_out(self, logout_tag=1):
        """退出
            logout_tag: 1退出  非1 取下退出
        """
        # 向上滑动屏幕
        self.screen_scoll(1)
        # 点击退出按钮
        self.click_element(Page.logout_btn_id)
        # 点击确认退出按钮
        if logout_tag ==1:
            # 退出操作
            self.click_element(Page.access_logout_btn_id)
        else:
            # 取消退出操作
            self.click_element(Page.dismiss_log_out_btn_id)