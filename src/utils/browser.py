from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


def open_browser() -> WebDriver:
    return webdriver.Chrome()


def navigate_to(driver: WebDriver, url: str) -> None:
    driver.maximize_window()
    driver.get(url)


def wait_element(driver: WebDriver, locator: tuple, timeout: int = 10) -> WebElement:
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
