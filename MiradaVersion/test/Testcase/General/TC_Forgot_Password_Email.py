import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.loginPages import PagesLogin
from MiradaVersion.pages.profilesPages import Profiles
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.test.id_Mirada_Register.TC_register_with_phone import (
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


def test_TC_Forgot_Password_Request_OTP_First_Time_Email(
    driver: WebDriver, sign_up_action: SignUp, login_action: PagesLogin, cache
):
    random_email = Register_with_email(driver)
    print(f"Generated Email: {random_email}")
    time.sleep(3)
    print("success")
    login_action.clickLogin()
    login_action.assertLoginPage()
    login_action.clickBtnForgotPassword()
    time.sleep(2)
    login_action.assertForgotPasswordPage()
    time.sleep(2)
    login_action.clickEmailSection()
    time.sleep(2)
    sign_up_action.inputEmail(random_email)
    time.sleep(2)
    sign_up_action.inputPassword("4321Lupaa")
    time.sleep(2)
    sign_up_action.clickButtonSendOtp()

    sign_up_action.assertSendOtpFirstTime()

    cache.set("email_1", random_email)
    time.sleep(125)


def test_TC_Forgot_Password_Request_Second_OTP_Email(
    sign_up_action: SignUp, login_action: PagesLogin, cache
):
    random_email = cache.get("email_1", None)
    if random_email is None:
        print("Email not found in cache")
        return
    time.sleep(2)
    sign_up_action.clickButtonSendOtp()
    otp = print_last_otp(random_email)
    print("cache1 " + otp)
    sign_up_action.assertSendOtpSecondTime()

    cache.set("otp1", otp)
    time.sleep(125)
    print("counting 2 minutes")


def test_TC_Forgot_Password_with_Email_OTP_Expired_2_minutes_Same_Otp(
    sign_up_action: SignUp, login_action: PagesLogin, cache
):
    otp = cache.get("otp1", None)
    if otp is None:
        print("OTP not found in cache")
        return

    print("result cache otp1" + otp)
    time.sleep(3)
    sign_up_action.inputOTP(otp)
    time.sleep(3)
    login_action.clickBtnSavePassword()
    time.sleep(2)
    sign_up_action.assertOTPExpired()
    time.sleep(5)
