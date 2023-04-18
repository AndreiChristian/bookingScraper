standard_room_types = [
    "River View Queen Room",
    "Standard King Room",
    "Classic Queen Room",
    "Classic Room",
    "Classic Garden View, Guest room, 1 King, Garden view",
    "Deluxe Ville View",
    "Fairmont Double Room with Partial Lake View"
]

superior_room_types = [
    "Deluxe Twin Room",
    "Superior Room with King Bed",
    "Exclusive King Room with Lake View",
    "Premium Room",
    "Deluxe Lake View, Guest room, 1 King, Lake view",
    "Premier Ville View",
    "Signature Double Room with Lake View"
]

junior_suites_room_types = [
    "Mandarin Junior Suite King",
    "Four Seasons Junior Suite King Bed",
    "Junior Suite with Lake View",
    "One bedroom Suite",
    "Lake Front Junior Suite, Suite, 1 King, Lake Front view",
    "Junior Suite Lake Panorama",
    "Junior Suite with Courtyard View"
]

suite_room_types = [
    "Family Suite Queen",
    "Four Seasons Loft Executive King Suite",
    "Presidential Suite with Lake View",
    "Panoramic Suite with Lake View",
    "Lake Front Suite, 1 Bedroom Suite, 1 King, Sofa bed, Balcony",
    "Penthouse Lake View",
    "Executive Suite"
]


def format_room_type(room_name):
    if room_name in standard_room_types:
        return "standard"
    elif room_name in superior_room_types:
        return "superior"
    elif room_name in junior_suites_room_types:
        return "junior"
    elif room_name in suite_room_types:
        return "suite"
    else:
        return False
