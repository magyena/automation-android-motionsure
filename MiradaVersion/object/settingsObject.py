class settingsObject:
    def __init__(self):
        self.txt_settings_page = "//*[contains(@text,'Settings')]"
        self.txt_settings_account_profile = '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.zte.iptvclient.android.idmnc:id/recycler_view"]/android.view.ViewGroup[3]'
        self.txt_account_page = "//*[contains(@text,'Account')]"
        self.txt_account_page_change_password = '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.zte.iptvclient.android.idmnc:id/recycler_view"]/android.widget.LinearLayout[3]'
        self.txt_account_page_change_password_page = (
            "//*[contains(@text,'Change Password')]"
        )
        self.txt_account_page_delete_account = "//*[contains(@text,'Delete account')]"
        self.txt_delete_account_page = "//*[contains(@text,'Delete Account')]"
        self.btn_logout = "com.zte.iptvclient.android.idmnc:id/close_session_button"
        self.txt_transaction_history = "//*[contains(@text,'Transaction history')]"
        self.txt_transaction_history_page = "//*[contains(@text,'Transaction History')]"
        self.txt_voucher = "//*[contains(@text,'Voucher')]"
        self.txt_pay_tv_account = "//*[contains(@text,'Pay TV account')]"
        self.txt_notification_centre = "//*[contains(@text,'Notification centre')]"
        self.manage_profiles = "//*[contains(@text,'Manage profiles')]"
        self.Request_household_PIN_to_add_profiles = (
            "//*[contains(@text,'Request household PIN to add profiles')]"
        )
        self.manage_profiles = "//*[contains(@text,'Manage profiles')]"
        self.Edit_household_PIN = "//*[contains(@text,'Edit household PIN')]"
        self.use_mobile_Data = "//*[contains(@text,'Use mobile data')]"
        self.default_video_quality = "//*[contains(@text,'Default video quality')]"
        self.manage_devices = "//*[contains(@text,'Manage devices')]"
        self.help = "//*[contains(@text,'Help')]"
        self.legal_information = "//*[contains(@text,'Legal information')]"
        self.txt_terms_of_use = "//*[contains(@text,'Terms of Use')]"
        self.txt_privacy_policy = "//*[contains(@text,'Privacy Policy')]"
        self.txt_software_licences = "//*[contains(@text,'Software Licenses')]"
        self.btn_back = "com.zte.iptvclient.android.idmnc:id/back"
        self.help_center_page = "//*[contains(@text,'Help Center')]"
        self.help_center_email = "//*[contains(@text,'Email')]"
        self.help_center_whatsapp = "//*[contains(@text,'Whatsapp')]"
        self.help_center_about_us = "//*[contains(@text,'About Us')]"
        self.help_center_subscription = "//*[contains(@text,'Subscription ')]"
        self.call_center = '//android.view.View[@content-desc="Whatsapp Live Chat"]'
        self.help_center_close_webview = "com.zte.iptvclient.android.idmnc:id/close"
        self.manage_profiles_add_profiles = "//*[contains(@text,'Add profile')]"
        self.back_to_settings = '//android.widget.ImageButton[@content-desc="Back"]'
        self.fld_change_password_current_password = (
            "//*[contains(@text,'Enter Current Password')]/following::*[2]"
        )
        self.fld_change_password_new_password = (
            "//*[contains(@text,'Enter Current Password')]/following::*[6]"
        )
        self.btn_next_change_password = '//android.widget.Button[@text="Next"]'

        self.txt_change_password_invalid_format_8_charracter = (
            "//*[contains(@text,'Password must be at least')]"
        )
        self.txt_change_password_invalid_format_uppercase = (
            "//*[contains(@text,'Password must contain at least one uppercase')]"
        )
        self.txt_change_password_invalid_format_6_charracter = (
            "//*[contains(@text,'Password must be at least 6')]"
        )
        self.txt_notif_invalid_current_password = (
            '//android.widget.TextView[@text="Invalid password"]'
        )
        self.btn_ok_invalid_password = '//android.widget.Button[@text="Close"]'
        self.txt_success_change_password = (
            "//*[contains(@text,'Password Succesfully Changed')]"
        )
        self.checkbox_accept_delete_account = '//android.widget.CheckBox[@text="I understand the information and I want to delete my account"]'
        self.btn_keep_account = '//android.widget.Button[@text="Keep Account"]'
        self.btn_process_delete_account = (
            '//android.widget.Button[@text="Proceed to Delete Account"]'
        )
        self.fld_password_delete_account = "//android.widget.EditText"
        self.btn_delete_account = '//android.widget.Button[@text="Delete Account"]'
        self.txt_delete_account_failed = (
            '//android.widget.TextView[@text="Delete Account Failed"]'
        )
        self.txt_success_delete_account = (
            '//android.view.View[@text="Your account is deleted"]'
        )
        self.fld_enter_voucher = "//android.widget.EditText"
        self.btn_redeem_voucher = '//android.widget.Button[@text="Reedem"]'
        self.img_tokopedia = '//android.view.View[@text="Tokopedia"]'
        self.img_lazada = '//android.view.View[@text="Lazada"]'
        self.img_blibli = '//android.view.View[@text="Blibli"]'
        self.img_coda = '//android.view.View[@text="Coda"]'
        self.txt_success_reedem = '//android.widget.TextView[@text="Voucher Redeemed"]'
        self.txt_see_my_status = '//android.widget.Button[@text="See my status"]'
        self.txt_transaction_details_voucher = (
            '//android.widget.TextView[@text="IKINGGH2WFXO3PREM"]'
        )
        self.txt_voucher_expired = '//android.view.View[@text="Voucher code expired"]'
        self.txt_voucher_invalid = '//android.view.View[@text="Invalid code"]'
        self.txt_help_center_voucher = '//android.widget.TextView[@text="Help Center"]'
        self.btn_profile_one = "//*[contains(@text,'ProfileSatu')]"
        self.btn_delete_profiles = '//android.widget.TextView[@resource-id="android:id/title" and @text="Delete profile"]'
        self.btn_accept_delete_profiles = "android:id/button1"
        self.btn_disconnect_all_manage_devices = (
            "com.zte.iptvclient.android.idmnc:id/disconnect_devices_button"
        )
        self.txt_no_devices_connected = (
            "com.zte.iptvclient.android.idmnc:id/errorTextView"
        )
        self.txt_transaction_history_pending = "//*[contains(@text,'Pending')]"
        self.txt_transaction_history_allstatus = "//*[contains(@text,'All Status')]"
        self.txt_transaction_history_success = "//*[contains(@text,'Success')]"
        self.txt_transaction_history_failed = "//*[contains(@text,'Failed')]"
        self.txt_transaction_history_no_transaction = (
            "//*[contains(@text,'No Transaction')]"
        )
        self.txt_transaction_history_failed_tab = "//*[contains(@text,'FAILED')]"
        self.txt_transaction_history_success_tab = "//*[contains(@text,'SUCCESS')]"
        self.txt_transaction_history_detail = (
            "//*[contains(@text,'Success')]/following::*[3]"
        )
        self.txt_transaction_history_detail_page = "//*[contains(@text,'Order ID')]"
        self.txt_server_error_transaction_history = (
            '(//android.widget.TextView[@text="Server Error"])[1]'
        )
        self.btn_close_server_error = '//android.widget.Button[@text="Close"]'
