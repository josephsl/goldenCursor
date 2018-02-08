# Golden Cursor #

* Author: salah atair, Joseph Lee
* Download [stable version][1]
* Download [development version][2]

Questo add-on permette di spostare il mouse con la tastiera e di salvare le
posizioni del mouse per le applicazioni. 

## Comandi disponibili

* Control+NVDA+L: mostra le posizioni salvate per qualsiasi applicazione se
  presenti.
* Shift+NVDA+l: Salva un tag o un'etichetta della posizione mouse corrente
  per l'applicazione focalizzata.
* Windows+NVDA+C: Cambia unità di movimento
* Windows+NVDA+R: commuta tra le due  restrizioni del mouse.
* nvda+win+s: attiva/disattiva l'annuncio dei movimenti del mouse in pixel.
* Windows+NVDA+J: Sposta il mouse ad una coordinata specifica X Y.
* Windows+NVDA+P: Annuncia posizione mouse.
* Windows+NVDA+M: attiva o disattiva il movimento del mouse tramite i tasti
  freccia.
* Windows+NVDA+frecce (o solo frecce se è attiva la funzione tasti freccia
  per il mouse: sposta il puntatore.

Nota: questi tasti possono essere riassegnati alla voce gesti e tasti di
immissione nel menu preferenze di NVDA alla categoria Golden Cursor.

## Note

* Se si condividono le posizioni (tag), la persona che le riceve deve
  utilizzare la medesima risoluzione dello schermo.
* Per una compatibilità ottimale, si consiglia di ingrandire la finestra
  servendosi della combinazione windows-freccia su.
* Quando si condividono le posizioni, eventuali etichette esistenti devono
  essere rinominate.
* I formati usati per salvare le posizioni mouse nelle versioni 1.x e 2.x
  sono incompatibili.
* Per eseguire le funzioni che richiedono l'uso dei tasti freccia,
  disattivare la funzione tasti freccia per il mouse.
* Quando si cancellano le posizioni memorizzate, se non sono rimaste
  posizioni salvate, verranno eliminate le posizioni per l'applicazione.

## Versione 2.1

* Risolto un problema di decodifica unicode quando si elimina il nome di un
  tag.
* Non vengono create più istanze all'apertura di varie finestre di dialogo
  del componente aggiuntivo.
* Migliorato l'aspetto dell'elenco posizioni mouse e della finestra "vai a".

## Versione 2.0

* Requires NVDA 2017.3 and later.
* Position file format is incompatible with 1.x versions. If 1.x position
  format is found, old positions will be migrated to the new format during
  installation.
* Added a new Golden Cursor settings dialog in NVDA's Preferences menu to
  configure mouse movement unit and announcement of mouse positions as mouse
  moves.
* Various messages from this add-on has changed.
* When toggling various settings, toggle tone will no longer be heard.
* You can now enter mouse arrows mode where you can move the mouse by
  pressing just arrow keys.
* Changes to positions list dialog, including new name (now called Mouse
  Positions) and layout, displaying mouse coordinates for a label, and
  showing the name of the active app as part of the title.
* From Mouse Positions dialog, pressing Enter on a saved label will move the
  mouse to the saved location.
* When renaming a mouse position, an error dialog will be shown if a label
  with the same name as the new name exists.
* When deleting or clearing mouse positions, you must now answer Yes before
  positions are deleted and/or cleared.
* Cambiamenti alla funzione "vai a", tra cui un nuovo nome (ora si chiama
  Nuova posizione del mouse) e la capacità di inserire le coordinate X e Y
  separatamente o utilizzando i tasti freccia su o giù. 
* La finestra di dialogo mostrata quando si salva la posizione corrente del
  mouse ora mostra le coordinate per la posizione corrente del mouse. 
* Durante il salvataggio delle posizioni, risolto un problema dove NVDA
  emetteva suoni di errore nel caso in cui la cartella contenente le
  posizioni non esisteva.

## Versione 1.4

* Rimosse le dipendenze Win32Api per rendere il componente compatibile con
  versioni passate e future di NVDA.

## Versione 1.0.

* Versione iniziale.

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
