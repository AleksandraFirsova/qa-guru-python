from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_google_search(driver):
    url = "https://www.google.com/"
    driver.get(url)
    search_string = "pytest selenium"

    assert driver.title == "Google"
    assert driver.current_url == url

    element = driver.find_element(By.NAME, "q")
    element.send_keys(search_string)
    element.submit()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#search"))
    )

    assert search_string in driver.page_source
