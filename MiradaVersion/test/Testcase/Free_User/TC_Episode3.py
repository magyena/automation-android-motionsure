import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.pages.livetvPages import LiveTV
from MiradaVersion.pages.vodPages import VOD
from MiradaVersion.pages.profilesPages import Profiles
from MiradaVersion.test.id_Mirada_Login.login_by_phone import login_free_by_phone
from MiradaVersion.test.id_Mirada_Login.login_by_email import login_free_by_email
from MiradaVersion.test.open_app import free_phone_data, free_email_data
from MiradaVersion.pages.settingsPages import SettingsPages


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
def setting_action(driver):
    return SettingsPages(driver)


@pytest.fixture(scope="module")
def profiles_action(driver):
    return Profiles(driver)


@pytest.fixture(scope="module")
def livetv_action(driver):
    return LiveTV(driver)


@pytest.fixture(scope="module")
def vod_action(driver):
    return VOD(driver)


def delay(action, delay=2):
    if callable(action):
        action()
        time.sleep(delay)
    else:
        raise TypeError(f"Expected a callable action, but got {type(action)}")


def test_TC_User_Can_Slide_list_Cluster_Series(
    homepage_action: HomePage,
    vod_action: VOD,
    free_phone_data,
    driver: WebDriver,
    profiles_action: Profiles,
):
    login_free_by_phone(driver, free_phone_data)
    delay(homepage_action.clickCategorySeries)

    for _ in range(1):
        profiles_action.scroll_left(
            start_x=543, start_y=2135, end_x=523, end_y=1118, duration=500
        )

    for _ in range(2):
        profiles_action.scroll_left(
            start_x=1025, start_y=1327, end_x=285, end_y=1331, duration=500
        )


def test_TC_User_Can_See_Detail_Sinopsis_VOD(
    homepage_action: HomePage,
    vod_action: VOD,
    driver: WebDriver,
    profiles_action: Profiles,
):
    delay(homepage_action.clickContentCategorySeries)
    delay(vod_action.assertDetailVod)
    delay(vod_action.clickSinopsis)


def test_TC_User_Open_VOD_for_Episode_3_or_other_Episode(
    homepage_action: HomePage,
    vod_action: VOD,
    driver: WebDriver,
    profiles_action: Profiles,
):
    delay(vod_action.clickChooseSeason)
    delay(vod_action.clickSeason1)
    for _ in range(1):
        profiles_action.scroll_left(
            start_x=507, start_y=1082, end_x=507, end_y=864, duration=500
        )

    delay(vod_action.clickEps3Premium)
    delay(vod_action.clickBtnSubscribe)
    delay(vod_action.assertListPackages)
    driver.press_keycode(4)
    driver.press_keycode(4)


def test_TC_User_Click_Trailer(
    vod_action: VOD,
    profiles_action: Profiles,
):
    delay(vod_action.clickChooseSeason)
    delay(vod_action.clickSeason0)
    for _ in range(1):
        profiles_action.scroll_left(
            start_x=507, start_y=1082, end_x=507, end_y=864, duration=500
        )
    delay(vod_action.clickEps3Premium)
    print("In trailer")


def test_TC_User_Add_Trailer_to_Watchlist(
    vod_action: VOD,
):
    delay(vod_action.clickAddtoList)
    delay(vod_action.clickAddtoList)


def test_TC_User_Share_Trailer(
    vod_action: VOD,
    driver: WebDriver,
):
    delay(vod_action.clickShare)
    driver.press_keycode(4)


def test_TC_User_Can_See_Download_VOD_Showing_Popup(
    homepage_action: HomePage,
    vod_action: VOD,
    driver: WebDriver,
):
    driver.press_keycode(4)
    driver.press_keycode(4)
    driver.press_keycode(4)

    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickMyDownloadsMenu)
    delay(homepage_action.assertMyDownloadsPage)
    delay(homepage_action.clickSubscribeMyDownloads)
    delay(homepage_action.clickBtnAccept)
    delay(vod_action.assertListPackages)
