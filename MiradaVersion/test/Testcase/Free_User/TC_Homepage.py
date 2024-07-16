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
from MiradaVersion.pages.vodPages import VOD
from selenium.common.exceptions import NoSuchElementException


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
def vod_action(driver):
    return VOD(driver)


@pytest.fixture(scope="module")
def profiles_action(driver):
    return Profiles(driver)


@pytest.fixture(scope="module")
def livetv_action(driver):
    return LiveTV(driver)


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
    for _ in range(5):
        profiles_action.scroll_left(
            start_x=732, start_y=511, end_x=362, end_y=515, duration=300
        )
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
    profiles_action: Profiles,
):
    for _ in range(7):
        profiles_action.scroll_left(
            start_x=889, start_y=1608, end_x=285, end_y=1608, duration=300
        )


def test_TC_UserCan_See_Detail_VOD_Vision_Original(
    driver: WebDriver,
    homepage_action: HomePage,
    vod_action: VOD,
):
    delay(homepage_action.clickContentClusterVplusOriginals)
    delay(vod_action.assertDetailVod)


def test_TC_User_Can_Play_Vod(
    driver: WebDriver,
    vod_action: VOD,
):
    delay(vod_action.clickBtnWatch)
    driver.press_keycode(4)


def test_TC_User_Can_Like_Vod(
    vod_action: VOD,
):
    delay(vod_action.clickLike)


def test_TC_User_Can_disLike_Vod(
    vod_action: VOD,
):
    delay(vod_action.clickDislike)


def test_TC_User_Can_Share_Vod(
    vod_action: VOD,
    driver: WebDriver,
):
    delay(vod_action.clickShare)
    driver.press_keycode(4)


def test_TC_User_Free_Play_Premium_VOD(
    vod_action: VOD,
):
    delay(vod_action.clickEps3Premium)
    delay(vod_action.assertContentPremium)
    delay(vod_action.clickBtnSubscribe)
    delay(vod_action.assertListPackages)


def test_TC_User_Click_any_Upgrade_Package_Subscribe(
    vod_action: VOD,
):
    delay(vod_action.clickPremiumSportsPackage)
    delay(vod_action.assertDetailPackage)
    delay(vod_action.clickBtnBack)
    delay(vod_action.clickBtnBack)
    delay(vod_action.clickBtnBack)


def test_TC_User_Can_Slide_list_Cluster_Live_TV_Channels(
    homepage_action: HomePage,
    driver: WebDriver,
    livetv_action: LiveTV,
):
    element_xpath = "//*[contains(@text,'Your Favorite TV Channel')]"
    try:
        element = Profiles.scroll_to_element(driver, element_xpath)
        print("Element found")
    except Exception as e:
        print(e)

    delay(homepage_action.clickViewlAllVplusOriginals)
    delay(homepage_action.assertClusterLiveTV)

    element_xpath = "//*[contains(@text,'Lifestyle')]"
    try:
        element = Profiles.scroll_to_element(driver, element_xpath)
        print("Element found")
    except Exception as e:
        print(e)


def test_TC_User_Click_Any_Live_Channels(
    homepage_action: HomePage,
    driver: WebDriver,
    livetv_action: LiveTV,
):
    profile = Profiles(driver)
    for _ in range(2):
        profile.scrollUp()

    delay(homepage_action.clickChannelClusterLivetv)
    delay(livetv_action.assertLiveTV)


def test_TC_User_Can_Slide_Cluster_VOD_in_Indonesia_Top_10_This_Week(
    homepage_action: HomePage,
    driver: WebDriver,
    profiles_action: Profiles,
):
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickMenuHome)
    element_xpath = "//*[contains(@text,'Top 10 This Week')]"
    try:
        element = Profiles.scroll_to_element(driver, element_xpath)
        print("Element found")
    except Exception as e:
        print(e)

    for _ in range(5):
        profiles_action.scroll_left(
            start_x=985, start_y=1846, end_x=197, end_y=1841, duration=100
        )


def test_TC_User_Can_Click_Cluster_VOD_in_Indonesia_Top_10_This_Week(
    homepage_action: HomePage,
    vod_action: VOD,
):
    delay(homepage_action.clickContentClusterTop10)
    delay(vod_action.assertDetailVod)


