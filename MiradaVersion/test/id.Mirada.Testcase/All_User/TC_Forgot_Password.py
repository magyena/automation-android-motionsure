import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.loginPages import PagesLogin
from MiradaVersion.test.id_Mirada_Register.TC_register_with_phone import (
    Register_with_phone,
    generate_random_phone_number,
)
from MiradaVersion.test.TC_Get_OTP import print_last_otp

phone_number = generate_random_phone_number()


@pytest.fixture(scope="module")
def driver():
    setup_appium = SetupAppium()
    driver = setup_appium.driver
    if not driver:
        pytest.fail("Driver initialization failed.")

    yield driver


@pytest.fixture(scope="module")
def reopendriver():
    setup_appium = SetupAppium()
    driver = setup_appium.driver
    if not driver:
        pytest.fail("Driver initialization failed.")
    yield driver


@pytest.fixture(scope="module")
def sign_up_action(driver):
    return SignUp(driver)


@pytest.fixture(scope="module")
def login_action(driver):
    return PagesLogin(driver)


def test_TC_Forgot_Password_Phone_Number_Less_Than_8_character(
    reopendriver: WebDriver, cache
):
    try:
        phone_number = Register_with_phone(reopendriver)
    except Exception as e:
        pytest.fail(f"Failed during phone registration: {e}")
    finally:
        reopendriver.quit()

    try:
        new_driver = SetupAppium().driver
        if not new_driver:
            pytest.fail("Failed to reinitialize driver.")
        time.sleep(3)
        login_action = PagesLogin(new_driver)
        sign_up_action = SignUp(new_driver)
        login_action.clickLogin()
        login_action.assertLoginPage()
        login_action.clickBtnForgotPassword()
        login_action.assertForgotPasswordPage()
        sign_up_action.inputPhoneNumber(phone_number)
        sign_up_action.inputPassword("432Aaa")
        sign_up_action.assertPasswordDoesntMatch()
        cache.set("phone_number1", phone_number)
    except Exception as e:
        pytest.fail(f"Test execution failed: {e}")
    finally:
        print("This phone number for next step " + phone_number)


def test_TC_Forgot_Password_Phone_Number_and_Input_Wrong_OTP(
    sign_up_action: SignUp, login_action: PagesLogin, cache
):
    phone_number1 = cache.get("phone_number1", None)
    login_action.clickLogin()
    login_action.assertLoginPage()
    login_action.clickBtnForgotPassword()
    login_action.assertForgotPasswordPage()
    sign_up_action.inputPhoneNumber(phone_number1)
    sign_up_action.inputPassword("4321Lupaa")
    sign_up_action.clickButtonSendOtp()
    sign_up_action.assertSendOtpViaMessage()
    sign_up_action.clickSendViaSms()
    otp = print_last_otp(phone_number1)
    time.sleep(2)
    sign_up_action.inputOTP("0000")
    login_action.clickBtnSavePassword()
    sign_up_action.assertWrongOtp()
    cache.set("otp", otp)
    time.sleep(130)


def test_TC_Forgot_Password_Request_OTP_First_Time(
    sign_up_action: SignUp, login_action: PagesLogin, cache
):
    otp = cache.get("otp", None)
    if otp is None:
        pytest.fail("OTP not found in cache.")

    sign_up_action.clickButtonSendOtp()
    sign_up_action.assertSendOtpViaMessage()
    sign_up_action.clickSendViaSms()
    time.sleep(2)
    sign_up_action.inputOTP(otp)


def test_TC_Forgot_Password_OTP_Expired_2minutes(
    sign_up_action: SignUp, login_action: PagesLogin
):
    login_action.clickBtnSavePassword()
    time.sleep(3)
    sign_up_action.assertWrongOtp()


def test_TC_Forgot_Password_User_Login_After_do_Forgot_Password_Phone_Number(
    driver: WebDriver, sign_up_action: SignUp, login_action: PagesLogin, cache
):
    driver.quit()

    # Reopen the driver
    driver = SetupAppium().driver
    if not driver:
        pytest.fail("Failed to reinitialize driver.")

    phone_number1 = cache.get("phone_number1", None)
    login_action = PagesLogin(driver)  # Re-initialize with the new driver
    sign_up_action = SignUp(driver)  # Re-initialize with the new driver

    login_action.clickLogin()
    login_action.assertLoginPage()
    login_action.clickBtnForgotPassword()
    login_action.assertForgotPasswordPage()
    sign_up_action.inputPhoneNumber(phone_number1)
    sign_up_action.inputPassword("4321Lupaa")
    time.sleep(300)
    sign_up_action.clickButtonSendOtp()
    sign_up_action.assertSendOtpViaMessage()
    sign_up_action.clickSendViaSms()
    otp = print_last_otp(phone_number1)
    time.sleep(2)
    sign_up_action.inputOTP(otp)
    login_action.clickBtnSavePassword()
    time.sleep(5)
    login_action.assertLoginPage()
    sign_up_action.inputPhoneNumber(phone_number1)
    sign_up_action.inputPassword("4321Lupaa")
    login_action.clickSubmitLogin()

    time.sleep(5)
