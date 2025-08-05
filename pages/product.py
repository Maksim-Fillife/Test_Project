from selenium.webdriver.common.by import By
import allure

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def check_title_is(self, title):
        with allure.step("check price"):
            product_title = self.driver.find_element(By.CSS_SELECTOR, "h3")
            assert product_title.text == title

    def check_product_name(self, expected_title):
        with allure.step("check product name"):
            product_title = self.driver.find_element(By.CSS_SELECTOR, "h2")
            assert product_title.text == expected_title