def test_TC_User_Can_Added_list_Watchlist_Series(
    vod_action: VOD,
    homepage_action: HomePage,
    driver: WebDriver,
):
    delay(vod_action.clickAddtoList)
    delay(vod_action.clickBtnBack)
    element_xpath = "//*[contains(@text,'Watchlist')]"
    try:
        element = Profiles.scroll_to_element(driver, element_xpath)
        print("Element found")
    except Exception as e:
        print(e)

    delay(homepage_action.assertClusterWatchlist)


def test_TC_User_Cant_See_Cluster_Watchlist_in_Other_Profile(
    vod_action: VOD,
    homepage_action: HomePage,
    driver: WebDriver,
    profiles_action: Profiles,
):
    delay(homepage_action.clickBtnProfile)
    delay(profiles_action.assertProfilesPages)
    delay(profiles_action.clickSecondProfile)
    element_xpath = "//*[contains(@text,'Watchlist')]"
    try:
        element = Profiles.scroll_to_element(driver, element_xpath)
        print("Element found")
    except NoSuchElementException:
        print("No element found")
    except Exception as e:
        print(f"An error occurred: {e}")


def test_TC_User_Can_Slide_Any_VOD_Cluster_NewRelease(
    homepage_action: HomePage,
    driver: WebDriver,
    profiles_action: Profiles,
):
    profile = Profiles(driver)
    for _ in range(5):
        profile.scrollUp()

    delay(homepage_action.clickBtnProfile)
    delay(profiles_action.clickFirstProfile)
    element_xpath = "//*[contains(@text,'New Releases')]"
    try:
        element = Profiles.scroll_to_element(driver, element_xpath)
        print("Element found")
    except Exception as e:
        print(e)

    delay(homepage_action.assertClusterNewReleases)

    for _ in range(5):
        profiles_action.scroll_left(
            start_x=905, start_y=1552, end_x=237, end_y=1560, duration=100
        )


def test_TC_User_Can_Click_Any_VOD_Cluster_NewRelease(
    vod_action: VOD,
    homepage_action: HomePage,
):
    delay(homepage_action.clickContentClusterNewReleases)
    delay(vod_action.assertDetailVod)
    delay(vod_action.clickBtnBack)


def test_TC_User_Cant_See_Live_TV_In_Cluster_Continue_Watching(
    driver: WebDriver,
):
    element_xpath = "//*[contains(@text,'Watchlist')]"
    try:
        element = Profiles.scroll_to_element(driver, element_xpath)
        print("Element found")
    except Exception as e:
        print(e)


def test_TC_User_Can_Click_Cluster_VOD_in_Explore_by_Genre(
    driver: WebDriver,
    homepage_action: HomePage,
):
    element_xpath = "//*[contains(@text,'Explore by Genre')]"
    try:
        element = Profiles.scroll_to_element(driver, element_xpath)
        print("Element found")
    except Exception as e:
        print(e)
    delay(homepage_action.assertClusterExplorebyGenre)
    delay(homepage_action.clickActionGenre)


def test_TC_User_Can_Play_Content_VOD_in_Explore_by_Genre(
    driver: WebDriver,
    homepage_action: HomePage,
    vod_action: VOD,
):
    delay(homepage_action.clickContentActionGenre)
    delay(vod_action.assertDetailVod)
    delay(vod_action.clickBtnWatch)
    driver.press_keycode(4)
    delay(vod_action.clickBtnBack)
    delay(vod_action.clickBtnBack)


def test_TC_User_Can_Click_Any_Section_in_Popular_Actors(
    driver: WebDriver,
    homepage_action: HomePage,
    vod_action: VOD,
):
    element_xpath = "//*[contains(@text,'Popular Actors')]"
    try:
        element = Profiles.scroll_to_element(driver, element_xpath)
        print("Element found")
    except Exception as e:
        print(e)
    delay(homepage_action.assertClusterPopularActors)
    delay(homepage_action.clickTheActors)


def test_TC_User_Can_Play_VOD_Popular_Actors(
    driver: WebDriver,
    homepage_action: HomePage,
    vod_action: VOD,
):
    delay(homepage_action.clickContentPopularActors)
    delay(vod_action.assertDetailVod)
    delay(vod_action.clickBtnWatch)
    driver.press_keycode(4)


def test_TC_User_Can_Slide_Last_Banner(
    profiles_action: Profiles,
    homepage_action: HomePage,
    vod_action: VOD,
):
    delay(vod_action.clickBtnBack)
    delay(vod_action.clickBtnBack)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickLiveTvMenu)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickMenuHome)

    for _ in range(5):
        profiles_action.scroll_left(
            start_x=961, start_y=527, end_x=310, end_y=519, duration=300
        )
