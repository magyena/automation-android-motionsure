import pytest
import time
from typing import Tuple
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.pages.loginPages import PagesLogin
from MiradaVersion.test.id_Mirada_Register.TC_register_with_phone import (
    Register_with_phone,
)
from MiradaVersion.test.id_Mirada_Register.TC_register_with_phone import (
    generate_random_phone_number,
)
from MiradaVersion.test.TC_Get_OTP import print_last_otp

phone_number = generate_random_phone_number()

password = "4321Lupa"
wrong_password = "4321Lup"


@pytest.fixture(scope="module")
def driver():
    setup_appium = SetupAppium()
    driver = setup_appium.driver
    yield driver
    time.sleep


@pytest.fixture(scope="module")
def reopendriver():
    setup_appium = SetupAppium()
    driver = setup_appium.driver
    yield driver
    time.sleep


@pytest.fixture(scope="module")
def sign_up_action(driver):
    return SignUp(driver)


@pytest.fixture(scope="module")
def login_action(driver):
    return PagesLogin(driver)


def test_TC_User_Click_Terms_of_Use(driver: WebDriver, sign_up_action: SignUp):
    sign_up_action.clickTermsOfUse()
    time.sleep(2)
    driver.press_keycode(4)
    # driver.press_keycode(4)


def test_TC_User_Click_Privacy_Policy(driver: WebDriver, sign_up_action: SignUp):
    sign_up_action.clickPrivacyPolicy()
    time.sleep(2)
    driver.press_keycode(4)
    # driver.press_keycode(4)


def test_TC_Unverified_Account_Phone_Number(driver: WebDriver, sign_up_action: SignUp):

    sign_up_action.clickSignUp()
    sign_up_action.assertRegisterPage()
    time.sleep(2)
    sign_up_action.inputPhoneNumber("888111222333")
    time.sleep(2)
    sign_up_action.inputPassword(password)
    time.sleep(2)
    sign_up_action.clickButtonSendOtp()
    time.sleep(2)
    sign_up_action.clickSendViaSms()
    time.sleep(2)
    sign_up_action.assertRegisterHasBeenRegistered()
    driver.press_keycode(4)


def test_Register_with_phone_Number_and_user_can_select_Country(
    driver: WebDriver, sign_up_action: SignUp
):

    sign_up_action.clickCountry()
    time.sleep(2)
    sign_up_action.assertCountryCode()
    time.sleep(2)
    sign_up_action.clickCountryMalaysia()
    time.sleep(2)
    sign_up_action.assertCountryCodeAfterChooseMalaysia()


def test_Register_with_phone_Number_and_user_can_search_Country(
    driver: WebDriver, sign_up_action: SignUp
):

    sign_up_action.clickCountry()
    time.sleep(2)
    sign_up_action.assertCountryCode()
    time.sleep(2)
    sign_up_action.inputCountryCodeNetherlands("Netherland")
    time.sleep(2)
    sign_up_action.clickResultSearchCountry()
    time.sleep(2)
    sign_up_action.assertCountryCodeAfterChooseNetherland()


def test_Register_with_phone_Number_and_user_can_search_Country_back_Default(
    driver: WebDriver, sign_up_action: SignUp
):  
    time.sleep(2)
    sign_up_action.clickCountry()
    time.sleep(2)
    sign_up_action.assertCountryCode()
    time.sleep(2)
    sign_up_action.clickCountryIndonesia()
    time.sleep(2)
    sign_up_action.assertCountryCodeAfterChooseIndonesia()


def test_Register_with_phone_Number_and_User_Input_Wrong_Keyword(
    driver: WebDriver, sign_up_action: SignUp
):

    sign_up_action.clickCountry()
    time.sleep(2)
    sign_up_action.assertCountryCode()
    time.sleep(2)
    sign_up_action.inputCountryCodeNetherlands("asdadqe213f")
    time.sleep(2)
    sign_up_action.assertNoCountryFound()
    time.sleep(2)
    sign_up_action.clickBtnCloseCountryCode()
    


def test_Register_with_phone_Number_Incorrect(
    driver: WebDriver, sign_up_action: SignUp
):
    time.sleep(2)
    sign_up_action.inputPhoneNumber("11111")
    sign_up_action.assertPhoneNumberIncorrect()


def test_Register_with_phone_Number_Special_Character(
    driver: WebDriver, sign_up_action: SignUp
):
    time.sleep(2)
    sign_up_action.inputPhoneNumber("22232")
    sign_up_action.assertPhoneNumberIncorrect()


