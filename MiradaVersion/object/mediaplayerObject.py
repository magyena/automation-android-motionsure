class mediaplayerObject:
    def __init__(self):
        self.btn_skip_add = "//*[contains(@text,'Skip Ad')]"
        self.txt_restart = "//*[contains(@text,'00:00:01')]"
        self.txt_forward = "//*[contains(@text,'00:00:10')]"
        self.txt_settings = "//*[contains(@text,'Audio')]"
        self.txt_tittle_media_playerpage = (
            "com.zte.iptvclient.android.idmnc:id/media_player_title_textview"
        )
        self.btn_rewind_media_playerpage = (
            "com.zte.iptvclient.android.idmnc:id/media_player_rewind_button"
        )
        self.btn_forward_media_playerpage = (
            "com.zte.iptvclient.android.idmnc:id/media_player_fastforward_button"
        )
        self.txt_currenttime_media_playerpage = (
            "com.zte.iptvclient.android.idmnc:id/media_player_currenttime"
        )
        self.txt_duration_media_playerpage = (
            "com.zte.iptvclient.android.idmnc:id/media_player_duration"
        )
        self.btn_next_episode_media_playerpage = (
            "com.zte.iptvclient.android.idmnc:id/remoteNextEpisode"
        )
        self.btn_previous_episode_media_playerpage = '//android.widget.Button[@resource-id="com.zte.iptvclient.android.idmnc:id/remotePrevEpisode"]'
        self.btn_pause_play_media_playerpage = (
            "com.zte.iptvclient.android.idmnc:id/media_player_play_pause_button"
        )
        self.btn_volume_media_playerpage = '//android.widget.RelativeLayout[@resource-id="com.zte.iptvclient.android.idmnc:id/media_player_volume_layout_container"]/android.widget.ImageView'
        self.btn_restart_media_playerpage = (
            "com.zte.iptvclient.android.idmnc:id/media_player_player_reload_button"
        )
        self.btn_settings_mediaplayer = (
            "com.zte.iptvclient.android.idmnc:id/media_player_language_and_subs_button"
        )
        self.btn_ok_settings_mediaplayer = "android:id/button1"
        self.radio_btn_indonesia_language_media_playerpage = (
            '//android.widget.RadioButton[@text="Indonesian"]'
        )
        self.radio_btn_disable_lang_media_playerpage = (
            '//android.widget.RadioButton[@text="Disabled"]'
        )
        self.radio_btn_english_language_media_playerpage = (
            '//android.widget.RadioButton[@text="English"]'
        )
        self.layout_media_player = '//android.widget.FrameLayout[@resource-id="com.zte.iptvclient.android.idmnc:id/exo_subtitles"]/android.view.View'
        self.img_buffering_media_player = (
            "com.zte.iptvclient.android.idmnc:id/media_player_progress_text"
        )
