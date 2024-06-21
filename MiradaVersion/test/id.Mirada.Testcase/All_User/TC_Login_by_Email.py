import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.loginPages import PagesLogin
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.test.id_Mirada_Login.login_by_email import (
    login_free_by_email,
    login_with_wrong_email,
)
from MiradaVersion.test.open_app import free_email_data, wrong_email_data


email_not_registered = "freerean@gmail.com"


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
def sign_up_action(driver):
    return SignUp(driver)


@pytest.fixture(scope="module")
def login_action(driver):
    return PagesLogin(driver)


def test_TC_Login_Email_User_not_able_login_User_Not_Registered(
    driver: WebDriver, sign_up_action: SignUp, login_action: PagesLogin
):

    login_action.clickLogin()
    login_action.clickEmailSection()
    sign_up_action.inputEmail(email_not_registered)
    sign_up_action.inputPassword("4321Lupa")
    login_action.clickSubmitLogin()
    login_action.assertAccountHasNotBeenRegistered()
    driver.press_keycode(4)
    driver.press_keycode(4)


def test_TC_Login_Email_Wrong_Email_or_Password(
    driver: WebDriver,
    wrong_email_data,
):
    login_with_wrong_email(driver, wrong_email_data)
    driver.press_keycode(4)


def test_TC_Login_Email_User_able_login(
    driver: WebDriver,
    free_email_data,
):
    login_free_by_email(driver, free_email_data)
