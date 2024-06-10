class loginObject:
    def __init__(self):
        self.btn_login = "com.zte.iptvclient.android.idmnc:id/login_button"
        self.txt_welcome = "com.zte.iptvclient.android.idmnc:id/welcossmeText"
        self.txt_fld_email = "//android.widget.ScrollView/android.widget.EditText[1]"
        self.txt_fld_password = "//android.widget.ScrollView/android.widget.EditText[2]"
        self.btn_submit_login = "(//android.widget.Button)[3]"
        self.btn_signup = "com.zte.iptvclient.android.idmnc:id/register_button"
        self.txt_register_page = "//*[contains(@text,'Register')]"
        self.txt_fld_phone_number = "//android.widget.TextView[contains(@text, 'Phone Number')]/following::android.widget.EditText[1]"
        self.btn_send_otp = "//*[contains(@text,'Send OTP')]"
        self.fld_otp = "//android.widget.ScrollView/android.widget.EditText[3]"
        self.resend_otp = "//*[contains(@text,'Resend in')]"
        self.btn_register = "//*/android.view.View[2]/android.widget.Button"
        self.email_section = "//*/android.widget.TextView[contains(@text, 'Email')]"
        self.txt_discover_profiles = (
            "com.zte.iptvclient.android.idmnc:id/profiles_discover"
        )
        self.btn_skip_discover_profiles = (
            "com.zte.iptvclient.android.idmnc:id/profiles_skip"
        )
        self.btn_add_profile_discover_profiles = (
            "com.zte.iptvclient.android.idmnc:id/add_profile_button"
        )
        self.txt_skip_profile = "com.zte.iptvclient.android.idmnc:id/profiles_skip"
        self.btn_cancel_skip_profile = (
            "com.zte.iptvclient.android.idmnc:id/profiles_cancel"
        )
        self.btn_continue_skip_profile = (
            "com.zte.iptvclient.android.idmnc:id/continue_button"
        )
        self.txt_login_page = "//*[contains(@text,'Login')]"
        self.txt_email_section = "//*[contains(@text,'Email ')]"
        self.txt_send_via_sms = "//*[contains(@text,'Send via SMS')]"
        self.txt_account_has_been_registered = (
            '//android.widget.TextView[@text="This account has been registered"]'
        )
        self.txt_terms_of_use = "com.zte.iptvclient.android.idmnc:id/terms_of_use"
        self.txt_privacy_policy = "com.zte.iptvclient.android.idmnc:id/privacy_policy"
