import time

from Homepage.Homepage_Handling import handle_homepage
from Click_On_Signup.Click_On_Signup_Button import handle_signup_btn
from Login.Verify_Login_Page_Visibility import handle_visibility_of_login_page
from Login.Login_Fields import handle_email_and_password_fields
from Click_On_Login_Button.Click_On_Login_Button import handle_login_btn_click
from Login_Error.Login_Error import handle_verification_of_error


def complete_test_case_3():
    url = "https://automationexercise.com"
    try:
        # task 1, 2, 3 are done here
        handle_homepage(url)
        # task 4 is done here
        handle_signup_btn()
        # task 5 is done here
        handle_visibility_of_login_page(url)
        # task 6 is done here
        handle_email_and_password_fields()
        # task 7 is done here
        handle_login_btn_click()
        # task 8 is done here
        handle_verification_of_error()
        time.sleep(2)

    except Exception as e:
        print("Main method Exception: ", type(e).__name__)


complete_test_case_3()
