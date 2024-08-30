import json
import deathbycaptcha
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

USERNAME = os.environ['DEATHBYCAPTCHA_USER']
PASSWORD = os.environ['DEATHBYCAPTCHA_PASSWORD']

def get_sitekey(driver):
    script_content = driver.find_element(By.XPATH, "/html/body/div[2]/div/script[2]").get_attribute("innerHTML")
    sitekey_match = re.search(r"'sitekey'\s*:\s*'([^']+)'", script_content)
    if sitekey_match:
        return sitekey_match.group(1)
    return None

def handle_captcha(driver, wait):
    try:
        print("Getting reCAPTCHA sitekey...")
        sitekey = get_sitekey(driver)
        if not sitekey:
            raise Exception("Sitekey not found.")

        url = driver.current_url

        print("Solving captcha...")
        client = deathbycaptcha.HttpClient(USERNAME, PASSWORD)
        captcha_payload = {
            'googlekey': sitekey,
            'pageurl': url,
        }
        json_captcha_payload = json.dumps(captcha_payload)
        captcha = client.decode(type=4, token_params=json_captcha_payload)
        
        if captcha:
            print(f"CAPTCHA solved: {captcha['text']}")
            g_recaptcha_response = wait.until(EC.presence_of_element_located((By.ID, "g-recaptcha-response")))
            driver.execute_script(f"arguments[0].innerHTML = '{captcha['text']}';", g_recaptcha_response)
            print("Captcha injected successfuly!")

            balance = client.get_balance()
            print(f"Death by Captcha balance: {balance}")

    except TimeoutException:
        print("CAPTCHA not detected, continuing...")
    finally:
        driver.switch_to.default_content()
