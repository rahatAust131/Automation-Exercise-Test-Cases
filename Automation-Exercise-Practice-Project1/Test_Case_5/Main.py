from Homepage.Homepage_Handling import handle_homepage
from Click_On_Signup.Click_On_Signup_Button import handle_signup_btn
from New_User_Page.New_User_Signup_Visibility import handle_new_user_signup_page
from New_User_Name_And_Email.Name_And_Email_Field_Handling import handle_name_and_email_for_new_user
from Signup_Button.Click_On_Signup_Button import handle_signup_btn_click
from Email_Error.Already_Existed_Email import handle_email_error_msg


def complete_all_tasks_after_test_case_5():
    try:
        # task 1, 2 & 3
        handle_homepage("https://automationexercise.com")
        # task 4
        handle_signup_btn()
        # task 5
        handle_new_user_signup_page()
        # task 6
        handle_name_and_email_for_new_user()
        # task 7
        handle_signup_btn_click()
        # task 8
        handle_email_error_msg()
    except Exception as e:
        print("Homepage Exception: ", type(e).__name__)


complete_all_tasks_after_test_case_5()
