import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.pages.livetvPages import LiveTV
from MiradaVersion.pages.vodPages import VOD
from MiradaVersion.test.id_Mirada_Login.login_by_email import login_premium_by_email
from MiradaVersion.test.open_app import premium_email_data
from MiradaVersion.pages.profilesPages import Profiles
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
def vod_action(driver):
    return VOD(driver)


@pytest.fixture(scope="module")
def player_action(driver):
    return mediaplayer(driver)


def delay(action, delay=0.5):
    if callable(action):
        action()
        time.sleep(delay)
    else:
        raise TypeError(f"Expected a callable action, but got {type(action)}")


def test_TC_User_Can_Playback_Fastforward_and_Backward_10_Second(
    driver: WebDriver,
    premium_email_data,
    homepage_action: HomePage,
    vod_action: VOD,
    player_action: mediaplayer,
):

    login_premium_by_email(driver, premium_email_data)

    delay(homepage_action.clickContentClusterVplusOriginals)
    delay(vod_action.clickBtnWatch)
    delay(player_action.assertMediaPlayer)
    time.sleep(5)
    delay(player_action.clickLayoutMediaPlayer)
    delay(player_action.clickPauseMediaPlayer)
    delay(player_action.clickRestartMediaPlayer)
    delay(player_action.clickPauseMediaPlayer)
    print("success pause")
    time.sleep(3)
    delay(player_action.clickLayoutMediaPlayer)
    delay(player_action.clickForward)
    delay(player_action.assertForwardMediaPlayer)
    time.sleep(3)
    delay(player_action.clickLayoutMediaPlayer)
    delay(player_action.clickBackward)
    time.sleep(5)


def test_TC_User_Can_Restart_Player_VOD(
    player_action: mediaplayer,
):
    delay(player_action.clickLayoutMediaPlayer)
    delay(player_action.clickLayoutMediaPlayer)
    time.sleep(10)
    delay(player_action.clickLayoutMediaPlayer)
    delay(player_action.clickRestartMediaPlayer)
    delay(player_action.assertRestartMediaPlayer)
    print("Success Restart")


def test_TC_User_Can_Click_Settings_Player(
    player_action: mediaplayer,
    driver: WebDriver,
):
    time.sleep(3)
    delay(player_action.clickLayoutMediaPlayer)
    delay(player_action.clickSettingsMediaPlayer)
    delay(player_action.assertSettingsMediaPlayer)
    delay(player_action.clickBtnOKSettingsMediaPlayer)
    print("Success Click Settings")
    driver.press_keycode(4)
    driver.press_keycode(4)


def test_TC_User_Can_Click_Settings_Player_Subtittle_Nonactive(
    player_action: mediaplayer,
    driver: WebDriver,
    homepage_action: HomePage,
    vod_action: VOD,
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
    delay(player_action.clickSettingsIndonesianSubtitles)
    delay(player_action.clickSettingsDisableSubtitles)


def test_TC_User_Can_Click_Close_Settings_Media_player(
    player_action: mediaplayer,
):
    delay(player_action.clickBtnOKSettingsMediaPlayer)
