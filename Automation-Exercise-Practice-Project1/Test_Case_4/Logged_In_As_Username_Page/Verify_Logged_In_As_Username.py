from Test_Case_4.Necessary_Packages.Necessary_Packages import *


def handle_logged_in_as_user_visibility():
    # Verify that 'Logged in as username' is visible
    try:
        login_as_user_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(10) a")))
        assert login_as_user_field.text == "Logged in as demo", f"Logged in as username mismatched!"
        print("Logged in as username successful")
    except Exception as e:
        print("Login as user Exception: ", type(e).__name__)
