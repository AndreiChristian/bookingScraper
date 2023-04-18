import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

hotels = [
    #   mandarin oriental
    {"name": "Mandarin Oriental",
     "url": "mandarin-oriental-geneva", "roomInfo": []},
    #   four seasons
    {"name": "Four Seasons Geneva",
     "url": "four-seasons-geneva", "roomInfo": []},
    #   Hotel d'Angleterre
    {"name": "Four Seasons Geneva",
     "url": "d-angleterre", "roomInfo": []},
    #   intercontinental-geneve
    {"name": "Intercontinental Geneve",
     "url": "intercontinental-geneve", "roomInfo": []},
    #   de-la-paix-ritz-carlton
    {"name": "Ritz Carlton Hotel de la Paix",
     "url": "de-la-paix-ritz-carlton", "roomInfo": []},
    #   Beau Rivage Geneva
    {"name": "Beau Rivage Geneva",
     "url": "beaurivagegeneva", "roomInfo": []},
    #   Fairmont Hotel
    {"name": "Fairmont Hotel", "url": "grand-kempinski-geneva", "roomInfo": []},
    # Hotel Metropole Geneva
    {"name": "Metropole Geneva", "url": "metropolegeneve", "roomInfo": []},
    # the-woodward
    {"name": "The Woodward", "url": "the-woodward", "roomInfo": []},

]


def getUrl(hotel_url):
    return f"https://www.booking.com/hotel/ch/{hotel_url}.en-gb.html?checkin=2023-04-18&checkout=2023-04-19&group_adults=2&group_children=0&no_rooms=1&selected_currency=EUR"


for hotel in hotels:
    response = requests.get(getUrl(hotel_url=hotel["url"]), headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    tr_arr = soup.find_all("tr")

    for tr in tr_arr:

        room_name = tr.find("span", {"class": "hprt-roomtype-icon-link"})
        room_price = tr.find("span", {"class": "prco-valign-middle-helper"})

        if (room_price != None) & (room_name != None):
            hotel["roomInfo"].append(
                {room_name.text.strip(): room_price.text[3:].strip()})

for hotel in hotels:
    print(hotel["name"])
    print(hotel["roomInfo"])
    print("_"*20)
