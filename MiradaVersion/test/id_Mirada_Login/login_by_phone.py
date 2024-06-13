import pytest
from MiradaVersion.test.open_app import (
    driver,
    free_phone_data,
    premium_phone_data,
    premium_sport_phone_data,
    Choose_Login_As,
)


def login_free_by_phone(driver, free_phone_data):
    Choose_Login_As(driver, "FREE", free_phone_data=free_phone_data)


def login_premium_by_phone(driver, premium_phone_data):
    Choose_Login_As(driver, "PREMIUM", premium_phone_data=premium_phone_data)


def login_premium_sport_by_phone(driver, premium_sport_phone_data):
    Choose_Login_As(
        driver, "PREMIUM_SPORT", premium_sport_phone_data=premium_sport_phone_data
    )
