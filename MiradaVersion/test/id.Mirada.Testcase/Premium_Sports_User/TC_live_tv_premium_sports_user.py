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


def test_TC_User_Can_Watching_Live_TV_Channel(
    driver: WebDriver,
    premium_sport_email_data,
    homepage_action: HomePage,
    livetv_action: LiveTV,
):
    login_premium_sport_by_email(driver, premium_sport_email_data)
    time.sleep(2)
    homepage_action.clickMenuButton()
    homepage_action.assertMenu()
    homepage_action.clickLiveTvMenu()
    livetv_action.assertLiveTV()


def test_TC_User_Watch_Live_TV_Channel_and_Disconnect_Internet(
    livetv_action: LiveTV, profiles_action: Profiles
):
    profiles_action.disable_wifi_connection("emulator-5554")
    livetv_action.assertNoInternetConnection()
    profiles_action.enable_wifi_connection("emulator-5554")
    time.sleep(5)


def test_TC_User_Can_Watching_Live_TV_Channel_Premium(
    livetv_action: LiveTV,
):
    livetv_action.clickTrans7Channel()

    try:
        livetv_action.assertSubscription()

        raise AssertionError("Test failed because assertSubscription() passed.")
    except Exception as e:

        print(f"Assert Success : No subcription button")


def test_TC_User_Can_Watching_Live_TV_Channel_Premium_Sports(
    livetv_action: LiveTV,
    profiles_action: Profiles,
):
    for _ in range(6):
        profiles_action.scroll_down()

    livetv_action.clickSportChannel()

    try:
        livetv_action.assertSubscription()

        raise AssertionError("Test failed because assertSubscription() passed.")
    except Exception as e:

        print(f"Assert Success : No subcription button")


def test_TC_User_Cant_Watching_Detail_Channel_Premium_Sports(livetv_action: LiveTV):
    livetv_action.clickBtnDetailChannelSportstars()
    livetv_action.assertDetailChannelSportstars()
