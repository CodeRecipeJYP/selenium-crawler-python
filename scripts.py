#-*- coding: utf-8 -*-
import time

from selenium.webdriver.common.keys import Keys
import selenium.webdriver.chrome.service as service
from selenium import webdriver

from src.config import MY_ACCOUNT, MY_PASSWORD


def open_browser():
    CHROMEDRIVER_PATH = '/Users/jaeyoung/workspace/python/PycharmProjects/정리필요/kucc_seminar_crawling/chromedriver'
    chrome_service = service.Service(CHROMEDRIVER_PATH)
    chrome_service.start()

    capabilities = {'chrome.binary': CHROMEDRIVER_PATH}
    return webdriver.Remote(chrome_service.service_url, capabilities)

def login(driver):
    ID_NAME = "user_id"
    PW_NAME = "password"

    elements_id = driver.find_element_by_name(ID_NAME)
    elements_pw = driver.find_element_by_name(PW_NAME)


    # elements.send_keys()
    print("sendkeys")
    elements_id.send_keys(MY_ACCOUNT)
    elements_pw.send_keys(MY_PASSWORD, Keys.ENTER)

def goto_site(driver,TARGET_URL):

    driver.get(TARGET_URL)

def join_board(driver,boardname):
    elements_board_link = driver.find_element_by_partial_link_text(boardname)
    elements_board_link.click()

def click_post_by_keyword(driver, keyword):
    elements_board_link = driver.find_elements_by_partial_link_text(keyword)
    print(len(elements_board_link))
    num_elements=len(elements_board_link)

    for idx in range(num_elements):
        elements_board_link = driver.find_elements_by_partial_link_text(keyword)

        print("idx : {}".format(idx))
        each = elements_board_link[idx]
        print(each)
        each.click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

TARGET_HOST = 'https://www.koreapas.com/'
TARGET_ENDPOINT = ""
TARGET_URL = TARGET_HOST+TARGET_ENDPOINT
BOARD_NAME ="소비자포럼"
KEYWORD = "전주"

driver = open_browser()
goto_site(driver,TARGET_URL)
login(driver)
time.sleep(1)
print("join_board")
join_board(driver,BOARD_NAME)
time.sleep(1)
print("click_post_by_keyword")
click_post_by_keyword(driver, KEYWORD)


time.sleep(20)
driver.quit()