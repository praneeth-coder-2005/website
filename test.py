import logging
import pyautogui

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("test.log"),  # Save logs to a file
        logging.StreamHandler()          # Also print logs to console
    ]
)

# Start logging
logging.debug("Script has started successfully.")

# Test PyAutoGUI
try:
    # Debugging info
    logging.info("Initializing PyAutoGUI...")

    # Move the mouse as a test
    pyautogui.FAILSAFE = False  # Disable failsafe
    logging.info("Moving mouse to (100, 100)...")
    pyautogui.moveTo(100, 100, duration=1)

    # Perform additional PyAutoGUI actions
    logging.info("Clicking at (100, 100)...")
    pyautogui.click(100, 100)

    logging.info("Typing text...")
    pyautogui.typewrite("Hello, PyAutoGUI is working!", interval=0.1)

    logging.info("Script completed successfully.")

except Exception as e:
    # Log any errors that occur
    logging.error(f"An error occurred: {e}")
    print(f"Error: {e}")

# Ensure script completion message
logging.debug("Script has finished execution.")
