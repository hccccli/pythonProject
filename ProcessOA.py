from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path=r"C:\Users\litong\AppData\Local\Programs\Python\Python39\Scripts\chromedriver.exe")
#driver.get("https://www.jd.com/")
#time.sleep(3)
driver.get('http://cmsoft.cmss.cmcc/portal/#/sidebar/index')
driver.maximize_window()

'''
调用selenium库中的find_element_by_xpath()方法定位搜索框，
同时使用send_keys()方法在其中输入信息
调用selenium库中的find_element_by_xpath()方法定位搜索按钮，
同时使用click()方法对按钮进行点击
'''

# driver.implicitly_wait(2) # seconds
WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//div[@class='login']")).click()
driver.find_element_by_xpath('//*[@id="username"]').send_keys('litong')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('MM2li78!@')
WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//*[@id="submitButton"]')).click()

time.sleep(2)
driver.refresh()

def OA():
        time.sleep(2)
        #option('0为公文，1为邮件')
        driver.find_element(By.XPATH,"//span[contains(text(),'我的待办')]/parent::div").click()
        time.sleep(2)
        wins = driver.window_handles
        business=driver.find_elements(By.XPATH,"//span[text()='业务联系单']")
        for i in range(len(business)):
            business[i].click()
            readtext(1)
            driver.switch_to.window(wins[0])
            time.sleep(2)

        receive=driver.find_elements(By.XPATH,"//span[text()='收文']")
        for i in range(len(receive)):
            receive[i].click()
            readtext(0)
            driver.switch_to.window(wins[0])
            time.sleep(2)

def readtext(n):
        framelist=["layui-layer-iframe11","layui-layer-iframe2",]
        #//input[starts-with(@name,'name1')];
        wins = driver.window_handles
        print(wins)
        driver.switch_to.window(wins[-1])
        print("切换之后的句柄：",driver.current_window_handle)
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@title='办理完成']").click()
        #WebDriverWait(driver,10).until(lambda driver:driver.switch_to.frame('layui-layer-iframe8'))
        driver.switch_to.frame(framelist[n])
        time.sleep(5)

        WebDriverWait(driver,10).until(lambda driver:driver.find_element(By.XPATH,'//*[@id="okbtn"]')).click()
if __name__=="__main__":
       OA()
       time.sleep(5)

#    driver.quit()
