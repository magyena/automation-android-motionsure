from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MiradaVersion.utils.handler import HandlerRemote
from selenium.common.exceptions import TimeoutException
from MiradaVersion.object.mediaplayerObject import mediaplayerObject


class mediaplayer:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.mediaplayerobj = mediaplayerObject()

    def assertMediaPlayer(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, self.mediaplayerobj.txt_tittle_media_playerpage)
                )
            )
            print("Assert Success : Assert Content Play Success")
        except AssertionError:
            print("Assert Failed : Assert Content Play Failed")

    def clickForward(self):

        btn_forward = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.ID, self.mediaplayerobj.btn_forward_media_playerpage)
            )
        )
        btn_forward.click()

    def clickBackward(self):

        btn_backward = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.ID, self.mediaplayerobj.btn_rewind_media_playerpage)
            )
        )
        btn_backward.click()

    def clickSkipAd(self):

        btn_skip_ad = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.mediaplayerobj.btn_skip_add))
        )
        btn_skip_ad.click()

    def clickLayoutMediaPlayer(self):

        layout_media_player = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.mediaplayerobj.layout_media_player)
            )
        )
        layout_media_player.click()

    def clickRestartMediaPlayer(self):

        btn_restart = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.ID, self.mediaplayerobj.btn_restart_media_playerpage)
            )
        )
        btn_restart.click()

    def clickSettingsMediaPlayer(self):

        btn_settings = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.ID, self.mediaplayerobj.btn_settings_mediaplayer)
            )
        )
        btn_settings.click()

    def clickBtnOKSettingsMediaPlayer(self):

        btn_ok_settings = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.ID, self.mediaplayerobj.btn_ok_settings_mediaplayer)
            )
        )
        btn_ok_settings.click()

    def assertSettingsMediaPlayer(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.mediaplayerobj.txt_settings)
                )
            )
            print("Assert Success : Assert Settings Media Player Success")
        except AssertionError:
            print("Assert Failed : Assert Settings Media Player Failed")

    def assertForwardMediaPlayer(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.mediaplayerobj.txt_forward)
                )
            )
            print("Assert Success : Assert Forward Success")
        except AssertionError:
            print("Assert Failed : Assert Forward Failed")

    def assertBackwardMediaPlayer(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.mediaplayerobj.txt_restart)
                )
            )
            print("Assert Success : Assert Backward Success")
        except AssertionError:
            print("Assert Failed : Assert Backward Failed")

    def assertRestartMediaPlayer(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.mediaplayerobj.txt_restart)
                )
            )
            print("Assert Success : Assert Restart Success")
        except AssertionError:
            print("Assert Failed : Assert Restart Failed")

    def clickPauseMediaPlayer(self):

        pause_media_player = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.ID, self.mediaplayerobj.btn_pause_play_media_playerpage)
            )
        )
        pause_media_player.click()

    def clickSettingsDisableSubtitles(self):

        disable_subtitles = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.mediaplayerobj.radio_btn_disable_lang_media_playerpage)
            )
        )
        disable_subtitles.click()

    def clickSettingsIndonesianSubtitles(self):

        indonesian_subtitles = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    self.mediaplayerobj.radio_btn_indonesia_language_media_playerpage,
                )
            )
        )
        indonesian_subtitles.click()

    def clickSettingsEnglishSubtitles(self):

        english_subtitles = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    self.mediaplayerobj.radio_btn_english_language_media_playerpage,
                )
            )
        )
        english_subtitles.click()
