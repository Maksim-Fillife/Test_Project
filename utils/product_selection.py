import random
import allure

class ProductSelection:
    def __init__(self, test_data):
        self.test_data = test_data
        self.selected_product = None

    def select_random_product(self):
        with allure.step("select a random product from the list"):
            products = self.test_data['products']
            self.selected_product = random.choice(products)
            print(f"Выбран продукт: {self.selected_product}")
            return self.selected_product