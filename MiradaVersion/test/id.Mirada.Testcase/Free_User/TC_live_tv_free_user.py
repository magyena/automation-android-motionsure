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


def test_TC_User_Cant_Watching_Live_TV_Channel_Premium(
    driver: WebDriver,
    free_phone_data,
    homepage_action: HomePage,
    livetv_action: LiveTV,
):
    login_free_by_phone(driver, free_phone_data)
    time.sleep(2)
    homepage_action.clickMenuButton()
    homepage_action.assertMenu()
    homepage_action.clickLiveTvMenu()
    livetv_action.assertLiveTV()
    livetv_action.clickTrans7Channel()
    livetv_action.assertSubscription()


def test_TC_User_Cant_Watching_Live_TV_Channel_Sports(
    livetv_action: LiveTV, profiles_action: Profiles
):
    for _ in range(6):
        profiles_action.scroll_down()

    livetv_action.clickSportChannel()
    livetv_action.assertSubscription()
