import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By
from MiradaVersion.utils.openchrome import inputCodeWeb
import time
import pyautogui
from appium.options.android import UiAutomator2Options


class SetupAppium:
    def __init__(self):
        options = UiAutomator2Options()

        device_name = os.getenv("ANDROID_DEVICE_NAME", "cisoeqnjnnhqmr5l")
        # device_name = os.getenv("ANDROID_DEVICE_NAME", "emulator-5544")
        options.set_capability("deviceName", device_name)

        # Set the app path
        app_path = "/Users/visionplus/Documents/Automation/automation-android-python/MiradaVersion/utils/mirada.apk"
        # app_path = "/Users/fatahalim/Documents/VisualStudio/automation-android-visionplus/utils/mirada.apk"
        if not os.path.exists(app_path):
            raise FileNotFoundError(f"APK file not found at {app_path}")

        options.set_capability("app", app_path)

        # Additional capabilities
        options.set_capability("autoGrantPermissions", "true")
        options.set_capability("automationName", "UiAutomator2")
        options.set_capability("newCommandTimeout", 86400)
        options.set_capability("enforceXPath1", True)

        # Appium server URL
        appium_server_url = "http://127.0.0.1:4723"

        # Initialize the Appium driver
        self.driver = webdriver.Remote(appium_server_url, options=options)

        # Print confirmation
        print(f"Appium driver initialized with device: {device_name}")
