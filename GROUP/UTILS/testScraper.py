import requests
from bs4 import BeautifulSoup

target_url = "https://www.booking.com/hotel/ch/montreuxpalace.en-gb.html?checkin=2023-04-18&checkout=2023-04-19&group_adults=2&group_children=0&no_rooms=1&selected_currency=EUR"

headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

response = requests.get(target_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# soup.find(html_element, {css_selector: css_identifier}).text


first_container = soup.find("tr", {"data-block-id": "6509831_368480097_2_2_0"})

room_name = first_container.find(
    "span", {"class": "hprt-roomtype-icon-link"}).text

room_price = first_container.find(
    "span", {"class": "prco-valign-middle-helper"}).text


second_container = soup.find(
    "tr", {"data-block-id": "6509804_368480097_2_2_0"})

second_room_name = second_container.find(
    "span", {"class": "hprt-roomtype-icon-link"}).text

second_room_price = second_container.find(
    "span", {"class": "prco-valign-middle-helper"}).text

print(room_name,room_price, second_room_name, second_room_price)

# 6509805_368480097_2_2_0
