from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Base:

    def __init__(self, driver):
        self.driver = driver
    def search_element(self, loc, timeout=10, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: 元祖 (By.ID,ID属性值) (By.CLASS_NAME,CLASS属性值) (By.XPATH,XPATH属性值)
        :param timeout: 搜索元素超时时间
        :param poll_frequency: 搜索间隔
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def search_elements(self, loc, timeout=10, poll_frequency=1.0):
        """
        定位一组元素
        :param loc: 元祖 (By.ID,ID属性值) (By.CLASS_NAME,CLASS属性值) (By.XPATH,XPATH属性值)
        :param timeout: 搜索元素超时时间
        :param poll_frequency: 搜索间隔
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=10, poll_frequency=1):
        """
        点击元素
        :param loc: 元祖 (By.ID,ID属性值) (By.CLASS_NAME,CLASS属性值) (By.XPATH,XPATH属性值)
        :param timeout: 搜索元素超时时间
        :param poll_frequency: 搜索间隔
        :return:
        """
        self.search_element(loc, timeout, poll_frequency).click()

    def send_element(self, loc, text, timeout=10, poll_frequency=1):
        """
        输入文本内容方法
        :param loc: 元祖 (By.ID,ID属性值) (By.CLASS_NAME,CLASS属性值) (By.XPATH,XPATH属性值)
        :param text: 发送文本内容
        :param timeout: 搜索元素超时时间
        :param poll_frequency: 搜索间隔
        :return:
        """
        input_text = self.search_element(loc, timeout, poll_frequency)
        # 清空输入框
        input_text.clear()
        # 输入内容
        input_text.send_keys(text)
    def screen_scoll(self, scroll_tag):
        """
        滑动屏幕方法
        :param scroll_tag: 1 向上滑动 2 向下滑动 3 向左滑动 4 向右滑动
        :return:
        """
        import time
        time.sleep(2)
        # ('width', 'height')
        screen_size = self.driver.get_window_size()
        # 宽
        width = screen_size.get("width")
        # 高
        height = screen_size.get("height")
        if scroll_tag == 1:
            self.driver.swipe(width*0.5, height*0.8, width*0.5, height*0.3)
        if scroll_tag == 2:
            self.driver.swipe(width*0.5, height*0.3, width*0.5, height*0.8)
        if scroll_tag == 3:
            self.driver.swipe(width*0.8, height*0.5, width*0.3, height*0.5)
        if scroll_tag == 4:
            self.driver.swipe(width*0.3, height*0.5, width*0.8, height*0.5)

    def get_toast(self, mes):
        """获取toast消息"""
        toast_mes_xpath = "//*[contains(@text,'{}')]".format(mes)
        # toast获取提示消息
        toast_message = self.search_element((By.XPATH, toast_mes_xpath), timeout=5, poll_frequency=0.5).text

        return toast_message