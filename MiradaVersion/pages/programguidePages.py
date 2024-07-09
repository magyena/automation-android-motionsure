from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MiradaVersion.utils.handler import HandlerRemote
from selenium.common.exceptions import TimeoutException
from MiradaVersion.object.programguideObject import guideObject
from MiradaVersion.object.livetvObject import livetvObject


class programguidePages:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.guideObj = guideObject()

    def assertProgramGuidePage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.guideObj.txt_program_guide)
                )
            )
            print("Assert Success : Assert Program Guide Page Success")
        except AssertionError:
            print("Assert Failed : Assert Program Guide Page Failed")

    def clickRctiGuide(self):

        rcti_guide = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.guideObj.img_rcti_guide))
        )
        rcti_guide.click()
