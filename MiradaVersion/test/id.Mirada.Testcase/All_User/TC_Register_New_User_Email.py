import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.test.id_Mirada_Register.TC_register_with_email import (
    Register_with_email,
    generate_random_email,
)
from MiradaVersion.test.TC_Get_OTP import print_last_otp

domains = ["visionplus.id"]
first_names = ["Testing"]

email = generate_random_email(domains, first_names)

password = "4321Lupa"
wrong_password = "4321Lup"
wrong_email = "Freetest.mail.com"


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


def test_TC_Unverified_Account_Email(driver: WebDriver, action: SignUp):

    action.clickSignUp()
    action.assertRegisterPage()
    action.clickEmailSection()
    action.inputEmail("freetest38@visionplus.id")
    action.inputPassword(password)
    action.clickButtonSendOtp()
    action.assertRegisterHasBeenRegistered()
    driver.press_keycode(4)


def test_TC_Register_with_Email_Invalid_Format(driver: WebDriver, action: SignUp):
    action.inputEmail(wrong_email)
    action.assertEmailInvalidFormat()


def test_TC_Register_New_User_Email(reopendriver: WebDriver):
    time.sleep(3)
    Register_with_email(reopendriver)
