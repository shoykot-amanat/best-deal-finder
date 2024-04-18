import booking.constants as const
from selenium import webdriver


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        super(Booking, self).__init__()
        self.teardown = teardown

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
        self.maximize_window()