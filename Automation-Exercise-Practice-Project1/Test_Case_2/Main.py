from Homepage.Homepage_Handling import handle_homepage
from Click_On_Signup.Click_On_Signup_Button import handle_signup_btn
from Login.Verify_Login_Page_Visibility import handle_visibility_of_login_page
from Login.Login_Fields import handle_email_and_password_fields
from Click_On_Login_Button.Click_On_Login_Button import handle_login_btn_click
from Logged_In_As_Username_Page.Verify_Logged_In_As_Username import handle_logged_in_as_user_visibility
from Logged_In_As_Username_Page.Delete_Account_Button import handle_delete_account_btn_click
from After_Account_Deletion_Page.Verify_Account_Deletion import handle_account_deletion_verification


def complete_test_case_2():
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
        handle_logged_in_as_user_visibility()
        # task 9 is done here
        handle_delete_account_btn_click()
        # task 10 is done here
        handle_account_deletion_verification()

    except Exception as e:
        print("Main method Exception: ", type(e).__name__)


complete_test_case_2()
