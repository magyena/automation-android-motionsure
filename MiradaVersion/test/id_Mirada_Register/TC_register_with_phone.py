from appium.webdriver.webdriver import WebDriver
import pytest
import random
import string
import time
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.test.TC_Get_OTP import print_last_otp
from MiradaVersion.pages.homepagePages import HomePage

password = "4321Lupa"


def generate_random_phone_number():
    return "89990000" + "".join(random.choices(string.digits, k=4))


@pytest.fixture(scope="module")
def driver():
    setup_appium = SetupAppium()
    yield setup_appium.driver


def Register_with_phone(driver: WebDriver):
    register = SignUp(driver)
    homepage = HomePage(driver)

    register.clickSignUp()
    register.assertRegisterPage()
    phone_number = generate_random_phone_number()
    register.inputPhoneNumber(phone_number)
    register.inputPassword(password)
    register.clickButtonSendOtp()
    register.assertSendOtpViaMessage()
    register.clickSendViaSms()
    otp = print_last_otp(phone_number)
    time.sleep(2)
    register.inputOTP(otp)
    register.clickSubmitRegister()
    register.assertDiscoverProfiles()
    register.clickBtnSkipDiscoverProfiles()
    register.assertSkipProfile()
    register.clickBtnContinueSkipProfile()
    homepage.assertHomePage()
