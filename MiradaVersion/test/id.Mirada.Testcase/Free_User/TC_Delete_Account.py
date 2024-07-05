import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.loginPages import PagesLogin
from MiradaVersion.pages.profilesPages import Profiles
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.pages.settingsPages import SettingsPages
from MiradaVersion.test.id_Mirada_Register.TC_register_with_phone import (
    Register_with_phone,
    generate_random_phone_number,
)

phone_number = generate_random_phone_number()
invalid_password = "43213Lupa"
new_password = "4321Lupaaa"
less_password = "4321L"
current_password = "4321Lupa"


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
def settings_action(driver):
    return SettingsPages(driver)


@pytest.fixture(scope="module")
def homepage_action(driver):
    return HomePage(driver)


def delay(action, delay=2):
    if callable(action):
        action()
        time.sleep(delay)
    else:
        raise TypeError(f"Expected a callable action, but got {type(action)}")


def test_TC_User_Cant_be_Deleted_Account_Wrong_Password(
    driver: WebDriver,
    sign_up_action: SignUp,
    login_action: PagesLogin,
    settings_action: SettingsPages,
    homepage_action: HomePage,
    cache,
):

    phone_number = Register_with_phone(driver)
    time.sleep(3)

    delay(login_action.clickLogin)
    delay(login_action.assertLoginPage)
    delay(lambda: sign_up_action.inputPhoneNumber(phone_number))
    delay(lambda: sign_up_action.inputPassword("4321Lupa"))
    delay(login_action.clickSubmitLogin)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickSettingsButton)
    delay(settings_action.clickSettingsProfile)
    delay(settings_action.clickDeleteAccount)
    delay(settings_action.assertDeleteAccountPage)
    delay(settings_action.clickAcceptDeleteAccount)
    delay(settings_action.clickProceedDeleteAccount)
    delay(settings_action.assertDeleteAccountPage)
    delay(lambda: settings_action.inputPasswordDeleteAccount(invalid_password))
    # driver.press_keycode(4)
    delay(settings_action.clickBtnDeleteAccount)
    delay(settings_action.assertInvalidDeleteAccount)
    delay(settings_action.clickBtnOKInvalidCurrentPassword)

    cache.set("phone_number1", phone_number)
    print("This phone number for next step " + phone_number)


def test_TC_User_Cant_be_Deleted_Account_Success(
    settings_action: SettingsPages,
):

    delay(lambda: settings_action.inputPasswordDeleteAccount(current_password))
    time.sleep(3)
    delay(settings_action.clickBtnDeleteAccount)
    delay(settings_action.assertDeleteAccountSuccess)
