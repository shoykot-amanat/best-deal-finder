from booking.booking import Booking
import time

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='EUR')
    bot.select_place_to_go('New York')
    time.sleep(5)
    