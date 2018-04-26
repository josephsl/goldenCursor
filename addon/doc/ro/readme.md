# Golden Cursor #

* Autori: salah atair, Joseph Lee
* Descarcă [versiunea stabilă][1]
* Descarcă [versiunea în dezvoltare][2]

Acest supliment îți permite să muți mausul folosind tastatura și să salvezi
pozițiile mausului pentru aplicații.

## Combinații de taste

* Control+NVDA+L: afișeaza pozițiile maus salvate pentru o anumită
  aplicație.
* Shift+NVDA+L: save a tag or a label for the current mouse position in the
  currently focused application.
* Windows+NVDA+C: schimbă unitatea de mișcare a mausului.
* NVDA+Win+R: Comută restricționarea mausului.
* NVDA+Win+S: Comută raportarea pixelilor.
* Windows+NVDA+J: mișca mausul la o poziție x,y specifică.
* Windows+NVDA+P: anunță poziția mausului.
* NVDA+Win+M: Comută mișcarea mausului prin apăsarea săgeților.
* Windows+NVDA+săgeți (sau doar săgeți daca săgețile maus sunt activate):
  mișcă mausul.

Notă: Aceste gesturi pot fi re-definite din dialogul Gesturi de intrare în
meniul NVDA, preferințe.

## Note.

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
* A fost rezolvată o problemă la salvarea pozițiilor prin care NVDA poate
  reda tonuri de eroare dacă folderul de poziții nu există.

## Versiunea 1.4

* A fost eliminată dependența win32api pentru a fi compatibil cu versiunile
  anterioare și viitoare ale NVDA.

## Versiunea 1.0

* Versiunea inițială

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
