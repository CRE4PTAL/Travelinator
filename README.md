# Travelinator - Asystent Podróży 🌍

Aplikacja konsolowa (CLI) integrująca dane z trzech niezależnych zewnętrznych API w celu dostarczenia kompleksowych informacji dla podróżujących. Program agreguje dane pogodowe, geograficzne oraz finansowe w czasie rzeczywistym.

## 🛠 Technologie
* **Język:** Python 3.x
* **Biblioteki:** `requests`
* **Format danych:** JSON

## 🔌 Wykorzystane API
Projekt demonstruje umiejętność pracy z REST API poprzez integrację następujących serwisów:
1. **OpenWeatherMap API:** Geokodowanie (zamiana nazwy miasta na współrzędne) oraz pobieranie aktualnej pogody.
2. **REST Countries:** Identyfikacja kraju oraz obowiązującej w nim waluty na podstawie kodu kraju.
3. **NBP API (Narodowy Bank Polski):** Pobieranie aktualnych kursów walut i przeliczanie budżetu użytkownika (PLN <-> Waluta obca).

## 🌟 Główne funkcjonalności
* **Geolokalizacja:** Wyszukiwanie współrzędnych geograficznych dla dowolnego miasta na świecie.
* **Kalkulator Walutowy:** Automatyczne rozpoznawanie waluty w kraju docelowym i przeliczanie budżetu podróżnego według średniego kursu NBP.
* **Monitor Pogody:** Sprawdzanie temperatury, ciśnienia i wilgotności w miejscu docelowym.
* **Interfejs:** Interaktywne menu tekstowe z obsługą błędów (np. błędna nazwa miasta).

## 💡 Wyzwania i rozwiązania
Głównym wyzwaniem było stworzenie **łańcucha zależności danych**. Aby przeliczyć walutę, aplikacja musi wykonać serię kroków:
`Miasto -> (API 1) -> Kraj -> (API 2) -> Kod Waluty -> (API 3) -> Kurs Waluty`

Wymagało to precyzyjnego parsowania odpowiedzi JSON i przekazywania wyników między funkcjami, a także obsługi sytuacji, w których jedno z ogniw łańcucha zwraca błąd (zastosowanie bloków `try-except`).

## 💻 Uruchomienie projektu

1. Zainstaluj wymagane biblioteki:
```bash
pip install requests
