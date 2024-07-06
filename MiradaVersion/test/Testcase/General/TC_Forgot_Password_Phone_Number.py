import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.loginPages import PagesLogin
from MiradaVersion.pages.profilesPages import Profiles
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.test.id_Mirada_Register.TC_register_with_phone import (
    Register_with_phone,
    generate_random_phone_number,
)
from MiradaVersion.test.id_Mirada_Register.TC_register_with_email import (
    Register_with_email,
    generate_random_email,
)
from MiradaVersion.test.TC_Get_OTP import print_last_otp


domains = ["visionplus.id"]

first_names = ["Testing"]
random_email = generate_random_email(domains, first_names)

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


@pytest.fixture(scope="module")
def profiles_action(driver):
    return Profiles(driver)


@pytest.fixture(scope="module")
def homepage_action(driver):
    return HomePage(driver)


def test_TC_Forgot_Password_Phone_Number_Less_Than_8_character(
    driver: WebDriver, sign_up_action: SignUp, login_action: PagesLogin, cache
):

    phone_number = Register_with_phone(driver)
    time.sleep(3)

    login_action.clickLogin()
    login_action.assertLoginPage()
    login_action.clickBtnForgotPassword()
    time.sleep(2)
    login_action.assertForgotPasswordPage()
    time.sleep(2)
    sign_up_action.inputPhoneNumber(phone_number)
    time.sleep(2)
    sign_up_action.inputPassword("432Aaa")
    time.sleep(2)
    sign_up_action.assertPasswordDoesntMatch()
    cache.set("phone_number1", phone_number)
    print("This phone number for next step " + phone_number)
    print("test_TC_Forgot_Password_Phone_Number_Less_Than_8_character DONE")


def test_TC_Forgot_Password_Phone_Number_and_Input_Wrong_OTP(
    sign_up_action: SignUp, login_action: PagesLogin, cache
):
    phone_number1 = cache.get("phone_number1", None)
    time.sleep(2)
    sign_up_action.inputPhoneNumber(phone_number1)
    time.sleep(2)   
    sign_up_action.inputPassword("4321Lupaa")
    time.sleep(2)
    sign_up_action.clickButtonSendOtp()
    time.sleep(2)
    sign_up_action.assertSendOtpViaMessage()
    time.sleep(2)
    sign_up_action.clickSendViaSms()
    otp = print_last_otp(phone_number1)
    time.sleep(2)
    sign_up_action.inputOTP("0000")
    time.sleep(2)
    login_action.clickBtnSavePassword()
    time.sleep(2)
    sign_up_action.assertWrongOtp()
    cache.set("otp", otp)
    time.sleep(130)
    print("test_TC_Forgot_Password_Phone_Number_and_Input_Wrong_OTP DONE")


def test_TC_Forgot_Password_Request_OTP_First_Time(
    sign_up_action: SignUp, login_action: PagesLogin, cache
):
    otp = cache.get("otp", None)
    if otp is None:
        pytest.fail("OTP not found in cache.")

    sign_up_action.clickButtonSendOtp()
    time.sleep(2)
    sign_up_action.assertSendOtpViaMessage()
    time.sleep(2)
    sign_up_action.clickSendViaSms()
    time.sleep(2)
    sign_up_action.inputOTP(otp)
    print("test_TC_Forgot_Password_Request_OTP_First_Time DONE")


def test_TC_Forgot_Password_OTP_Expired_2minutes(
    sign_up_action: SignUp, login_action: PagesLogin
):
    login_action.clickBtnSavePassword()
    time.sleep(3)
    sign_up_action.assertWrongOtp()
    print("test_TC_Forgot_Password_OTP_Expired_2minutes DONE")


def test_TC_Forgot_Password_User_Login_After_do_Forgot_Password_Phone_Number(
    sign_up_action: SignUp,
    login_action: PagesLogin,
    homepage_action: HomePage,
    cache,
    driver:WebDriver,
):

    phone_number1 = cache.get("phone_number1", None)
    time.sleep(2)
    sign_up_action.inputPhoneNumber(phone_number1)
    time.sleep(2)
    sign_up_action.inputPassword("4321Lupaa")
    time.sleep(305)
    sign_up_action.clickButtonSendOtp()
    time.sleep(2)
    sign_up_action.assertSendOtpViaMessage()
    time.sleep(2)
    sign_up_action.clickSendViaSms()
    time.sleep(2)
    otp = print_last_otp(phone_number1)
    time.sleep(2)
    sign_up_action.inputOTP(otp)
    time.sleep(2)
    login_action.clickBtnSavePassword()
    time.sleep(10)
    print("for login again" + phone_number1)
    time.sleep(3)
    driver.press_keycode(4)
    login_action.clickLogin()
    sign_up_action.inputPhoneNumber(phone_number1)
    time.sleep(2)
    sign_up_action.inputPassword("4321Lupaa")
    time.sleep(2)
    login_action.clickSubmitLogin()
    time.sleep(3)
    homepage_action.clickMenuButton()
    homepage_action.assertMenu()
    homepage_action.clickSettingsButton()
    time.sleep(2)
    homepage_action.assertSettingsPage()
    time.sleep(2)
    homepage_action.clickSettingsProfile()
    time.sleep(2)
    homepage_action.assertSettingsAccountPage()
    time.sleep(2)
    homepage_action.clickLogoutButton()

    time.sleep(5)
    print(
        "test_TC_Forgot_Password_User_Login_After_do_Forgot_Password_Phone_Number DONE"
    )
