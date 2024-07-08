class profileObject:
    def __init__(self):
        self.txt_Hello = "label == 'Hello! Who's watching?'"
        self.first_profile = '(//android.widget.ImageView[@content-desc="false"])[1]'
        self.second_profile = '(//android.widget.ImageView[@content-desc="false"])[2]'
        self.third_profile = '(//android.widget.ImageView[@content-desc="false"])[3]'
        self.fourth_profile = '(//android.widget.ImageView[@content-desc="false"])[4]'
        self.fifth_profile = '(//android.widget.ImageView[@content-desc="false"])[5]'
        self.sixth_profile = '(//android.widget.ImageView[@content-desc="false"])[6]'
        self.seventh_profile = '(//android.widget.ImageView[@content-desc="false"])[7]'
        self.eight_profile = '(//android.widget.ImageView[@content-desc="false"])[8]'
        self.add_profile_button = (
            "com.zte.iptvclient.android.idmnc:id/add_profile_button"
        )
        self.txt_create_profile = (
            "com.zte.iptvclient.android.idmnc:id/titleCreateProfile"
        )
        self.fld_create_profile = "com.zte.iptvclient.android.idmnc:id/profileName"
        self.btn_cancel_create_profile = "//*[contains(@text,'CANCEL')]"
        self.btn_ok_create_profile = "//*[contains(@text,'OK')]"
        self.txt_success_create_profile = (
            "com.zte.iptvclient.android.idmnc:id/profiles_done"
        )
        self.btn_done_success_create_profile = (
            "com.zte.iptvclient.android.idmnc:id/done_button"
        )
        self.btn_cancel_success_create_profile = (
            "com.zte.iptvclient.android.idmnc:id/cancel_button"
        )
        self.txt_create_profile_satu = "//*[contains(@text,'ProfileSatu')]"
        self.txt_create_profile_dua = "//*[contains(@text,'ProfileDua')]"
        self.txt_create_profile_tiga = "//*[contains(@text,'ProfileTiga')]"
        self.txt_create_profile_empat = "//*[contains(@text,'ProfileEmpat')]"
        self.txt_create_profile_lima = "//*[contains(@text,'ProfileLima')]"
        self.txt_create_profile_enam = "//*[contains(@text,'ProfileEnam')]"
        self.txt_create_profile_tujuh = "//*[contains(@text,'ProfileTujuhhhh')]"
        self.img_avatar = "com.zte.iptvclient.android.idmnc:id/imageAvatar"
        self.img_avatar_second = (
            '(//android.widget.ImageView[@content-desc="Choose an avatar"])[2]'
        )
        self.btn_ok_change_avatar = (
            '//android.widget.Button[@resource-id="android:id/button1"]'
        )
        self.txt_avatar_page = "com.zte.iptvclient.android.idmnc:id/chooseAvatarTitle"
        self.txt_name_already_exist = (
            "com.zte.iptvclient.android.idmnc:id/popup_message"
        )
        self.btn_ok = "android:id/button1"
        self.btn_cancel = "android:id/button2"
