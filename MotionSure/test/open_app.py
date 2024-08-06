from appium.webdriver.webdriver import WebDriver
import pytest
import json
from MotionSure.utils.setup import SetupAppium
from MotionSure.pages.homepagePages import HomePage
import time

# motion


@pytest.fixture(scope="module")
def driver():
    setup_appium = SetupAppium()
    yield setup_appium.driver


def openapp(driver: WebDriver):
    element_xpath = "//*[contains(@text,'Saya menyetujui dan memahami Kebijakan')]"

    try:
        time.sleep(10)
        element = HomePage.scroll_to_element(driver, element_xpath)
        print("Element found")
    except Exception as e:
        print(f"An error occurred: {e}")
