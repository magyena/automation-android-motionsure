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


def test_TC_User_Need_Login_Phone_Number(
    driver: WebDriver,
    free_phone_data,
    homepage_action: HomePage,
    setting_action: SettingsPages,
):
    login_free_by_phone(driver, free_phone_data)
    time.sleep(2)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickSettingsButton)
    delay(setting_action.clickSettingsProfile)
    delay(setting_action.clickLogoutButton)


def test_TC_User_Need_Login_Email(
    driver: WebDriver,
    free_email_data,
    homepage_action: HomePage,
    setting_action: SettingsPages,
):
    login_free_by_email(driver, free_email_data)
    time.sleep(2)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickSettingsButton)
    delay(setting_action.clickSettingsProfile)
    delay(setting_action.clickLogoutButton)


def test_TC_User_Will_be_direct_to_Terms_of_Use(
    driver: WebDriver,
    homepage_action: HomePage,
):
    delay(homepage_action.BtnTerms)
    driver.press_keycode(4)
    driver.press_keycode(4)


def test_TC_User_Will_be_direct_to_Privacy_Policy(
    driver: WebDriver,
    homepage_action: HomePage,
):
    delay(homepage_action.BtnPrivacy)
    driver.press_keycode(4)
    driver.press_keycode(4)


def test_TC_User_See_Detail_Banner(
    driver: WebDriver,
    free_phone_data,
    homepage_action: HomePage,
    vod_action: VOD,
):
    login_free_by_phone(driver, free_phone_data)
    time.sleep(2)

    delay(homepage_action.clickBanner)

    driver.press_keycode(4)


def test_TC_User_See_Cluster_Love_In_The_Air(
    driver: WebDriver,
    homepage_action: HomePage,
    vod_action: VOD,
):
    element_xpath = "//*[contains(@text,'Just Wanna Say I Love U')]"
    try:
        element = Profiles.scroll_to_element(driver, element_xpath)
        print("Element found")
    except Exception as e:
        print(e)

    delay(homepage_action.assertClusterJustWannaSay)


def test_TC_User_Play_Content_Cluster_Love_In_The_Air(
    driver: WebDriver,
    homepage_action: HomePage,
    vod_action: VOD,
):
    delay(homepage_action.clickContentClusterJustWannaSay)
    delay(vod_action.assertDetailVod)
    delay(vod_action.clickBtnWatch)
    driver.press_keycode(4)
    driver.press_keycode(4)


def test_TC_User_Can_Added_list_Watchlist_Series(
    driver: WebDriver,
    homepage_action: HomePage,
    vod_action: VOD,
):
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickBtnSearch)
    delay(lambda: homepage_action.inputSearch("Roy marten"))
    delay(homepage_action.clickSearchResultThree)
    delay(vod_action.clickAddtoList)
    driver.press_keycode(4)
    driver.press_keycode(4)
    element_xpath = "//*[contains(@text,'Watchlist')]"
    try:
        element = Profiles.scroll_to_element(driver, element_xpath)
        print("Element found")
    except Exception as e:
        print(e)


def test_TC_User_Can_Click_any_VOD_in_Cluster_Watchlist(
    driver: WebDriver,
    homepage_action: HomePage,
    vod_action: VOD,
):
    delay(homepage_action.clickContentClusterWatchlist)
    delay(vod_action.assertDetailVod)


def test_TC_User_Can_Delete_watchlist(
    driver: WebDriver,
    homepage_action: HomePage,
    vod_action: VOD,
):
    delay(vod_action.clickAddtoList)


def test_TC_User_Play_VOD_in_Watchlist(
    driver: WebDriver,
    homepage_action: HomePage,
    vod_action: VOD,
):
    delay(vod_action.clickBtnWatch)
    driver.press_keycode(4)
    driver.press_keycode(4)


def test_TC_User_Slide_Add_More_list(
    driver: WebDriver,
    homepage_action: HomePage,
    vod_action: VOD,
    profiles_action: Profiles,
):
    element_xpath = "//*[contains(@text,'Watchlist')]"
    try:
        element = Profiles.scroll_to_element(driver, element_xpath)
        print("Element found")
    except Exception as e:
        print(e)

    for _ in range(2):
        profiles_action.scroll_left(
            start_x=953, start_y=1709, end_x=338, end_y=1693, duration=300
        )


def test_TC_User_Play_From_Banner(
    driver: WebDriver,
    homepage_action: HomePage,
    vod_action: VOD,
):
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickMenuHome)
    delay(homepage_action.clickBanner)
    delay(vod_action.clickBtnWatch)
    driver.press_keycode(4)
    driver.press_keycode(4)


def test_TC_User_Can_Click_any_Section_in_Serial_Komedi(
    driver: WebDriver,
    homepage_action: HomePage,
    vod_action: VOD,
    profiles_action: Profiles,
):
    element_xpath = "//*[contains(@text,'Indonesian Comedy Series')]"
    try:
        element = Profiles.scroll_to_element(driver, element_xpath)
        print("Element found")
    except Exception as e:
        print(e)

    delay(homepage_action.assertClusterComedy)
    delay(homepage_action.clickContentClusterComedy)


def test_TC_User_Can_Play_VOD_in_Serial_Komedi(
    driver: WebDriver,
    vod_action: VOD,
):
    delay(vod_action.assertDetailVod)
    delay(vod_action.clickBtnWatch)
    driver.press_keycode(4)
    driver.press_keycode(4)


def test_TC_User_Can_Click_any_Section_in_Because_You_Watched(
    driver: WebDriver,
    homepage_action: HomePage,
    vod_action: VOD,
    profiles_action: Profiles,
):
    element_xpath = "//*[contains(@text,'Because you watched')]"
    try:
        element = Profiles.scroll_to_element(driver, element_xpath)
        print("Element found")
    except Exception as e:
        print(e)

    delay(homepage_action.assertClusterBecauseYouWatched)
    delay(homepage_action.clickContentClusterBecauseYouWatched)


def test_TC_User_Can_Play_VOD_in_Because_You_Watched(
    driver: WebDriver,
    vod_action: VOD,
):
    delay(vod_action.assertDetailVod)
    delay(vod_action.clickBtnWatch)
    driver.press_keycode(4)
    driver.press_keycode(4)
