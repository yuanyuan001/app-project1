
"""
首页
"""
# 我的
from selenium.webdriver.common.by import By

my_btn_id = (By.ID, "com.yunmall.lc:id/tab_me")
"""
注册页面
"""
# 已有账号去登录
exits_account_btn_id = (By.ID, "com.yunmall.lc:id/textView1")
"""
登录页面
"""
# 用户名输入框
login_name_id = (By.ID, "com.yunmall.lc:id/logon_account_textview")
# 密码输入框
login_passwd_id = (By.ID, "com.yunmall.lc:id/logon_password_textview")
# 登录按钮
login_btn_id = (By.ID, "com.yunmall.lc:id/logon_button")
# 关闭登录页面按钮
login_close_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")
"""
个人中心页面
"""
# 我的收藏按钮
my_like_id = (By.ID, "com.yunmall.lc:id/txt_my_shoppingcart")
# 设置按钮
setting_btn_id= (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")
"""
设置页面
"""
# 退出按钮
logout_btn_id = (By.ID, "com.yunmall.lc:id/setting_logout")
# 确认退出按钮
access_logout_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")
# 取消退出按钮
dismiss_log_out_btn_id = (By.ID, "com.yunmall.lc:id/ymdialog_left_button")