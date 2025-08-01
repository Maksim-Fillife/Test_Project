from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://demoblaze.com/")

    def click_iphone_6s(self):
        iphone = self.driver.find_element(By.XPATH, "//a[text()='Iphone 6 32gb']")
        iphone.click()

    def click_monitor(self):
        monitor_link = self.driver.find_element(By.XPATH, "//a[text()='Monitors']")
        monitor_link.click()

    def click_laptops(self):
        laptops_link = self.driver.find_element(By.XPATH, "//a[text()='Laptops']")  # находим категорию ноутбуки
        laptops_link.click()

    def click_phones(self):
        phones_link = self.driver.find_element(By.XPATH, "//a[text()='Phones']")  # находим категорию смартфоны
        phones_link.click()

    def check_product_count(self, count):
        monitor_count = self.driver.find_elements(By.CSS_SELECTOR, ".card")
        assert len(monitor_count) == count