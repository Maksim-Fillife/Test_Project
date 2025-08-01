#from selenium.webdriver.common.by import By
#import random
import time
from pages.homepage import HomePage
from pages.product import ProductPage



def test_ui_open_iphone_6s_price(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_iphone_6s()
    time.sleep(2)
    product_page = ProductPage(driver)
    product_page.check_title_is("$790 *includes tax")

def test_ui_count_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)
    homepage.check_product_count(2)

def test_ui_count_laptops(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_laptops()
    time.sleep(2)
    homepage.check_product_count(6)

def test_ui_cout_phones(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_phones()
    time.sleep(2)
    homepage.check_product_count(7)


# def test_ui_open_random_product(driver, test_data):
#     product = test_data['products']
#     product_name = random.choice(product)
#     print(f"{product_name}")
#     driver.get("https://demoblaze.com/")
#     time.sleep(2)
#
#     found = False
#
#     while not found:
#         try:
#             product_link = driver.find_element(By.XPATH, f"//a[text()='{product_name}'] ")
#             product_link.click()
#             time.sleep(2)
#             driver.find_element(By.CSS_SELECTOR, "h2")
#             found = True
#
#         except:
#             try:
#                 next_page = driver.find_element(By.CSS_SELECTOR, "[id='next2']")
#                 next_page.click()
#                 time.sleep(2)
#             except:
#                 break
#     assert found, f"Product {product_name} not found"