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
        self.email_section = "//*[contains(@text,'Email')]"
        self.phone_section = "//*[contains(@text,'Phone Number')]"
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
        self.txt_send_otp_via_whatsapp = "//*[contains(@text,'Send OTP ')]"
        self.drop_country = "//android.widget.ScrollView/android.widget.EditText[1]/android.view.View/android.view.View"
        self.fld_country_code = "/hierarchy/android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.widget.EditText"
        self.country_code_indonesia = '//android.widget.TextView[@text="+62"]'
        self.country_code_malaysia = '//android.widget.TextView[@text="+60"]'
        self.btn_close_country_code = '//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View/android.view.View[2]'
        self.txt_country_code = "//*[contains(@text,'Country Code')]"
        self.txt_result_search_country = '//android.view.ViewGroup[@resource-id="android:id/content"]/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View'
        self.country_code_netherland = '//android.widget.TextView[@text="+31"]'
        self.txt_no_country_found = "//*[contains(@text,'No country code found.')]"
        self.txt_phone_number_inccorrect = (
            '//android.widget.TextView[@text="Phone number incorrect."]'
        )
        self.btn_visible_password = '//android.widget.EditText[@text="••••••••"]/android.view.View/android.view.View[1]/android.widget.Button'
        self.txt_password_does_not_criteria = (
            "//*[contains(@text,'Password does not match the criteria.')]"
        )
        self.txt_wrong_otp = "//*[contains(@text,'Wrong OTP code')]"
        self.txt_otp_expired = "//*[contains(@text,'OTP Expired')]"
        self.resend_second_otp = "//*[contains(@text,'Resend in 04:')]"
        self.txt_first_otp = "//*[contains(@text,'Resend in 01:')]"
        self.txt_invalid_phone_number = "//*[contains(@text,'Phone number incorrect.')]"
        self.txt_invisible_password = "//*[contains(@text,'4321Lupa')]"
        self.txt_invalid_email = (
            "//*[contains(@text,'Email address format incorrect.')]"
        )
        self.btn_login_from_register = "//*[contains(@text,'Login')]"
        self.txt_this_account_has_Not_been_registered = (
            "//*[contains(@text,'This account has not been registered.')]"
        )
        self.btn_forgot_password = "//*[contains(@text,'Forgot Password?')]"
        self.txt_forgot_password = "//*[contains(@text,'Forgot Password')]"
        self.btn_save_password = "//*[contains(@text,'Save Password')]"
        self.txt_error_login="//*[contains(@text,'Expected response')]"