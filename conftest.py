from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pathlib import Path
import pytest
import json


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


# @pytest.fixture
# def test_data():
#     DATA_FILE = Path(r"C:\Users\user\PycharmProjects\Test_Project\resource\test_data.json")
#
#     def load_test_data():
#         with open(DATA_FILE, 'r', encoding='utf-8') as f:
#             return json.load(f)
#
#     return load_test_data()