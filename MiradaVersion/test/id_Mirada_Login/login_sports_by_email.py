from appium.webdriver.webdriver import WebDriver
import pytest
import json
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.loginPages import PagesLogin
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.profilesPages import Profiles
from MiradaVersion.pages.homepagePages import HomePage


@pytest.fixture(scope="module")
def driver():
    setup_appium = SetupAppium()
    yield setup_appium.driver


@pytest.fixture
def login_data():
    with open(
        "/Users/fatahalim/Documents/Vision/automation-android-python/MiradaVersion/utils/id_Mirada_TestData_Login/premiumSport_email.json"
    ) as file:
        data = json.load(file)
    print("Loaded login data:", data)
    return data


def test_loginByEmailSuccess(driver: WebDriver, login_data):
    if isinstance(login_data, list) and len(login_data) > 0:
        login_action = PagesLogin(driver)
        login = SignUp(driver)
        profile = Profiles(driver)
        homepage = HomePage(driver)

        login_action.clickLogin()
        login_action.assertLoginPage()
        login_action.clickEmailSection()
        login_action.assertEmailSection()
        login_action.inputEmail(login_data[0]["username"])
        login.inputPassword(login_data[0]["password"])
        login_action.clickSubmitLogin()
        profile.assertProfilesPages()
        profile.clickFirstProfile()
        homepage.assertHomePage()
    else:
        raise ValueError("login_data is not a non-empty list as expected.")
