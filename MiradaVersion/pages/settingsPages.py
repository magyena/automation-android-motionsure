from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MiradaVersion.utils.handler import HandlerRemote
from selenium.common.exceptions import TimeoutException
from MiradaVersion.object.settingsObject import settingsObject
from MiradaVersion.object.homeObject import homeObject


class SettingsPages:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.settingsObj = settingsObject()
        self.homeObj = homeObject()
    
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


    def clickLegalInformation(self):

        legal_information = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.legal_information))
        )
        legal_information.click()

    def assertLegalInformation(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.settingsObj.legal_information)
                )
            )
            print("Assert Success : Assert Legal Information Success")
        except AssertionError:
            print("Assert Failed : Assert Legal Information Failed")

    def clickTerms0fUse(self):

        terms_of_use = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.txt_terms_of_use))
        )
        terms_of_use.click()

    def clickPrivacyPolicy(self):

        privacy_policy = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.txt_privacy_policy))
        )
        privacy_policy.click()

    def clickSoftwareLicenses(self):

        software_licenses = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.settingsObj.txt_software_licences)
            )
        )
        software_licenses.click()

    def clickBacktoSettingsPage(self):

        btn_back_settings = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.settingsObj.btn_back))
        )
        btn_back_settings.click()

    def clickHelp(self):

        help = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.help))
        )
        help.click()

    def assertHelpCenterPage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.settingsObj.help_center_page)
                )
            )
            print("Assert Success : Assert Help Center Page Success")
        except AssertionError:
            print("Assert Failed : Assert Help Center Page Failed")

    def clickEmailHelpCenter(self):

        email_help = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.help_center_email))
        )
        email_help.click()

    def clickWhatsappHelpCenter(self):

        whatsapp_help_center = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.settingsObj.help_center_whatsapp)
            )
        )
        whatsapp_help_center.click()

    def clickAboutUSHelpCenter(self):

        about_help_center = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.settingsObj.help_center_about_us)
            )
        )
        about_help_center.click()

    def clickSubscriptionHelpCenter(self):

        subscription_help_center = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.settingsObj.help_center_subscription)
            )
        )
        subscription_help_center.click()

    def assertAboutUsPage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.settingsObj.help_center_about_us)
                )
            )
            print("Assert Success : Assert About US Page Success")
        except AssertionError:
            print("Assert Failed : Assert About US Page Failed")

    def assertSubscriptionPage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.settingsObj.help_center_subscription)
                )
            )
            print("Assert Success : Assert Subscription Page Success")
        except AssertionError:
            print("Assert Failed : Assert Subscription Page Failed")

    def clickCallCenter(self):

        call_center = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.call_center))
        )
        call_center.click()

    def clickCloseToSettings(self):

        btn_close = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.ID, self.settingsObj.help_center_close_webview)
            )
        )
        btn_close.click()

    def clickManageProfiles(self):

        manage_profiles = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.manage_profiles))
        )
        manage_profiles.click()

    def assertManageProfiles(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.settingsObj.manage_profiles)
                )
            )
            print("Assert Success : Assert Manage Profiles Page Success")
        except AssertionError:
            print("Assert Failed : Assert Manage Profiles Page Failed")

    def clickAddProfileManageProfiles(self):

        manage_profiles_add_profile = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.settingsObj.manage_profiles_add_profiles)
            )
        )
        manage_profiles_add_profile.click()

    def clickNotification(self):

        notification = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.settingsObj.txt_notification_centre)
            )
        )
        notification.click()

    def assertNotificationCentre(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.settingsObj.txt_notification_centre)
                )
            )
            print("Assert Success : Assert Notification Centre Page Success")
        except AssertionError:
            print("Assert Failed : Assert Notification Centre Page Failed")

    def clickBackSettings(self):

        back = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.back_to_settings))
        )
        back.click()
