from selenium import webdriver


def test_google_search():
    driver = webdriver.Chrome()
    url = "https://www.google.com/"
    driver.get(url)

    assert driver.title == "Google"
    assert driver.current_url == url
