import pyautogui
import time
import webbrowser
import os

# Open Hotstar in a real browser
def open_hotstar():
    print("Opening Hotstar website...")
    webbrowser.open("https://www.hotstar.com/in")  # Opens Hotstar in the default web browser
    time.sleep(10)  # Allow time for the page to load

# Enter the mobile number
def enter_mobile_number():
    print("Please position your mouse over the mobile number field.")
    time.sleep(5)  # Give you time to position the mouse
    x, y = pyautogui.position()  # Record the coordinates of the field
    print(f"Captured mobile number input field at ({x}, {y})")

    # Get mobile number from user
    mobile_number = input("Enter your mobile number: ")

    # Move and click on the input field
    pyautogui.click(x, y)
    time.sleep(1)
    pyautogui.typewrite(mobile_number)  # Type the mobile number
    pyautogui.press("enter")
    print("Mobile number entered.")

# Enter the OTP
def enter_otp():
    print("Please position your mouse over the OTP field.")
    time.sleep(5)  # Give you time to position the mouse
    x, y = pyautogui.position()  # Record the coordinates of the field
    print(f"Captured OTP input field at ({x}, {y})")

    # Get OTP from user
    otp = input("Enter the OTP received: ")

    # Move and click on the OTP field
    pyautogui.click(x, y)
    time.sleep(1)
    pyautogui.typewrite(otp)  # Type the OTP
    pyautogui.press("enter")
    print("OTP entered. Waiting for login confirmation...")

# Main function
def main():
    try:
        open_hotstar()  # Step 1: Open the website
        enter_mobile_number()  # Step 2: Enter mobile number
        time.sleep(10)  # Wait for OTP field to appear
        enter_otp()  # Step 3: Enter OTP
        print("Login process completed. Verify on the browser if login was successful.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the script
if __name__ == "__main__":
    main()
