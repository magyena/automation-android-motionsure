class playstoreObject:
    def __init__(self):
        self.img_profile = '//android.widget.ImageView[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]'
        self.img_payments_subscriptions = '//android.widget.TextView[@resource-id="com.android.vending:id/0_resource_name_obfuscated" and @text="Payments & subscriptions"]'
        self.txt_first_current_package = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[1]"
        self.txt_second_current_package = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[2]"
        self.img_subscriptions = '//android.widget.TextView[@resource-id="com.android.vending:id/0_resource_name_obfuscated" and @text="Subscriptions"]'
        self.btn_cancel_subscription = (
            '//android.widget.TextView[@content-desc="Cancel subscription"]'
        )
        self.btn_no_thanks = '//android.widget.TextView[@content-desc="No thanks"]'
        self.reason_cancel = (
            '//android.widget.RadioButton[@content-desc="Decline to answer"]'
        )
        self.btn_continue = '//android.widget.TextView[@content-desc="Continue"]'
        self.btn_back = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.Button"
        self.btn_subscribe = '//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]'
