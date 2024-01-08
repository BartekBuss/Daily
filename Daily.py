user_choice = -1
tasks = []
days_and_calories = {"Poniedziałek": 0, "Wtorek": 0, "Środa": 0, "Czwartek": 0, "Piątek": 0, "Sobota": 0, "Niedziela": 0}

#funkcje lista zadań

def show_tasks():
    task_index = 0
    for task in tasks:
        print("[" + str(task_index) + "]" + task)
        task_index += 1
    print(" ")

def add_task():
    task = input("Wpisz treść zadania: ")
    tasks.append(task)
    print("Dodano zadanie!")

def delete_task():
    task_index = int(input("Podaj indeks zadania do usunięcia: "))
    if task_index < 0 or task_index > len(tasks) -1:
        print("Zadanie o tym indeksie nie istnieje!")
        return
    tasks.pop(task_index)
    print("Usunięto zadanie!")

def save_tasks_to_file():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task+"\n")
    file.close()
    print("Zapisano do pliku")

def load_tasks_from_file():
    try:
        file = open("tasks.txt")
        for line in file.readlines():
            tasks.append(line.strip())
        print("Odczytano dane z pliku")
        file.close()
    except FileNotFoundError:
        print("Nie znaleziono pliku, tworzę nowy!")
        file = open("tasks.txt", "w")
        file.close()
        return

#funkcje do kalkulatora

def dodaj():
    try:
        one = int(input("Wpisz pierwszą liczbę do dodania! "))
    except ValueError:
            print()
            print("Wpisz liczbę!")
    try:
        two = int(input("Wpisz drugą liczbę do dodania! "))
    except ValueError:
            print()
            print("Wpisz liczbę!")
    print("Wynik to:",one + two)

def odejmij():
    try:
        one = int(input("Wpisz pierwszą liczbę do odjęcia! "))
    except ValueError:
            print()
            print("Wpisz liczbę!")
    try:
        two = int(input("Wpisz drugą liczbę do odjęcia! "))
    except ValueError:
            print()
            print("Wpisz liczbę!")
    print("Wynik to:",one - two)

def mnoz():
    try:
        one = int(input("Wpisz pierwszą liczbę do mnożenia! "))
    except ValueError:
            print()
            print("Wpisz liczbę!")
    try:
        two = int(input("Wpisz drugą liczbę do mnożenia! "))
    except ValueError:
            print()
            print("Wpisz liczbę!")
    print("Wynik to:",one * two)

def dziel():
    try:
        one = int(input("Wpisz pierwszą liczbę do podzielenia! "))
    except ValueError:
            print()
            print("Wpisz liczbę!")
    try:
        two = int(input("Wpisz drugą liczbę do podzielenia! "))
    except ValueError:
            print()
            print("Wpisz liczbę!")
    print("Wynik to:",one / two)

def potega():
    try:
        a = int(input("Wpisz liczbę, którą chcesz podnieść do potęgi! "))
    except ValueError:
            print()
            print("Wpisz liczbę!")
    try:
        b = int(input("Wpisz potęgę! "))
    except ValueError:
            print()
            print("Wpisz liczbę!")
    print("Wunik to:", a ** b)

#funkcje do kalkulatora kalorii

def show_kcal():
    global days_and_calories
    for day, calories in days_and_calories.items():
        print(day, ":", calories)

def add_kcal():
    global days_and_calories
    try:
        day = str(input("Podaj w jaki dzień chcesz dodać kalorie: ").capitalize())
        calories = int(input("Podaj ile kalorii dodać: "))
        days_and_calories[day] += int(calories)
        print("Dodano", calories,"kcal w dniu:", day)
    except ValueError:
        print("Wpisz ilość kalorii!")
    except KeyError:
        print("Wpisz dzień tygodnia!")

def sub_kcal():
    global days_and_calories
    try:
        day = input("Podaj w jaki dzień chcesz odjąć kalorie: ").capitalize()
        calories = input("Podaj ile kalorii chcesz odjąć: ")
        days_and_calories[day] -= int(calories)
        print("Odjęto", calories,"kcal w dniu:", day)
    except ValueError:
        print("Wpisz ilość kalorii!")
    except KeyError:
        print("Wpisz dzień tygodnia!")

def load_kcal_from_file():
    global days_and_calories
    try:
        file = open("kcal.txt")
        i = 0
        for line in file:
            if i == 0:
                a = "Poniedziałek"
            if i == 1:
                a = "Wtorek"
            if i == 2:
                a = "Środa"
            if i == 3:
                a = "Czwartek"
            if i == 4:
                a = "Piątek"
            if i == 5:
                a = "Sobota"
            if i == 6:
                a = "Niedziela"
            tak = line.replace("\n", "").rstrip()
            days_and_calories[a] = int(tak)
            i += 1
        file.close()
        print("Odczytano dane z pliku")
    except FileNotFoundError:
        print("Nie znaleziono pliku, tworzę nowy!")
        save_kcal_to_file()
        return

