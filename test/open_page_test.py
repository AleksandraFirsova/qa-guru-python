def test_github_open(driver):
    url = "https://github.com/"
    driver.get(url)

    assert "GitHub" in driver.title
    assert driver.current_url == url


def test_selenium_open(driver):
    url = "https://www.selenium.dev/"
    driver.get(url)

    assert "Selenium" in driver.title
    assert driver.current_url == url
