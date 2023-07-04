from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button(browser):
    browser.get(link)
    time.sleep(30)  # Визуально смотрим, что сайт на правильном языке
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")  # Проверяем, что не False

