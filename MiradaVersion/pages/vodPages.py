from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MiradaVersion.utils.handler import HandlerRemote
from selenium.common.exceptions import TimeoutException
from MiradaVersion.object.vodObject import vodObject
import time


class VOD:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.vod = vodObject()

    def assertDetailVod(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.vod.txt_detail_vod))
            )
            print("Assert Success : Assert Detail VOD Success")
        except AssertionError:
            print("Assert Failed : Assert Detail VOD Failed")

    def inputSearch(self, keyword):
        self.wait = WebDriverWait(self.driver, 20)

        fld_search = self.driver.find_element(By.ID, self.homeObj.fld_search)

        fld_search.clear()
        fld_search.click()
        time.sleep(3)
        fld_search.send_keys(keyword)
        time.sleep(3)
        self.driver.press_keycode(4)

    def clickEpisode2(self):

        eps2 = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.vod.btn_eps2))
        )
        eps2.click()

    def clickBtnDownload(self):

        btn_download = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.vod.btn_download))
        )
        btn_download.click()

    def assertDownloadProgress(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, self.vod.txt_download_progress)
                )
            )
            print("Assert Success : Assert Download in Progress Success")
        except AssertionError:
            print("Assert Failed : Assert Download in Progress Failed")

    def clickBtnCancelDownload(self):

        btn_cancel_download = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.vod.txt_download_progress))
        )
        btn_cancel_download.click()

    def clickAcceptCancelDownload(self):

        btn_acc_cancel_download = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.vod.btn_accept_cancel_download))
        )
        btn_acc_cancel_download.click()

    def assertBtnWatch(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.ID, self.vod.btn_watch))
            )
            print("Assert Success :  Button Watch Showing ")
        except AssertionError:
            print("Assert Failed :  Button Watch not Showing ")

    def clickBtnWatch(self):

        btn_watch = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.vod.btn_watch))
        )
        btn_watch.click()

    def assertListPackages(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.ID, self.vod.list_packages))
            )
            print("Assert Success :  Assert List Packages Showing ")
        except AssertionError:
            print("Assert Failed :  Assert List Packages not Showing ")

    def clickLike(self):

        btn_like = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.vod.btn_like))
        )
        btn_like.click()

    def clickDislike(self):

        btn_dislike = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.vod.btn_dislike))
        )
        btn_dislike.click()

    def clickShare(self):

        btn_share = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.vod.btn_share))
        )
        btn_share.click()

    def clickAddtoList(self):

        btn_add_list = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.vod.btn_add_to_list))
        )
        btn_add_list.click()
