import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.pages.livetvPages import LiveTV
from MiradaVersion.pages.profilesPages import Profiles
from MiradaVersion.test.id_Mirada_Login.login_by_phone import login_free_by_phone
from MiradaVersion.test.open_app import free_phone_data
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


def delay(action, delay=4):
    if callable(action):
        action()
        time.sleep(delay)
    else:
        raise TypeError(f"Expected a callable action, but got {type(action)}")


def test_TC_User_Can_See_Detail_Banner(
    driver: WebDriver,
    free_phone_data,
    homepage_action: HomePage,
    profiles_action: Profiles,
):
    login_free_by_phone(driver, free_phone_data)

    delay(homepage_action.assertHomePage)
    # for _ in range(5):
    #     profiles_action.scroll_left(
    #         start_x=732, start_y=511, end_x=362, end_y=515, duration=300
    #     )
    delay(homepage_action.clickBanner)
    driver.press_keycode(4)


def test_TC_User_Can_Click_View_All_Vplus_Originals_Cluster(
    driver: WebDriver,
    homepage_action: HomePage,
):
    delay(homepage_action.clickViewlAllVplusOriginals)
    delay(homepage_action.assertBannerInfo)
    driver.press_keycode(4)


def test_TC_User_Can_Slide_list_Cluster_Vision_Originals(
    driver: WebDriver,
    homepage_action: HomePage,
    profiles_action: Profiles,
):
    for _ in range(7):
        profiles_action.scroll_left(
            start_x=889, start_y=1608, end_x=285, end_y=1608, duration=300
        )
