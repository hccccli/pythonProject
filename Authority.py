from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome(executable_path=r"C:\Users\litong\AppData\Local\Programs\Python\Python39\Scripts\chromedriver.exe")
#driver.get("https://www.jd.com/")
#time.sleep(3)
driver.implicitly_wait(45) # seconds
driver.maximize_window()
t=5
def login():
    driver.get('http://ccops-paas.cmecloud.cn/o/ops-portal/#/main/index')
    time.sleep(t)
    driver.find_element_by_xpath('//*[@id="user"]').send_keys('')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('')
    driver.find_element_by_xpath('//*[@id="code-btn"]').click()
    code=input('input code')
    driver.find_element_by_xpath('//*[@id="verify_code"]').send_keys(code)
    driver.find_element_by_xpath('//*[@id="login-btn"]').click()
    time.sleep(2*t)

def mainpage(name='工单系统'):
    ActionChains(driver).move_by_offset(300, 200).click().perform() # 鼠标左键点击， 200为x坐标， 100为y坐标
    ActionChains(driver).move_to_element(driver.find_element_by_xpath("//a[@class='tools-link bk-menu-item']")).perform()  # perform代表执行的意思
    #time.sleep(1)
    page = "//span[contains(text(),'" + name + "')]"
    driver.find_element_by_xpath(page).click()
    wins = driver.window_handles
    print(wins)
    driver.switch_to.window(wins[-1])
    driver.find_element_by_xpath("//span[contains(.,'新建工单')]/preceding-sibling::i").click()
def oder4A():

    #time.sleep(2)
    driver.find_element_by_xpath("//h1[contains(.,'权限申请流程')]/parent::div").click()
    driver.switch_to.window(driver.window_handles[-1])
    str1='监控调度一组PAAS/SAAS条线现网-云解析等资源4A权限申请'
    str2='监控调度一组PAAS/SAAS条线现网-云解析等资源4A权限申请\n因涉及多个人申请同样的权限，故申请人员名单以附件形式上传，请知悉。'
    driver.find_element_by_xpath('//*[@id="title"]').send_keys(str1)
    driver.find_element_by_xpath('//textarea[@placeholder="请输入"]').send_keys(str2)
    driver.find_element_by_xpath('//input[@name="file"]').send_keys(r"C:\Users\litong\Desktop\PAASSAAS账号清单.xlsx")

    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # 定位到资源池下拉框元素
    driver.find_elements(By.XPATH,"//input[@type='text']")[1].click()
    time.sleep(t)
    driver.find_element_by_xpath("//span[contains(.,'广西')]/ancestor::li").click()
    #定位到应用系统下拉框
    driver.find_elements(By.XPATH,"//input[@type='text']")[2].click()
    time.sleep(t)
    driver.find_element_by_xpath("//span[contains(.,'移动云帮助中心')]/ancestor::li").click()
    #定位到权限类型
    driver.find_elements(By.XPATH,"//input[@type='text']")[3].click()
    time.sleep(t)
    driver.find_element_by_xpath("//span[contains(.,'4A权限')]/ancestor::li").click()
    #定位到权限申请维度
    driver.find_elements(By.XPATH,"//input[@type='text']")[4].click()
    time.sleep(t)
    driver.find_element_by_xpath("//span[contains(.,'4A角色')]/ancestor::li").click()

    driver.find_elements(By.XPATH,"//input[@type='text']")[5].click()
    time.sleep(t)
    driver.find_elements(By.XPATH,"//span[contains(.,'否')]")[1].click()

    driver.find_elements(By.XPATH, "//input[@type='text']")[6].click()
    time.sleep(t)
    driver.find_elements(By.XPATH,"//span[contains(.,'否')]")[1].click()
    #开始时间
    driver.find_elements(By.XPATH, "//input[@type='text']")[7].click()
    time.sleep(t)
    day=datetime.date.today().day+1
    begin="//span[contains(text(),'"+str(day)+"')]"
    driver.find_element_by_xpath(begin).click()

    #结束时间
    driver.find_elements(By.XPATH, "//input[@type='text']")[8].click()
    time.sleep(t)
    driver.find_elements(By.XPATH,"//button[@aria-label='后一年']")[1].click()
    driver.find_elements(By.XPATH,begin)[1].click()
# 创建一个下拉框对象
#sel = Select(el_select)
#sel.select_by_index(0)
#增加4A账号与从账号、资源组
def account(n=1):
    for i in range(n):
        driver.find_element_by_xpath('//span[contains(text(),"增加")]//ancestor::button').click()
        driver.find_elements(By.XPATH,"//input[@placeholder='请输入4A账号名称']")[i].send_keys('litong')
        driver.find_elements(By.XPATH,"//input[@placeholder='请输入从账号']")[i].send_keys('deployer')
        driver.find_elements(By.XPATH, "//input[@placeholder='请输入4A账号名称']/ancestor::tr//span[@class='el-checkbox__inner']")[i].click()
        driver.find_element_by_xpath('//button[contains(.,"批量设置角色组")]').click()
        #申请4A资源角色组权限
        driver.find_element_by_xpath('//input[@placeholder="请输入IP"]').clear()
        driver.find_element_by_xpath('//input[@placeholder="请输入IP"]').send_keys('10.180.41.57')
        driver.find_element_by_xpath('//span[contains(text(),"搜索")]//ancestor::button').click()
        time.sleep(t+10)
        driver.find_element_by_xpath('//div[contains(text(),"apps")]//ancestor::tr//td[1]//span').click()
        driver.find_element_by_xpath('//div[contains(text(),"deployer")]//ancestor::tr//td[1]//span').click()
        #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.find_element_by_xpath('//span//button[@class="el-button el-button--primary"]').click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
def submmit():
    #滑动到底部
    #driver.close()
    driver.find_elements(By.XPATH,"//input[@placeholder='请选择']")[6].send_keys(Keys.PAGE_DOWN)
    time.sleep(t)
    driver.find_elements(By.XPATH,"//input[@placeholder='请选择']")[6].click()
    driver.find_element_by_xpath("//span[contains(.,'唐鹏')]/ancestor::li").click()
    driver.find_element_by_xpath("//span[contains(.,'保存草稿')]/ancestor::button").click()
    time.sleep(t)
    driver.find_elements(By.XPATH,"//span[contains(.,'确定')]")[4].click()

if __name__=='__main__':
    login()
    mainpage("工单系统")
    oder4A()
    account(3)
    submmit()





