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
    login_premium_by_phone,
    login_premium_sport_by_phone,
)
from MiradaVersion.test.open_app import (
    free_phone_data,
    premium_phone_data,
    premium_sport_phone_data,
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


def test_TC_User_Free_Cant_Watching_Guide(
    driver: WebDriver,
    homepage_action: HomePage,
    free_phone_data,
    guide_action: programguidePages,
    vod_action: VOD,
    profiles_action: Profiles,
    livetv_action: LiveTV,
):
    login_free_by_phone(driver, free_phone_data)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickProgramGuide)
    delay(guide_action.assertProgramGuidePage)
    for _ in range(4):
        profiles_action.scroll_left(
            start_x=410, start_y=595, end_x=752, end_y=595, duration=300
        )
    delay(guide_action.clickRctiGuide)
    delay(livetv_action.assertLiveTVBroadcasted)
    delay(vod_action.clickBtnWatch)
    delay(vod_action.assertListPackages)
    driver.press_keycode(4)
    driver.press_keycode(4)


def test_TC_User_Premium_be_able_to_Showing_7_Days_After_Guide(
    driver: WebDriver,
    homepage_action: HomePage,
    premium_phone_data,
    guide_action: programguidePages,
    livetv_action: LiveTV,
    profiles_action: Profiles,
    settings_action: SettingsPages,
):
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickSettingsButton)
    delay(settings_action.clickSettingsProfile)
    delay(settings_action.clickLogoutButton)
    login_premium_by_phone(driver, premium_phone_data)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickProgramGuide)
    delay(guide_action.assertProgramGuidePage)
    for _ in range(45):
        profiles_action.scroll_left(
            start_x=700, start_y=386, end_x=281, end_y=418, duration=100
        )
    delay(guide_action.clickRctiGuide)
    delay(livetv_action.assertLiveTVBroadcast)


def test_TC_User_Premium_be_able_to_Showing_7_Days_Before_Guide(
    driver: WebDriver,
    homepage_action: HomePage,
    profiles_action: Profiles,
):
    driver.press_keycode(4)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickLiveTvMenu)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickProgramGuide)
    for _ in range(10):
        profiles_action.scroll_left(
            start_x=277, start_y=406, end_x=788, end_y=406, duration=100
        )


def test_TC_User_Premium_be_able_to_Play_Guide(
    driver: WebDriver,
    guide_action: programguidePages,
    livetv_action: LiveTV,
    vod_action: VOD,
):
    delay(guide_action.clickRctiGuide)
    delay(livetv_action.assertLiveTVBroadcasted)
    delay(vod_action.clickBtnWatch)
    print("play live tv guide")
    driver.press_keycode(4)
    driver.press_keycode(4)


def test_TC_User_Premium_Sport_be_able_to_Play_Guide(
    driver: WebDriver,
    homepage_action: HomePage,
    premium_sport_phone_data,
    guide_action: programguidePages,
    livetv_action: LiveTV,
    profiles_action: Profiles,
    settings_action: SettingsPages,
    vod_action: VOD,
):
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickSettingsButton)
    delay(settings_action.clickSettingsProfile)
    delay(settings_action.clickLogoutButton)

    login_premium_sport_by_phone(driver, premium_sport_phone_data)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickLiveTvMenu)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickProgramGuide)
    for _ in range(10):
        profiles_action.scroll_left(
            start_x=277, start_y=406, end_x=788, end_y=406, duration=100
        )
    delay(guide_action.clickRctiGuide)
    delay(livetv_action.assertLiveTVBroadcasted)
    delay(vod_action.clickBtnWatch)
    print("play live tv guide")
    driver.press_keycode(4)
