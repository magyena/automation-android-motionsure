from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MiradaVersion.utils.handler import HandlerRemote
from selenium.common.exceptions import TimeoutException
import time
import subprocess
from MiradaVersion.object.profileObject import profileObject
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Profiles:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.profileobj = profileObject()

    def scrollDown(self):
        finger = PointerInput(interaction.POINTER_TOUCH, "finger")
        actions = ActionChains(self.driver)

        actions.w3c_actions.pointer_action.move_to_location(570, 1730)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(570, 590)
        actions.w3c_actions.pointer_action.pointer_up()

        actions.perform()

    def scroll_down(self):

        size = self.driver.get_window_size()
        start_x = size["width"] // 5
        start_y = size["height"] * 6 // 7
        end_x = size["width"] // 5
        end_y = size["height"] // 7

        self.driver.swipe(start_x, start_y, end_x, end_y, 790)

    @staticmethod
    def scroll_to_element(driver, element_xpath, max_swipes=15):
        size = driver.get_window_size()
        start_x = size["width"] // 5
        start_y = size["height"] * 6 // 7
        end_x = start_x
        end_y = size["height"] // 7

        for _ in range(max_swipes):
            try:
                element = driver.find_element(By.XPATH, element_xpath)
                if element.is_displayed():
                    return element
            except NoSuchElementException:
                driver.swipe(start_x, start_y, end_x, end_y, 800)
            else:
                break  # Stop swiping if element is found

        raise Exception("Element not found after maximum swipes")

    def scroll_left(
        self,
        start_x=None,
        start_y=None,
        end_x=None,
        end_y=None,
        start_x_ratio=None,
        start_y_ratio=None,
        end_x_ratio=None,
        end_y_ratio=None,
        duration=300,
    ):

        size = self.driver.get_window_size()

        if start_x is None and start_x_ratio is not None:
            start_x = int(size["width"] * start_x_ratio)
        if start_y is None and start_y_ratio is not None:
            start_y = int(size["height"] * start_y_ratio)
        if end_x is None and end_x_ratio is not None:
            end_x = int(size["width"] * end_x_ratio)
        if end_y is None and end_y_ratio is not None:
            end_y = int(size["height"] * end_y_ratio)

        if None in [start_x, start_y, end_x, end_y]:
            raise ValueError(
                "You must provide either absolute positions or relative ratios for all start and end points."
            )

        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def scroll_right(
        self,
        start_x=None,
        start_y=None,
        end_x=None,
        end_y=None,
        start_x_ratio=None,
        start_y_ratio=None,
        end_x_ratio=None,
        end_y_ratio=None,
        duration=300,
    ):

        size = self.driver.get_window_size()

        if start_x is None and start_x_ratio is not None:
            start_x = int(size["width"] * start_x_ratio)
        if start_y is None and start_y_ratio is not None:
            start_y = int(size["height"] * start_y_ratio)
        if end_x is None and end_x_ratio is not None:
            end_x = int(size["width"] * end_x_ratio)
        if end_y is None and end_y_ratio is not None:
            end_y = int(size["height"] * end_y_ratio)

        if None in [start_x, start_y, end_x, end_y]:
            raise ValueError(
                "You must provide either absolute positions or relative ratios for all start and end points."
            )

        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def scrollUp(self):
        finger = PointerInput(interaction.POINTER_TOUCH, "finger")
        actions = ActionChains(self.driver)

        actions.w3c_actions.pointer_action.move_to_location(507, 350)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(487, 1777)
        actions.w3c_actions.pointer_action.pointer_up()

        actions.perform()

    def disable_wifi_connection(self, emulator_id):
        # adb_path = "/Users/fatahalim/Library/Android/sdk/platform-tools/adb"
        adb_path = "/users/visionplus/Library/Android/sdk/platform-tools/adb"

        try:
            subprocess.run(
                [adb_path, "-s", emulator_id, "shell", "svc", "wifi", "disable"],
                check=True,
            )
            print(f"WiFi disabled successfully.")
        except subprocess.CalledProcessError as e:
            print("Error disabling WiFi:", e)

    def enable_wifi_connection(self, emulator_id):
        # adb_path = "/Users/fatahalim/Library/Android/sdk/platform-tools/adb"
        adb_path = "/users/visionplus/Library/Android/sdk/platform-tools/adb"

        try:
            subprocess.run(
                [adb_path, "-s", emulator_id, "shell", "svc", "wifi", "enable"],
                check=True,
            )
            print("Wifi data enabled successfully.")
        except subprocess.CalledProcessError as e:
            print("Error enabling Wifi data:", e)

    def clickFirstProfile(self):

        img_first_profile = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.profileobj.first_profile))
        )
        img_first_profile.click()

    def assertProfilesPages(self):
        try:
            self.wait = WebDriverWait(self.driver, 20)
            element = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.profileobj.first_profile)
                )
            )
            print("Assert Success : Assert Profile Pages Success")
            return element
        except AssertionError:
            print("Assert Failed : Assert Profile Pages Success")
            return element

    def inputPhoneNumber(self, phone):
        self.wait = WebDriverWait(self.driver, 20)

        txt_fld_phone_number = self.driver.find_element(
            By.XPATH, self.loginObj.txt_fld_phone_number
        )

        txt_fld_phone_number.click()
        time.sleep(3)
        txt_fld_phone_number.send_keys(phone)

    def clickAddProfile(self):

        btn_add_profile = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.profileobj.add_profile_button))
        )
        btn_add_profile.click()

    def clickCancelAddProfile(self):

        btn_cancel = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.profileobj.btn_cancel_create_profile)
            )
        )
        btn_cancel.click()

    def clickOKAddProfile(self):

        btn_ok = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.profileobj.btn_ok_create_profile)
            )
        )
        btn_ok.click()

    def assertCreateProfilePage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, self.profileobj.txt_create_profile)
                )
            )
            print("Assert Success : Assert Create Profile Page Success")
        except AssertionError:
            print("Assert Failed : Assert Create Profile Page Failed")

    def inputProfile(self, profile):
        self.wait = WebDriverWait(self.driver, 20)

        input_profile = self.driver.find_element(
            By.ID, self.profileobj.fld_create_profile
        )

        input_profile.clear()
        time.sleep(3)
        input_profile.click()
        time.sleep(3)
        input_profile.send_keys(profile)

    def assertSuccessCreateProfile(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, self.profileobj.txt_success_create_profile)
                )
            )
            print("Assert Success : Assert Done Create Profile Success")
        except AssertionError:
            print("Assert Failed : Assert Done Create Profile Failed")

    def clickBtnDoneSuccessCreateProfile(self):

        btn_done = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.ID, self.profileobj.btn_done_success_create_profile)
            )
        )
        btn_done.click()

    def assertCreateProfileSatu(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.profileobj.txt_create_profile_satu)
                )
            )
            print("Assert Success : Assert Create Profile Satu Success")
        except AssertionError:
            print("Assert Failed : Assert Create Profile Satu Failed")

    def assertCreateProfileDua(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.profileobj.txt_create_profile_dua)
                )
            )
            print("Assert Success : Assert Create Profile Dua Success")
        except AssertionError:
            print("Assert Failed : Assert Create Profile Dua Failed")

    def assertCreateProfileTiga(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.profileobj.txt_create_profile_tiga)
                )
            )
            print("Assert Success : Assert Create Profile Tiga Success")
        except AssertionError:
            print("Assert Failed : Assert Create Profile Tiga Failed")

    def assertCreateProfileEmpat(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.profileobj.txt_create_profile_empat)
                )
            )
            print("Assert Success : Assert Create Profile Empat Success")
        except AssertionError:
            print("Assert Failed : Assert Create Profile Empat Failed")

    def assertCreateProfileLima(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.profileobj.txt_create_profile_lima)
                )
            )
            print("Assert Success : Assert Create Profile Lima Success")
        except AssertionError:
            print("Assert Failed : Assert Create Profile Lima Failed")

    def assertCreateProfileEnam(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.profileobj.txt_create_profile_enam)
                )
            )
            print("Assert Success : Assert Create Profile Enam Success")
        except AssertionError:
            print("Assert Failed : Assert Create Profile Enam Failed")

    def assertCreateProfileTujuh(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.profileobj.txt_create_profile_tujuh)
                )
            )
            print("Assert Success : Assert Create Profile Tujuh Success")
        except AssertionError:
            print("Assert Failed : Assert Create Profile Tujuh Failed")

    def clickChangeAvatar(self):

        img_avatar = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.profileobj.img_avatar))
        )
        img_avatar.click()

    def clickChooseAvatar(self):

        choose_avatar = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.profileobj.img_avatar_second))
        )
        choose_avatar.click()

    def clickBtnOkChooseAvatar(self):

        btn_ok_avatar = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.profileobj.btn_ok_change_avatar))
        )
        btn_ok_avatar.click()

    def assertAvatarPage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, self.profileobj.txt_avatar_page)
                )
            )
            print("Assert Success : Assert Avatar Page Success")
        except AssertionError:
            print("Assert Failed : Assert Avatar Page Failed")

    def clickBtnOk(self):

        btn_ok = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.profileobj.btn_ok))
        )
        btn_ok.click()

    def assertProfileError(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, self.profileobj.txt_name_already_exist)
                )
            )
            print("Assert Success : Assert Profile already exist Success")
        except AssertionError:
            print("Assert Failed : Assert Profile already exist Failed")

    def clickCancelSuccessAddProfile(self):

        btn_cancel = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.ID, self.profileobj.btn_cancel_success_create_profile)
            )
        )
        btn_cancel.click()

    def clickBtnCancelAvatar(self):

        btn_cancel = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.profileobj.btn_cancel))
        )
        btn_cancel.click()

    def clickSecondProfile(self):

        btn_second_profile = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.profileobj.second_profile))
        )
        btn_second_profile.click()
