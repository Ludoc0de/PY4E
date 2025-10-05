from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# 1. URL target
URL_TARGET = "https://www.google.com"
TEXT_TO_SEARCH = "test"

# 2. Init the webdriver
try:
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    print("Browser started successfully.")
except Exception as e:
    print(f"Error when starting the driver : {e}")
    # Exit if initialization is critical
    exit()

# 3. Open the web page
driver.get(URL_TARGET)
print(f"Open the URL : {URL_TARGET}")

# Optionnel : Wait a moment for the page load
import time

time.sleep(5)

# 4. Look for the link containing the word target

xpath_lien = f"//a[contains(text(), '{TEXT_TO_SEARCH}')]"
print(f"Look for the link with the text : '{TEXT_TO_SEARCH}'...")

try:
    # try to find the first element equal to XPath
    link_to_click = driver.find_element(By.XPATH, xpath_lien)

    # 5. If found, click on it
    print(f"Link found ! Click on it : {link_to_click.text}")
    link_to_click.click()
    print("Click, The browser navigate to the new page.")

    time.sleep(5)

except NoSuchElementException:
    print(f"❌ Link containing the text '{TEXT_TO_SEARCH}' not found on the page.")

except Exception as e:
    print(f"An error occurred while clicking: {e}")

finally:
    # 6. Close the browser (very important not to leave open processes)
    driver.quit()
    print("Script finished and browser closed.")
