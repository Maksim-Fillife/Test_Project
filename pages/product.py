from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def check_title_is(self, title):
        product_title = self.driver.find_element(By.CSS_SELECTOR, "h3")
        assert product_title.text == title