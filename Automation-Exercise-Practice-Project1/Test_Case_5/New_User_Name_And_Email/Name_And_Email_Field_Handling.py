from Test_Case_5.Necessary_Packages.Necessary_Packages import *


def handle_name_and_email_for_new_user():
    # Enter name in the name field
    try:
        username_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[type='text']")))
        username_field.send_keys("demo")
        print("Name entered successfully!")
    except Exception as e:
        print("Name field exception: ", type(e).__name__)

    # Enter already registered email address in email field
    try:
        email_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[action='\/signup'] [type='email']")))
        email_field.send_keys("demo@yahoo.com")
        print("Email entered successfully!")
    except Exception as e:
        print("Email field exception: ", type(e).__name__)
