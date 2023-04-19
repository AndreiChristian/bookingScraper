import UTILS.testScraper
import UTILS.sort
import UTILS.gui

# a list of dictionaries that hold the data necessary to pass the info to the scraper
# the url holds a dynamic url segment in order to scrape the data from the right website
# standard, supeior, junior and suite will hold the prices for the according room type.
# In order to fit the room type in these categories, the testScraper file calls the fmt function,
# from the ./UTILS/fmt.py

hotels = [
    #   mandarin oriental
    {"name": "Mandarin Oriental",
     "url": "mandarin-oriental-geneva", "standard": 0, "superior": 0, "junior": 0, "suite": 0},
    #   four seasons
    {"name": "Four Seasons Geneva",
     "url": "four-seasons-geneva", "standard": 0, "superior": 0, "junior": 0, "suite": 0},
    #   Hotel d'Angleterre
    {"name": "Hotel d'Angleterre",
     "url": "d-angleterre", "standard": 0, "superior": 0, "junior": 0, "suite": 0},
    #   intercontinental-geneve
    {"name": "Intercontinental Geneve",
     "url": "intercontinental-geneve", "standard": 0, "superior": 0, "junior": 0, "suite": 0},
    #   de-la-paix-ritz-carlton
    {"name": "Ritz Carlton Hotel de la Paix",
     "url": "de-la-paix-ritz-carlton", "standard": 0, "superior": 0, "junior": 0, "suite": 0},
    #   Beau Rivage Geneva
    {"name": "Beau Rivage Geneva",
     "url": "beaurivagegeneva", "standard": 0, "superior": 0, "junior": 0, "suite": 0},
    #   Fairmont Hotel
    {"name": "Fairmont Hotel", "url": "grand-kempinski-geneva",
        "standard": 0, "superior": 0, "junior": 0, "suite": 0},
]

# a function that scrapes the hotel data, get the room rates and add the raw data to example.csv the and the sorted data to mydata_sorted.csv
UTILS.testScraper.scrapeHotels(hotels=hotels)

# a function that sorts the data from the example.csv and sorts it asscendingly by "name" column
UTILS.sort.sortData()
