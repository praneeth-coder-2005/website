from playwright.sync_api import sync_playwright
import time

def hotstar_login():
    with sync_playwright() as p:
        try:
            # Launch browser in non-headless mode for debugging
            print("Launching browser...")
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            # Navigate to Hotstar
            print("Navigating to Hotstar...")
            page.goto("https://www.hotstar.com/in")
            time.sleep(5)  # Wait for page to load

            # Step 1: Click Login Button
            print("Attempting to locate and click the login button...")
            login_button = page.query_selector("text=Login")
            if login_button:
                login_button.click()
                time.sleep(2)
                print("Login button clicked.")
            else:
                print("Login button not found. Retrying...")
                page.reload()
                time.sleep(5)
                login_button = page.query_selector("text=Login")
                if login_button:
                    login_button.click()
                else:
                    print("Login button still not found. Exiting.")
                    return

            # Step 2: Enter Mobile Number
            print("Locating the mobile number input field...")
            mobile_input = page.query_selector("input[type='tel']")
            if mobile_input:
                print("Mobile number input field located.")
                mobile_number = input("Enter your mobile number: ")
                mobile_input.fill(mobile_number)
                mobile_input.press("Enter")
                print("Mobile number submitted.")
            else:
                print("Mobile number input field not found. Retrying...")
                page.reload()
                time.sleep(5)
                mobile_input = page.query_selector("input[type='tel']")
                if mobile_input:
                    mobile_input.fill(input("Enter your mobile number: "))
                    mobile_input.press("Enter")
                else:
                    print("Mobile input field still not found. Exiting.")
                    return

            # Step 3: Check for OTP Prompt or Errors
            print("Waiting for OTP field or error message...")
            time.sleep(5)
            if "error" in page.content().lower() or "invalid" in page.content().lower():
                print("Error detected on the page. Please verify the mobile number.")
                return

            # Step 4: Enter OTP
            print("Locating the OTP input field...")
            otp_input = page.query_selector("input[type='text']")
            if otp_input:
                otp = input("Enter the OTP received on your phone: ")
                otp_input.fill(otp)
                otp_input.press("Enter")
                print("OTP submitted.")
            else:
                print("OTP input field not found. Retrying...")
                page.reload()
                time.sleep(5)
                otp_input = page.query_selector("input[type='text']")
                if otp_input:
                    otp = input("Enter the OTP received on your phone: ")
                    otp_input.fill(otp)
                    otp_input.press("Enter")
                else:
                    print("OTP input field still not found. Exiting.")
                    return

            # Step 5: Confirm Login Success or Failure
            print("Checking for login confirmation...")
            time.sleep(5)
            if "error" in page.content().lower():
                print("Login failed. Please check the OTP and try again.")
            else:
                print("Login successful!")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Close the browser
            print("Closing the browser.")
            browser.close()

if __name__ == "__main__":
    hotstar_login()
