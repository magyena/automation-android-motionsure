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
        txt_fld_phone_number.clear()
        txt_fld_phone_number.click()
        txt_fld_phone_number.send_keys(phone)

    def inputPassword(self, password):
        self.wait = WebDriverWait(self.driver, 20)

        txt_fld_password = self.driver.find_element(
            By.XPATH, self.loginObj.txt_fld_password
        )
        txt_fld_password.clear()
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

        fld_otp.clear()
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

    def clickPhoneNumberSection(self):
        btn_phone_number = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.loginObj.phone_section))
        )
        btn_phone_number.click()

    def inputEmail(self, email):
        self.wait = WebDriverWait(self.driver, 20)

        input_email = self.driver.find_element(By.XPATH, self.loginObj.txt_fld_email)

        input_email.clear()
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

    def assertSendOtpViaMessage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.txt_send_otp_via_whatsapp)
                )
            )
            print("Assert Success : Assert Send OTP via Whatsapp Success")
        except AssertionError:
            print("Assert Failed : Assert Send OTP via Whatsapp Failed")

    def clickCountry(self):
        drop_country_code = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.loginObj.drop_country))
        )
        drop_country_code.click()

    def assertCountryCode(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.txt_country_code)
                )
            )
            print("Assert Success : Assert Country Code Success")
        except AssertionError:
            print("Assert Failed : Assert Country Code Failed")

    def clickCountryIndonesia(self):
        country_code_ind = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.loginObj.country_code_indonesia))
        )
        country_code_ind.click()

    def clickCountryMalaysia(self):
        country_code_malaysia = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.loginObj.country_code_malaysia))
        )
        country_code_malaysia.click()

    def assertCountryCodeAfterChooseMalaysia(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.country_code_malaysia)
                )
            )
            print("Assert Success : Assert Country Code After Choose Success")
        except AssertionError:
            print("Assert Failed : Assert Country Code After Choose Failed")

    def inputCountryCodeNetherlands(self, country_code):
        wait = WebDriverWait(self.driver, 20)
        fld_country_code = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.loginObj.fld_country_code))
        )

        fld_country_code.send_keys(country_code)

    def clickResultSearchCountry(self):
        result_search_country = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.loginObj.txt_result_search_country)
            )
        )
        result_search_country.click()

    def assertCountryCodeAfterChooseNetherland(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.country_code_netherland)
                )
            )
            print(
                "Assert Success : Assert Country Code After Choose Netherland Success"
            )
        except AssertionError:
            print("Assert Failed : Assert Country Code After Choose Netherland Failed")

    def assertCountryCodeAfterChooseIndonesia(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.country_code_indonesia)
                )
            )
            print("Assert Success : Assert Country Code After Choose Indonesia Success")
        except AssertionError:
            print("Assert Failed : Assert Country Code After Choose Indonesia Failed")

    def assertNoCountryFound(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.txt_no_country_found)
                )
            )
            print("Assert Success : Assert No Country Found Success")
        except AssertionError:
            print("Assert Failed : Assert No Country Found Failed")

    def clickBtnCloseCountryCode(self):
        btn_close_country_code = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.loginObj.btn_close_country_code))
        )
        btn_close_country_code.click()

    def assertPhoneNumberIncorrect(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.txt_phone_number_inccorrect)
                )
            )
            print("Assert Success : Assert Phone Number Incorrect Success")
        except AssertionError:
            print("Assert Failed : Assert Phone Number Incorrect Failed")

    def clickInvisiblePassword(self):
        btn_visible_password = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.loginObj.btn_visible_password))
        )
        btn_visible_password.click()

    def assertPasswordDoesntMatch(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.txt_password_does_not_criteria)
                )
            )
            print(
                "Assert Success : Assert Password does not match the criteria Success"
            )
        except AssertionError:
            print("Assert Failed : Assert Password does not match the criteria Failed")

    def assertWrongOtp(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.txt_wrong_otp)
                )
            )
            print("Assert Success : Assert Wrong Otp Success")
        except AssertionError:
            print("Assert Failed : Assert Wrong Otp Failed")

    def assertOTPExpired(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.txt_otp_expired)
                )
            )
            print("Assert Success : Assert OTP Expired Success")
        except AssertionError:
            print("Assert Failed : Assert OTP Expired Failed")

    def assertSendOtpSecondTime(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.resend_second_otp)
                )
            )
            print("Assert Success : Assert Resend Second OTP Success")
        except AssertionError:
            print("Assert Failed : Assert Resend Second OTP Failed")

    def assertInvalidPhoneNumber(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.txt_invalid_phone_number)
                )
            )
            print("Assert Success : Assert Invalid Phone Number Success")
        except AssertionError:
            print("Assert Failed : Assert Invalid Phone Number Failed")

    def assertInvisiblePassword(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.txt_invisible_password)
                )
            )
            print("Assert Success : Assert Invisible Password Success")
        except AssertionError:
            print("Assert Failed : Assert Invisible Password Failed")

    def assertEmailInvalidFormat(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.txt_invalid_email)
                )
            )
            print("Assert Success : Assert Invalid Format Email Success")
        except AssertionError:
            print("Assert Failed : Assert Invalid Format Email Failed")

    def clickBtnLoginFromRegister(self):
        btn_login_from_register = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.loginObj.btn_login_from_register)
            )
        )
        btn_login_from_register.click()

    def assertSendOtpFirstTime(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.loginObj.txt_first_otp)
                )
            )
            print("Assert Success : Assert Send First OTP Success")
        except AssertionError:
            print("Assert Failed : Assert Send First OTP Failed")
