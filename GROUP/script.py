import UTILS.testScraper

hotels = [
    #   mandarin oriental
    {"name": ["Mandarin Oriental"],
     "url": "mandarin-oriental-geneva", "roomTypes": [], "roomPrices":[]},
    #   four seasons
    {"name": ["Four Seasons Geneva"],
     "url": "four-seasons-geneva", "roomTypes": [], "roomPrices":[]},
    #   Hotel d'Angleterre
    {"name": ["Hotel d'Angleterre"],
     "url": "d-angleterre", "roomTypes": [], "roomPrices":[]},
    #   intercontinental-geneve
    {"name": ["Intercontinental Geneve"],
     "url": "intercontinental-geneve", "roomTypes": [], "roomPrices":[]},
    #   de-la-paix-ritz-carlton
    {"name": ["Ritz Carlton Hotel de la Paix"],
     "url": "de-la-paix-ritz-carlton", "roomTypes": [], "roomPrices":[]},
    #   Beau Rivage Geneva
    {"name": ["Beau Rivage Geneva"],
     "url": "beaurivagegeneva", "roomTypes": [], "roomPrices":[]},
    #   Fairmont Hotel
    {"name": ["Fairmont Hotel"], "url": "grand-kempinski-geneva",
        "roomTypes": [], "roomPrices":[]},
    # Hotel Metropole Geneva
    {"name": ["Metropole Geneva"], "url": "metropolegeneve",
        "roomTypes": [], "roomPrices":[]},
    # the-woodward
    {"name": ["The Woodward"],
     "url": "the-woodward",
        "roomTypes": [], "roomPrices":[]},

]

UTILS.testScraper.scrapeHotels(hotels=hotels)
