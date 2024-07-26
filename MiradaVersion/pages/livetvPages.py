from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MiradaVersion.utils.handler import HandlerRemote
from selenium.common.exceptions import TimeoutException
from MiradaVersion.object.loginObject import loginObject
from MiradaVersion.object.homeObject import homeObject
from MiradaVersion.object.livetvObject import livetvObject


class LiveTV:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.livetvObj = livetvObject()

    def assertLiveTV(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.livetvObj.img_rcti))
            )
            print("Assert Success : Assert Live TV Page Success")
        except AssertionError:
            print("Assert Failed : Assert Live TV Page Failed")

    def assertLiveTVInews(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.livetvObj.img_inews))
            )
            print("Assert Success : Assert Live TV Page Success")
        except AssertionError:
            print("Assert Failed : Assert Live TV Page Failed")

    def clickTrans7Channel(self):

        trans7_channel = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.livetvObj.img_trans7))
        )
        trans7_channel.click()

    def assertSubscription(self):
        self.wait = WebDriverWait(self.driver, 40)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.livetvObj.txt_subscribe)
                )
            )
            print("Assert Success : Assert Subscription Success")
        except AssertionError:
            print("Assert Failed : Assert Subscription Failed")

    def clickSportChannel(self):

        soccer_channel = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.livetvObj.img_sportstarts2))
        )
        soccer_channel.click()

    def assertNoInternetConnection(self):
        self.wait = WebDriverWait(self.driver, 40)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, self.livetvObj.btn_goto_mydownloads)
                )
            )
            print("Assert Success : Assert No Internet Connection Success")
        except AssertionError:
            print("Assert Failed : Assert No Internet Connection Failed")

    def clickBtnDetailChannelSportstars(self):

        btn_detail_channel = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.livetvObj.btn_detail_channel_sportstars)
            )
        )
        btn_detail_channel.click()

    def assertDetailChannelSportstars(self):
        self.wait = WebDriverWait(self.driver, 40)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.livetvObj.txt_detail_channel_sportstars)
                )
            )
            print("Assert Success : Assert Detail Sportstars Channel Success")
        except AssertionError:
            print("Assert Failed : Assert Detail Sportstars Channel Failed")

    def assertLiveTVBroadcast(self):
        self.wait = WebDriverWait(self.driver, 40)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.livetvObj.txt_broadcast)
                )
            )
            print("Assert Success : Assert Live tv Broadcast Success")
        except AssertionError:
            print("Assert Failed : Assert Live tv Broadcast Failed")

    def assertLiveTVBroadcasted(self):
        self.wait = WebDriverWait(self.driver, 40)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.livetvObj.txt_broadcasted)
                )
            )
            print("Assert Success : Assert Live tv Broadcasted Success")
        except AssertionError:
            print("Assert Failed : Assert Live tv Broadcasted Failed")

    def clickBtnSubscribe(self):

        btn_subscribe = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.livetvObj.btn_subscribe))
        )
        btn_subscribe.click()
