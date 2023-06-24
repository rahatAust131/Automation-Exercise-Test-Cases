from Test_Case_4.Necessary_Packages.Necessary_Packages import *


def handle_page_after_logout(url):
    # Verify that user is navigated to login page
    try:
        assert f"{url}/login" in driver.current_url, f"Navigation to Login page URL mismatched!"
        print("User is navigated to login page successfully!")
    except Exception as e:
        print("Navigation to Login page URL Exception: ", type(e).__name__)
