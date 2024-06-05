from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def inputCodeWeb(angka):
    drivem = webdriver.Chrome()
    drivem.maximize_window()
    drivem.implicitly_wait(10)
    drivem.get("https://visionplus.id")
    drivem.find_element(By.XPATH, "//span[contains(text(), 'Log in/Register')]").click()
    mainWindow = drivem.current_window_handle  
    for handle in drivem.window_handles:  
        if handle != mainWindow:
            drivem.switch_to.window(handle)
            break
    time.sleep(3)  # Pastikan untuk mengimpor modul time
    drivem.find_element(By.XPATH, "//input[@id='phone']").send_keys("8997775838")
    drivem.find_element(By.XPATH, "//input[@id='fld_Password']").send_keys("4321Lupa")
    time.sleep(1)
    drivem.find_element(By.XPATH, "//button[@id='btn_Login']").click()
            # wait ganti element
    time.sleep(5)
    mainWindow = drivem.window_handles[0]  
    drivem.switch_to.window(mainWindow)
            # time.sleep(500)
    drivem.find_element(By.XPATH, "(//div[@class='profiles-container']//div//div//div//img)[1]").click()
    time.sleep(1)
    drivem.get("https://visionplus.id/webclient/#/activate?code="+angka)
    time.sleep(2)
    drivem.find_element(By.XPATH, "//span[text()='Submit']").click()
    time.sleep(1)
    drivem.quit()