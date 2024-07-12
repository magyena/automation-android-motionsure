import pytest # type: ignore
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.vodPages import VOD
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.pages.profilesPages import Profiles
from MiradaVersion.pages.livetvPages import LiveTV
from MiradaVersion.pages.settingsPages import SettingsPages
from MiradaVersion.pages.programguidePages import programguidePages
from MiradaVersion.test.id_Mirada_Login.login_by_email import (
    login_premium_sport_by_email,
)
from MiradaVersion.test.open_app import (
    premium_sport_email_data,
)


@pytest.fixture(scope="module")
def driver():
    setup_appium = SetupAppium()
    driver = setup_appium.driver
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def reopendriver():
    setup_appium = SetupAppium()
    driver = setup_appium.driver
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def vod_action(driver):
    return VOD(driver)


@pytest.fixture(scope="module")
def homepage_action(driver):
    return HomePage(driver)


@pytest.fixture(scope="module")
def settings_action(driver):
    return SettingsPages(driver)


@pytest.fixture(scope="module")
def profiles_action(driver):
    return Profiles(driver)


@pytest.fixture(scope="module")
def guide_action(driver):
    return programguidePages(driver)


@pytest.fixture(scope="module")
def livetv_action(driver):
    return LiveTV(driver)


def delay(action, delay=2):
    if callable(action):
        action()
        time.sleep(delay)
    else:
        raise TypeError(f"Expected a callable action, but got {type(action)}")


def test_TC_Transaction_History_All_Transaction(
    driver: WebDriver,
    homepage_action: HomePage,
    premium_sport_email_data,
    settings_action: SettingsPages,
):
    login_premium_sport_by_email(driver, premium_sport_email_data)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickSettingsButton)
    delay(settings_action.clickTransactionHistory)
    delay(settings_action.assertTransactionHistoryPage)

    Profiles.scrollDown


def test_TC_Transaction_History_has_No_Transaction_History(
    settings_action: SettingsPages,
):

    delay(settings_action.clickTabPendingTransactionHistory)
    delay(settings_action.assertNoTransactionHistory)


def test_TC_Transaction_History_Success_Transaction(
    settings_action: SettingsPages,
):

    delay(settings_action.clickTabSuccessTransactionHistory)
    delay(settings_action.assertTransactionHistorySuccess)


def test_TC_Transaction_History_Failed_Transaction(
    settings_action: SettingsPages,
):

    delay(settings_action.clickTabFailedTransactionHistory)
    delay(settings_action.assertTransactionHistoryFailed)


def test_TC_Transaction_History_Pending_Transaction(
    settings_action: SettingsPages,
):

    delay(settings_action.clickTabPendingTransactionHistory)


def test_TC_Transaction_History_Detail(
    settings_action: SettingsPages,
):
    delay(settings_action.clickTabSuccessTransactionHistory)
    delay(settings_action.clickDetailTransaction)
    delay(settings_action.assertTransactionDetails)
