import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        super(Booking, self).__init__()
        self.teardown = teardown
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
        dismis_signin_popup = self.find_element(By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']")
        dismis_signin_popup.click()

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.XPATH, "//span[contains(text(),'BDT')]")
        currency_element.click()
        selected_currency_element = self.find_element(
            By.XPATH, f"//div[@data-testid='Suggested for you']//div[contains(@class,'ea1163d21f')][normalize-space()='{currency}']"
        )
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, ":re:")
        search_field.clear()
        search_field.send_keys(place_to_go)
        time.sleep(2)
        first_result = self.find_element(By.ID, "autocomplete-result-0")
        first_result.click()
        