import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.loginPages import PagesLogin
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


@pytest.fixture(scope="module")
def action2(driver):
    return PagesLogin(driver)


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


def test_TC_Register_with_Email_User_fill_Create_Password_field_with_by_8_character(
    driver: WebDriver, action: SignUp
):
    time.sleep(3)
    action.inputEmail("freetest40@visionplus.id")
    action.clickInvisiblePassword()
    action.assertInvisiblePassword()


def test_TC_Register_with_Email_User_fill_Create_Password_field_less_than_8_character(
    driver: WebDriver, action: SignUp
):
    action.clickPhoneNumberSection()
    action.clickEmailSection()
    action.inputEmail("freetest40@visionplus.id")
    action.inputPassword(wrong_password)
    action.assertPasswordDoesntMatch()


def test_TC_Register_with_Email_Wrong_OTP(driver: WebDriver, action: SignUp):
    action.clickPhoneNumberSection()
    action.clickEmailSection()
    action.inputEmail(email)
    action.inputPassword(password)
    action.clickButtonSendOtp()
    time.sleep(2)
    action.inputOTP("0000")
    action.clickSubmitRegister()
    action.assertWrongOtp()


def test_TC_Register_with_Email_Request_Otp_Second_Time(
    driver: WebDriver, action: SignUp
):

    time.sleep(125)
    action.clickButtonSendOtp()
    action.assertSendOtpSecondTime()
    otp = print_last_otp(email)
    time.sleep(2)
    action.inputOTP(otp)
    time.sleep(310)
    action.clickSubmitRegister()
    action.assertOTPExpired()


def test_TC_Register_with_Email_Account_has_Been_Registered(
    driver: WebDriver, action: SignUp, action2: PagesLogin
):
    driver.press_keycode(4)
    action.clickSignUp()
    action.assertRegisterPage()
    action.clickEmailSection()
    action.inputEmail("freetest38@visionplus.id")
    action.inputPassword(password)
    action.clickButtonSendOtp()
    action.assertRegisterHasBeenRegistered()


def test_TC_Register_with_Email_Account_has_Been_Registered_Click_Login(
    driver: WebDriver, action: SignUp, action2: PagesLogin
):
    action.clickBtnLoginFromRegister()
    action2.assertLoginPage()
    time.sleep(6)


def test_TC_Register_New_User_Email(reopendriver: WebDriver):
    time.sleep(3)
    Register_with_email(reopendriver)
