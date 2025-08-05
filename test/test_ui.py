import time
from utils.product_selection import ProductSelection
from pages.homepage import HomePage
from pages.product import ProductPage
import allure


@allure.feature("product search")
@allure.story("search and check price iphone 6s")
def test_ui_open_iphone_6s_price(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_iphone_6s()
    time.sleep(2)
    product_page = ProductPage(driver)
    product_page.check_title_is("$790 *includes tax")

@allure.feature("product search")
@allure.story("check count monitors")
def test_ui_count_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)
    homepage.check_product_count(2)

@allure.feature("product search")
@allure.story("check count laptops")
def test_ui_count_laptops(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_laptops()
    time.sleep(2)
    homepage.check_product_count(6)

@allure.feature("product search")
@allure.story("check count phones")
def test_ui_cout_phones(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_phones()
    time.sleep(2)
    homepage.check_product_count(7)

@allure.feature("product search")
@allure.story("select random product")
def test_ui_open_random_product(driver, test_data):
    product_selection = ProductSelection(test_data)
    product_name = product_selection.select_random_product()
    homepage = HomePage(driver)
    homepage.open()
    time.sleep(2)

    found = False
    while not found:
        try:
            homepage.search_product(product_name)
            time.sleep(2)
            product_page = ProductPage(driver)
            product_page.check_product_name(product_name)
            found = True

        except:
            try:
                homepage.click_buton_next()
                time.sleep(2)
            except:
                break
    assert found, f"Product {product_name} not found"