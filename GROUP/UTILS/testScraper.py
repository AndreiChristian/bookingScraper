# import requests
# from bs4 import BeautifulSoup
# import time
# import csv
# from datetime import datetime

# now = datetime.now()  # get the current date and time
# # format the date and time as a string
# time_str = now.strftime("%Y-%m-%d %H:%M:%S")


# headers = {
#     "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}


# def getUrl(hotel_url):
#     return f"https://www.booking.com/hotel/ch/{hotel_url}.en-gb.html?checkin=2023-04-18&checkout=2023-04-19&group_adults=2&group_children=0&no_rooms=1&selected_currency=EUR"


# def scrapeHotels(hotels):

#     print("Fetching hotels data started!")

#     with open("./example.csv", mode='a', newline='') as csv_file:
#         writer = csv.writer(csv_file)

#     for hotel in hotels:
#         response = requests.get(
#             getUrl(hotel_url=hotel["url"]), headers=headers)
#         soup = BeautifulSoup(response.text, "html.parser")

#         tr_arr = soup.find_all("tr")

#         for tr in tr_arr:

#             room_name = tr.find("span", {"class": "hprt-roomtype-icon-link"})
#             room_price = tr.find(
#                 "span", {"class": "prco-valign-middle-helper"})

#             if (room_price != None) & (room_name != None):
#                 hotel["roomTypes"].append(room_name.text.strip())
#                 hotel["roomPrices"].append(room_price.text[3:].strip())
#                 writer.writerow(
#                     [time_str, hotel["name"], room_name.text.strip(), room_price.text[3:].strip()])

#         print(f"Fetched data for {hotel['name']}")

import requests
from bs4 import BeautifulSoup
import time
import csv
from datetime import datetime

now = datetime.now()  # get the current date and time
# format the date and time as a string
time_str = now.strftime("%Y-%m-%d %H:%M:%S")


headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}


def getUrl(hotel_url):
    return f"https://www.booking.com/hotel/ch/{hotel_url}.en-gb.html?checkin=2023-04-18&checkout=2023-04-19&group_adults=2&group_children=0&no_rooms=1&selected_currency=EUR"


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
                    hotel["roomTypes"].append(room_name.text.strip())
                    hotel["roomPrices"].append(room_price.text[3:].strip())
                    writer.writerow(
                        [time_str, hotel["name"], room_name.text.strip(), room_price.text[3:].strip()])

            print(f"Fetched data for {hotel['name']}")
