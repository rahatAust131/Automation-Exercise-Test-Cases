from Test_Case_3.Necessary_Packages.Necessary_Packages import *


def handle_login_btn_click():
    # Click on 'Login' button
    try:
        login_btn = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[action='\/login'] .btn-default",)))
        login_btn.click()
        print("Login button clicked successfully!")
    except Exception as e:
        print("Login button click exception: ", type(e).__name__)

