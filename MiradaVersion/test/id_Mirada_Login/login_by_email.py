import pytest
from MiradaVersion.test.open_app import (
    driver,
    free_email_data,
    premium_email_data,
    premium_sport_email_data,
    Choose_Login_As,
)


def login_free_by_email(driver, free_email_data):
    Choose_Login_As(driver, "FREE", free_email_data, None, None)


def login_premium_by_email(driver, premium_email_data):
    Choose_Login_As(driver, "PREMIUM", None, premium_email_data, None)


def login_premium_sport_by_email(driver, premium_sport_email_data):
    Choose_Login_As(driver, "PREMIUM_SPORT", None, None, premium_sport_email_data)
