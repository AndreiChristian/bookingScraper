import requests
from bs4 import BeautifulSoup


def scrape(url, html_element, css_selector, css_identifier, is_nested=False ):

    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # soup.find(html_element, {css_selector: css_identifier}).text

    if is_nested == True:
        anchor_tag = soup.find(html_element, {css_selector: css_identifier})
        return(anchor_tag.find('span').text)
    else :
        return soup.find(html_element, {css_selector: css_identifier}).text

