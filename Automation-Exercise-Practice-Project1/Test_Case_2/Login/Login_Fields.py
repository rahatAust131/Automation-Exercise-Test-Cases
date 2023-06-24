from Test_Case_2.Necessary_Packages.Necessary_Packages import *


def handle_email_and_password_fields():
    try:
        # Email field checking
        email_field = WebDriverWait(driver, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[action='\/login'] [type='email']")))
        email_field.send_keys("demo123@yahoo.com")
        print("Email entered successfully!")
    except Exception as e:
        print("Email field Exception: ", type(e).__name__)

    try:
        # Password field checking
        password_field = WebDriverWait(driver, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[action='\/login'] [type='password']")))
        password_field.send_keys("23232323")
        print("Password entered successfully!")
    except Exception as e:
        print("Password field Exception: ", type(e).__name__)
