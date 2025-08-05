from selenium.webdriver.common.by import By
import allure

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        with allure.step("open home page"):
            self.driver.get("https://demoblaze.com/")

    def click_iphone_6s(self):
        with allure.step("click_iphone_6s"):
            iphone = self.driver.find_element(By.XPATH, "//a[text()='Iphone 6 32gb']")
            iphone.click()

    def click_monitor(self):
        with allure.step("click button 'monitors'"):
            monitor_link = self.driver.find_element(By.XPATH, "//a[text()='Monitors']")
            monitor_link.click()

    def click_laptops(self):
        with allure.step("click buttin 'laptops'"):
            laptops_link = self.driver.find_element(By.XPATH, "//a[text()='Laptops']")
            laptops_link.click()

    def click_phones(self):
        with allure.step("click button 'phones'"):
            phones_link = self.driver.find_element(By.XPATH, "//a[text()='Phones']")
            phones_link.click()

    def check_product_count(self, count):
        with allure.step("check count product"):
            product_count = self.driver.find_elements(By.CSS_SELECTOR, ".card")
            assert len(product_count) == count

    def click_buton_next(self):
        with allure.step("if product not found, click button 'Next'"):
            button = self.driver.find_element(By.XPATH, "//button[@id='next2' and text()='Next']")
            button.click()

    def search_product(self, product_name):
        with allure.step("search product"):
            locator = f"//a[@class='hrefch' and contains(text(), '{product_name}')]"
            product = self.driver.find_element(By.XPATH, locator)
            product.click()

    # def click_buton_previous(self):
    #     button = self.driver.find_element(By.ID, "prev2")
    #     button.click()