def save_kcal_to_file():
    global days_and_calories
    file = open("kcal.txt", "w")
    for line in days_and_calories.values():
        file.write(str(line) + "\n")
    file.close()
    print("Zapisano do pliku")

def kcal_statistics():
    global days_and_calories
    all_kcal = 0
    for calories in days_and_calories.values():
        all_kcal += calories
    print("W tym tygodniu zostało sporzyte", all_kcal, "kcal")
    print()
    print("Średnio dziennie zostało sporzyte", int(all_kcal/7), "kcal")
    print()


def reset():
    global days_and_calories
    days_and_calories["Poniedziałek"] = 0
    days_and_calories["Wtorek"] = 0
    days_and_calories["Środa"] = 0
    days_and_calories["Czwartek"] = 0
    days_and_calories["Piątek"] = 0
    days_and_calories["Sobota"] = 0
    days_and_calories["Niedziela"] = 0
    print("Zresetowano dane i statystyki")
    print()
    save_kcal_to_file()


def confirmation():
    print()
    print("Czy napewno chcesz to zrobić?")
    print("Nastąpi reset danych oraz statystyk!")
    print()
    print("1. Potwierdż")
    print("2. Anuluj")
    print()
    try:
        user_choice = int(input("Wybierz opcję: "))
        print()
        if user_choice == 1:
            reset()
    except ValueError:
        print("Wpisz liczbę!")
        print()
    

#główny kalkulator kalorii

def kcalCalculator(user_choice):
    load_kcal_from_file()

    while user_choice != 7:
        if user_choice == 1:
            show_kcal()
        if user_choice == 2:
            add_kcal()
        if user_choice == 3:
            sub_kcal()
        if user_choice == 4:
            save_kcal_to_file()
        if user_choice == 5:
            kcal_statistics()
        if user_choice == 6:
            confirmation()

        print()
        print("1. Pokaż ilość kalorii")
        print("2. Dodaj kalorie")
        print("3. Odejmij kalorie")
        print("4. Zapisz do pliku")
        print("5. Statystyki z tygodnia/dnia")
        print("6. Nowy tydzień (Uwaga nastąpi reset wartość z aktalnego tygodnia!)")
        print("7. Wyjdź")
        print()

        try:
            user_choice = int(input("Wybierz opcję: "))
            print()
        except ValueError:
            print("Wpisz liczbę!")
            print()

#główny kalkulator

def licz():
    while(True):
        print()
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print("5. Potęgowanie")
        print("6. Wyjdź")
        print()
        try:
            choice = int(input("Wybierz jakie działanie chcesz wykonać: "))
            if choice == 1:
                dodaj()
            if choice == 2:
                odejmij()
            if choice == 3:
                mnoz()
            if choice == 4:
                dziel()
            if choice == 5:
                potega()
            if choice == 6:
                break
        except ValueError:
            print()
            print("Wpisz liczbę!")

#główny wypłata

def payment():
    print()
    print("Cześć, zaraz obliczymy Twoją wypłatę!")
    print()
    try:
        hours = float(input("Wpisz ile godzin przepracowałeś w danym miesiącu: "))
        hourly_rate = 23.50
        payment = hourly_rate * hours
        print()
        print("Twoja wypłata za ten miesiąc wynosi:", payment, "zł")
        print()
    except ValueError:
        print("Wpisz liczbę godzin, jako seprator dziesiętny użyj kropki!")

#główny lista zadań

def ToDoList(user_choice):
    load_tasks_from_file()

    while user_choice != 5:
        if user_choice == 1:
            show_tasks()

        if user_choice == 2:
            add_task()

        if user_choice == 3:
            show_tasks()
            delete_task()

        if user_choice == 4:
            save_tasks_to_file()

        print()
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Usuń zadanie")
        print("4. Zapisz zmiany do pliku")
        print("5. Wyjdź")
        print()
        
        try:
            user_choice = int(input("Wybierz opcję: "))
            print()
        except ValueError:
            print("Wpisz liczbę!")
            print()


### Menu główne


while user_choice != 5:
    if user_choice == 1:
        licz()
    if user_choice == 2:
        payment()
    if user_choice == 3:
        ToDoList(user_choice)
    if user_choice == 4:
        kcalCalculator(user_choice)

    print("Witaj w programie!")
    print()
    print("1. Prosty kalkulator")
    print("2. Liczenie wypłaty")
    print("3. Lista zadań")
    print("4. Licznik kalorii")
    print("5. Koniec programu")
    print()
    try:
        user_choice = int(input("Wybierz opcję: "))
        print()
    except ValueError:
        print("Wpisz liczbę!")
        print()