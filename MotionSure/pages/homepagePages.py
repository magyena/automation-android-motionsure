from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MotionSure.utils.handler import HandlerRemote
from selenium.common.exceptions import TimeoutException
from MotionSure.object.homeObject import homeObject
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MotionSure.utils.handler import HandlerRemote
from selenium.common.exceptions import TimeoutException
import time
import subprocess
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.homeObj = homeObject()

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
                driver.swipe(start_x, start_y, end_x, end_y, 650)
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

    def assertScroll(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.homeObj.txt_scroll))
            )
            print("Assert Success : Assert Scroll Success")
        except AssertionError:
            print("Assert Failed : Assert Scroll Failed")

    def clickCheckbox(self):

        btn_checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.homeObj.btn_checkbox))
        )
        btn_checkbox.click()

    def clickBtnAgree(self):

        btn_agree = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.homeObj.btn_agree))
        )
        btn_agree.click()

    def clikBtnScroll(self):

        btn_Scroll = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.txt_scroll))
        )
        btn_Scroll.click()

    def clickBtnNext(self):

        btn_next = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.homeObj.btn_next))
        )
        btn_next.click()

    def clikBtnStart(self):

        btn_start = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.homeObj.btn_start))
        )
        btn_start.click()
