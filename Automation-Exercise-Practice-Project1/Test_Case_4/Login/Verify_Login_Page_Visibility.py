from Test_Case_4.Necessary_Packages.Necessary_Packages import *


def handle_visibility_of_login_page(url):
    try:
        assert f"{url}/login" in driver.current_url, f"Login Page URL mismatched!"
        print("'Login To Your Account Page' visible!")
    except Exception as e:
        print("Login page url Exception: ", type(e).__name__)
