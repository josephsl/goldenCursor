# Golden Cursor #

* Autori: salah atair, Joseph Lee
* Descarcă [versiunea stabilă][1]
* Compatibilitate NVDA: 2019.3 și mai nou

Acest supliment îți permite să muți mausul folosind tastatura și să salvezi
pozițiile mausului pentru aplicații.

## Combinații de taste

* Control+NVDA+L: afișeaza pozițiile maus salvate pentru o anumită
  aplicație.
* Shift+NVDA+l: salveaza o etichetă pentru poziția actuală a mausului în
  aplicația activă.
* Windows+NVDA+C: schimbă unitatea de mișcare a mausului.
* NVDA+Win+R: Comută restricționarea mausului.
* NVDA+Win+S: Comută raportarea pixelilor.
* Windows+NVDA+J: mișca mausul la o poziție x,y specifică.
* Windows+NVDA+P: anunță poziția mausului.
* NVDA+Win+M: Comută între activarea și dezactivarea mișcării mausului prin
  apăsarea săgeților.
* Windows+NVDA+săgeți (sau doar săgeți daca săgețile maus sunt activate):
  mișcă mausul.

Notă: Aceste gesturi pot fi re-definite din dialogul Gesturi de intrare în
meniul NVDA, preferințe.

## Note

* Când distribui poziții, toată echipa trebuie să utilizeze aceiași
  rezoluție.
* Pentru o compatibilitate maximă, trebuie să maximizezi fereastra apăsând
  Windows+Săgeată sus.
* Când distribui poziții, eticheta poziției existente trebuie să fie
  redenumită.
* Formaturile pozițiilor maus 1.x și 2.x sunt incompatibile.
* Pentru a efectua funcții care necesită utilizarea tastelor săgeți in mod
  standard, dezactivați mai întâi săgețile maus.
* Atunci când ștergeți ultima poziție salvată, pozițiile aplicației vor fi
  curățate .

## Version 5.0

* Modernized add-on source code to make it compatible with NVDA 2021.1.
* Resolved many coding style issues and potential bugs with Flake8.

## Versiunea 4.0

* Necesită NVDA 2019.3 sau mai nou.
* Dialogul de setări Golden Cursor a fost înlocuit cu un panou de setări.

## Versiunea 3.3

* Au fost făcute modificări interne pentru ca viitoarele versiuni de NVDA să
  fie suportate.

## Versiunea 3.2

* Suplimentul este compatibil cu NVDA 2018.3 (wxPython 4).

## Versiunea 3.0

* Dacă se utilizează NVDA 2018.2, setările suplimentului vor fi găsite în
  noul ecran al multicategoriei de setări, sub categoria „Golden Cursor”.

## Versiunea 2.1

* A fost rezolvată o Eroare de decodare unicode cand numele pozițiilor
  incercau sa fie șterse.
* Previne instanțe multiple la deschiderea diverselor dialoguri.
* Aparițiea listei de poziții maus și a dialogurilor de sărire a fost
  îmbunătățită.

## Versiunea 2.0

* Necesită NVDA 2017.3 sau mai nou.
* Formatul fișierului de poziții este incompatibil cu versiunile 1.x. Dacă
  se găsește un format de poziție 1.x, pozițiile vechi vor fi migrate la
  noul format în timpul instalării.
* A fost adăugat un nou dialog de setări pentru Golden Cursor în meniul
  Preferințe al NVDA. Acesta face posibilă configurarea unității de mișcare
  a mausului și anunțării pozițiilor mausului in timp ce mausul se mișcă.
* S-au făcut schimbări la diferite mesaje ale acestui supliment.
* Când comutați între diferite setări, tonul de comutare nu va mai fi redat.
* Acum puteți folosi modul săgeți care va permite să deplasați mausul
  apăsând doar tastele săgeată.
* Modificări la  dialogul lista poziții, inclusiv noul nume (pozițiile
  maus). Acum vor fi afișate in titlul dialogului atât coordonatele mausului
  pentru o poziție, cat și numele aplicației active.
* Din dialogul "Pozițiile maus", apăsând pe o poziție salvată va deplasa
  mausul în locația salvată.
* La redenumirea unei poziții maus, se va afișa un dialog de eroare dacă
  există o poziție cu același nume.
* Când ștergeți sau goliți pozițiile maus, trebuie să confirmați cu Da
  înainte ca pozițiile să fie șterse.
* Modificări la funcțiea de săritura mausului, inclusiv un nume nou (denumit
  acum poziția maus nouă). De asemenea, s/a adaugat capacitatea de a
  introduce coordonatele X și Y separat sau prin utilizarea săgeților sus și
  jos.
* Dialogul afișat atunci când salvați poziția actuală a mouse-ului afișează
  acum coordonatele pentru locația actuală a mouse-ului.
* When saving positions, resolved an issue where NVDA may play error tones
  if the positions folder does not exist.

## Versiunea 1.4

* A fost eliminată dependența win32api pentru a fi compatibil cu versiunile
  anterioare și viitoare ale NVDA.

## Versiunea 1.0

* Versiunea inițială.

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
