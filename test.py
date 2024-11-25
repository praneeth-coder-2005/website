from playwright.sync_api import sync_playwright
import time

def hotstar_login():
    with sync_playwright() as p:
        # Launch browser
        print("Launching browser...")
        browser = p.chromium.launch(headless=False)  # Set headless=True to hide the browser
        context = browser.new_context()
        page = context.new_page()

        # Navigate to Hotstar login page
        print("Navigating to Hotstar website...")
        page.goto("https://www.hotstar.com/in")
        time.sleep(5)  # Allow time for the page to load

        # Click on login button
        print("Clicking login button...")
        login_button = page.query_selector("text=Login")
        if login_button:
            login_button.click()
            time.sleep(2)
        else:
            print("Login button not found!")
            return

        # Enter mobile number
        mobile_number = input("Enter your mobile number: ")
        print("Entering mobile number...")
        mobile_input = page.query_selector("input[type='tel']")
        if mobile_input:
            mobile_input.fill(mobile_number)
            mobile_input.press("Enter")
            time.sleep(5)
        else:
            print("Mobile number input field not found!")
            return

        # Enter OTP
        otp = input("Enter the OTP received: ")
        print("Entering OTP...")
        otp_input = page.query_selector("input[type='text']")
        if otp_input:
            otp_input.fill(otp)
            otp_input.press("Enter")
            time.sleep(5)
        else:
            print("OTP input field not found!")
            return

        # Check for login success
        if "error" in page.content().lower():
            print("Login failed. Please check the OTP and try again.")
        else:
            print("Login successful!")

        # Close the browser
        browser.close()

if __name__ == "__main__":
    hotstar_login()
