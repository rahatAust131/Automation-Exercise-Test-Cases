from Test_Case_5.Necessary_Packages.Necessary_Packages import *


def handle_email_error_msg():
    try:
        error_text = WebDriverWait(driver, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[action] p")))
        assert error_text.text == "Email Address already exist!", f"Wrong error text"
        print("Error text matched successfully!")
    except Exception as e:
        print("Email error Exception: ", type(e).__name__)
