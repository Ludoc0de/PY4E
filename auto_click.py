from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# 1. URL target
URL_TARGET = "https://www.google.com"
URL_LOGIN = "https://accounts.google.com"
USERNAME = "bob"
PASSWORD = "test"
TEXT_TO_SEARCH = "test"
TEXT_TO_CLICK = "affecter"
USERNAME_SELECTOR_BY = By.NAME
USERNAME_SELECTOR_VALUE = "username"
PASSWORD_SELECTOR_BY = By.NAME
PASSWORD_SELECTOR_VALUE = "password"
SUCCESS_ELEMENT_SELECTOR_BY = By.CLASS_NAME
SUCCESS_ELEMENT_VALUE = ""  # A class name of an element that is present only when login is successful (to be defined)
PROFILE_PATH = r""  # Path to your Chrome profile

# 2. Init the webdriver
try:
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # Add specific user
    options.add_argument(f"user-data-dir={PROFILE_PATH}")
    driver = webdriver.Chrome(service=service, options=options)
    print("Browser started successfully with persistant user.")
except Exception as e:
    print(f"Error when starting the driver : {e}")
    # Exit if initialization is critical
    exit()

# 3. Open the web page
driver.get(URL_TARGET)
print(f"Open the URL : {URL_TARGET}")

# Optionnel : Wait a moment for the page load
time.sleep(5)

if URL_LOGIN in driver.current_url:
    print(
        f"Redirection vers la page de connexion ({driver.current_url}) détectée. Tentative d'authentification..."
    )

    try:
        # Attendre que le champ de saisie du nom d'utilisateur soit visible (max 15 secondes)
        username_field = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (USERNAME_SELECTOR_BY, USERNAME_SELECTOR_VALUE)
            )
        )

        # Saisir le nom d'utilisateur
        username_field.send_keys(USERNAME)
        print(f"Nom d'utilisateur '{USERNAME}' saisi.")

        # Appuyer sur Entrée
        username_field.send_keys(Keys.ENTER)
        print("Touche Entrée simulée.")

    except TimeoutException:
        print(
            f"❌ Échec: Le champ Nom d'utilisateur ({USERNAME_SELECTOR_BY}: {USERNAME_SELECTOR_VALUE}) n'a pas été trouvé à temps."
        )
        driver.quit()
        exit()

    try:
        # Attendre que le champ de saisie du nom d'utilisateur soit visible (max 15 secondes)
        password_field = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (PASSWORD_SELECTOR_BY, PASSWORD_SELECTOR_VALUE)
            )
        )

        # Saisir le nom d'utilisateur
        password_field.send_keys(PASSWORD)
        print(f"Mot de passe utilisateur saisi.")

        # Appuyer sur Entrée
        password_field.send_keys(Keys.ENTER)
        print("Touche Entrée simulée.")

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (SUCCESS_ELEMENT_SELECTOR_BY, SUCCESS_ELEMENT_VALUE)
            )
        )
        print("Connexion réussie ! L'élément de succès a été trouvé.")

    except TimeoutException:
        print(
            f"❌ Échec: Le champ Mot de passe ({PASSWORD_SELECTOR_BY}: {PASSWORD_SELECTOR_VALUE}) n'a pas été trouvé à temps."
        )
        driver.quit()
        exit()

    except Exception as e:
        print(f"Erreur lors de l'étape de connexion : {e}")
        driver.quit()
        exit()
else:
    print("Pas de redirection immédiate vers la page de login, poursuite...")


# 4. Look for the link containing the word target

ALL_CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÛÜÝ"
ALL_LOWER = "abcdefghijklmnopqrstuvwxyzàáâãäåçèéêëìíîïñòóôõöùúûüý"

# xpath_link = f"//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVXXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{TEXT_TO_SEARCH}')]"
xpath_link = f"//a[contains(translate(normalize-space(.), '{ALL_CAPS}', '{ALL_LOWER}'), '{TEXT_TO_SEARCH}')]"

print(f"Look for the link with the text : '{TEXT_TO_SEARCH}'...")

try:
    # try to find the first element equal to XPath
    link_to_click = driver.find_element(By.XPATH, xpath_link)

    # 5. If found, click on it
    print(f"Link found ! Click on it : {link_to_click.text}")
    link_to_click.click()
    print("Click, The browser navigate to the new page.")

    time.sleep(5)

except NoSuchElementException:
    print(f"❌ Link containing the text '{TEXT_TO_SEARCH}' not found on the page.")

# 6. Look for the link affectation
xpath_affectation = f"//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVXXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{TEXT_TO_CLICK}')]"
print(f"Look for the link with the text : '{TEXT_TO_CLICK}'...")

try:
    # try to find the first element equal to XPath
    link_to_click = driver.find_element(By.XPATH, xpath_affectation)

    print(f"Link found ! Click on it : {link_to_click.text}")
    link_to_click.click()
    print("Click, The browser navigate to the new page.")

    time.sleep(5)

except NoSuchElementException:
    print(f"❌ Link containing the text '{TEXT_TO_CLICK}' not found on the page.")

except Exception as e:
    print(f"An error occurred while clicking: {e}")

finally:
    # 6. Close the browser (very important not to leave open processes)
    driver.quit()
    print("Script finished and browser closed.")
