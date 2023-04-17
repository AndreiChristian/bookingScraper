import requests
from bs4 import BeautifulSoup

l = []
g = []

hotel = {}
k = {}

fac = []

fac_arr = []

# setting the headers f
headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}


target_url = "https://www.booking.com/hotel/ch/montreuxpalace.en-gb.html?checkin=2023-04-18&checkout=2023-04-19&group_adults=2&group_children=0&no_rooms=1&selected_currency=EUR"
response = requests.get(target_url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')


# hp_address_subtitle
# js-hp_address_subtitle
# jq_tooltip


hotel["name"] = soup.find("h2", {"class": "d2fee87262 pp-header__title"})

print(hotel["name"])

hotel["adress"] = soup.find("h2", {"class": "d2fee87262 pp-header__title"})

