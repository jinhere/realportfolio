from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#browser=webdriver.Chrome("C:\\Users\\Notebook\\Downloads\\chromedriver_win32\\chromedriver.exe")

browser=webdriver.Edge("C:\\Users\\user\\Downloads\\edgedriver_win64\\msedgedriver.exe")
browser.get('https://id.iamservice.net/login?serviceId=partner&channelId=iamclass&nextUrl=https%3A%2F%2Fclass.iamservice.net%2Flogin%2Fcallback')
elem=browser.find_element_by_id("id")

elem.send_keys("74103177")
elem=browser.find_element_by_id("password")
elem.send_keys("10261026*")
elem=browser.find_element_by_id("login_btn")
elem.click()
time.sleep(2)
elem=browser.find_element_by_xpath('//*[@id="rzbesqkq54-close"]') #est,grace
elem.click()
elem=browser.find_element_by_link_text("알림장")
elem.click()
time.sleep(5)
elem=browser.find_element_by_link_text("알림장 작성")
elem.click()
#time.sleep(1)
#elem=browser.find_element_by_xpath('//*[@id="class3"]')
#elem.click()
i=0
for x in range(1):
    i+=1
    browser.execute_script('window.open("https://class.iamservice.net/agenda#/add");')
time.sleep(4)   
for y in range(i):
    browser.switch_to.window(browser.window_handles[y+1])
    elem2=browser.find_element_by_id("cont_txt")
    #elem2.send_keys("안녕하세요.\n지난 달(11월) Monthly Report 보내 드립니다.\n참고 부탁드립니다.\n감사합니다:)")   
    elem2.send_keys("안녕하세요.\n지난주 (1/3-1/7) Weekly Report 올려 드립니다.\n참고 부탁드립니다.\n감사합니다^^")   

    
    elem=browser.find_element_by_xpath('//*[@id="class3"]')
    elem.click()
    browser.find_element_by_xpath('//*[@id="cont_txt"]').send_keys(Keys.PAGE_DOWN)
    time.sleep(2)