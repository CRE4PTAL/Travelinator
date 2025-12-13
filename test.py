import requests
from pprint import pprint
 
# Asystent podróży
# Api pogoodwe - https://openweathermap.org/api
# Api z informacjami o krajach - https://restcountries.com/
# Api z informacjami o kursach walut - https://api.nbp.pl/#info
 
 
API_KEY = "a4b9a4bcf33acc78ab107b7be7e3e84d"
 
def check_coordinates(city, API_KEY):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}')
    #print(response.status_code)
    #pprint(response.json())
    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']
    city = response.json()[0]['name']
    country = response.json()[0]['country']
    return lat, lon, city, country
 
def get_weather_info(lat,lon):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&limit=1&appid={API_KEY}&lang=PL&units=metric')
    #print(response.status_code)
    #pprint(response.json())
    response_json = response.json()
    weather = response_json['weather'][0]['description']
    temperature = response_json['main']['temp']
    pressure = response_json['main']['pressure']
    humidity = response_json['main']['humidity']
    return weather, temperature, pressure, humidity
 
def get_currency_code(country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code.upper()}"
    response = requests.get(url)
    currency_code = list(response.json()[0]['currencies'].keys())[0]
    return currency_code
 
def get_country_full_name(country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code.upper()}"
    response = requests.get(url)
    country_name = response.json()[0]['name']['common']
    return country_name
 
def get_currency_ratio(ori_curr, dest_curr):
    if ori_curr != "PLN":
        url = f"http://api.nbp.pl/api/exchangerates/rates/A/{ori_curr.lower()}/"
        response = requests.get(url)
        ori_ratio = response.json()['rates'][0]['mid']
    else:
        ori_ratio = 1
 
    if dest_curr != "PLN":
        url = f"http://api.nbp.pl/api/exchangerates/rates/A/{dest_curr.lower()}/"
        response = requests.get(url)
        dest_ratio = response.json()['rates'][0]['mid']
    else:
        dest_ratio = 1
 
    ratio = float(ori_ratio) / float(dest_ratio)
    return ratio
 
def calculate_user_currency(user_money, ratio):
    user_money = user_money * ratio
    return user_money
 
# print("Witaj, jestem Travelinator, twój inteligentny asystent podróży")
# origin_city = input("Podaj nazwę miasta z którego podróżujesz: ")
# destitanion_city = input("Podaj nazwę miasta do którego podróżujesz: ")
# user_money = float(input("Podaj swój budżet: "))
 
 
# origin_lat, origin_lon, origin_city, origin_country = check_coordinates(origin_city,API_KEY)
# destitanion_lat, destitanion_lon, destitanion_city, destitanion_country = check_coordinates(destitanion_city,API_KEY)
 
# ori_curr = get_currency_code(origin_country)
# dest_curr = get_currency_code(destitanion_country)
# ratio = get_currency_ratio(ori_curr, dest_curr)
# user_calculated_money = calculate_user_currency(user_money, ratio)
 
# weather, temperature, pressure, humidity = get_weather_info(destitanion_lat,destitanion_lon)
 
# print(f"Miasto z którego podróżujesz: {origin_city}")
# print(f"Leży w kraju {get_country_full_name(origin_country)}")
# print(f"Obowiązująca waluta to {ori_curr}")
# print(f"Miasto do którego podróżujesz: {destitanion_city}")
# print(f"Miasto leży w kraju {get_country_full_name(destitanion_country.lower())}")
# print(f"Obowiązująca waluta to {dest_curr}")
# print(f"Średni kurs z {ori_curr} na {dest_curr} to {ratio}")
# print(f"Użytkownik miał {user_money} {ori_curr}, w finalnym kraju będzie miał {user_calculated_money} {dest_curr}")
# print(f"Jego współrzędne geograficzne to:\n{destitanion_lat} szerokości geograficznej \n{destitanion_lon} dlugości geograficznej")
# print(f"Pogoda : {weather}")   
# print(f"Temperatura {temperature} st.Celcjusza")
# print(f"wilgotność: {humidity}%")
# print(f"ciśnienie atmosferyczne {pressure}hPa")
 
print("Witaj, jestem Travelinator, twój inteligentny asystent podróży")
 
origin_city = None
destitanion_city = None
 
while True:
    print('''Jaką akcję chcesz wykonać?
             1. Podaj/zmień miejsce startowe
             2. Podaj/zmień miejsce docelowe
             3. Podaj budżet i przelicz na lokalną walutę
             4. Sprawdź pogodę miejsca docelowego
             5. Sprawdź lokalizację miejsca docelowego
             6. Koniec''')

    try:
        chosen_option = int(input())
    except ValueError:
        print("Wpisz numer opcji!")
        continue

    if chosen_option == 1:
        origin_city = input("Podaj nazwę miasta z którego podróżujesz: ")
    elif chosen_option == 2:
        destitanion_city = input("Podaj nazwę miasta do którego podróżujesz: ")
    elif chosen_option == 3:
        try:
            user_money = float(input("Podaj swój budżet: "))
        except ValueError:
            print("Podaj poprawną kwotę!")
            continue
        if origin_city and destitanion_city:
            try:
                origin_lat, origin_lon, origin_city, origin_country = check_coordinates(origin_city,API_KEY)
                destitanion_lat, destitanion_lon, destitanion_city, destitanion_country = check_coordinates(destitanion_city,API_KEY)
                ori_curr = get_currency_code(origin_country)
                dest_curr = get_currency_code(destitanion_country)
                ratio = get_currency_ratio(ori_curr, dest_curr)
                user_calculated_money = calculate_user_currency(user_money, ratio)
                print(f"Użytkownik miał {user_money} {ori_curr}, w finalnym kraju będzie miał {user_calculated_money} {dest_curr}")
            except Exception as e:
                print("Wystąpił błąd podczas pobierania danych:", e)
        else:
            print("Brakuje danych!")
    elif chosen_option == 4:
        if destitanion_city:
            try:
                destitanion_lat, destitanion_lon, destitanion_city, destitanion_country = check_coordinates(destitanion_city,API_KEY)
                weather, temperature, pressure, humidity = get_weather_info(destitanion_lat, destitanion_lon)
                print(f"Pogoda: {weather}, Temperatura: {temperature}°C, Wilgotność: {humidity}%, Ciśnienie: {pressure} hPa")
            except Exception as e:
                print("Wystąpił błąd podczas pobierania pogody:", e)
        else:
            print("Najpierw podaj miejsce docelowe!")
    elif chosen_option == 5:
        if destitanion_city:
            try:
                destitanion_lat, destitanion_lon, destitanion_city, destitanion_country = check_coordinates(destitanion_city,API_KEY)
                print(f"Lokalizacja {destitanion_city}: szerokość {destitanion_lat}, długość {destitanion_lon}")
            except Exception as e:
                print("Wystąpił błąd podczas pobierania lokalizacji:", e)
        else:
            print("Najpierw podaj miejsce docelowe!")
    elif chosen_option == 6:
        break
    else:
        print("Nie ma takiej opcji!")
 
 
# 1. Aplikacja ma działać non stop, dopóki nie wyjdziemy
# 2. Menu, żeby mozna było wybrać co wyświetlić
#       Jaką akcję chcesz wykonać?
        # 1. Podaj miejsce docelowe
        # 2. Podaj miejsce startowe
        # 3. Sprawdz pogode
        # 4. Sprawdz ...