def test_Register_with_Phone_Number_User_fill_Create_Password_field_with_by_8_character(
    driver: WebDriver, sign_up_action: SignUp
):
    sign_up_action.clickEmailSection()
    time.sleep(2)
    sign_up_action.clickPhoneNumberSection()
    time.sleep(2)
    sign_up_action.inputPhoneNumber("888111222333")
    time.sleep(2)
    sign_up_action.inputPassword(password)
    time.sleep(2)
    sign_up_action.clickInvisiblePassword()
    time.sleep(2)
    sign_up_action.assertInvisiblePassword()


def test_Register_with_Phone_Number_User_fill_Create_Password_field_less_than_8_character(
    driver: WebDriver, sign_up_action: SignUp
):
    sign_up_action.clickEmailSection()
    time.sleep(2)
    sign_up_action.clickPhoneNumberSection()
    time.sleep(2)
    sign_up_action.inputPhoneNumber("888111222333")
    time.sleep(2)
    sign_up_action.inputPassword(wrong_password)
    time.sleep(2)
    sign_up_action.assertPasswordDoesntMatch()


def test_Register_with_Phone_Number_Wrong_OTP(
    driver: WebDriver, sign_up_action: SignUp
):

    sign_up_action.inputPhoneNumber(phone_number)
    time.sleep(2)
    sign_up_action.inputPassword(password)
    time.sleep(2)
    sign_up_action.clickButtonSendOtp()
    time.sleep(2)
    sign_up_action.assertSendOtpViaMessage()
    time.sleep(2)
    sign_up_action.clickSendViaSms()
    time.sleep(2)
    sign_up_action.inputOTP("0000")
    sign_up_action.clickSubmitRegister()
    sign_up_action.assertWrongOtp()


def test_Register_with_Phone_Number_Request_Otp_Second_Time(
    driver: WebDriver, sign_up_action: SignUp
):

    time.sleep(125)
    sign_up_action.clickButtonSendOtp()
    time.sleep(2)
    sign_up_action.assertSendOtpViaMessage()
    time.sleep(2)
    sign_up_action.clickSendViaSms()
    time.sleep(2)
    sign_up_action.assertSendOtpSecondTime()
    otp = print_last_otp(phone_number)
    time.sleep(3)
    sign_up_action.inputOTP(otp)
    time.sleep(310)


def test_Register_with_Phone_Number_OTP_Expired_After_2_minutes(
    driver: WebDriver, sign_up_action: SignUp
):
    sign_up_action.clickSubmitRegister()
    time.sleep(2)
    sign_up_action.assertOTPExpired()


def test_Register_with_Phone_Number_Input_Invalid_Phone_Number(
    driver: WebDriver, sign_up_action: SignUp
):  
    time.sleep(2)
    sign_up_action.inputPhoneNumber("11111")
    sign_up_action.assertInvalidPhoneNumber()


def test_Register_with_Phone_Number_Click_Icon_Eyes_Password(
    driver: WebDriver, sign_up_action: SignUp
):  
    time.sleep(2)
    sign_up_action.inputPhoneNumber("111111111")
    time.sleep(2)
    sign_up_action.inputPassword("4321Lupa")
    sign_up_action.clickInvisiblePassword()
    sign_up_action.assertInvisiblePassword()


def test_Register_with_Phone_Number_Account_has_Been_Registered(
    driver: WebDriver, sign_up_action: SignUp
):
    driver.press_keycode(4)
    sign_up_action.clickSignUp()
    sign_up_action.assertRegisterPage()
    time.sleep(2)
    sign_up_action.inputPhoneNumber("888111222333")
    time.sleep(2)
    sign_up_action.inputPassword(password)
    time.sleep(2)
    sign_up_action.clickButtonSendOtp()
    time.sleep(2)
    sign_up_action.clickSendViaSms()
    sign_up_action.assertRegisterHasBeenRegistered()


def test_TC_Register_with_Phone_Number_Account_has_Been_Registered_Click_Login(
    driver: WebDriver, sign_up_action: SignUp, login_action: PagesLogin
):
    sign_up_action.clickBtnLoginFromRegister()
    login_action.assertLoginPage()


def test_TC_Register_New_User_Phone_Number(reopendriver: WebDriver):
    time.sleep(3)
    Register_with_phone(reopendriver)
