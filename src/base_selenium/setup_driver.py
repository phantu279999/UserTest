from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from src.config import settings


import chromedriver_autoinstaller
# Tự động tải chromedriver
chromedriver_autoinstaller.install()


def setup_chrome():
    option = Options()
    option.page_load_strategy = settings.PAGE_LOAD_STRATEGY

    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(settings.IMPLICITLY_WAIT)
    driver.set_page_load_timeout(settings.LOAD_TIME_OUT)
    driver.maximize_window()

    return driver

