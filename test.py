import pyautogui
import time
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("hotstar_login.log"),
        logging.StreamHandler()
    ]
)

# Ensure DISPLAY is set for headless environments
if 'DISPLAY' not in os.environ:
    logging.warning("DISPLAY environment variable is not set. Setting it to ':1'.")
    os.environ['DISPLAY'] = ':1'


# Open Hotstar manually or with browser
def open_hotstar():
    logging.info("Opening Hotstar login page...")
    # Replace with your preferred way to open the browser
    os.system("firefox https://www.hotstar.com/in &")  # Opens in Firefox
    time.sleep(10)  # Wait for the browser to load


# Input the mobile number
def enter_mobile_number():
    mobile_number = input("Enter your mobile number: ")
    logging.info(f"Entering mobile number: {mobile_number}")
    pyautogui.click(500, 500)  # Adjust coordinates for the mobile input field
    time.sleep(1)
    pyautogui.typewrite(mobile_number)
    pyautogui.press("enter")
    logging.info("Mobile number entered. Waiting for OTP screen...")


# Input the OTP
def enter_otp():
    otp = input("Enter the OTP received: ")
    logging.info(f"Entering OTP: {otp}")
    pyautogui.typewrite(otp)
    pyautogui.press("enter")
    logging.info("OTP entered. Waiting for login confirmation...")

    # Check for success or error on screen
    time.sleep(5)
    if pyautogui.locateOnScreen("success_indicator.png", confidence=0.8):
        logging.info("Login successful!")
    elif pyautogui.locateOnScreen("error_indicator.png", confidence=0.8):
        logging.error("Login failed. Incorrect OTP or other issue.")
    else:
        logging.warning("Could not confirm login status. Check manually.")


# Main function
def main():
    try:
        open_hotstar()
        time.sleep(2)
        enter_mobile_number()
        time.sleep(10)  # Wait for OTP screen
        enter_otp()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.debug("Script execution completed.")


if __name__ == "__main__":
    main()
