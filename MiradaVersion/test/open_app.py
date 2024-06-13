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
def free_email_data():
    with open(
        "/Users/fatahalim/Documents/Vision+/automation-android-python/MiradaVersion/utils/id_Mirada_TestData_Login/free_email.json"
    ) as file:
        data = json.load(file)
    print("Loaded free email data:", data)
    return data


@pytest.fixture
def premium_email_data():
    with open(
        "/Users/fatahalim/Documents/Vision+/automation-android-python/MiradaVersion/utils/id_Mirada_TestData_Login/loginPremium.json"
    ) as file:
        data = json.load(file)
    print("Loaded premium email data:", data)
    return data


@pytest.fixture
def premium_sport_email_data():
    with open(
        "/Users/fatahalim/Documents/Vision+/automation-android-python/MiradaVersion/utils/id_Mirada_TestData_Login/premiumSport_email.json"
    ) as file:
        data = json.load(file)
    print("Loaded premium sport email data:", data)
    return data


@pytest.fixture
def free_phone_data():
    with open(
        "/Users/fatahalim/Documents/Vision+/automation-android-python/MiradaVersion/utils/id_Mirada_TestData_Login/free_phone.json"
    ) as file:
        data = json.load(file)
    print("Loaded login data:", data)
    return data


@pytest.fixture
def premium_phone_data():
    with open(
        "/Users/fatahalim/Documents/Vision+/automation-android-python/MiradaVersion/utils/id_Mirada_TestData_Login/premium_phone.json"
    ) as file:
        data = json.load(file)
    print("Loaded login data:", data)
    return data


@pytest.fixture
def premium_sport_phone_data():
    with open(
        "/Users/fatahalim/Documents/Vision+/automation-android-python/MiradaVersion/utils/id_Mirada_TestData_Login/sport_phone.json"
    ) as file:
        data = json.load(file)
    print("Loaded login data:", data)
    return data


def loginFreeByEmail(driver: WebDriver, login_data):
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


def loginPremiumbyEmail(driver: WebDriver, login_data):
    if isinstance(login_data, list) and len(login_data) > 0:
        login_action = PagesLogin(driver)
        login = SignUp(driver)
        profile = Profiles(driver)
        homepage = HomePage(driver)

        login_action.clickLogin()
        login_action.assertLoginPage()
        login_action.clickEmailSection()
        login_action.assertEmailSection()
        login_action.inputEmail(
            login_data[0]["email"]
        )  # Ensure this key matches your JSON structure
        login.inputPassword(login_data[0]["password"])
        login_action.clickSubmitLogin()
        profile.assertProfilesPages()
        profile.clickFirstProfile()
        homepage.assertHomePage()
    else:
        raise ValueError("login_data is not a non-empty list as expected.")


def loginSportbyEmail(driver: WebDriver, login_data):
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


def loginFreebyPhone(driver: WebDriver, login_data):
    if isinstance(login_data, list) and len(login_data) > 0:
        login_action = PagesLogin(driver)
        login = SignUp(driver)
        profile = Profiles(driver)
        homepage = HomePage(driver)

        login_action.clickLogin()
        login_action.assertLoginPage()
        login.inputPhoneNumber(login_data[0]["phone"])
        login.inputPassword(login_data[0]["password"])
        login_action.clickSubmitLogin()
        profile.assertProfilesPages()
        profile.clickFirstProfile()
        homepage.assertHomePage()
    else:
        raise ValueError("login_data is not a non-empty list as expected.")


def loginPremiumbyPhone(driver: WebDriver, login_data):
    if isinstance(login_data, list) and len(login_data) > 0:
        login_action = PagesLogin(driver)
        login = SignUp(driver)
        profile = Profiles(driver)
        homepage = HomePage(driver)

        login_action.clickLogin()
        login_action.assertLoginPage()
        login.inputPhoneNumber(login_data[0]["phone"])
        login.inputPassword(login_data[0]["password"])
        login_action.clickSubmitLogin()
        profile.assertProfilesPages()
        profile.clickFirstProfile()
        homepage.assertHomePage()
    else:
        raise ValueError("login_data is not a non-empty list as expected.")


def loginSportbyPhone(driver: WebDriver, login_data):
    if isinstance(login_data, list) and len(login_data) > 0:
        login_action = PagesLogin(driver)
        login = SignUp(driver)
        profile = Profiles(driver)
        homepage = HomePage(driver)

        login_action.clickLogin()
        login_action.assertLoginPage()
        login.inputPhoneNumber(login_data[0]["phone"])
        login.inputPassword(login_data[0]["password"])
        login_action.clickSubmitLogin()
        profile.assertProfilesPages()
        profile.clickFirstProfile()
        homepage.assertHomePage()
    else:
        raise ValueError("login_data is not a non-empty list as expected.")


def Choose_Login_As(
    driver: WebDriver,
    login_type: str,
    free_email_data=None,
    premium_email_data=None,
    premium_sport_email_data=None,
    free_phone_data=None,
    premium_phone_data=None,
    premium_sport_phone_data=None,
):
    if login_type == "FREE":
        if free_phone_data:
            loginFreebyPhone(driver, free_phone_data)
        elif free_email_data:
            loginFreeByEmail(driver, free_email_data)
        else:
            raise ValueError(
                "Free phone data or free email data is required for FREE login"
            )
    elif login_type == "PREMIUM":
        if premium_email_data:
            loginPremiumbyEmail(driver, premium_email_data)
        elif premium_phone_data:
            loginPremiumbyPhone(driver, premium_phone_data)
        else:
            raise ValueError(
                "Premium phone data or Premium email data is required for Premium login"
            )
    elif login_type == "PREMIUM_SPORT":
        if premium_sport_email_data:
            loginSportbyEmail(driver, premium_sport_email_data)
        elif premium_sport_phone_data:
            loginSportbyPhone(driver, premium_sport_phone_data)
        else:
            raise ValueError(
                "Premium Sport phone data or Premium Sport email data is required for Premium  Sport login"
            )
    else:
        raise ValueError("Invalid login type")
