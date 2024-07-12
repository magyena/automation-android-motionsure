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
voucher = "IKINGGH2WFXO3PREM"
expired_voucher = "premsportautomateKRNNEDG22Fade"
invalid_voucher = "G"


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


def delay(action, delay=0):
    if callable(action):
        action()
        time.sleep(delay)
    else:
        raise TypeError(f"Expected a callable action, but got {type(action)}")


def test_TC_User_Cant_Reedem_Voucher_Expired(
    driver: WebDriver,
    sign_up_action: SignUp,
    login_action: PagesLogin,
    settings_action: SettingsPages,
    homepage_action: HomePage,
):
    email = Register_with_email(driver)

    delay(login_action.clickLogin)
    delay(login_action.assertLoginPage)
    delay(login_action.clickEmailSection)
    delay(lambda: sign_up_action.inputEmail(email))
    delay(lambda: sign_up_action.inputPassword("4321Lupa"))
    delay(login_action.clickSubmitLogin)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickSettingsButton)
    delay(settings_action.clickVoucher)
    time.sleep(5)
    delay(settings_action.assertVoucherPage)
    delay(lambda: settings_action.inputRedeemVoucher(expired_voucher))
    delay(settings_action.clickBtnRedeemVoucher)
    delay(lambda: settings_action.inputRedeemVoucher(expired_voucher))
    delay(settings_action.clickBtnRedeemVoucher)


def test_TC_User_Cant_Reedem_Voucher_Invalid(
    driver: WebDriver,
    settings_action: SettingsPages,
):
    delay(lambda: settings_action.inputRedeemVoucher(invalid_voucher))
    delay(settings_action.clickBtnRedeemVoucher)


def test_TC_User_Can_Direct_to_Market_Place(
    driver: WebDriver,
    settings_action: SettingsPages,
):
    print("dimatketplce")
    delay(settings_action.clickMarketPlaceTokopedia)
    time.sleep(3)
    driver.press_keycode(4)
    delay(settings_action.clickMarketPlaceLazada)
    time.sleep(3)
    driver.press_keycode(4)
    delay(settings_action.clickMarketPlaceBlibli)
    time.sleep(3)
    driver.press_keycode(4)
    delay(settings_action.clickMarketPlaceCoda)
    time.sleep(3)
    driver.press_keycode(4)


def test_TC_User_Can_Direct_to_Help_Center(
    driver: WebDriver,
    settings_action: SettingsPages,
):
    delay(settings_action.clickHelpCenterVoucher)
    delay(settings_action.assertHelpCenterPage)
    driver.press_keycode(4)


def test_TC_User_Success_Reedem_Voucher(
    driver: WebDriver,
    settings_action: SettingsPages,
):
    delay(settings_action.clickVoucher)
    time.sleep(3)
    delay(lambda: settings_action.inputRedeemVoucher(voucher))
    delay(settings_action.clickBtnRedeemVoucher)
    delay(settings_action.assertSuccessReedemVoucher)
    delay(settings_action.clickBtnSeeMyStatus)
    delay(settings_action.assertTransactionDetailsVoucher)
    delay(settings_action.clickCloseToSettings)


def test_TC_User_Success_Reedem_Again_With_Same_Voucher(
    driver: WebDriver,
    settings_action: SettingsPages,
):
    delay(settings_action.clickVoucher)
    time.sleep(5)
    delay(settings_action.assertVoucherPage)
    delay(lambda: settings_action.inputRedeemVoucher(voucher))
    delay(settings_action.clickBtnRedeemVoucher)
