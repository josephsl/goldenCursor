# Aranykurzor #

* Készítők: salah atair, Joseph Lee
* Letöltés [Stabil verzió][1]
* Kompatibilitás: NVDA 2019.3 és újabb kiadások

Ez a kiegészítő lehetővé teszi az egérkurzor mozgatását a billentyűzet
használatával, ill. elmenthet vele egérkurzor-koordinátákat a különböző
alkalmazásokhoz.

## Billentyűparancsok

* Ctrl+NVDA+L: Az aktív alkalmazáshoz elmentett egérpozíciók listája,
  amennyiben van ilyen.
* Shift+NVDA+l: Aktuális egérpozíció elmentése az aktív alkalmazáshoz.
* Windows+NVDA+C: az egérmutató elmozdulás mértékének változtatása.
* Windows+NVDA+R: Be- vagy kikapcsolja az Egérmozgatás korlátozását az aktív
  ablakra.
* Windows+NVDA+S: Be- vagy kikapcsolja az egérkurzor pozíciójának
  bemondását. Az egérkurzor helye képpontban értendő.
* Windows+NVDA+J: Az egérkurzort a képernyő egy x, y koordinátákkal megadott
  pontjára helyezi.
* Windows+NVDA+P: aktuális egérpozíció bejelentése.
* Windows+NVDA+M: egérmozgatás nyílbillentyűkkel be- vagy kikapcsolása.
* Windows+NVDA+nyílbillentyűk (vagy csak nyílbillentyűk, ha az egérmozgatás
  nyílbillentyűkkel be van kapcsolva ): egérkurzor mozgatása.

Megjegyzés: Ezek a parancsok megváltoztathatók az NVDA Beviteli parancsok
párbeszédpanelén az Aranykurzor kategóriában.

## Megjegyzések

* A pozíciók megosztása csak azonos képernyőfelbontást használók között
  működik megfelelően.
* A legmegfelelőbb működéshez tegye teljes képernyőssé az ablakokat a
  Windows gomb+felnyíl paranccsal
* A pozíciók megosztása esetén át kell nevezni a már létező elnevezésekkel
  ütközőket.
* Az 1.x és a 2.x verzióban elmentett egérkurzor pozíciók adatai nem
  kompatibilisek egymással.
* Amint ismét a nyílbillentyűk hagyományos funkcióira van szükség ki kell
  kapcsolni az egérmozgatás nyílbillentyűkkel opciót.
* Amennyiben az elmentett egérpozíciók törlése után nem marad adott
  alkalmazáshoz egy egérpozíció sem, az alkalmazáshoz tartozó egérpozíciós
  fájl is törlődik.

## Version 5.0

* Modernized add-on source code to make it compatible with NVDA 2021.1.
* Resolved many coding style issues and potential bugs with Flake8.

## 4.0-s verzió

* Az NVDA 2019.3 és újabb verziójára van szükség a futtatáshoz.
* Az Aranykurzor beállításai mostantól az NVDA beállításai között érhetőek
  el az Aranykurzor kategóriában.

## 3.3-as verzió

* későbbi NVDA kiadások támogatása

## 3.2-es verzió

* A bővítmény már kompatibilis az NVDA 2018.3 kiadásával (wxPython 3).

## 3.0-s verzió

* Az NVDA 2018.2 kiadásában az Aranykurzor beállításai az NVDA beállításai
  közé kerültek az Aranykurzor kategóriába.

## 2.1-es verzió

* Javították az Unicode kódolási hibát ami az elnevezett egérpozíciók
  törlésénél lépett fel.
* A bővítménynek mindig csak egy párbeszédablaka lehet nyitva.
* Javították az egérpozíciók listájának és a megadott pozícióra ugrás
  ablakának megjelenését.

## 2.0-s verzió

* Az NVDA 2017.3 vagy újabb kiadására van szükség a bővítmény használatához.
* Az 1.x verzióban elmentett egérpozíciók nem kompatibilisek ezzel a
  kiadással, de a bővítmény telepítése során a program elvégzi a szükséges
  átalakításokat, hogy a korábban elmentett egérpozíciók továbbra is
  használhatóak legyenek.
* Az Aranykurzor beállításai elérhetők az NVDA Beállítások menüjéből. A
  megjelenő párbeszédablakon az egérpozíció bemondását és az egérkurzor
  elmozdulásának a mértékét lehet beállítani.
* A bővítményben több üzenetet is megváltoztattak.
* A beállítások változtatásakor a program már nem ad hangjelzést.
* Már lehetséges az egérkurzort a nyílbillentyűkkel mozgatni, ehhez be kell
  kapcsolni az egérmozgatás a nyílbillentyűkkel opciót.
* Az egérpozíciók listáján az elmentett egérpozíciók mellett már látszanak
  az elmentett pozíció koordinátái, illetve az ablak címsorának már része az
  alkalmazás neve,amihez az elmentett egérpozíciók tartoznak.
* Az egérpozíciók listáján már az enter lenyomásával is a kívánt pozícióra
  ugrik az egérkurzor.
* Az elmentett egérpozíciók átnevezésénél a program már figyelmeztet, ha egy
  már létező nevet próbálunk megadni.
* Az elmentett egérpozíciók törlésénél a program már kér megerősítést a
  művelet végrehajtása előtt.
* Megváltozott az Ugrás pozícióra lehetőség: Meg lehet adni az x és y
  koordinátákat egymástól külön-külön, számértékekkel, vagy a felnyíl és
  lenyíl segítségével.
* Az egérpozíciók elmentésére szolgáló ablak már mutatja az aktuális
  egérpozíció koordinátáit.
* When saving positions, resolved an issue where NVDA may play error tones
  if the positions folder does not exist.

## 1.4-es verzió

* eltávolították a Win32 API függőséget, hogy a bővítmény kompatibilis
  legyen az NVDA későbbi kiadásaival.

## 1.0-s verzió

* Első kiadás

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
