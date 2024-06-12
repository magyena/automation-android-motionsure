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


class Profiles:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.profileobj = profileObject()

    def scrollDown(self):
        finger = PointerInput(interaction.POINTER_TOUCH, "finger")
        actions = ActionChains(self.driver)

        actions.w3c_actions.pointer_action.move_to_location(587, 1733)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(587, 599)
        actions.w3c_actions.pointer_action.pointer_up()

        actions.perform()

    def scrollUp(self):
        finger = PointerInput(interaction.POINTER_TOUCH, "finger")
        actions = ActionChains(self.driver)

        actions.w3c_actions.pointer_action.move_to_location(507, 350)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(487, 1777)
        actions.w3c_actions.pointer_action.pointer_up()

        actions.perform()

    def disable_wifi_connection(self):
        adb_path = "/Users/fatahalim/Library/Android/sdk/platform-tools/adb"
        # adb_path = "/users/visionplus/Library/Android/sdk/platform-tools/adb"

        try:
            subprocess.run([adb_path, "shell", "svc", "wifi", "disable"], check=True)
            print("Wifi data disabled successfully.")
        except subprocess.CalledProcessError as e:
            print("Error disabling Wifi data:", e)

    def enable_wifi_connection(self):
        adb_path = "/Users/fatahalim/Library/Android/sdk/platform-tools/adb"
        # adb_path = "/users/visionplus/Library/Android/sdk/platform-tools/adb"

        try:
            subprocess.run([adb_path, "shell", "svc", "wifi", "enable"], check=True)
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
        txt_fld_phone_number.send_keys(phone)
