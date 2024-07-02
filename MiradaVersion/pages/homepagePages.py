from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MiradaVersion.utils.handler import HandlerRemote
from selenium.common.exceptions import TimeoutException
from MiradaVersion.object.loginObject import loginObject
from MiradaVersion.object.homeObject import homeObject


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.loginObj = loginObject()
        self.homeObj = homeObject()

    def assertHomePage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.ID, self.homeObj.txt_vision_logo))
            )
            print("Assert Success : Assert Homepage Logo Success")
        except AssertionError:
            print("Assert Failed : Assert Homepage Logo Failed")

    def clickMenuButton(self):

        btn_menu = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.homeObj.btn_menu_button))
        )
        btn_menu.click()

    def assertMenu(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.homeObj.img_home))
            )
            print("Assert Success : Assert Menu Button Success")
        except AssertionError:
            print("Assert Failed : Assert Menu Button Failed")

    def clickSettingsButton(self):

        btn_settings_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.homeObj.btn_settings_button))
        )
        btn_settings_button.click()

    def assertSettingsPage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.txt_settings_page)
                )
            )
            print("Assert Success : Assert Settings Page Success")
        except AssertionError:
            print("Assert Failed : Assert Settings Page Failed")

    def clickSettingsProfile(self):

        settings_profile = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.homeObj.txt_settings_account_profile)
            )
        )
        settings_profile.click()

    def assertSettingsAccountPage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.homeObj.txt_account_page)
                )
            )
            print("Assert Success : Assert Account Page Success")
        except AssertionError:
            print("Assert Failed : Assert Account Page Failed")

    def clickLogoutButton(self):

        logout_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.homeObj.btn_logout))
        )
        logout_button.click()

    def clickLiveTvMenu(self):

        live_tv_menu = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.homeObj.img_live_tv))
        )
        live_tv_menu.click()
