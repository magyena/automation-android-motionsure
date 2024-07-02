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
    login_action.assertForgotPasswordPage()
    login_action.clickEmailSection()
    sign_up_action.inputEmail(random_email)
    sign_up_action.inputPassword("4321Lupaa")
    sign_up_action.clickButtonSendOtp()
    sign_up_action.assertSendOtpFirstTime()

    cache.set("email_1", random_email)
    time.sleep(125)


def test_TC_Forgot_Password_Request_Second_OTP_Email(
    sign_up_action: SignUp, login_action: PagesLogin, cache
):
    sign_up_action.clickButtonSendOtp()
    sign_up_action.assertSendOtpSecondTime()
