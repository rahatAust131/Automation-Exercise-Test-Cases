from Test_Case_5.Necessary_Packages.Necessary_Packages import *


def handle_new_user_signup_page():
    # Verify 'New User Signup!' is visible
    assert "https://automationexercise.com/login" in driver.current_url, f"Signup URL mismatched!"
    print("New User Sign up page opened successfully!")
