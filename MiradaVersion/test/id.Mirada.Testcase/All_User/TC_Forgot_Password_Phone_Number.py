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
    login_action.assertForgotPasswordPage()
    sign_up_action.inputPhoneNumber(phone_number)
    sign_up_action.inputPassword("432Aaa")
    sign_up_action.assertPasswordDoesntMatch()
    cache.set("phone_number1", phone_number)
    print("This phone number for next step " + phone_number)
    print("test_TC_Forgot_Password_Phone_Number_Less_Than_8_character DONE")


def test_TC_Forgot_Password_Phone_Number_and_Input_Wrong_OTP(
    sign_up_action: SignUp, login_action: PagesLogin, cache
):
    phone_number1 = cache.get("phone_number1", None)
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
    print("test_TC_Forgot_Password_Phone_Number_and_Input_Wrong_OTP DONE")


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
):

    phone_number1 = cache.get("phone_number1", None)
    sign_up_action.inputPhoneNumber(phone_number1)
    sign_up_action.inputPassword("4321Lupaa")
    time.sleep(305)
    sign_up_action.clickButtonSendOtp()
    sign_up_action.assertSendOtpViaMessage()
    sign_up_action.clickSendViaSms()
    otp = print_last_otp(phone_number1)
    time.sleep(2)
    sign_up_action.inputOTP(otp)
    login_action.clickBtnSavePassword()
    time.sleep(10)
    print("for login again" + phone_number1)
    sign_up_action.clickEmailSection()
    sign_up_action.clickPhoneNumberSection()
    sign_up_action.inputPhoneNumber(phone_number1)
    sign_up_action.inputPassword("4321Lupaa")
    login_action.clickSubmitLogin()
    time.sleep(3)
    homepage_action.clickMenuButton()
    homepage_action.assertMenu()
    homepage_action.clickSettingsButton()
    homepage_action.assertSettingsPage()
    homepage_action.clickSettingsProfile()
    homepage_action.assertSettingsAccountPage()
    homepage_action.clickLogoutButton()

    time.sleep(5)
    print(
        "test_TC_Forgot_Password_User_Login_After_do_Forgot_Password_Phone_Number DONE"
    )


# def test_TC_Forgot_Password_Request_OTP_First_Time_Email(
#     driver: WebDriver, sign_up_action: SignUp, login_action: PagesLogin, cache
# ):
#     random_email = Register_with_email(driver)
#     print(f"Generated Email: {random_email}")
#     time.sleep(3)
#     print("success")
#     login_action.clickLogin()
#     login_action.assertLoginPage()
#     login_action.clickBtnForgotPassword()
#     login_action.assertForgotPasswordPage()
#     login_action.clickEmailSection()
#     sign_up_action.inputEmail(random_email)
#     sign_up_action.inputPassword("4321Lupaa")
#     sign_up_action.clickButtonSendOtp()
#     sign_up_action.assertSendOtpFirstTime()

#     cache.set("email_1", random_email)
#     time.sleep(125)


# def test_TC_Forgot_Password_Request_Second_OTP_Email(
#     sign_up_action: SignUp, login_action: PagesLogin, cache
# ):
#     sign_up_action.clickButtonSendOtp()
#     sign_up_action.assertSendOtpSecondTime()
