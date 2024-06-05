from appium.webdriver.webdriver import WebDriver
import pytest
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.loginPages import PagesLogin


@pytest.fixture(scope="module")
def driver():
    setup_appium = SetupAppium()
    yield setup_appium.driver


def test_loginByEmailSuccess(driver: WebDriver):
    login_action = PagesLogin(driver)

    login_action.goToLoginByEmail()
    login_action.inputLoginFreeCredentials("michaeltesting99@visionplus.id", "4321Lupa")
    login_action.clickSubmitLogin()
    login_action.assertMyProfile()
