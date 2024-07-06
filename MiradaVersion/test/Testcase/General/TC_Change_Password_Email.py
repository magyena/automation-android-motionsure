import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.loginPages import PagesLogin
from MiradaVersion.pages.profilesPages import Profiles
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.pages.settingsPages import SettingsPages

from MiradaVersion.test.id_Mirada_Register.TC_register_with_email import (
    Register_with_email,
    generate_random_email,
)
from MiradaVersion.test.TC_Get_OTP import print_last_otp


domains = ["visionplus.id"]

first_names = ["Testing"]
random_email = generate_random_email(domains, first_names)

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


def test_TC_User_Change_Password_Invalid_Current_Password(
    driver: WebDriver,
    sign_up_action: SignUp,
    login_action: PagesLogin,
    settings_action: SettingsPages,
    homepage_action: HomePage,
    cache,
):

    email = Register_with_email(driver)
    time.sleep(3)

    login_action.clickLogin()
    login_action.assertLoginPage()
    login_action.clickEmailSection()
    sign_up_action.inputEmail(email)
    sign_up_action.inputPassword("4321Lupa")
    login_action.clickSubmitLogin()
    homepage_action.clickMenuButton()
    homepage_action.clickSettingsButton()
    settings_action.clickSettingsProfile()
    time.sleep(2)
    settings_action.clickChangePassword()
    settings_action.assertChangePasswordPage()
    time.sleep(3)
    settings_action.inputCurrentPassword(invalid_password)
    time.sleep(2)
    settings_action.inputNewPassword(new_password)
    time.sleep(2)
    settings_action.clickBtnNextChangePassword()
    settings_action.assertChangePasswordInvalidCurrentPassword()
    settings_action.clickBtnOKInvalidCurrentPassword()
    cache.set("email1", email)
    print("This email for next step " + email)


def test_TC_User_Cant_Created_Password_Less_Than_8_Character(
    settings_action: SettingsPages,
):
    time.sleep(2)
    settings_action.inputNewPassword(less_password)
    settings_action.assertChangePasswordLess8Charracter()
    time.sleep(2)


def test_TC_User_Success_Change_Password(
    settings_action: SettingsPages,
):
    settings_action.inputCurrentPassword(current_password)
    time.sleep(2)
    settings_action.inputNewPassword(new_password)
    time.sleep(2)
    settings_action.clickBtnNextChangePassword()
    settings_action.assertSuccessChangePassword()
    settings_action.clickCloseToSettings()
    time.sleep(2)
    settings_action.clickLogoutButton()


def test_TC_User_Login_Again_After_do_Change_Password(
    sign_up_action: SignUp,
    login_action: PagesLogin,
    homepage_action: HomePage,
    cache,
):
    email = cache.get("email1", None)
    if email is None:
        print("Email not found in cache")
        return
    login_action.clickLogin()
    login_action.clickEmailSection()
    login_action.inputEmail(email)
    sign_up_action.inputPassword(new_password)
    login_action.clickSubmitLogin()
    homepage_action.assertHomePage()
