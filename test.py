import pyautogui
import time
import os
import logging
import webbrowser

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("hotstar_login.log"),
        logging.StreamHandler()
    ]
)

# Ensure DISPLAY is set for Xvfb (for headless environments)
if 'DISPLAY' not in os.environ:
    logging.warning("DISPLAY environment variable is not set. Setting it to ':1'.")
    os.environ['DISPLAY'] = ':1'

# Open Hotstar in the browser
def open_hotstar():
    logging.info("Opening Hotstar login page...")
    webbrowser.open("https://www.hotstar.com/in")  # Opens Hotstar website
    time.sleep(5)  # Wait for the browser to load

# Input mobile number
def enter_mobile_number():
    mobile_number = input("Enter your mobile number: ")  # Get mobile number from user
    logging.info(f"Entering mobile number: {mobile_number}")
    pyautogui.click(500, 500)  # Adjust coordinates to click the input field
    time.sleep(1)
    pyautogui.typewrite(mobile_number)
    pyautogui.press("enter")
    logging.info("Mobile number entered. Waiting for OTP...")

# Input OTP
def enter_otp():
    otp = input("Enter the OTP received: ")  # Get OTP from user
    logging.info(f"Entering OTP: {otp}")
    pyautogui.typewrite(otp)
    pyautogui.press("enter")
    logging.info("OTP entered. Logging in...")

# Main function
def main():
    try:
        open_hotstar()
        time.sleep(2)
        enter_mobile_number()
        time.sleep(10)  # Wait for OTP screen to load
        enter_otp()
        logging.info("Login successful!")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.debug("Script execution completed.")

# Run the script
if __name__ == "__main__":
    main()
