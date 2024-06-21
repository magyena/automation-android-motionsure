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
def sign_up_action(driver):
    return SignUp(driver)


@pytest.fixture(scope="module")
def login_action(driver):
    return PagesLogin(driver)


def test_TC_Unverified_Account_Email(driver: WebDriver, sign_up_action: SignUp):

    sign_up_action.clickSignUp()
    sign_up_action.assertRegisterPage()
    sign_up_action.clickEmailSection()
    sign_up_action.inputEmail("freetest38@visionplus.id")
    sign_up_action.inputPassword(password)
    sign_up_action.clickButtonSendOtp()
    sign_up_action.assertRegisterHasBeenRegistered()
    driver.press_keycode(4)


def test_TC_Register_with_Email_Invalid_Format(
    driver: WebDriver, sign_up_action: SignUp
):
    sign_up_action.inputEmail(wrong_email)
    sign_up_action.assertEmailInvalidFormat()


def test_TC_Register_with_Email_User_fill_Create_Password_field_with_by_8_character(
    driver: WebDriver, sign_up_action: SignUp
):
    time.sleep(3)
    sign_up_action.inputEmail("freetest40@visionplus.id")
    sign_up_action.clickInvisiblePassword()
    sign_up_action.assertInvisiblePassword()


def test_TC_Register_with_Email_User_fill_Create_Password_field_less_than_8_character(
    driver: WebDriver, sign_up_action: SignUp
):
    sign_up_action.clickPhoneNumberSection()
    sign_up_action.clickEmailSection()
    sign_up_action.inputEmail("freetest40@visionplus.id")
    sign_up_action.inputPassword(wrong_password)
    sign_up_action.assertPasswordDoesntMatch()


def test_TC_Register_with_Email_Wrong_OTP(driver: WebDriver, sign_up_action: SignUp):
    sign_up_action.clickPhoneNumberSection()
    sign_up_action.clickEmailSection()
    sign_up_action.inputEmail(email)
    sign_up_action.inputPassword(password)
    sign_up_action.clickButtonSendOtp()
    time.sleep(2)
    sign_up_action.inputOTP("0000")
    sign_up_action.clickSubmitRegister()
    sign_up_action.assertWrongOtp()


def test_TC_Register_with_Email_Request_Otp_Second_Time(
    driver: WebDriver, sign_up_action: SignUp
):

    time.sleep(125)
    sign_up_action.clickButtonSendOtp()
    sign_up_action.assertSendOtpSecondTime()
    otp = print_last_otp(email)
    time.sleep(2)
    sign_up_action.inputOTP(otp)
    time.sleep(310)
    sign_up_action.clickSubmitRegister()
    sign_up_action.assertOTPExpired()


def test_TC_Register_with_Email_Account_has_Been_Registered(
    driver: WebDriver, sign_up_action: SignUp, login_action: PagesLogin
):
    driver.press_keycode(4)
    sign_up_action.clickSignUp()
    sign_up_action.assertRegisterPage()
    sign_up_action.clickEmailSection()
    sign_up_action.inputEmail("freetest38@visionplus.id")
    sign_up_action.inputPassword(password)
    sign_up_action.clickButtonSendOtp()
    sign_up_action.assertRegisterHasBeenRegistered()


def test_TC_Register_with_Email_Account_has_Been_Registered_Click_Login(
    driver: WebDriver, sign_up_action: SignUp, login_action: PagesLogin
):
    sign_up_action.clickBtnLoginFromRegister()
    login_action.assertLoginPage()
    time.sleep(6)


def test_TC_Register_New_User_Email(reopendriver: WebDriver):
    time.sleep(3)
    Register_with_email(reopendriver)
