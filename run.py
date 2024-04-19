from booking.booking import Booking
import time

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='USD')
    bot.select_place_to_go('New York')
    bot.select_dates(check_in_date='2024-04-22', 
                     check_out_date='2024-04-25')
    bot.select_adults(count=10)
    bot.search()
    time.sleep(5)
    