# zadanie 1
def pobierz_liczbe(komunikat):
    while True:
        try:
            liczba = float(input(komunikat))
            return liczba
        except ValueError:
            print("Błąd: Proszę wpisać poprawną liczbę!")

def kalkulator():
    print("\nProsty kalkulator dwóch liczb zmiennoprzecinkowych.")
    liczba1 = pobierz_liczbe("Podaj pierwszą liczbę: ")
    liczba2 = pobierz_liczbe("Podaj drugą liczbę: ")
    operacja = input("Wybierz operację (+, -, *, /): ")
    
    wynik = 0
    operacja_prawidlowa = True

    if operacja == "+":
        wynik = liczba1 + liczba2
    elif operacja == "-":
        wynik = liczba1 - liczba2
    elif operacja == "*":
        wynik = liczba1 * liczba2
    elif operacja == "/":
        if liczba2 != 0:
            wynik = liczba1 / liczba2
        else:
            print("Błąd: Nie można dzielić przez zero!")
            operacja_prawidlowa = False
    else:
        print("Błąd: Nieznana operacja!")
        operacja_prawidlowa = False

    if operacja_prawidlowa:
        print(f"Wynik: {wynik}")
# zadanie 2
def pobierz_kierunek():
    while True:
        kierunek = input("Wybierz kierunek konwersji (C - Celsjusz na Fahrenheit, F - Fahrenheit na Celsjusz): ").strip().upper()
        if kierunek in ['C', 'F']:
            return kierunek
        else:
            print("Błąd: Proszę wprowadzić 'C' lub 'F'.")

def konwerter_temperatury():
    print("\nKonwerter temperatur (Celsjusz - Fahrenheit)")
    kierunek = pobierz_kierunek()
    temperatura = pobierz_temperature()

    if kierunek == 'C':
        wynik = temperatura * 1.8 + 32
        print(f"{temperatura}°C = {wynik:.2f}°F")
    elif kierunek == 'F':
        wynik = (temperatura - 32) / 1.8
        print(f"{temperatura}°F = {wynik:.2f}°C")

def pobierz_temperature():
    while True:
        try:
            temperatura = float(input("Podaj wartość temperatury: "))
            return temperatura
        except ValueError:
            print("Błąd: Proszę wpisać poprawną wartość liczbową!")
# zadanie 3
def srednia_ocen():
    print("\nObliczanie średniej ocen ucznia i sprawdzanie zaliczenia")
    print("Wpisuj oceny w skali 1–6. Wpisz 0, aby zakończyć.")
    
    suma_ocen = 0
    liczba_ocen = 0
    
    while True:
        try:
            ocena = float(input("Podaj ocenę (skala 1–6 lub 0, aby zakończyć): "))
            if ocena == 0:
                break
            elif 1 <= ocena <= 6:
                suma_ocen += ocena
                liczba_ocen += 1
            else:
                print("Błąd: Ocena musi mieścić się w zakresie od 1 do 6.")
        except ValueError:
            print("Błąd: Proszę wpisać poprawną wartość liczbową.")

    if liczba_ocen > 0:
        srednia = suma_ocen / liczba_ocen
        print(f"Średnia: {srednia:.2f}")
        if srednia >= 3.0:
            print("Uczeń zdał.")
        else:
            print("Uczeń nie zdał.")
    else:
        print("Nie wpisano żadnych ocen.")

# menu główne
def main():
    while True:
        print("\nMENU GŁÓWNE")
        print("1. Kalkulator")
        print("2. Konwerter temperatur")
        print("3. Obliczanie średniej ocen")
        print("0. Wyjście")
        
        wybor = input("Wybierz opcję (1-3, 0-koniec): ")
        
        match wybor:
            case "1":
                kalkulator()
            case "2":
                konwerter_temperatury()
            case "3":
                srednia_ocen()
            case "0":
                print("Koniec programu.")
                break
            case _:
                print("Nieprawidłowy wybór. Proszę wybrać opcję od 1 do 4.")

if __name__ == "__main__":
    main()