import UTILS.testScraper

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
    # Hotel Metropole Geneva
    {"name": "Metropole Geneva", "url": "metropolegeneve",
        "standard": 0, "superior": 0, "junior": 0, "suite": 0},
    # the-woodward
    {"name": "The Woodward",
     "url": "the-woodward",
        "standard": 0, "superior": 0, "junior": 0, "suite": 0},
]

UTILS.testScraper.scrapeHotels(hotels=hotels)
