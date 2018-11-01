# Golden Cursor #

* Author: salah atair, Joseph Lee
* Preuzmi [stable version][1]
* Preuzmi [development version][2]

Ovaj dodatak dozvoljava vam da pomičete strelicu miša koristeći tipkovnicu i
pohranjujete pozicije miša za različite aplikacije.

## Tipkovničke kratice 

* Control+NVDA+L: pregledajte spremljene pozicije miša za neku aplikaciju
  ako postoje.
* Shift+NVDA+l: save a tag or a label for the current mouse position in the
  currently focused application.
* Windows+NVDA+C: promijeni jedinicu kretanja miša.
* Windows+NVDA+R: toggle mouse restriction.
* Windows+NVDA+S: toggle reporting of mouse position in pixels.
* Windows+NVDA+J: premjesti poziciju miša na određeni položaj x y.
* Windows+NVDA+P: izvijesti o poziciji miša.
* Windows+NVDA+M: sswitch mouse arrows on or off.
* Windows+NVDA+navigacijske strelice (ili samo navigacijske strelice ako je
  uključena strelica miša): pomakni miš.

Note: these gestures can be reassigned via NVDA's Input Gestures dialog
under Golden Cursor category.

## Napomene

* When sharing positions (tags), each party should use same display
  resolution.
* Za maksimalnu kompatibilnost, trebate maksimizirati prozore pritiskom
  kombinacije tipaka Windows+Strelica gore.
* Kada dijelite pozicije, trebate preimenovati postojeće vrijednosti
  pozicija.
* Formati verzije 1 x i 2 x pozicije miša nisu kompatibilni.
* Za izvođenje funkcija koje zahtijevaju korištenje strelica, prvo uključite
  strelicu miša.
* Tijekom brisanja spremljenih pozicija, ako više nema spremljenih pozicija,
  pozicije će za tu aplikaciju bit će obrisane.

## Version 3.2

* Add-on is compatible with NVDA 2018.3 (wxPython 4).

## Version 3.0

* If using NVDA 2018.2, add-on settings will be found in new multi-category
  settings screen under "Golden Cursor" category.

## Inačica 2.1

* Ispravljena greška dekodiranja Unicode-a tijekom pokušaja brisanja naziva
  oznake.
* Sprječava višestruke instance prilikom otvaranja različitih dijaloških
  okvira dodatka.
* Poboljšan izgled popisa pozicija miša i skok na dijaloške okvire pozicija.

## Inačica 2.0

* Zahtijeva NVDA 2017.3 i noviji.
* Format datoteke pozicije nije kompatibilan s 1.x inačicama. Ako je
  pronađen format pozicije u 1.x formatu, pozicije u starom formatu bit će
  pretvorene u novi format tijekom instalacije.
* Dodan je novi dijaloški okvir postavki Golden Cursor dodatka u
  podizborniku postavki NVDA za definiranje jedinice pokreta miša i
  obavijesti o pozicijama miša kao pokretima miša.
* Različite poruke ovog dodatka su promijenjene.
* Dok uključujete i isključujete različite postavke, više nećete čuti
  odgovarajući zvuk.
* Sada možete ući u način strelice miša gdje možete pomicati miša samo
  pritišćući tipke sa strelicama.
* Promjene u dijaloškom okviru popisa pozicija,uključujući novo ime (sada se
  naziva Pozicije Miša) i raspored, sada se prikazuju koordinate miša i ime
  trenutne aplikacije kao dio naslova.
* Iz dijaloškog okvira Pozicije miša, pritisnete li Enter na spremljenu
  vrijednost pomaknut će miša na spremljenu lokaciju.
* Ako preiimenujete poziciju miša, pojavit će se dijaloški okvir greške ako
  postoji vrijednost s istim imenom. 
* Ako brišete pozicije miša, sada morate odgovoriti sa Da prije nego što se
  pozicije obrišu.
* Promjene u značajki Skok na poziciju miša, uključujući novo ime (sada se
  naziva Nova pozicija miša) i mogućnost unošenja X i Y koordinata odvojeno,
  ili korištenja tipki sa strelicama gore i dolje.
* Dijaloški okvir koji se prikazuje tijekom spremanja trenutne pozicije miša
  sada prikazuje koordinate za trenutnu lokaciju miša. 
* Tijekom spremanja pozicija, ispravljena je greška gdje je NVDA ponekad
  reproducirao zvukove pogreške ako mapa pozicija nije postojala.

## Inačica 1.4

* Uklonjena je ovisnost od win32api kbko bi dodatak bio kompatibilan s
  prošlim i budućim inačicama NVDA.

## Inačica 1.0

* Inicijalno izdanje.

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
