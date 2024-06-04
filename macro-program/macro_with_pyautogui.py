import os
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def click_by_xpath(xpath):
    error = False
    while not error:
        try:
            driver.find_element(by=By.XPATH, value=xpath).click()
            error = True
        except:
            pass


def wait_until_loaded_by_class(class_name):
    error = False
    while not error:
        try:
            driver.find_element(by=By.CLASS_NAME, value=class_name)
            error = True
        except:
            pass


# Assuming DRIVER_PATH is correctly defined and points to the chromedriver executable.
DRIVER_PATH = os.path.join(os.path.dirname(__file__), 'chromedriver')
service = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=service)

# 크롬드라이버가 켜졌을 때 일관성을 유지하기 위해 화면에 뜰 위치와 크기를 지정해준다.
driver.set_window_position(0, 0, windowHandle='current')
driver.set_window_size(1300, 1000)

# 예약 페이지 접속
driver.get('https://dayne-w.github.io/SSU-IOCS-WEB/')

# 크롬드라이버에 포커싱이 안되있을 경우 마우스 올려도 안뜨기 때문에  포커스 자동으로 주기
driver.switch_to.window(driver.window_handles[0])

wait_until_loaded_by_class("calendar")

# 4월 20일 좌표로 마우스 이동
pyautogui.moveTo(880, 600, 0.23)

# 4월 20일 선택
pyautogui.click()

# 다음 버튼 마우스 이동
pyautogui.moveTo(650, 870, 0.14)

# 다음 버튼 클릭
pyautogui.click()

wait_until_loaded_by_class("container")

# 19번 좌석 마우스 이동
pyautogui.moveTo(870, 660, 0.17)

# 19번 좌석 선택
pyautogui.click()

# 예약하기 버튼 이동
pyautogui.moveTo(660, 980, 0.32)

# 예약하기 버튼 클릭
pyautogui.click()

time.sleep(300)
