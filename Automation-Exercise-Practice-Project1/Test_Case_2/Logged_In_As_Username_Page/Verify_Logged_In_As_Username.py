from Test_Case_2.Necessary_Packages.Necessary_Packages import *


def handle_logged_in_as_user_visibility():
    # Verify that 'Logged in as username' is visible
    try:
        login_as_user_text = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(10) a")))
        if login_as_user_text.text == "Logged in as Demo":
            print("Logged in as username successful")
        else:
            print("Couldn't log in as user")
    except Exception as e:
        print("Login as user Exception: ", type(e).__name__)
