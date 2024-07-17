import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.pages.livetvPages import LiveTV
from MiradaVersion.pages.profilesPages import Profiles
from MiradaVersion.test.id_Mirada_Login.login_by_email import (
    login_premium_sport_by_email,
)
from MiradaVersion.test.open_app import premium_sport_email_data
from MiradaVersion.pages.profilesPages import Profiles
from MiradaVersion.pages.vodPages import VOD
from MiradaVersion.pages.mediaplayerPages import mediaplayer


@pytest.fixture(scope="module")
def driver():
    setup_appium = SetupAppium()
    driver = setup_appium.driver
    if not driver:
        pytest.fail("Driver initialization failed.")

    yield driver


@pytest.fixture(scope="module")
def sign_up_action(driver):
    return SignUp(driver)


@pytest.fixture(scope="module")
def homepage_action(driver):
    return HomePage(driver)


@pytest.fixture(scope="module")
def livetv_action(driver):
    return LiveTV(driver)


@pytest.fixture(scope="module")
def profiles_action(driver):
    return Profiles(driver)


@pytest.fixture(scope="module")
def player_action(driver):
    return mediaplayer(driver)


@pytest.fixture(scope="module")
def vod_action(driver):
    return VOD(driver)


def delay(action, delay=0.5):
    if callable(action):
        action()
        time.sleep(delay)
    else:
        raise TypeError(f"Expected a callable action, but got {type(action)}")


def test_TC_Detail_Banner_Sports(
    driver: WebDriver,
    premium_sport_email_data,
    homepage_action: HomePage,
    vod_action: VOD,
    player_action: mediaplayer,
):
    login_premium_sport_by_email(driver, premium_sport_email_data)
    time.sleep(2)

    delay(homepage_action.clickBanner)
    delay(vod_action.assertDetailVod)
    delay(vod_action.clickBtnBack)


def test_TC_Detail_VOD_Originals_Sports(
    homepage_action: HomePage,
    vod_action: VOD,
):
    delay(homepage_action.clickContentClusterVplusOriginals)
    delay(vod_action.assertDetailVod)
    delay(vod_action.clickBtnWatch)
    time.sleep(10)


def test_TC_User_Click_Restart_VOD(
    player_action: mediaplayer,
    driver: WebDriver,
):
    delay(player_action.clickLayoutMediaPlayer)
    delay(player_action.clickRestartMediaPlayer)
    delay(player_action.clickPauseMediaPlayer)
    time.sleep(5)
    delay(player_action.clickLayoutMediaPlayer)
    driver.press_keycode(4)
    driver.press_keycode(4)


def test_TC_User_Click_Setting_Subtitle_English(
    player_action: mediaplayer,
    homepage_action: HomePage,
    vod_action: VOD,
    driver: WebDriver,
):
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickBtnSearch)
    delay(lambda: homepage_action.inputSearch("arab maklum"))
    delay(homepage_action.clickResultTwo)
    delay(vod_action.assertDetailVod)
    delay(vod_action.clickBtnWatch)
    delay(player_action.clickLayoutMediaPlayer)
    delay(player_action.clickSettingsMediaPlayer)
    delay(player_action.assertSettingsMediaPlayer)
    delay(player_action.clickSettingsEnglishSubtitles)
    delay(player_action.clickBtnOKSettingsMediaPlayer)
    driver.press_keycode(4)
    driver.press_keycode(4)
    driver.press_keycode(4)


def test_TC_User_Slide_Any_Live_Channels(
    player_action: mediaplayer,
    homepage_action: HomePage,
    driver: WebDriver,
):
    element_xpath = "//*[contains(@text,'Your Favorite TV Channel')]"
    try:
        element = Profiles.scroll_to_element(driver, element_xpath)
        print("Element found")
    except Exception as e:
        print(e)
    delay(homepage_action.clickViewlAllVplusOriginals)
    delay(homepage_action.assertClusterLiveTV)


def test_TC_User_Click_Any_Live_Channels(
    player_action: mediaplayer,
    homepage_action: HomePage,
    driver: WebDriver,
    livetv_action: LiveTV,
):
    delay(homepage_action.clickChannelClusterLivetv)
    delay(livetv_action.assertLiveTV)
