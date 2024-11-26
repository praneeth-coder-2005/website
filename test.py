from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def bypass_telegram_link(url):
    """
    Uses Selenium to open the provided URL, follow all redirections, and locate the Telegram file button.
    """
    # Configure Selenium WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Replace with the path to your ChromeDriver
    driver_path = "/path/to/chromedriver"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        print(f"Opening URL: {url}")
        driver.get(url)
        time.sleep(5)  # Wait for the page to load and redirections to complete

        # Locate the Telegram file button (adjust the selector as needed)
        button = driver.find_element(By.XPATH, "//a[contains(@href, 'telegram')]")
        if button:
            final_url = button.get_attribute("href")
            print(f"Bypassed URL: {final_url}")
            return final_url
        else:
            print("Telegram file button not found.")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        driver.quit()

def main():
    print("Welcome to the Telegram File Button Bypasser")
    input_url = input("Enter the URL: ").strip()
    result = bypass_telegram_link(input_url)
    if result:
        print(f"Final URL: {result}")
    else:
        print("Could not bypass the link.")

if __name__ == "__main__":
    main()
