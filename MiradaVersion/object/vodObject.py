class vodObject:
    def __init__(self):
        self.txt_detail_vod = "//*[contains(@text,'Subscriptions')]"
        self.fld_search = "com.zte.iptvclient.android.idmnc:id/search_edit_text"
        self.result_search_one = '//android.view.View[@content-desc="Montir Cantik"]'
        self.btn_watch = "com.zte.iptvclient.android.idmnc:id/watchButton"
        self.btn_add_to_list = "com.zte.iptvclient.android.idmnc:id/saveButton"
        self.btn_like = "com.zte.iptvclient.android.idmnc:id/likeButtonIcon"
        self.btn_dislike = "com.zte.iptvclient.android.idmnc:id/dislikeButtonIcon"
        self.btn_share = '//android.widget.TextView[@text="Share"]'
        self.btn_download = '//android.widget.TextView[@text="Download"]'
        self.txt_alert_gps = "com.zte.iptvclient.android.idmnc:id/alertTitle"
        self.btn_turn_on = "android:id/button1"
        self.btn_cancel_download = '//android.widget.TextView[@text="Cancel download"]'
        self.txt_cancel_dwnload = "com.zte.iptvclient.android.idmnc:id/alertTitle"
        self.btn_resume_download = "android:id/button2"
        self.btn_accept_cancel_download = "android:id/button1"
        self.btn_subscribe = "com.zte.iptvclient.android.idmnc:id/subscribeButton"
        self.list_packages = (
            "com.zte.iptvclient.android.idmnc:id/other_showings_group_header_title"
        )
        self.premium = '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.zte.iptvclient.android.idmnc:id/multi_line_popup_main_view"]/android.widget.RelativeLayout[6]'
        self.premium_sports = '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.zte.iptvclient.android.idmnc:id/multi_line_popup_main_view"]/android.widget.RelativeLayout[3]'
        self.txt_subscription_detail = (
            "com.zte.iptvclient.android.idmnc:id/subscriptionImage"
        )
        self.btn_eps1 = "//*[contains(@text,'Season ')]/following::*[2]"
        self.btn_eps2 = "//*[contains(@text,'Season ')]/following::*[3]"
        self.txt_download_progress = (
            "com.zte.iptvclient.android.idmnc:id/progressBarDownloaded"
        )
        self.btn_eps3 = "//*[contains(@text,'Season ')]/following::*[4]"
        self.btn_back = "com.zte.iptvclient.android.idmnc:id/backButton"
