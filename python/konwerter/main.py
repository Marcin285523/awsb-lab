def pobierz_kierunek():
    while True:
        kierunek = input("Wybierz kierunek konwersji (C - Celsjusz na Fahrenheit, F - Fahrenheit na Celsjusz): ").strip().upper()
        if kierunek in ['C', 'F']:
            return kierunek
        else:
            print("Błąd: Proszę wprowadzić 'C' lub 'F'.")

def pobierz_temperature():
    while True:
        try:
            temperatura = float(input("Podaj wartość temperatury: "))
            return temperatura
        except ValueError:
            print("Błąd: Proszę wpisać poprawną wartość liczbową!")

def main():
    print("Konwerter temperatur (Celsjusz - Fahrenheit)")

    # Pobranie kierunku konwersji
    kierunek = pobierz_kierunek()

    # Pobranie wartości temperatury
    temperatura = pobierz_temperature()

    # Konwersja i wyświetlenie wyniku
    if kierunek == 'C':
        wynik = temperatura * 1.8 + 32
        print(f"{temperatura}°C = {wynik:.2f}°F")
    elif kierunek == 'F':
        wynik = (temperatura - 32) / 1.8
        print(f"{temperatura}°F = {wynik:.2f}°C")
    else:
        print("Wystąpił nieoczekiwany błąd.")  # To zabezpieczenie, choć nie powinno być użyte

if __name__ == "__main__":
    main()
