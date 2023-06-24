from Test_Case_4.Necessary_Packages.Necessary_Packages import *


def handle_logout_account_btn_click():
    # Delete Account button click checking
    try:
        logout_btn = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[href='\/logout']")))
        logout_btn.click()
        print("Logout button clicked successfully!")
    except Exception as e:
        print("Logout button Exception: ", type(e).__name__)
