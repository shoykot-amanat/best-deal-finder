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
        # dismis_signin_popup = self.find_element(By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']")
        # dismis_signin_popup.click()

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

    def select_dates(self, check_in_date, check_out_date):
        self.execute_script("window.scrollBy(0, 400);", "")
        check_in_element = self.find_element(By.CSS_SELECTOR, f"span[data-date='{check_in_date}']")
        # self.execute_script("arguments[0].scrollIntoView(true);", check_in_element)
        check_in_element.click()
        check_out_element = self.find_element(By.CSS_SELECTOR, f"span[data-date='{check_out_date}']")
        # self.execute_script("arguments[0].scrollIntoView(true);", check_out_element)
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element(
            By.CSS_SELECTOR, "span[data-testid='searchbox-form-button-icon']"
        ) # find the fillup button for the adults
        selection_element.click()
        time.sleep(2)
        default_adults = int(self.find_element(
            By.XPATH, "//div[@id=':rf:']//div[@class='a7a72174b8'][1]//span[@class='d723d73d5f']"
        ).text) # find the default number of adults  
        print(default_adults)

        # increase or decrease the number of adults
        # based on the difference between the default number of adults and the desired number of adults

        if default_adults < count:                 
            for _ in range(count - default_adults):
                self.find_element(
                    By.XPATH, "//div[@id=':rf:']//div[@class='a7a72174b8'][1]//button[2]"
                ).click()
        elif default_adults > count:
            for _ in range(default_adults - count):
                self.find_element(
                    By.XPATH, "//div[@id=':rf:']//div[@class='a7a72174b8'][1]//button[1]"
                ).click()

    def search(self):
        search_button = self.find_element(By.CSS_SELECTOR, "button[type='submit']")
        search_button.click()
        