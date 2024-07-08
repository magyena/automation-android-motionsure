class livetvObject:
    def __init__(self):
        self.img_rcti = "//*[contains(@text,'001')]"
        self.img_inews = "//*[contains(@text,'004')]"
        self.img_transtv = "//*[contains(@text,'006')]"
        self.img_trans7 = "//*[contains(@text,'007')]"
        self.btn_subscribe = "//*[contains(@text,'SUBSCRIBE')]"
        self.txt_subscribe = "//*[contains(@text,'This is a subscription channel')]"
        self.img_sportstarts = "//*[contains(@text,'112')]"
        self.img_sportstarts2 = "//*[contains(@text,'113')]"
        self.img_sportstarts3 = "//*[contains(@text,'114')]"
        self.img_soccer = "//*[contains(@text,'115')]"
        self.btn_goto_mydownloads = (
            "com.zte.iptvclient.android.idmnc:id/buttonGoMyDownloads"
        )
        self.btn_detail_channel_sportstars = (
            "//*[contains(@text,'113')]/following::*[11]"
        )
        self.txt_detail_channel_sportstars = "//*[contains(@text,'Sportstars 2')]"
