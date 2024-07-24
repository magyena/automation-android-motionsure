from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from MiradaVersion.utils.handler import HandlerRemote
from selenium.common.exceptions import TimeoutException
from MiradaVersion.object.settingsObject import settingsObject
from MiradaVersion.object.homeObject import homeObject
import time


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

    def assertFirstProfile(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.settingsObj.btn_profile_one)
                )
            )
            print("Assert Success : Assert Profile One Success")
        except AssertionError:
            print("Assert Failed : Assert Profile One Failed")

    def clickFirstProfiles(self):

        profile_one = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.btn_profile_one))
        )
        profile_one.click()

    def assertDetailProfile(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.settingsObj.btn_profile_one)
                )
            )
            print("Assert Success : Assert Detail Profiles Page Success")
        except AssertionError:
            print("Assert Failed : Assert Detail Profiles Page Failed")

    def clickDeleteProfile(self):

        delete_profile = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.btn_delete_profiles))
        )
        delete_profile.click()

    def clickAcceptDeleteProfile(self):

        acc_delete = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.ID, self.settingsObj.btn_accept_delete_profiles)
            )
        )
        acc_delete.click()

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

    def clickChangePassword(self):

        change_password = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.settingsObj.txt_account_page_change_password)
            )
        )
        change_password.click()

    def assertChangePasswordPage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.settingsObj.txt_account_page_change_password_page)
                )
            )
            print("Assert Success : Assert Change Password Page Success")
        except AssertionError:
            print("Assert Failed : Assert Change Password Page Failed")

    def inputCurrentPassword(self, currentpassword):
        self.wait = WebDriverWait(self.driver, 20)

        fld_current_password = self.driver.find_element(
            By.XPATH, self.settingsObj.fld_change_password_current_password
        )
        fld_current_password.clear()
        time.sleep(3)
        fld_current_password.click()
        time.sleep(3)
        fld_current_password.send_keys(currentpassword)
        time.sleep(3)
        self.driver.press_keycode(4)

    def inputNewPassword(self, currentpassword):
        self.wait = WebDriverWait(self.driver, 20)

        fld_new_password = self.driver.find_element(
            By.XPATH, self.settingsObj.fld_change_password_new_password
        )
        fld_new_password.clear()
        time.sleep(3)
        fld_new_password.click()
        time.sleep(3)
        fld_new_password.send_keys(currentpassword)
        time.sleep(3)
        self.driver.press_keycode(4)

    def assertChangePasswordInvalidCurrentPassword(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.settingsObj.txt_notif_invalid_current_password)
                )
            )
            print("Assert Success : Assert Invalid Current Password Success")
        except AssertionError:
            print("Assert Failed : Assert Invalid Current Password Failed")

    def clickBtnOKInvalidCurrentPassword(self):

        btn_ok = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.settingsObj.btn_ok_invalid_password)
            )
        )
        btn_ok.click()

    def clickBtnNextChangePassword(self):

        btn_next = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.settingsObj.btn_next_change_password)
            )
        )
        btn_next.click()

    def assertChangePasswordLess8Charracter(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.txt_change_password_invalid_format_8_charracter,
                    )
                )
            )
            print("Assert Success : Assert Password must be at least 8 Success")
        except AssertionError:
            print("Assert Failed : Assert Password must be at least 8 Failed")

    def assertSuccessChangePassword(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.txt_success_change_password,
                    )
                )
            )
            print("Assert Success : Assert Sucessfully Change Password Success")
        except AssertionError:
            print("Assert Failed : Assert Sucessfully Change Password Failed")

    def clickDeleteAccount(self):

        delete_account = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.settingsObj.txt_account_page_delete_account)
            )
        )
        delete_account.click()

    def clickAcceptDeleteAccount(self):

        chbx_delete = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.settingsObj.checkbox_accept_delete_account)
            )
        )
        chbx_delete.click()

    def clickProceedDeleteAccount(self):

        btn_proceed_delete = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.settingsObj.btn_process_delete_account)
            )
        )
        btn_proceed_delete.click()

    def assertDeleteAccountPage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.txt_delete_account_page,
                    )
                )
            )
            print("Assert Success : Assert Delete Account Page Success")
        except AssertionError:
            print("Assert Failed : Assert Delete Account Page Failed")

    def inputPasswordDeleteAccount(self, currentpassword):
        self.wait = WebDriverWait(self.driver, 20)

        fld_password_delete = self.driver.find_element(
            By.XPATH, self.settingsObj.fld_password_delete_account
        )
        fld_password_delete.clear()
        time.sleep(2)
        fld_password_delete.click()
        time.sleep(2)
        fld_password_delete.send_keys(currentpassword)
        time.sleep(2)
        self.driver.press_keycode(4)

    def clickBtnDeleteAccount(self):

        btn_delete = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.btn_delete_account))
        )
        btn_delete.click()

    def assertDeleteAccountSuccess(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.txt_success_delete_account,
                    )
                )
            )
            print("Assert Success : Assert Succes Delete Account Success")
        except AssertionError:
            print("Assert Failed : Assert Succes Delete Account Failed")

    def assertInvalidDeleteAccount(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.txt_delete_account_failed,
                    )
                )
            )
            print("Assert Success : Assert Delete Account Failed Success")
        except AssertionError:
            print("Assert Failed : Assert Delete Account Failed Failed")

    def clickVoucher(self):

        menu_voucher = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.txt_voucher))
        )
        menu_voucher.click()

    def assertVoucherPage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.txt_voucher,
                    )
                )
            )
            print("Assert Success : Assert Voucer Page Success")
        except AssertionError:
            print("Assert Failed : Assert Voucer Page Failed")

    def inputRedeemVoucher(self, voucher):
        self.wait = WebDriverWait(self.driver, 20)

        fld_voucher = self.driver.find_element(
            By.XPATH, self.settingsObj.fld_enter_voucher
        )
        fld_voucher.clear()
        time.sleep(3)
        fld_voucher.click()
        time.sleep(3)
        fld_voucher.send_keys(voucher)
        time.sleep(3)
        self.driver.press_keycode(4)

    def clickBtnRedeemVoucher(self):

        btn_reedem = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.btn_redeem_voucher))
        )
        btn_reedem.click()

    def assertSuccessReedemVoucher(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.txt_success_reedem,
                    )
                )
            )
            print("Assert Success : Assert Successfully Reedem Voucher Success")
        except AssertionError:
            print("Assert Failed : Assert Successfully Reedem Voucher Failed")

    def clickBtnSeeMyStatus(self):

        btn_transaction_details = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.txt_see_my_status))
        )
        btn_transaction_details.click()

    def assertTransactionDetailsVoucher(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.txt_transaction_details_voucher,
                    )
                )
            )
            print("Assert Success : Assert Details Transactions Voucher Success")
        except AssertionError:
            print("Assert Failed : Assert Details Transactions Voucher Failed")

    def assertVoucherExpired(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.txt_voucher_expired,
                    )
                )
            )
            print("Assert Success : Assert Voucher Expired Success")
        except AssertionError:
            print("Assert Failed : Assert Voucher Expired Failed")

    def assertVoucherInvalid(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.txt_voucher_invalid,
                    )
                )
            )
            print("Assert Success : Assert Voucher Invalid Success")
        except AssertionError:
            print("Assert Failed : Assert Voucher Invalid Failed")

    def clickMarketPlaceTokopedia(self):

        tokopedia = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.img_tokopedia))
        )
        tokopedia.click()

    def clickMarketPlaceLazada(self):

        lazada = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.img_lazada))
        )
        lazada.click()

    def clickMarketPlaceBlibli(self):

        blibli = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.img_blibli))
        )
        blibli.click()

    def clickMarketPlaceCoda(self):

        coda = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.img_coda))
        )
        coda.click()

    def clickHelpCenterVoucher(self):

        help_center = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.settingsObj.txt_help_center_voucher)
            )
        )
        help_center.click()

    def clickManageDevices(self):

        manage_devices = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.settingsObj.manage_devices))
        )
        manage_devices.click()

    def assertManageDevicesPage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.manage_devices,
                    )
                )
            )
            print("Assert Success : Assert Manage Devices Page Success")
        except AssertionError:
            print("Assert Failed : Assert Manage Devices Page Failed")

    def clickDiscconnectManageDevices(self):

        disconnect_all = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.ID, self.settingsObj.btn_disconnect_all_manage_devices)
            )
        )
        disconnect_all.click()

    def assertNoDevicesConnected(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.ID,
                        self.settingsObj.txt_no_devices_connected,
                    )
                )
            )
            print("Assert Success : Assert No devices Connected Success")
        except AssertionError:
            print("Assert Failed : Assert No devices Connected Failed")

    def clickTransactionHistory(self):

        transaction_history = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.settingsObj.txt_transaction_history)
            )
        )
        transaction_history.click()

    def assertTransactionHistoryPage(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.txt_transaction_history_page,
                    )
                )
            )
            print("Assert Success : Assert Transaction History Page Success")
        except AssertionError:
            print("Assert Failed : Assert Transaction History Page Failed")

    def clickTabSuccessTransactionHistory(self):

        transaction_history_success = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.settingsObj.txt_transaction_history_success)
            )
        )
        transaction_history_success.click()

    def clickTabFailedTransactionHistory(self):

        transaction_history_failed = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.settingsObj.txt_transaction_history_failed)
            )
        )
        transaction_history_failed.click()

    def clickTabPendingTransactionHistory(self):

        transaction_history_pending = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.settingsObj.txt_transaction_history_pending)
            )
        )
        transaction_history_pending.click()

    def assertTransactionHistorySuccess(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.txt_transaction_history_success_tab,
                    )
                )
            )
            print("Assert Success : Assert Transaction History Success Success")
        except AssertionError:
            print("Assert Failed : Assert Transaction History Success Failed")

    def assertTransactionHistoryFailed(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.txt_transaction_history_failed_tab,
                    )
                )
            )
            print("Assert Success : Assert Transaction History Failed Success")
        except AssertionError:
            print("Assert Failed : Assert Transaction History Failed Failed")

    def assertNoTransactionHistory(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.txt_transaction_history_no_transaction,
                    )
                )
            )
            print("Assert Success : Assert No Transaction History Success")
        except AssertionError:
            print("Assert Failed : Assert  NO Transaction History Failed")

    def clickDetailTransaction(self):

        transaction_detail = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.settingsObj.txt_transaction_history_detail)
            )
        )
        transaction_detail.click()

    def assertTransactionDetails(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.txt_transaction_history_detail_page,
                    )
                )
            )
            print("Assert Success : Assert Detail Transaction Success")
        except AssertionError:
            print("Assert Failed : Assert  Detail Transaction Failed")

    def assertError500TransactionHistory(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.txt_error_transaction_history,
                    )
                )
            )
            print("Assert Success : Assert Transaction History Error 500 Success")
        except AssertionError:
            print("Assert Failed : Assert Transaction History Error 500 Failed")

    def assertTransactionHistoryPremium(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.txt_transaction_history_premium,
                    )
                )
            )
            print("Assert Success : Assert Transaction History Premium Success")
        except AssertionError:
            print("Assert Failed : Assert Transaction History Premium Failed")

    def assertTransactionHistoryPremiumSports(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        self.settingsObj.txt_transaction_history_premium_sports,
                    )
                )
            )
            print("Assert Success : Assert Transaction History Premium Sports Success")
        except AssertionError:
            print("Assert Failed : Assert Transaction History Premium  Sports Failed")
