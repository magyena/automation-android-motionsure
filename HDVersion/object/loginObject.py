class loginObject:
    def __init__(self):
        self.btn_login = "com.zte.iptvclient.android.idmnc:id/login_button"
        self.txt_welcome = "com.zte.iptvclient.android.idmnc:id/welcossmeText"
        self.btn_Login_by_email = (
            "//*/android.widget.TextView[contains(@text, 'Email')]"
        )
        self.txt_fld_email = "//android.widget.ScrollView/android.widget.EditText[1]"
        self.txt_fld_password = "//android.widget.ScrollView/android.widget.EditText[2]"
        self.btn_submit_login = "(//android.widget.Button)[3]"
        self.btn_signup = "com.zte.iptvclient.android.idmnc:id/register_button"
        self.txt_register_page = "//*[contains(@text,'Register')]"
        self.txt_fld_phone_number="//android.widget.TextView[contains(@text, 'Phone Number')]/following::android.widget.EditText[1]"
        self.btn_send_otp="//*[contains(@text,'Send OTP')]"
        self.fld_otp = "//android.widget.ScrollView/android.widget.EditText[3]"
        self.resend_otp="//*[contains(@text,'Resend in')]"
        self.btn_register="//*/android.view.View[2]/android.widget.Button"
        self.email_section="//*/android.widget.TextView[contains(@text, 'Email')]"