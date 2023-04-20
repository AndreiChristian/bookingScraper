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
        print(
            f"{yellow_cli}Select your language (1/2/3) :")
        print()
        print(f"{reset_cli}1. English")
        print(f"{reset_cli}2. Russian")
        print(f"{reset_cli}3. Arabic")
        print
        selected_language = input("Your choice (1/2/3) : ")
        print()

        if selected_language == "1":
            print(f"{yellow_cli}Select what would you like to do:")
            print(f"{reset_cli}1. Scrape some more data!")
            print(f"{reset_cli}2. Generate a linear regression:")
            print(f"{red_cli}q. Quit:")
            user_response = input(f"{reset_cli}Your choice (1/2/q): ")
        if selected_language == "2":
            print(f"{yellow_cli}Выберите, что вы хотели бы сделать:")
            print(f"{reset_cli}1. Собрать еще больше данных!")
            print(f"{reset_cli}2. Создать линейную регрессию:")
            print(f"{red_cli}q. Выйти:")
            user_response = input(f"{reset_cli}Ваш выбор (1/2/q): ")
        if selected_language == "3":
            print(f"{yellow_cli}اختر ما تريد أن تفعل:")
            print(f"{reset_cli}1. جمع المزيد من البيانات!")
            print(f"{reset_cli}2. إنشاء انحدار خطي:")
            print(f"{red_cli}q. إنهاء:")
            user_response = input(f"{reset_cli}اختيارك (1/2/q): ")

        if user_response == "1":
            print()
            UTILS.testScraper.scrapeHotels(
                selected_language=selected_language, hotels=hotels)
            UTILS.sort.sortData()
            print()
            if selected_language == "1":
                print(f"{green_cli}Hotel data fetched successfully!")
            elif selected_language == "2":
                print(f"{green_cli}Данные об отеле успешно получены!")
            elif selected_language == "3":
                print(f"{green_cli}تم جلب بيانات الفندق بنجاح!")
            print()

        elif user_response == "2":

            if selected_language == "1":
                print()
                print(f"{blue_cli}Choose a room type{reset_cli}")
                print()
                print("1. Standard Room")
                print("2. Superior Room")
                print("3. Junior Suite")
                print("4. Suite")
                print()
                room_type_chosen = input("Your choice: 1/2/3/4/q: ")
            elif selected_language == "2":
                print()
                print(f"{blue_cli}Выберите тип номера{reset_cli}")
                print()
                print("1. Стандартный номер")
                print("2. Улучшенный номер")
                print("3. Младший номер-люкс")
                print("4. Номер-люкс")
                print()
                room_type_chosen = input("Ваш выбор: 1/2/3/4/q: ")
            elif selected_language == "3":
                print()
                print(f"{blue_cli}اختر نوع الغرفة{reset_cli}")
                print()
                print("1. غرفة قياسية")
                print("2. غرفة متميزة")
                print("3. جناح صغير")
                print("4. جناح")
                room_type_chosen = input("اختيارك: 1/2/3/4/q: ")
                print()

            if room_type_chosen == "1":
                UTILS.linear.make_linear_regression(
                    "Standard", selected_language)
            elif room_type_chosen == "2":
                UTILS.linear.make_linear_regression(
                    "Superior", selected_language)
            elif room_type_chosen == "3":
                UTILS.linear.make_linear_regression(
                    "Junior Suite", selected_language)
            elif room_type_chosen == "4":
                UTILS.linear.make_linear_regression("Suite", selected_language)
            else:
                pass
        elif user_response == "q":
            print()
            if selected_language == "1":
                print("See u later!")
            elif selected_language == "2":
                print("До скорой встречи!")
            elif selected_language == "3":
                print("أراك لاحقًا!")
            print()
            userIsActive = False
        else:
            print(f"{blue_cli}Choose one of the next options: 1/2/q")
