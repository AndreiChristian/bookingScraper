import UTILS.testScraper
import UTILS.sort
import UTILS.linear

red_cli = "\033[31m"
green_cli = "\033[32m"
blue_cli = "\033[34m"
yellow_cli = "\033[33m"
reset_cli = "\033[0m"


def cli(hotels):
    userIsActive = True
    print()
    print(f"{blue_cli}Welcome to pyStay. The number one hotel price generator. Our machine learning models and datasets will help you get the vacation of your dream at a great discount!")
    print()
    while userIsActive:
        print(f"{yellow_cli}Select what would you like to do:")
        print(f"{reset_cli}1. Scrape some more data!")
        print(f"{reset_cli}2. Generate a linear regression:")
        print(f"{red_cli}q. Quit:")
        user_response = input(f"{reset_cli}Your choice (1/2/q): ")
        if user_response == "1":
            print()
            UTILS.testScraper.scrapeHotels(hotels=hotels)
            UTILS.sort.sortData()
            print()
            print(f"{green_cli}Hotel data fetched successfully!")
            print()

        elif user_response == "2":
            print()
            print(f"{blue_cli}Choose a room type{reset_cli}")
            print()
            print("1. Standard Room")
            print("2. Superior Room")
            print("3. Junior Suite")
            print("4. Suite")
            print()
            room_type_chosen = input("Your choice: 1/2/3/4/q: ")

            if room_type_chosen == "1":
                UTILS.linear.make_linear_regression("Standard")
            elif room_type_chosen == "2":
                UTILS.linear.make_linear_regression("Superior")
            elif room_type_chosen == "3":
                UTILS.linear.make_linear_regression("Junior Suite")
            elif room_type_chosen == "4":
                UTILS.linear.make_linear_regression("Suite")
            else:
                pass
        elif user_response == "q":
            print()
            print("See u later!")
            print()
            userIsActive = False
        else:
            print(f"{blue_cli}Choose one of the next options: 1/2/q")
