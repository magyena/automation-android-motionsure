import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.loginPages import PagesLogin
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.test.id_Mirada_Login.login_by_phone import login_free_by_phone
from MiradaVersion.test.open_app import free_phone_data

phone_not_registered = "878787878"


@pytest.fixture(scope="module")
def driver():
    setup_appium = SetupAppium()
    driver = setup_appium.driver
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def reopendriver():
    setup_appium = SetupAppium()
    driver = setup_appium.driver
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def action(driver):
    return SignUp(driver)


@pytest.fixture(scope="module")
def action2(driver):
    return PagesLogin(driver)


def test_TC_Login_Phone_Number_User_not_able_login_User_Not_Registered(
    driver: WebDriver, action: SignUp, action2: PagesLogin
):

    action2.clickLogin()
    action.inputPhoneNumber(phone_not_registered)
    action.inputPassword("4321Lupa")
    action2.clickSubmitLogin()
    action2.assertAccountHasNotBeenRegistered()
    driver.press_keycode(4)
    driver.press_keycode(4)


def test_TC_Login_Phone_Number_User_able_login(
    driver: WebDriver, action: SignUp, action2: PagesLogin, free_phone_data
):
    login_free_by_phone(driver, free_phone_data)
