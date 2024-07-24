import pytest
import time
from appium.webdriver.webdriver import WebDriver
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.pages.loginPages import PagesLogin
from MiradaVersion.pages.homepagePages import HomePage
from MiradaVersion.pages.vodPages import VOD
from MiradaVersion.pages.settingsPages import SettingsPages
from MiradaVersion.pages.playstorePages import playstore
from MiradaVersion.test.id_Mirada_Register.TC_register_with_email import (
    Register_with_email,
    generate_random_email,
)
from MiradaVersion.test.TC_Get_OTP import print_last_otp
import subprocess

domains = ["visionplus.id"]
first_names = ["Testing"]

email = generate_random_email(domains, first_names)

password = "4321Lupa"


@pytest.fixture(scope="module")
def driver():
    setup_appium = SetupAppium()
    driver = setup_appium.driver
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def reopendriver():
    setup_appium = SetupAppium()
    driver = setup_appium.driver
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def sign_up_action(driver):
    return SignUp(driver)


@pytest.fixture(scope="module")
def login_action(driver):
    return PagesLogin(driver)


@pytest.fixture(scope="module")
def homepage_action(driver):
    return HomePage(driver)


@pytest.fixture(scope="module")
def vod_action(driver):
    return VOD(driver)


@pytest.fixture(scope="module")
def playstore_action(driver):
    return playstore(driver)


@pytest.fixture(scope="module")
def setting_action(driver):
    return SettingsPages(driver)


def delay(action, delay=1):
    if callable(action):
        action()
        time.sleep(delay)
    else:
        raise TypeError(f"Expected a callable action, but got {type(action)}")


def open_play_store(emulator_id):
    # adb = "/Users/fatahalim/Library/Android/sdk/platform-tools/adb"
    adb = "/users/visionplus/Library/Android/sdk/platform-tools/adb"
    command = f"{adb} -s {emulator_id} shell am start -a android.intent.action.VIEW -d 'https://play.google.com/store'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr


# emulator_id = "cisoeqnjnnhqmr5l"
emulator_id = "emulator-5554"


def bring_app_to_foreground(package_name: str):
    # adb_path = "/Users/fatahalim/Library/Android/sdk/platform-tools/adb"
    adb_path = "/users/visionplus/Library/Android/sdk/platform-tools/adb"  # Uncomment this line if needed

    """Function to bring a specific app to the foreground."""
    subprocess.run(
        [
            adb_path,
            "shell",
            "monkey",
            "-p",
            package_name,
            "-c",
            "android.intent.category.LAUNCHER",
            "1",
        ]
    )


def Cancel_Subscriptions(
    playstore_action: playstore,
):
    open_play_store(emulator_id)
    delay(playstore_action.clickProfilePlaystore)
    delay(playstore_action.clickPayments)
    delay(playstore_action.clickSubscriptions)

    try:
        checked_first_package = False
        while True:
            package_found = False
            if not checked_first_package and playstore_action.assertFirstPackage():
                delay(playstore_action.clickFirstPackage)
                package_found = True
                checked_first_package = True
            elif playstore_action.assertSecondPackage():
                delay(playstore_action.clickSecondPackage)
                package_found = True
                if package_found:
                    delay(playstore_action.clickBtnCancelSubscription)
                    delay(playstore_action.clickBtnNoThanks)
                    delay(playstore_action.clickReasonCancel)
                    delay(playstore_action.clickBtnContinue)
                    delay(playstore_action.clickBtnCancelSubscription)
                    delay(playstore_action.clickBtnBack)
                break
            else:
                print("Neither Premium Package nor Premium Sport Package is present.")
                break

            if package_found:
                delay(playstore_action.clickBtnCancelSubscription)
                delay(playstore_action.clickBtnNoThanks)
                delay(playstore_action.clickReasonCancel)
                delay(playstore_action.clickBtnContinue)
                delay(playstore_action.clickBtnCancelSubscription)
                delay(playstore_action.clickBtnBack)
            else:
                print(
                    "No subscription package found, so cancellation steps are not executed."
                )
                break
    except Exception as e:
        print("No active package")


def test_TC_Free_User_Payment_Premiu_Sports(
    driver: WebDriver,
    login_action: PagesLogin,
    homepage_action: HomePage,
    sign_up_action: SignUp,
    vod_action: VOD,
    playstore_action: playstore,
):
    Cancel_Subscriptions(playstore_action)
    vision_plus_package_name = "com.zte.iptvclient.android.idmnc"
    bring_app_to_foreground(vision_plus_package_name)

    time.sleep(3)

    register_email = Register_with_email(driver)
    time.sleep(3)

    delay(login_action.clickLogin)
    delay(login_action.assertLoginPage)
    delay(login_action.clickEmailSection)
    delay(lambda: sign_up_action.inputEmail(register_email))
    delay(lambda: sign_up_action.inputPassword("4321Lupa"))
    delay(login_action.clickSubmitLogin)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickPaymentPackage)
    delay(homepage_action.assertBuyPackageMenu)
    delay(homepage_action.clickPackagePremiumSports30)
    delay(vod_action.assertDetailPackage)
    delay(vod_action.clickBtnSubscribe)
    delay(playstore_action.clickBtnSubscribePlaystore)
    time.sleep(3)
    delay(homepage_action.clickBtnAccept)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickMenuHome)
    delay(homepage_action.clickMenuButton)
    delay(homepage_action.clickPaymentPackage)
    delay(homepage_action.assertBuyPackageMenu)
    delay(homepage_action.assertFirstEntitlement)
