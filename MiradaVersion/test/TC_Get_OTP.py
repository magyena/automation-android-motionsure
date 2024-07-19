from MiradaVersion.utils.connect_db import get_otp_from_db


def print_last_otp(phone_number, message=""):
    # Call the get_last_otp function with the provided phone number
    last_otp = get_otp_from_db(phone_number)

    # Check if an OTP was returned
    if last_otp:
        print(f"{message} OTP Found for {phone_number}: {last_otp}")
        return last_otp
    else:
        print(f"{message} No OTP found in db for {phone_number}")
        return None
