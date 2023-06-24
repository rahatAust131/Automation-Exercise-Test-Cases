from Test_Case_3.Necessary_Packages.Necessary_Packages import *


def handle_verification_of_error():
    # Verify error 'Your email or password is incorrect!' is visible
    try:
        error_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[action] p",)))
        assert error_field.text == "Your email or password is incorrect!", f"Error Text mismatched!"
        print("Error Text shown successfully!")
    except Exception as e:
        print("Error Text exception: ", type(e).__name__)
