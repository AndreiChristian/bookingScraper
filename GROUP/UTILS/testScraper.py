from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import time
import csv
from datetime import datetime
import UTILS.fmt

now = datetime.now()  # get the current date and time
# format the date and time as a string
time_str = now.strftime("%Y-%m-%d %H:%M:%S")


# Get the current date
current_date = datetime.now()

# Calculate the next day's date by adding one day to the current date
next_day = current_date + timedelta(days=1)

# Format the current and next day's dates in 'yyyy-mm-dd' format
formatted_current_date = current_date.strftime('%Y-%m-%d')
formatted_next_day = next_day.strftime('%Y-%m-%d')


headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}


def getUrl(hotel_url):
    return f"https://www.booking.com/hotel/ch/{hotel_url}.en-gb.html?checkin={formatted_current_date}&checkout={formatted_next_day}&group_adults=2&group_children=0&no_rooms=1&selected_currency=EUR"


def scrapeHotels(hotels):

    print("Fetching hotels data started!")

    with open("./example.csv", mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        for hotel in hotels:
            response = requests.get(
                getUrl(hotel_url=hotel["url"]), headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")

            tr_arr = soup.find_all("tr")

            for tr in tr_arr:

                room_name = tr.find(
                    "span", {"class": "hprt-roomtype-icon-link"})
                room_price = tr.find(
                    "span", {"class": "prco-valign-middle-helper"})

                if (room_price != None) & (room_name != None):

                    is_room_name_ok = UTILS.fmt.format_room_type(
                        room_name=room_name.text.strip())

                    if is_room_name_ok:
                        hotel[is_room_name_ok] = room_price.text

            writer.writerow(
                [time_str, hotel["name"], hotel["standard"], hotel["superior"], hotel["junior"], hotel["suite"]])

            print(f"Fetched data for {hotel['name']}")
