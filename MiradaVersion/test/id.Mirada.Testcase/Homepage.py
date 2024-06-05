from appium.webdriver.webdriver import WebDriver
import pytest
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.loginPages import PagesLogin


@pytest.fixture(scope="module")
def driver():
    setup_appium = SetupAppium()
    yield setup_appium.driver