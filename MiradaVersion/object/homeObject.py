class homeObject:
    def __init__(self):
        self.txt_Hello = "label == 'Hello! Who's watching?'"
        self.txt_vision_logo = "com.zte.iptvclient.android.idmnc:id/appLogo"
        self.btn_menu_button = "com.zte.iptvclient.android.idmnc:id/menuButton"
        self.btn_search = '//android.widget.ImageButton[@resource-id="com.zte.iptvclient.android.idmnc:id/search_button"]'
        self.btn_voice_search = "com.zte.iptvclient.android.idmnc:id/voiceSearchButton"
        self.img_home = "//*[contains(@text,'Home')]"
        self.img_originals = "//*[contains(@text,'Originals')]"
        self.img_Sports = "//*[contains(@text,'Sports')]"
        self.img_movies = "//*[contains(@text,'Movies')]"
        self.img_tv_shows = "//*[contains(@text,'TV Shows')]"
        self.img_live_tv = "//*[contains(@text,'Live TV')]"
        self.img_program_guide = "//*[contains(@text,'Program Guide')]"
        self.img_buy_package = "//*[contains(@text,'Buy Package')]"
        self.img_my_downloads = "//*[contains(@text,'My Downloads')]"
        self.btn_settings_button = "com.zte.iptvclient.android.idmnc:id/settings_button"
        self.txt_settings_page = "//*[contains(@text,'Settings')]"
        self.txt_settings_account_profile = '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.zte.iptvclient.android.idmnc:id/recycler_view"]/android.view.ViewGroup[3]'
        self.txt_account_page = "//*[contains(@text,'Account')]"
        self.txt_account_page_change_password = "//*[contains(@text,'Change password')]"
        self.txt_account_page_delete_account = "//*[contains(@text,'Delete account')]"
        self.btn_logout = "com.zte.iptvclient.android.idmnc:id/close_session_button"
        self.btn_profile = "com.zte.iptvclient.android.idmnc:id/profileButton"
        self.txt_search_page = "//*[contains(@text,'You can search for things like')]"
        self.txt_back = "com.zte.iptvclient.android.idmnc:id/back"
        self.fld_search = "com.zte.iptvclient.android.idmnc:id/search_edit_text"
        self.result_search_one = '//android.view.View[@content-desc="Montir Cantik"]'
        self.result_search_livetv = '(//android.view.View[@content-desc="iNews"])[2]'
        self.txt_search_no_result = "com.zte.iptvclient.android.idmnc:id/errorTextView"
        self.detail_banner = "com.zte.iptvclient.android.idmnc:id/container_banner_info"
        self.txt_viewl_all_cluster_originals = (
            "com.zte.iptvclient.android.idmnc:id/stripActionButton"
        )
        self.txt_first_view_all_cluster_originals = (
            "//*[contains(@text,'Teenage')]/following::*[2]"
        )
        self.txt_content_detail_cluster_vplus_originals = (
            "//*[contains(@text,'VIEW ALL')]/following::*[3]"
        )
        self.txt_cluster_livetv = "//*[contains(@text,'Your Favorite TV Channel')]"
        self.txt_channel_cluster_live_tv = (
            "//*[contains(@text,'National TV')]/following::*[2]"
        )
        self.txt_cluster_top_10_this_week = "//*[contains(@text,'Top 10 This Week')]"
        self.txt_content_cluster_10_this_week = (
            "//*[contains(@text,'Top 10 This Week')]/following::*[3]"
        )
        self.txt_cluster_watchlist = "//*[contains(@text,'Watchlist')]"
        self.txt_cluster_new_releases = "//*[contains(@text,'New Releases')]"
        self.content_cluster_new_releases = (
            "//*[contains(@text,'New Releases')]/following::*[2]"
        )
        self.txt_genre_action = (
            "//*[contains(@text,'Explore by Genre')]/following::*[2]"
        )
        self.cluster_genre_action = "//*[contains(@text,'Explore by Genre')]"
        self.content_genre_action = '//android.view.View[@content-desc="12 Hari"]'
        self.btn_popular_actors = (
            "//*[contains(@text,'Popular Actors')]/following::*[2]"
        )
        self.cluster_popular_actors = "//*[contains(@text,'Popular Actors')]"
        self.content_popular_actors = (
            '//android.view.View[@content-desc="2 Tahun Ikatan Cinta"]'
        )
