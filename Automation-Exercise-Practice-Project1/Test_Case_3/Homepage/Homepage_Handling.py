from Test_Case_3.Necessary_Packages.Necessary_Packages import *


def handle_homepage(url):
    try:
        driver.get(url)
        assert url in driver.current_url, f"URL mismatched!"
        print("Homepage opened successfully!")
    except Exception as e:
        print("Homepage URL Exception: ", type(e).__name__)
