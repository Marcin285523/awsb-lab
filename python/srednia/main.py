def main():
    print("Obliczanie średniej ocen ucznia i sprawdzanie zaliczenia")
    print("Wpisuj oceny w skali 1–6. Wpisz 0, aby zakończyć.")

    suma_ocen = 0
    liczba_ocen = 0

    while True:
        try:
            ocena = float(input("Podaj ocenę (skala 1–6 lub 0, aby zakończyć): "))
            if ocena == 0:
                # Kończymy pobieranie ocen
                break
            elif 1 <= ocena <= 6:
                suma_ocen += ocena
                liczba_ocen += 1
            else:
                print("Błąd: Ocena musi mieścić się w zakresie od 1 do 6.")
        except ValueError:
            print("Błąd: Proszę wpisać poprawną wartość liczbową.")

    if liczba_ocen > 0:
        # Obliczenie średniej
        srednia = suma_ocen / liczba_ocen
        print(f"Średnia: {srednia:.2f}")

        # Sprawdzenie zaliczenia
        if srednia >= 3.0:
            print("Uczeń zdał.")
        else:
            print("Uczeń nie zdał.")
    else:
        print("Nie wpisano żadnych ocen.")

if __name__ == "__main__":
    main()
