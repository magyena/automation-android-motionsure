import pytest
import time
from MotionSure.test.open_app import (
    driver,
    openapp,
)


def test_login_free_by_phone(driver):
    openapp(driver)
