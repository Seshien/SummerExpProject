# Allegro Summer Experience 2021 - Zadanie 3

## Wymagania:
### Python;
### Flask;

## Instalacja lokalna:
  1. Zainstalowanie języka python oraz potrzebnego pakietu.
  2. Pobranie zawartości repozytorium.
  3. Uruchomienie skryptu main.py (prawdopodobnie 'python main.py \<argumenty\>')


## Funkcjonalności:
  Aplikacja tworzy serwer, działający domyślnie na adresie http://127.0.0.1:5000/
  Poszczególne funkcje programu:
*    zapytanie GET na endpointcie http://\<adres\>:\<port\>/repositories/\<username\> - Zwraca listę wszystkich publicznych repozytoriów użytkownika
*    zapytanie GET na endpointcie http://\<adres\>:\<port\>/stars/\<username\> - Zwraca sumę gwiazd wszyskich publicznych repozytoriów użytkownika
*    http://\<adres\>:\<port\>/ - tradycyjne "Hello World" 
*    Aplikacja może przyjąć trzy argumenty: --host, --port, --debug, które działają zgodnie z dokumentacją Flask app.run()
  
## Przyszłość aplikacji:
###  Istnieją pewne możliwości rozwoju (i poprawy) aplikacji:
    - możliwość podania tokenu autoryzacyjnego githuba, co umożliwiłoby dostęp do prywatnych repozytoriów oraz poprawilo ogólną dostępność api githuba
    - dodanie frontendu, który umożliwiałby korzystanie z aplikacji wszystkim użytkownikom
    - uzyskiwanie i wyświetlanie większej ilości informacji 
    - przetwarzanie informacji dla uzyskania bardziej interesujących wyników (przykładowo średnia ilość gwiazd na repozytorium dla użytkownika)
    - prawdopodobonie napisanie aplikacji od nowa
