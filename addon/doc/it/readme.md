# Golden Cursor #

* Autori: salah atair, Joseph Lee
* Scarica la [versione stabile][1]
* NVDA compatibility: 2019.3 and beyond
* Download [older version][3] compatible with NVDA 2019.2.1 and earlier

Questo add-on permette di spostare il mouse con la tastiera e di salvare le
posizioni del mouse per le applicazioni. 

## Comandi disponibili

* Control+NVDA+L: Visualizza le posizioni del mouse salvate per
  l'applicazione corrente se disponibili.
* Shift+NVDA+l: Apre una finestra di dialogo per etichettare e salvare la
  posizione corrente del mouse.
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

## Version 4.0

* Requires NVDA 2019.3 or later.
* Golden Cursor settings dialog has been replaced by Golden Cursor settings
  panel.

## Version 3.3

* Internal changes to support future NVDA releases.

## Version 3.2

* Compatibile con NVDA 2018.3 (wxPython 4).

## Versione 3.0

* Se si utilizza NVDA 2018.2, le impostazioni del componente aggiuntivo si
  trovano nella nuova schermata multicategoria delle impostazioni di NVDA,
  alla voce Golden Cursor.

## Versione 2.1

* Risolto un problema di decodifica unicode quando si elimina il nome di un
  tag.
* Non vengono create più istanze all'apertura di varie finestre di dialogo
  del componente aggiuntivo.
* Migliorato l'aspetto dell'elenco posizioni mouse e della finestra "vai a".

## Versione 2.0

* Richiede NVDA 2017.3 e successive.
* Il Formato del file contenente le posizioni è incompatibile con la
  versione 1.x. Se viene rilevato un formato precedente, le posizioni
  verranno migrate al nuovo formato durante l'installazione.
* Aggiunta una nuova finestra di dialogo chiamata Golden Cursor nel menu
  preferenze di NVDA  per configurare l'unità di movimento del mouse e la
  lettura della posizione del mouse mentre si sposta.
* Modificati diversi messaggi di questo componente aggiuntivo
* Durante la modifica delle impostazioni, non si udirà più il segnale
  acustico di alternanza delle impostazioni stesse
* Ora è disponibile una nuova funzione,  modalità frecce per il mouse, in
  questo modo sarà possibile spostare il puntatore direttamente con i tasti
  freccia
* Modifiche all'elenco delle posizioni, che comprendono un nuovo nome (ora
  chiamato posizioni mouse) ed un nuovo layout, che visualizza le coordinate
  mouse per un'etichetta, e e il nome dell'app attiva come parte del titolo.
* Dalle impostazioni posizione mouse, premendo invio su un'etichetta, il
  mouse si sposterà alla posizione salvata.
* Quando si rinomina una posizione mouse, verrà mostrato un messaggio di
  errore nel caso in cui esista già un'etichetta con lo stesso nome.
* Quando si cancellano o si puliscono i settaggi delle posizioni mouse, sarà
  necessario confermare con un sì!
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

[3]: https://addons.nvda-project.org/files/get.php?file=gc-2019
