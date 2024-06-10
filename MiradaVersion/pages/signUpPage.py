from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MiradaVersion.utils.handler import HandlerRemote
from selenium.common.exceptions import TimeoutException
import time
from appium import webdriver
from MiradaVersion.object.loginObject import loginObject
from MiradaVersion.object.homeObject import homeObject
from selenium import webdriver


class SignUp:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.loginObj = loginObject()
        self.homeObj = homeObject()

    # def backGesture(driver: WebDriver):

    #     back_gesture = TouchAction(driver)
    #     back_gesture.press(x=500, y=1500).move_to(x=100, y=1500).release().perform()

    def clickSignUp(self):

        btn_SignUp = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.loginObj.btn_signup))
        )
        btn_SignUp.click()

    def assertRegisterPage(self):
        try:
            self.wait = WebDriverWait(self.driver, 20)
            element = self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.txt_register_page)
                )
            )
            print("Sukses")
            return element
        except AssertionError:
            print("gagal")
            return element

    def inputPhoneNumber(self, phone):
        self.wait = WebDriverWait(self.driver, 20)

        txt_fld_phone_number = self.driver.find_element(
            By.XPATH, self.loginObj.txt_fld_phone_number
        )

        txt_fld_phone_number.click()
        txt_fld_phone_number.send_keys(phone)

    def inputPassword(self, password):
        self.wait = WebDriverWait(self.driver, 20)

        txt_fld_password = self.driver.find_element(
            By.XPATH, self.loginObj.txt_fld_password
        )

        txt_fld_password.click()
        txt_fld_password.send_keys(password)

        self.driver.press_keycode(4)

    def clickButtonSendOtp(self):
        btn_Send_Otp = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.loginObj.btn_send_otp))
        )
        btn_Send_Otp.click()

    def clearInputPhoneNumber(self):
        self.wait = WebDriverWait(self.driver, 20)

        txt_fld_phone_number = self.driver.find_element(
            By.XPATH, self.loginObj.txt_fld_phone_number
        )

        txt_fld_phone_number.clear()

    def inputOTP(self, otp):
        self.wait = WebDriverWait(self.driver, 20)

        fld_otp = self.driver.find_element(By.XPATH, self.loginObj.fld_otp)

        fld_otp.click()
        fld_otp.send_keys(otp)
        self.driver.press_keycode(4)

    def clickSubmitRegister(self):
        btn_register = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.loginObj.btn_register))
        )
        btn_register.click()

    def clickEmailSection(self):
        btn_email = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.loginObj.email_section))
        )
        btn_email.click()

    def inputEmail(self, email):
        self.wait = WebDriverWait(self.driver, 20)

        input_email = self.driver.find_element(By.XPATH, self.loginObj.txt_fld_email)

        input_email.click()
        input_email.send_keys(email)

    def assertDiscoverProfiles(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, self.loginObj.txt_discover_profiles)
                )
            )
            print("Assert Success : Assert Discover Profiles Success")
        except AssertionError:
            print("Assert Failed : Assert Discover Profiles Failed")

    def clickBtnSkipDiscoverProfiles(self):
        btn_skip = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.ID, self.loginObj.btn_skip_discover_profiles)
            )
        )
        btn_skip.click()

    def clickBtnAddProfileDiscoverProfiles(self):
        btn_add_profile = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.ID, self.loginObj.btn_add_profile_discover_profiles)
            )
        )
        btn_add_profile.click()

    def clickBtnContinueSkipProfile(self):
        btn_skip = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.loginObj.btn_continue_skip_profile))
        )
        btn_skip.click()

    def assertSkipProfile(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, self.loginObj.txt_skip_profile)
                )
            )
            print("Assert Success : Assert Skip Profile Creation Success")
        except AssertionError:
            print("Assert Failed : Assert Skip Profile Creation Failed")

    def clickSendViaSms(self):
        txt_send_via_sms = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.loginObj.txt_send_via_sms))
        )
        txt_send_via_sms.click()

    def assertRegisterHasBeenRegistered(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.txt_account_has_been_registered)
                )
            )
            print("Assert Success : Assert Account Has Been Registered Success")
        except AssertionError:
            print("Assert Failed : Assert Account Has Been Registered Failed")

    def clickTermsOfUse(self):
        txt_term_of_use = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.loginObj.txt_terms_of_use))
        )
        txt_term_of_use.click()

    def clickPrivacyPolicy(self):
        txt_privacy_policy = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.loginObj.txt_privacy_policy))
        )
        txt_privacy_policy.click()
