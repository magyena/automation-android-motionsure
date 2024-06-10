import pytest
import time

from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.test.id_Mirada_Register.TC_register_with_phone import (
    Register_with_phone,
)

password = "4321Lupa"


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


def test_TC_User_Click_Terms_of_Use(driver: WebDriver):
    Firstpage = SignUp(driver)

    Firstpage.clickTermsOfUse()
    time.sleep(2)
    driver.press_keycode(4)


def test_TC_User_Click_Privacy_Policy(driver: WebDriver):
    Firstpage = SignUp(driver)

    Firstpage.clickPrivacyPolicy()
    time.sleep(2)
    driver.press_keycode(4)


def test_TC_Unverified_Account(driver: WebDriver):
    register = SignUp(driver)
    homepage = HomePage(driver)

    register.clickSignUp()
    register.assertRegisterPage()
    register.inputPhoneNumber("888111222333")
    register.inputPassword(password)
    register.clickButtonSendOtp()
    register.clickSendViaSms()
    register.assertRegisterHasBeenRegistered()
    driver.quit()


def test_TC_Register_New_User_Phone_Number(reopendriver: WebDriver):
    time.sleep(3)
    Register_with_phone(reopendriver)
