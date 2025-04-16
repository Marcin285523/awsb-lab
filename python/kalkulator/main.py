def pobierz_liczbe(komunikat):
    while True:
        try:
            liczba = float(input(komunikat))
            return liczba
        except ValueError:
            print("Błąd: Proszę wpisać poprawną liczbę!")


def main():
    print("Prosty kalkulator dwóch liczb zmiennoprzecinkowych.")

    liczba1 = pobierz_liczbe("Podaj pierwszą liczbę: ")
    liczba2 = pobierz_liczbe("Podaj drugą liczbę: ")

    operacja = input("Wybierz operację (+, -, *, /): ")

    wynik = 0
    operacja_prawidlowa = True

    # Sprawdzenie, która operacja została wybrana i wykonanie odpowiedniego działania
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

    # Wyświetlenie wyniku
    if operacja_prawidlowa:
        print(f"Wynik: {wynik}")


if __name__ == "__main__":
    main()
