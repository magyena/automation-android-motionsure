from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MiradaVersion.utils.handler import HandlerRemote
from selenium.common.exceptions import TimeoutException
import time
from MiradaVersion.object.profileObject import profileObject


class Profiles:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.profileobj = profileObject()

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
        except TimeoutException:
            print("Assert Failed : Assert Profile Pages Success")
            return element

    def inputPhoneNumber(self, phone):
        self.wait = WebDriverWait(self.driver, 20)

        txt_fld_phone_number = self.driver.find_element(
            By.XPATH, self.loginObj.txt_fld_phone_number
        )

        txt_fld_phone_number.click()
        txt_fld_phone_number.send_keys(phone)
