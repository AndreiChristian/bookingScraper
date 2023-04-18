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

hotel["name"] = soup.find("h2", {"class": "d2fee87262 pp-header__title"}).text

print(hotel["name"])

hotel["adress"] = soup.find("span", {"class": "hp_address_subtitle"}).text

print(hotel["adress"])

# fc63351294 a168c6f285 d1c4779e7a js-legacy-room-name a25b1d9e47

hotel["category_one"] = soup.find("span", {"class": "hp_address_subtitle"}).text




