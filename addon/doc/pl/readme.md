# Golden Cursor #

* Autorzy: salah atair, Joseph Lee
* Pobierz [wersja stabilna][1]
* Zgodność z wersjami NVDA: 2019.3 and beyond

Ten dodatek umożliwia ruszanie myszą za pomocą klawiatury i zapisywanie
pozycji myszy dla danej aplikacji.

## Polecenia klawiszowe

* Control+NVDA+L: przeglądaj zapisane pozycje myszy dla danej aplikacji,
  jeśli jakieś zostały wcześniej zapisane.
* Shift+NVDA+L: Zapisz tag lub oznaczenie dla aktualnej pozycji myszy w
  aktualnie otwartej aplikacji.
* Windows+NVDA+C: Zmień jednostkę ruchu myszy.
* Windows+NVDA+R: Przełącz ograniczenie myszy.
* Windows+NVDA+S: Przełącz odczytywanie pozycji myszy w pikselach.
* Windows+NVDA+J: Przesuń mysz do konkretnej pozycji x y.
* Windows+NVDA+P: Odczytaj pozycję myszy.
* Windows+NVDA+M: włącz lub wyłącz strzałki myszy.
* Windows+NVDA+klawisze strzałek (lub tylko klawisze strzałek, jeśli
  strzałki myszy są włączone): ruszaj myszą.

Uwaga! Powyższe gesty można przypisać ponownie w Zdarzeniach Wejścia NVDA, w
kategorii Golden Cursor.

## Uwagi

* Gdy użytkownicy dzielą się ze sobą pozycjami myszy (ich tagami), każdy z
  nich powinien mieć taką samą rozdzielczość ekranu.
* Dla jak największej zgodności, należy zmaksymalizować widok systemu
  naciskając Windows+Strzałka w gurę.
* Podczas dzielenia pozycji myszy, nazwy istniejących pozycji powinny zostać
  zmienione.
* w wersjach 1.x i 2.x formaty pozycji myszy nie są ze sobą zgodne.
* Przed wykonywaniem czynności, które wymagają używania klawiszy strzałek,
  należy wyłączyć strzałki myszy.
* Jeżeli wszystkie zapisane w dodatku pozycje zostaną usunięte, lista
  pozycji dla danej aplikacji zostanie wyczyszczona.

## Version 5.0

* Modernized add-on source code to make it compatible with NVDA 2021.1.
* Resolved many coding style issues and potential bugs with Flake8.

## Wersja 4.0

* Wymaga NVDA 2019.3 lub nowszej.
* Dialogowe okno ustawień Golden Cursor zostało zmienione na panel.

## Wersja 3.3

* Zmiany wewnętrzne do wsparcia nowszych wersji NVDA.

## Wersja 3.2

* Dodatek jest zgodny z NVDA 2018.3 (wxPython 4).

## Wersja 3.0

* Jeżeli państwo używają NVDA 2018.2, ustawienia dodatku można znaleść w
  nowym wielopanelowym  dialogu ustawień w kategorii "Golden Cursor".

## Wersja 2.1

* Naprawiono błąd dekodowania unikodu podczas usuwania nazwy tagu.
* Należy zapobiegać tworzeniu się wielu instancji dodatku, podczas
  otwierania jego różnych okien dialogowych.
* Poprawiono wygląd listy pozycji myszy i okien dialogowych przeskakiwania
  do pozycji.

## Wersja 2.0

* Wymaga NVDA w wersji 2017.3 lub nowszej.
* Format pliku pozycji jest niezgodny z wersjami 1.x. Jeśli program znajdzie
  format pozycji 1.x, stare pozycje zostaną zamienione na nowy format
  podczas instalacji aktualizacji.
* Dodano nowe okno ustawień Golden Cursor do menu ustawień NVDA. Służy ono
  do konfigurowania jednostki ruchu myszy i ustawiania ogłaszania pozycji
  myszy, gdy się nią rusza.
* Zmianie uległy różnego rodzaju wiadomości w tym dodatku.
* Nie będzie już słychać dźwięku przełączania podczas zmiany ustawień.
* Dostępny jest tryb strzałek myszy, który umożliwia ruszanie myszą za
  pomocą samych klawiszy strzałek.
* Zmianom uległo okno dialogowe listy pozycji. Między innymi, zmieniono
  nazwę okna na Pozycje Myszy, a także jego układ, wyświetlanie
  współrzędnych oznaczenia, oraz pokazywanie nazwy otwartej aplikacji jako
  część tytułu okna.
* Naciśnięcie klawisza Enter na zapisanym oznaczeniu w oknie dialogowym
  Pozycje Myszy, przeniesie mysz do zapisanej lokalizacji.
* Gdy podczas zmiany pliku okaże się, że plik o takiej samej nazwie już
  istnieje, pojawi się okno błędu.
* Aby usunąć lub wyczyścić pozycje myszy, musisz potwierdzić swój zamiar
  przyciskiem Tak. Dopiero wtedy pozycje zostaną usunięte lub wyczyszczone.
* Zmiana do funkcji przeskakiwania miszy, włączając w to nową nazwę (od
  teraz się nazywa nowa pozycja myszy) a także możliwość wpisywania
  współrzędnych x i y oddzielnie lub używając strzałek.
* Dialog do zapisywania aktualnej pozycji myszy teraz pokazuje współrzędne
  dla aktualnej pozycji myszy.
* When saving positions, resolved an issue where NVDA may play error tones
  if the positions folder does not exist.

## Wersja 1.4

* Usunięto zależność win32api, aby uzgodnić dodatek z starymi i nowymi
  wersjami NVDA.

## Wersja 1.0

* Wersja pierwotna.

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
