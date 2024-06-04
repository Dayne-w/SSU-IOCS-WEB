import os
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def click_by_xpath(xpath):
    error = False
    while error == False:
        try:
            driver.find_element(by=By.XPATH, value=xpath).click()
            error = True
        except:
            pass


# Assuming DRIVER_PATH is correctly defined and points to the chromedriver executable.
DRIVER_PATH = os.path.join(os.path.dirname(__file__), 'chromedriver')
service = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=service)

# 크롬드라이버가 켜졌을 때 일관성을 유지하기 위해 화면에 뜰 위치와 크기를 지정해준다.
driver.set_window_position(0, 0, windowHandle='current')
driver.set_window_size(1300, 800)

# 예약 페이지 접속
driver.get('https://dayne-w.github.io/SSU-IOCS-WEB/')

# 4월 20일 선택
click_by_xpath('/html/body/table/tbody/tr[4]/td[7]')

# 다음 버튼 클릭
click_by_xpath('//*[@id="nextButton"]')

# 19번 좌석 선택
click_by_xpath('/html/body/div/div[2]/div[9]')

# 예약하기 버튼 클릭
click_by_xpath('//*[@id="reserveButton"]')

time.sleep(120)