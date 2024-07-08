import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.livetvPages import LiveTV
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.pages.vodPages import VOD
from MiradaVersion.test.id_Mirada_Login.login_by_email import login_premium_by_email
from MiradaVersion.test.open_app import premium_email_data


@pytest.fixture(scope="module")
def driver():
    setup_appium = SetupAppium()
    driver = setup_appium.driver
    if not driver:
        pytest.fail("Driver initialization failed.")

    yield driver


@pytest.fixture(scope="module")
def vod_action(driver):
    return VOD(driver)


@pytest.fixture(scope="module")
def homepage_action(driver):
    return HomePage(driver)


@pytest.fixture(scope="module")
def livetv_action(driver):
    return LiveTV(driver)


def delay(action, delay=1):
    if callable(action):
        action()
        time.sleep(delay)
    else:
        raise TypeError(f"Expected a callable action, but got {type(action)}")


def test_TC_User_Can_Search_Not_Result(
    driver: WebDriver,
    premium_email_data,
    homepage_action: HomePage,
):
    login_premium_by_email(driver, premium_email_data)
    time.sleep(2)
    homepage_action.clickMenuButton()
    homepage_action.assertMenu()
    delay(homepage_action.clickBtnSearch)
    delay(lambda: homepage_action.inputSearch("xxasdasdasd"))
    delay(homepage_action.assertSearchNoResult)


def test_TC_User_Can_Search_VOD(
    driver: WebDriver,
    homepage_action: HomePage,
    vod_action: VOD,
):

    delay(lambda: homepage_action.inputSearch("montir"))
    delay(homepage_action.clickResultOne)
    delay(vod_action.assertDetailVod)
    driver.press_keycode(4)


def test_TC_User_Can_Search_LiveTV(
    driver: WebDriver,
    homepage_action: HomePage,
    livetv_action: LiveTV,
):
    delay(lambda: homepage_action.inputSearch("inews"))
    delay(homepage_action.clickResultLiveTV)
    delay(livetv_action.assertLiveTVInews)
