# Pokročilý kurzor myši #

* Autori: salah atair, Joseph Lee
* Stiahnuť [stabilnú verziu][1]
* Funguje s NVDA od verzie 2019.3

Umožňuje pohybovať kurzorom myši z klávesnice a uložiť pozície myši pre
klikanie v aplikáciách.

## Klávesové skratky

* Nvda+ctrl+l: Zobraz uložené pozície pre otvorenú aplikáciu.
* Nvda+shift+L: Zapamätaj si pozíciu myši pre otvorenú aplikáciu.
* nvda+windows+c: Zmeň jednotku pohybu kurzora myši.
* Nvda+windows+R: Zapni alebo vypni obmedzenie pohybu kurzora myši na
  aktuálne okno.
* Nvda+windows+S: zapni alebo vypni oznamovanie pozície kurzora myši v
  pixeloch.
* NVDA+windows+j: Presuň kurzor myši na zadané súradnice.
* NVDA+windows+P: Oznám súradnice kurzora myši.
* NVDA+windows+m: Zapni alebo vypni pohybovanie kurzorom myši pomocou
  kurzorových kláves (šípky hore, dole, doľava a doprava).
* Windows+nvda+šípky: Presuň kurzor myšy (ak je aktivované pohybovanie
  kurzorom myši pomocou kurzorových kláves, stačí použiť len šípky).

Klávesové skratky môžete zmeniť v dialógu klávesové skratky.

## Poznámky

* Ak posielate uložené pozície kurzora myši na použitie niekomu ďalšiemu,
  obaja musíte používať rovnaké rozlíšenie obrazovky.
* Takisto odporúčame vždy maximalizovať aktuálne okno skratkou Windows+šípka
  hore.
* Ak zdieľate pozície, odporúčame vám skontrolovať ich názvy a prípadne ich
  premenovať.
* Uložené pozície z verzie doplnku 1.X nie sú kompatibilné s novými verziami
  doplnku.
* Ak chcete používať šípky na štandardné príkazy, najprv vypnite ovládanie
  myši pomocou kurzorových kláves.
* Ak vymažete poslednú zapamätanú pozíciu pre aktuálnu aplikáciu, zmaže sa
  celý súbor s dátami pre aktuálnu aplikáciu.

## Version 5.0

* Modernized add-on source code to make it compatible with NVDA 2021.1.
* Resolved many coding style issues and potential bugs with Flake8.

## Verzia 4.0

* Vyžaduje NVDA od verzie 2019.3.
* Panel nastavení zmenený na dialóg.

## Verzia 3.3

* Kód upravený pre podporu budúcich vydaní NVDA..

## Verzia 3.2

* Upravené pre NVDA 2018.3 (wxPython 4).

## Verzia 3.0

* Dialóg s nastaveniami bol presunutý do stromu nastavení pre NVDA od verzie
  2018.2.

## Verzia 2.1

* Opravená chyba unicode decode error pri mazaní uložených pozícií.
* Odteraz nie je možné mať otvorených viacero okien doplnku súčasne.
* Opravená odozva dialógov a okien.

## Verzia 2.0

* Vyžaduje NVDA od verzie 2017.3.
* Zmenil sa formát uložených súradníc. Staré súradnice sa prevedú do nového
  formátu po inštalácii doplnku.
* Pridaný dialóg s nastaveniami, kde je možné nastaviť oznamovanie pozície
  kurzora myši a jednotku pohybu kurzora.
* Upravené správy.
* Pri prepínaní nastavení sa neprehráva zvuk.
* Odteraz je možné pohybovať kurzorom len za použitia kurzorových kláves (po
  zapnutí príslušného režimu).
* Upravený dialóg na ukladanie. Odteraz obsahuje zapamätané súradnice a
  názov aplikácie.
* Kláves enter v zozname uložených súradníc automaticky presunie myš na
  požadované miesto.
* Pri premenovaní názvu NVDA skontroluje, či neexistuje uložená pozícia s
  rovnakým menom a ak áno, zobrazí chybu.
* Odstránenie súradníc je potrebné odteraz potvrdiť.
* Zmenený dialóg na presun kurzora myšy. Zmenil sa názov okna a súradnice je
  možné zadať alebo nastaviť šípkami.
* Dialóg pri ukladaní obsahuje aktuálnu pozíciu kurzora myši.
* When saving positions, resolved an issue where NVDA may play error tones
  if the positions folder does not exist.

## Verzia 1.4

* Odstránená knižnica win32api, ktorá nie je podporovaná v novších verziách
  NVDA.

## Verzia 1.0

* Prvé vydanie.

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
