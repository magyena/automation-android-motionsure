import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.vodPages import VOD
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.pages.profilesPages import Profiles
from MiradaVersion.pages.livetvPages import LiveTV
from MiradaVersion.pages.settingsPages import SettingsPages
from MiradaVersion.pages.programguidePages import programguidePages
from MiradaVersion.test.id_Mirada_Login.login_by_phone import (
    login_free_by_phone,
)
from MiradaVersion.test.open_app import (
    free_phone_data,
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


def test_TC_User_Can_Show_Manage_Devices(
    driver: WebDriver,
    homepage_action: HomePage,
    free_phone_data,
    settings_action: SettingsPages,
):
    login_free_by_phone(driver, free_phone_data)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickLiveTvMenu)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickSettingsButton)
    delay(settings_action.clickManageDevices)
    delay(settings_action.assertManageDevicesPage)


def test_TC_User_Can_Disconnect_Devices(
    settings_action: SettingsPages,
):
    delay(settings_action.clickDiscconnectManageDevices)
    delay(settings_action.clickAcceptDeleteProfile)


def test_TC_User_Show_no_Devices_Connected(
    settings_action: SettingsPages,
):
    delay(settings_action.assertNoDevicesConnected)
