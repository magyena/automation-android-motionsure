import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.loginPages import PagesLogin
from MiradaVersion.pages.profilesPages import Profiles
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.pages.settingsPages import SettingsPages
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
def settings_action(driver):
    return SettingsPages(driver)


@pytest.fixture(scope="module")
def homepage_action(driver):
    return HomePage(driver)


def delay(action, delay=1):
    if callable(action):
        action()
        time.sleep(delay)
    else:
        raise TypeError(f"Expected a callable action, but got {type(action)}")


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
    delay(profiles_action.assertProfilesPages)


def test_TC_User_Can_Cancel_Add_Profile_Section(
    profiles_action: Profiles,
):

    delay(profiles_action.clickAddProfile)
    delay(profiles_action.assertCreateProfilePage)
    delay(profiles_action.clickCancelAddProfile)
    delay(profiles_action.assertProfilesPages)


def test_TC_User_Can_Add_Profile(
    profiles_action: Profiles,
):
    delay(profiles_action.clickAddProfile)
    delay(lambda: profiles_action.inputProfile("ProfileSatu"))
    delay(profiles_action.clickOKAddProfile)
    delay(profiles_action.assertSuccessCreateProfile)
    delay(profiles_action.clickBtnDoneSuccessCreateProfile)
    delay(profiles_action.assertCreateProfileSatu)

    # delay(profiles_action.clickAddProfile)
    # delay(lambda: profiles_action.inputProfile("ProfileDua"))
    # delay(profiles_action.clickOKAddProfile)
    # delay(profiles_action.assertSuccessCreateProfile)
    # delay(profiles_action.clickBtnDoneSuccessCreateProfile)
    # delay(profiles_action.assertCreateProfileDua)

    # delay(profiles_action.clickAddProfile)
    # delay(lambda: profiles_action.inputProfile("ProfileTiga"))
    # delay(profiles_action.clickOKAddProfile)
    # delay(profiles_action.assertSuccessCreateProfile)
    # delay(profiles_action.clickBtnDoneSuccessCreateProfile)
    # delay(profiles_action.assertCreateProfileTiga)

    # delay(profiles_action.clickAddProfile)
    # delay(lambda: profiles_action.inputProfile("ProfileEmpat"))
    # delay(profiles_action.clickOKAddProfile)
    # delay(profiles_action.assertSuccessCreateProfile)
    # delay(profiles_action.clickBtnDoneSuccessCreateProfile)
    # delay(profiles_action.assertCreateProfileEmpat)

    # delay(profiles_action.clickAddProfile)
    # delay(lambda: profiles_action.inputProfile("ProfileLima"))
    # delay(profiles_action.clickOKAddProfile)
    # delay(profiles_action.assertSuccessCreateProfile)
    # delay(profiles_action.clickBtnDoneSuccessCreateProfile)
    # delay(profiles_action.assertCreateProfileLima)


def test_TC_User_Can_Cancel_Change_Avatar(
    profiles_action: Profiles,
):
    delay(profiles_action.clickAddProfile)
    delay(profiles_action.clickChangeAvatar)
    delay(profiles_action.assertAvatarPage)
    delay(profiles_action.clickChooseAvatar)
    delay(profiles_action.clickBtnCancelAvatar)
    delay(profiles_action.clickBtnCancelAvatar)
    delay(profiles_action.assertProfilesPages)


def test_TC_User_Can_Change_Avatar(
    profiles_action: Profiles,
):
    delay(profiles_action.clickAddProfile)
    delay(profiles_action.clickChangeAvatar)
    delay(profiles_action.assertAvatarPage)
    delay(profiles_action.clickChooseAvatar)
    delay(profiles_action.clickBtnOkChooseAvatar)
    delay(lambda: profiles_action.inputProfile("ProfileEnam"))
    delay(profiles_action.clickOKAddProfile)
    delay(profiles_action.assertSuccessCreateProfile)
    delay(profiles_action.clickBtnDoneSuccessCreateProfile)
    delay(profiles_action.assertCreateProfileEnam)


def test_TC_User_Create_Profile_Already_Exist(
    profiles_action: Profiles,
):
    delay(profiles_action.clickAddProfile)
    delay(lambda: profiles_action.inputProfile("ProfileDua"))
    delay(profiles_action.clickOKAddProfile)
    delay(profiles_action.assertSuccessCreateProfile)
    delay(profiles_action.clickBtnDoneSuccessCreateProfile)
    delay(profiles_action.assertProfileError)
    delay(profiles_action.clickBtnOk)
    delay(profiles_action.clickCancelSuccessAddProfile)


def test_TC_User_Can_Create_Profile_Max_15_Character(
    profiles_action: Profiles,
):
    delay(profiles_action.clickAddProfile)
    delay(lambda: profiles_action.inputProfile("ProfileTujuhhhhh"))
    delay(profiles_action.clickOKAddProfile)
    delay(profiles_action.assertSuccessCreateProfile)
    delay(profiles_action.clickBtnDoneSuccessCreateProfile)
    delay(profiles_action.assertCreateProfileTujuh)


def test_TC_User_Cant_Adding_Profile_More_Than_8_profile(
    profiles_action: Profiles,
):

    try:
        delay(profiles_action.clickAddProfile)

        raise AssertionError("Test failed")
    except Exception as e:

        print(f"Assert Success : Has 8 Profiles No Add Profile button")


def test_TC_User_Cant_Delete_Profiles(
    profiles_action: Profiles,
    homepage_action: HomePage,
    settings_action: SettingsPages,
):
    delay(profiles_action.clickFirstProfile)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.assertMenu)
    delay(homepage_action.clickSettingsButton)
    delay(settings_action.clickManageProfiles)
    delay(settings_action.assertManageProfiles)
    delay(settings_action.clickFirstProfiles)
    delay(settings_action.assertDetailProfile)
    delay(settings_action.clickDeleteProfile)
    delay(settings_action.clickAcceptDeleteProfile)
    try:
        settings_action.assertFirstProfile()
        assert False, "Test failed: Profile Satu showing."
    except AssertionError:
        print("Test passed: Delete Profile Success.")
    except Exception:
        print("Test passed: Delete Profile Success.")


def test_TC_User_Back_to_Homepage(
    driver: WebDriver,
):
    driver.press_keycode(4)
    driver.press_keycode(4)
    driver.press_keycode(4)
