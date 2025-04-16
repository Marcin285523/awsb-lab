using System;

class Program
{
    static void Main()
    {
        // Główna pętla programu
        while (true)
        {
            Console.WriteLine("\nMENU GŁÓWNE");
            Console.WriteLine("1. Kalkulator");
            Console.WriteLine("2. Konwerter temperatur");
            Console.WriteLine("3. Obliczanie średniej ocen");
            Console.WriteLine("0. Wyjście");
            Console.Write("Wybierz opcję (1-3, 0 - koniec): ");

            switch (Console.ReadLine())
            {
                case "1":
                    Kalkulator();
                    break;
                case "2":
                    KonwerterTemperatur();
                    break;
                case "3":
                    SredniaOcen();
                    break;
                case "0":
                    Console.WriteLine("Koniec programu.");
                    return;
                default:
                    Console.WriteLine("Nieprawidłowy wybór. Proszę wybrać poprawną opcję.");
                    break;
            }
        }
    }

    // Logika kalkulatora
    static void Kalkulator()
    {
        Console.WriteLine("\nProsty kalkulator dwóch liczb zmiennoprzecinkowych.");
        double liczba1 = PobierzLiczbe("Podaj pierwszą liczbę: ");
        double liczba2 = PobierzLiczbe("Podaj drugą liczbę: ");
        Console.Write("Wybierz operację (+, -, *, /): ");
        char operacja = Convert.ToChar(Console.ReadLine());

        double wynik = 0;
        bool operacjaPrawidlowa = true;

        if (operacja == '+') wynik = liczba1 + liczba2;
        else if (operacja == '-') wynik = liczba1 - liczba2;
        else if (operacja == '*') wynik = liczba1 * liczba2;
        else if (operacja == '/')
        {
            if (liczba2 != 0) wynik = liczba1 / liczba2;
            else
            {
                Console.WriteLine("Błąd: Nie można dzielić przez zero!");
                operacjaPrawidlowa = false;
            }
        }
        else
        {
            Console.WriteLine("Błąd: Nieznana operacja!");
            operacjaPrawidlowa = false;
        }

        if (operacjaPrawidlowa) Console.WriteLine($"Wynik: {wynik}");
    }

    // Konwersja temperatur
    static void KonwerterTemperatur()
    {
        Console.WriteLine("\nKonwerter temperatur (Celsjusz - Fahrenheit)");
        char kierunek;
        
        while (true)
        {
            Console.Write("Wybierz kierunek konwersji (C - Celsjusz na Fahrenheit, F - Fahrenheit na Celsjusz): ");
            kierunek = Convert.ToChar(Console.ReadLine().ToUpper());
            if (kierunek == 'C' || kierunek == 'F') break;
            Console.WriteLine("Błąd: Wprowadź 'C' lub 'F'.");
        }

        double temperatura = PobierzLiczbe("Podaj wartość temperatury: ");
        double wynik = kierunek == 'C' ? temperatura * 1.8 + 32 : (temperatura - 32) / 1.8;
        Console.WriteLine(kierunek == 'C' 
            ? $"{temperatura}°C = {wynik:F2}°F" 
            : $"{temperatura}°F = {wynik:F2}°C");
    }

    // Obliczanie średniej ocen
    static void SredniaOcen()
    {
        Console.WriteLine("\nObliczanie średniej ocen ucznia i sprawdzanie zaliczenia");
        Console.WriteLine("Wpisuj oceny w skali 1–6. Wpisz 0, aby zakończyć.");

        double sumaOcen = 0;
        int liczbaOcen = 0;

        while (true)
        {
            Console.Write("Podaj ocenę (skala 1–6 lub 0, aby zakończyć): ");
            if (!double.TryParse(Console.ReadLine(), out double ocena)) 
            {
                Console.WriteLine("Błąd: Proszę wpisać poprawną wartość liczbową.");
                continue;
            }

            if (ocena == 0) break;
            if (ocena < 1 || ocena > 6)
            {
                Console.WriteLine("Błąd: Ocena musi mieścić się w zakresie od 1 do 6.");
                continue;
            }

            sumaOcen += ocena;
            liczbaOcen++;
        }

        if (liczbaOcen > 0)
        {
            double srednia = sumaOcen / liczbaOcen;
            Console.WriteLine($"Średnia: {srednia:F2}");
            Console.WriteLine(srednia >= 3.0 ? "Uczeń zdał." : "Uczeń nie zdał.");
        }
        else
        {
            Console.WriteLine("Nie wpisano żadnych ocen.");
        }
    }

    // Pomocnicza funkcja do pobierania liczb
    static double PobierzLiczbe(string komunikat)
    {
        while (true)
        {
            Console.Write(komunikat);
            if (double.TryParse(Console.ReadLine(), out double liczba))
                return liczba;
            Console.WriteLine("Błąd: Proszę wpisać poprawną liczbę!");
        }
    }
}