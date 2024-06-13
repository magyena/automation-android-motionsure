import pytest
import time
from typing import Tuple
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.homepagePages import HomePage
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
def action(driver):
    return SignUp(driver)


def test_TC_User_Click_Terms_of_Use(driver: WebDriver, action: SignUp):
    action.clickTermsOfUse()
    time.sleep(2)
    driver.press_keycode(4)


def test_TC_User_Click_Privacy_Policy(driver: WebDriver, action: SignUp):
    action.clickPrivacyPolicy()
    time.sleep(2)
    driver.press_keycode(4)


def test_TC_Unverified_Account(driver: WebDriver, action: SignUp):

    action.clickSignUp()
    action.assertRegisterPage()
    action.inputPhoneNumber("888111222333")
    action.inputPassword(password)
    action.clickButtonSendOtp()
    action.clickSendViaSms()
    action.assertRegisterHasBeenRegistered()
    driver.press_keycode(4)


def test_Register_with_phone_Number_and_user_can_select_Country(
    driver: WebDriver, action: SignUp
):

    action.clickCountry()
    action.assertCountryCode()
    action.clickCountryMalaysia()
    action.assertCountryCodeAfterChooseMalaysia()


def test_Register_with_phone_Number_and_user_can_search_Country(
    driver: WebDriver, action: SignUp
):

    action.clickCountry()
    action.assertCountryCode()
    action.inputCountryCodeNetherlands("Netherland")
    action.clickResultSearchCountry()
    action.assertCountryCodeAfterChooseNetherland()


def test_Register_with_phone_Number_and_user_can_search_Country_back_Default(
    driver: WebDriver, action: SignUp
):

    action.clickCountry()
    action.assertCountryCode()
    action.clickCountryIndonesia()
    action.assertCountryCodeAfterChooseIndonesia()


def test_Register_with_phone_Number_and_User_Input_Wrong_Keyword(
    driver: WebDriver, action: SignUp
):

    action.clickCountry()
    action.assertCountryCode()
    action.inputCountryCodeNetherlands("asdadqe213f")
    action.assertNoCountryFound()
    action.clickBtnCloseCountryCode()


def test_Register_with_phone_Number_Incorrect(driver: WebDriver, action: SignUp):

    action.inputPhoneNumber("11111")
    action.assertPhoneNumberIncorrect()


def test_Register_with_phone_Number_Special_Character(
    driver: WebDriver, action: SignUp
):

    action.inputPhoneNumber("22232")
    action.assertPhoneNumberIncorrect()


def test_Register_with_Phone_Number_User_fill_Create_Password_field_with_by_8_character(
    driver: WebDriver, action: SignUp
):
    action.clickEmailSection()
    action.clickPhoneNumberSection()
    action.inputPhoneNumber("888111222333")
    action.inputPassword(password)
    action.clickInvisiblePassword()


def test_Register_with_Phone_Number_User_fill_Create_Password_field_less_than_8_character(
    driver: WebDriver, action: SignUp
):
    action.clickEmailSection()
    action.clickPhoneNumberSection()
    action.inputPhoneNumber("888111222333")
    action.inputPassword(wrong_password)
    action.assertPasswordDoesntMatch()


def test_Register_with_Phone_Number_Wrong_OTP(driver: WebDriver, action: SignUp):

    action.inputPhoneNumber(phone_number)
    action.inputPassword(password)
    action.clickButtonSendOtp()
    action.assertSendOtpViaMessage()
    action.clickSendViaSms()
    action.inputOTP("0000")
    action.clickSubmitRegister()
    action.assertWrongOtp()


def test_Register_with_Phone_Number_Request_Otp_Second_Time(
    driver: WebDriver, action: SignUp
):

    time.sleep(125)
    action.clickButtonSendOtp()
    action.assertSendOtpViaMessage()
    action.clickSendViaSms()
    action.assertSendOtpSecondTime()
    otp = print_last_otp(phone_number)
    action.inputOTP(otp)
    time.sleep(310)
    action.clickSubmitRegister()
    action.assertOTPExpired()


def test_Register_with_Phone_Number_OTP_Expired_After_2_minutes(
    driver: WebDriver, action: SignUp
):
    action.clickSubmitRegister()
    action.assertOTPExpired()


def test_TC_Register_New_User_Phone_Number(reopendriver: WebDriver):
    time.sleep(3)
    Register_with_phone(reopendriver)
