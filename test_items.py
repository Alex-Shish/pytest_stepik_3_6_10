import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_find_add_to_card(browser):
    browser.get(link)
    time.sleep(3)
    assert browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket').is_displayed(), \
        'Кнопка добавления товара в корзину отсутсвует'
