import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.loginPages import PagesLogin
from MiradaVersion.pages.profilesPages import Profiles
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.test.id_Mirada_Register.TC_register_with_phone import (
    Register_with_phone,
)
from MiradaVersion.test.TC_Get_OTP import print_last_otp
from MiradaVersion.test.id_Mirada_Register.TC_register_with_phone import (
    generate_random_phone_number,
)

phone_number = generate_random_phone_number()
password = "4321Lupa"


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
def login_action(driver):
    return PagesLogin(driver)


@pytest.fixture(scope="module")
def profiles_action(driver):
    return Profiles(driver)


@pytest.fixture(scope="module")
def homepage_action(driver):
    return HomePage(driver)


def test_TC_User_Can_Access_Add_Profile_Section(
    driver: WebDriver,
    sign_up_action: SignUp,
    login_action: PagesLogin,
    profiles_action: Profiles,
    homepage_action: HomePage,
):
    phone_number = Register_with_phone(driver)
    time.sleep(3)
    login_action.clickLogin()
    sign_up_action.inputPhoneNumber(phone_number)
    sign_up_action.inputPassword(password)
    login_action.clickSubmitLogin()
    homepage_action.clickBtnProfile()
    profiles_action.assertProfilesPages()


def test_TC_User_Can_Cancel_Add_Profile_Section(
    profiles_action: Profiles,
):

    profiles_action.clickAddProfile()
    profiles_action.assertCreateProfilePage()
    profiles_action.clickCancelAddProfile()
    profiles_action.assertProfilesPages()


def test_TC_User_Can_Add_Profile(
    profiles_action: Profiles,
):
    profiles_action.clickAddProfile()
    profiles_action.inputProfile("ProfileSatu")
    profiles_action.clickOKAddProfile()
    profiles_action.assertSuccessCreateProfile()
    profiles_action.clickBtnDoneSuccessCreateProfile()
    profiles_action.assertCreateProfileSatu()

    profiles_action.clickAddProfile()
    profiles_action.inputProfile("ProfileDua")
    profiles_action.clickOKAddProfile()
    profiles_action.assertSuccessCreateProfile()
    profiles_action.clickBtnDoneSuccessCreateProfile()
    profiles_action.assertCreateProfileDua()

    profiles_action.clickAddProfile()
    profiles_action.inputProfile("ProfileTiga")
    profiles_action.clickOKAddProfile()
    profiles_action.assertSuccessCreateProfile()
    profiles_action.clickBtnDoneSuccessCreateProfile()
    profiles_action.assertCreateProfileTiga()

    profiles_action.clickAddProfile()
    profiles_action.inputProfile("ProfileEmpat")
    profiles_action.clickOKAddProfile()
    profiles_action.assertSuccessCreateProfile()
    profiles_action.clickBtnDoneSuccessCreateProfile()
    profiles_action.assertCreateProfileEmpat()

    profiles_action.clickAddProfile()
    profiles_action.inputProfile("ProfileLima")
    profiles_action.clickOKAddProfile()
    profiles_action.assertSuccessCreateProfile()
    profiles_action.clickBtnDoneSuccessCreateProfile()
    profiles_action.assertCreateProfileLima()


def test_TC_User_Can_Change_Avatar(
    profiles_action: Profiles,
):
    profiles_action.clickAddProfile()
    profiles_action.clickChangeAvatar()
    profiles_action.assertAvatarPage()
    profiles_action.clickChooseAvatar()
    profiles_action.clickBtnOkChooseAvatar()
    profiles_action.inputProfile("ProfileEnam")
    profiles_action.clickOKAddProfile()
    profiles_action.assertSuccessCreateProfile()
    profiles_action.clickBtnDoneSuccessCreateProfile()
    profiles_action.assertCreateProfileEnam()


def test_TC_User_Can_Create_Profile_Max_15_Character(
    profiles_action: Profiles,
):
    profiles_action.clickAddProfile()
    profiles_action.inputProfile("ProfileTujuhhhhh")
    profiles_action.clickOKAddProfile()
    profiles_action.assertSuccessCreateProfile()
    profiles_action.clickBtnDoneSuccessCreateProfile()
    profiles_action.assertCreateProfileTujuh()


def test_TC_User_Cant_Adding_Profile_More_Than_8_profile(
    profiles_action: Profiles,
):

    try:
        profiles_action.clickAddProfile()

        raise AssertionError("Test failed")
    except Exception as e:

        print(f"Assert Success : Has 8 Profiles No Add Profile button")
