from appium.webdriver.webdriver import WebDriver
import pytest
import random
import time
from MiradaVersion.utils.setup import SetupAppium
from MiradaVersion.pages.signUpPage import SignUp
from MiradaVersion.test.TC_Get_OTP import print_last_otp
from MiradaVersion.pages.homepagePages import HomePage

password = "4321Lupa"

def generate_random_integer_string(length):
    return ''.join(str(random.randint(0, 9)) for _ in range(length))

def generate_random_email(domain_list, first_names):
    first_name = random.choice(first_names).lower()
    random_integer_string = generate_random_integer_string(random.randint(5, 10))
    domain = random.choice(domain_list)
    return f"{first_name}{random_integer_string}qa@{domain}"

domains = ["visionplus.id"]

first_names = ["Testing"]

random_email = generate_random_email(domains, first_names)
print(random_email)


@pytest.fixture(scope="module")
def driver():
    setup_appium = SetupAppium()
    yield setup_appium.driver

def test_Register(driver: WebDriver):
    register = SignUp(driver)
    homepage = HomePage(driver)
    
    register.clickSignUp()
    register.assertRegisterPage()
    register.clickEmailSection()
    random_email = generate_random_email(domains, first_names)  
    register.inputEmail(random_email) 
    register.inputPassword(password)
    register.clickButtonSendOtp()
    otp = print_last_otp(random_email)
    register.inputOTP(otp)
    register.clickSubmitRegister()
    register.assertDiscoverProfiles()
    register.clickBtnSkipDiscoverProfiles()
    register.assertSkipProfile()
    register.clickBtnContinueSkipProfile()
    
    homepage.assertHomePage()
    
    