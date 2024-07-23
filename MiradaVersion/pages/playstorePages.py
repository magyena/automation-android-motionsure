from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MiradaVersion.utils.handler import HandlerRemote
from selenium.common.exceptions import TimeoutException
from MiradaVersion.object.playstoreObject import playstoreObject
import time


class playstore:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.playstore = playstoreObject()

    def assertFirstPackage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.playstore.txt_first_current_package)
                )
            )
            print("Assert Success : Assert First Package Success")
            return True
        except TimeoutException:
            print("Assert Failed : Assert First Package Failed")
            return False

    def assertSecondPackage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.playstore.txt_second_current_package)
                )
            )
            print("Assert Success : Assert Second Package Success")
            return True
        except TimeoutException:
            print("Assert Failed : Assert Second Package Failed")
            return False

    def clickProfilePlaystore(self):

        img_profile = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.playstore.img_profile))
        )
        img_profile.click()

    def clickPayments(self):

        payments_menu = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.playstore.img_payments_subscriptions)
            )
        )
        payments_menu.click()

    def clickSubscriptions(self):

        subscriptions = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.playstore.img_subscriptions))
        )
        subscriptions.click()

    def clickFirstPackage(self):

        first_package = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.playstore.txt_first_current_package)
            )
        )
        first_package.click()

    def clickSecondPackage(self):

        second_package = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.playstore.txt_second_current_package)
            )
        )
        second_package.click()

    def clickBtnCancelSubscription(self):

        btn_cancel_subscription = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.playstore.btn_cancel_subscription)
            )
        )
        btn_cancel_subscription.click()

    def clickBtnNoThanks(self):

        btn_no_thanks = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.playstore.btn_no_thanks))
        )
        btn_no_thanks.click()

    def clickReasonCancel(self):

        radio_decline = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.playstore.reason_cancel))
        )
        radio_decline.click()

    def clickBtnContinue(self):

        btn_continue = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.playstore.btn_continue))
        )
        btn_continue.click()

    def clickBtnBack(self):

        btn_back = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.playstore.btn_back))
        )
        btn_back.click()

    def clickBtnSubscribePlaystore(self):

        btn_subscribe = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.playstore.btn_subscribe))
        )
        btn_subscribe.click()
