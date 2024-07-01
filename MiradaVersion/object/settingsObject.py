class settingsObject:
    def __init__(self):
        self.txt_settings_page = "//*[contains(@text,'Settings')]"
        self.txt_settings_account_profile = '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.zte.iptvclient.android.idmnc:id/recycler_view"]/android.view.ViewGroup[3]'
        self.txt_account_page = "//*[contains(@text,'Account')]"
        self.txt_account_page_change_password = "//*[contains(@text,'Change password')]"
        self.txt_account_page_delete_account = "//*[contains(@text,'Delete account')]"
        self.btn_logout = "com.zte.iptvclient.android.idmnc:id/close_session_button"
        self.txt_transaction_history = "//*[contains(@text,'Transaction history')]"
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
