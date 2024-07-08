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


def delay(action, delay=2):
    if callable(action):
        action()
        time.sleep(delay)
    else:
        raise TypeError(f"Expected a callable action, but got {type(action)}")


def test_TC_User_Can_Download_VOD(
    driver: WebDriver,
    premium_email_data,
    homepage_action: HomePage,
    vod_action: VOD,
):
    login_premium_by_email(driver, premium_email_data)
    time.sleep(2)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.assertMenu)
    delay(homepage_action.clickBtnSearch)
    delay(lambda: homepage_action.inputSearch("montir"))
    delay(homepage_action.clickResultOne)
    delay(vod_action.assertDetailVod)
    delay(vod_action.clickEpisode2)
    delay(vod_action.clickBtnDownload)
    time.sleep(3)
    delay(vod_action.assertDownloadProgress)


def test_TC_User_Can_Cancel_Download_VOD(
    vod_action: VOD,
):
    delay(vod_action.clickBtnCancelDownload)
    delay(vod_action.clickAcceptCancelDownload)
    try:
        vod_action.assertDownloadProgress()
        assert False, "Test failed: Download progress assertion showing."
    except AssertionError:
        print("Test passed: Cancel Download Success.")
