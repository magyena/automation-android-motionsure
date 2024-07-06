from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MiradaVersion.utils.handler import HandlerRemote
from selenium.common.exceptions import TimeoutException
import time
from MiradaVersion.object.loginObject import loginObject
from MiradaVersion.object.homeObject import homeObject


class PagesLogin:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.loginObj = loginObject()
        self.homeObj = homeObject()

    def clickLogin(self):

        btn_Login = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.loginObj.btn_login))
        )
        btn_Login.click()

    def clickEmailSection(self):
        btn_email = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.loginObj.email_section))
        )
        btn_email.click()

    def inputEmail(self, email):
        self.wait = WebDriverWait(self.driver, 20)

        txt_fld_email = self.driver.find_element(By.XPATH, self.loginObj.txt_fld_email)

        txt_fld_email.click()
        time.sleep(3)
        txt_fld_email.send_keys(email)

    def inputPass(self, password):
        self.wait = WebDriverWait(self.driver, 20)

        txt_fld_password = self.driver.find_element(
            By.XPATH, self.loginObj.txt_fld_password
        )

        txt_fld_password.click()
        time.sleep(3)
        txt_fld_password.send_keys(password)
        time.sleep(3)
        self.driver.press_keycode(4)

    def clickSubmitLogin(self):
        btn_submit_login = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.loginObj.btn_submit_login))
        )
        # btn_submit_login = self.driver.find_element(By.XPATH,self.loginObj.btn_submit_login)
        btn_submit_login.click()

    def assertMyProfile(self):
        self.wait = WebDriverWait(self.driver, 20)
        return self.wait.until(
            EC.visibility_of_element_located((By.ID, self.loginObj.txt_welcome))
        )

    def assertLoginPage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.txt_login_page)
                )
            )
            print("Assert Success : Assert Login Page Success")
        except AssertionError:
            print("Assert Failed : Assert Login Page Failed")

    def assertEmailSection(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.txt_email_section)
                )
            )
            print("Assert Success : Assert Email Section Success")
        except AssertionError:
            print("Assert Failed : Assert Email Section Failed")

    def assertAccountHasNotBeenRegistered(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.txt_this_account_has_Not_been_registered)
                )
            )
            print(
                "Assert Success : Assert This account has not been registered Success"
            )
        except AssertionError:
            print("Assert Failed : Assert This account has not been registered Failed")

    def clickBtnForgotPassword(self):
        btn_forgot_password = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.loginObj.btn_forgot_password))
        )
        btn_forgot_password.click()

    def assertForgotPasswordPage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.txt_forgot_password)
                )
            )
            print("Assert Success : Assert Forgot Password Page Success")
        except AssertionError:
            print("Assert Failed : Assert Forgot Password Page Failed")

    def clickBtnSavePassword(self):
        btn_save_password = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.loginObj.btn_save_password))
        )
        btn_save_password.click()
