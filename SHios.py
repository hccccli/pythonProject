# 1.导入selenium
from selenium import webdriver
import time

# 2.选择让谷歌模拟的设备
mobileEmulation = {"deviceName": "iPhone X"}

# 3.将设备加入到浏览器
# 实例化谷歌浏览器加载项
options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation", mobileEmulation)
# 4.带着加载项打开百度
driver = webdriver.Chrome(options=options)
# 5.访问百度
driver.get("https://mcftbsfbkj.ugc.wb.miemie.la/H5/check_in_act?act_hid=r9g0wpk3z&is_hidden_weiban_logo=0")  # 打开手机版本百度
time.sleep(2)
# 6.打开模拟手机百度
# 7.关闭
driver.quit()
