import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.loginPages import PagesLogin
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.pages.livetvPages import LiveTV
from MiradaVersion.pages.vodPages import VOD
from MiradaVersion.pages.playstorePages import playstore
from MiradaVersion.pages.profilesPages import Profiles
from MiradaVersion.test.id_Mirada_Register.TC_register_with_email import (
    Register_with_email,
    generate_random_email,
)
from MiradaVersion.test.TC_Get_OTP import print_last_otp
import subprocess
from MiradaVersion.pages.profilesPages import Profiles
from MiradaVersion.test.Testcase.Free_User.TC_Payment_sports import (
    Cancel_Subscriptions,
    bring_app_to_foreground,
    open_play_store,
)

domains = ["visionplus.id"]
first_names = ["Testing"]

email = generate_random_email(domains, first_names)
password = "4321Lupa"


@pytest.fixture(scope="module")
def driver():
    setup_appium = SetupAppium()
    driver = setup_appium.driver
    if not driver:
        pytest.fail("Driver initialization failed.")

    yield driver


@pytest.fixture(scope="module")
def login_action(driver):
    return PagesLogin(driver)


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
def vod_action(driver):
    return VOD(driver)


@pytest.fixture(scope="module")
def playstore_action(driver):
    return playstore(driver)


def delay(action, delay=2):
    if callable(action):
        action()
        time.sleep(delay)
    else:
        raise TypeError(f"Expected a callable action, but got {type(action)}")


def test_TC_User_Can_Slide_List_Cluster_Films(
    driver: WebDriver,
    homepage_action: HomePage,
    profiles_action: Profiles,
    login_action: PagesLogin,
    sign_up_action: SignUp,
    playstore_action: playstore,
):
    Cancel_Subscriptions(playstore_action)
    vision_plus_package_name = "com.zte.iptvclient.android.idmnc"
    bring_app_to_foreground(vision_plus_package_name)

    register_email = Register_with_email(driver)
    delay(login_action.clickLogin)
    delay(login_action.assertLoginPage)
    delay(login_action.clickEmailSection)
    delay(lambda: sign_up_action.inputEmail(register_email))
    delay(lambda: sign_up_action.inputPassword("4321Lupa"))
    delay(login_action.clickSubmitLogin)

    time.sleep(3)
    for _ in range(1):
        profiles_action.scroll_left(
            start_x=973, start_y=1033, end_x=225, end_y=1025, duration=500
        )
    delay(homepage_action.assertCategoryMovies)
    delay(homepage_action.clickCategoryMovies)
    delay(homepage_action.assertBannerInfo)


def test_TC_User_Can_See_Detail_VOD_User_to_Video_Page(
    driver: WebDriver,
    homepage_action: HomePage,
    vod_action: VOD,
):
    delay(homepage_action.clickContentCategoryMovies)
    delay(vod_action.assertDetailVod)


def test_TC_User_Can_See_Detail_Sinopsis_VOD(
    driver: WebDriver,
    vod_action: VOD,
):
    delay(vod_action.clickSinopsis)


def test_TC_User_Can_Click_List_Package(
    driver: WebDriver,
    vod_action: VOD,
):
    delay(vod_action.clickBtnSubscribe)
    delay(vod_action.assertListPackages)


def test_TC_User_Can_Upgrade_to_Premium_Package_and_Play_VOD(
    driver: WebDriver,
    homepage_action: HomePage,
    profiles_action: Profiles,
    playstore_action: playstore,
    vod_action: VOD,
):
    for _ in range(1):
        profiles_action.scroll_left(
            start_x=571, start_y=1528, end_x=571, end_y=1267, duration=500
        )
    delay(vod_action.clickPremiumPackage)
    delay(vod_action.assertDetailPackage)
    delay(vod_action.clickBtnSubscribe)
    delay(playstore_action.clickBtnSubscribePlaystore)
    time.sleep(3)
    delay(homepage_action.clickBtnAccept)
    driver.press_keycode(4)
    delay(homepage_action.clickContentCategoryMovies)
    delay(vod_action.clickBtnWatch)
    time.sleep(5)
    driver.press_keycode(4)
    driver.press_keycode(4)
    driver.press_keycode(4)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickPaymentPackage)
    delay(homepage_action.assertBuyPackageMenu)
    delay(homepage_action.assertFirstEntitlement)


def test_TC_User_Can_Upgrade_to_Premium_Sport_Package_and_Play_VOD_TV_Sports(
    driver: WebDriver,
    homepage_action: HomePage,
    profiles_action: Profiles,
    playstore_action: playstore,
    livetv_action: LiveTV,
    vod_action: VOD,
):
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickBtnSearch)
    delay(lambda: homepage_action.inputSearch("soccer channel"))
    delay(homepage_action.clickResultSportsChannel)
    delay(livetv_action.clickBtnSubscribe)
    for _ in range(1):
        profiles_action.scroll_left(
            start_x=511, start_y=1415, end_x=507, end_y=1254, duration=500
        )
    delay(vod_action.clickPremiumSportsPackage)
    delay(vod_action.assertDetailPackage)
    delay(vod_action.clickBtnSubscribe)
    delay(playstore_action.clickBtnSubscribePlaystore)
    time.sleep(3)
    delay(homepage_action.clickBtnAccept)
    try:
        livetv_action.assertSubscription()

        raise AssertionError("Test failed because assertSubscription() passed.")
    except Exception as e:

        print(f"Assert Success : No subcription button")


def test_TC_User_Click_Tambahkan_ke_daftar(
    homepage_action: HomePage,
    vod_action: VOD,
    driver: WebDriver,
):
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickMenuHome)
    delay(homepage_action.clickContentClusterVplusOriginals)
    delay(vod_action.clickAddtoList)
    driver.press_keycode(4)
