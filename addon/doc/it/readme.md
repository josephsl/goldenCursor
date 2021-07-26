# Golden Cursor #

* Autori: salah atair, Joseph Lee
* Scarica la [versione stabile][1]
* Compatibilità con NVDA: versione 2019.3 e successive

Questo add-on permette di spostare il mouse con la tastiera e di salvare le
posizioni del mouse per le applicazioni.

## Comandi disponibili

* Control+NVDA+L: Visualizza le posizioni del mouse salvate per
  l'applicazione corrente se disponibili.
* Shift+NVDA+l: Apre una finestra di dialogo per etichettare e salvare la
  posizione corrente del mouse.
* Windows+NVDA+C: Cambia l'unità di misura per il movimento del mouse.
* Windows+NVDA+R: commuta tra le due  restrizioni del mouse.
* Windows+nvda+s: attiva/disattiva la vocalizzazione della posizione del
  mouse in pixel.
* Windows+NVDA+J: Sposta il mouse ad una coordinata specifica X Y.
* Windows+NVDA+P: Dice la posizione del mouse.
* Windows+NVDA+M: attiva o disattiva il movimento del mouse tramite i tasti
  freccia.
* Windows+NVDA+frecce (o solo frecce se è attiva la funzione movimento del
  mouse tramite tasti freccia: sposta il mouse.

Nota: questi tasti possono essere riassegnati alla voce gesti e tasti di
immissione nel menu preferenze di NVDA alla categoria Golden Cursor.

## Note

* Se si condividono le posizioni (tag), la persona che le riceve deve
  utilizzare la stessa risoluzione dello schermo.
* Per una compatibilità ottimale, si consiglia di ingrandire la finestra
  servendosi della combinazione windows-freccia su.
* Quando si condividono le posizioni, eventuali etichette esistenti devono
  essere rinominate.
* I formati usati per salvare le posizioni mouse nelle versioni 1.x e 2.x
  sono incompatibili.
* Per eseguire le funzioni che richiedono l'uso dei tasti freccia,
  disattivare la funzione movimento del mouse tramite tasti freccia.
* Quando si cancellano le posizioni memorizzate, se non sono rimaste
  posizioni salvate, verranno eliminate le posizioni per l'applicazione.

## Version 5.0

* Modernized add-on source code to make it compatible with NVDA 2021.1.
* Resolved many coding style issues and potential bugs with Flake8.

## Novità nella versione 4.0

* Richiede NVDA 2019.3 o superiore.
* La finestra di dialogo Impostazioni di Golden Cursor, presente nel menu
  Preferenze di NVDA, è stata sostituita dalla categoria Golden Cursor nella
  finestra Impostazioni di NVDA.

## Novità nella versione 3.3

* Modifiche interne per supportare le versioni future di NVDA.

## Novità nella versione 3.2

* Compatibile con NVDA 2018.3 (wxPython 4).

## Novità nella versione 3.0

* Se si utilizza NVDA 2018.2, le impostazioni del componente aggiuntivo si
  trovano nella nuova schermata multicategoria delle impostazioni di NVDA,
  alla voce Golden Cursor.

## Novità nella versione 2.1

* Risolto un problema di decodifica unicode quando si elimina il nome di un
  tag.
* Non vengono create più istanze all'apertura di varie finestre di dialogo
  del componente aggiuntivo.
* Migliorato l'aspetto dell'elenco posizioni mouse e della finestra "vai a
  posizione".

## Novità nella versione 2.0

* Richiede NVDA 2017.3 o superiore.
* Il Formato del file contenente le posizioni è incompatibile con la
  versione 1.x. Se viene rilevato un formato precedente, le posizioni
  verranno migrate al nuovo formato durante l'installazione.
* Aggiunta una nuova finestra di dialogo chiamata Golden Cursor nel menu
  preferenze di NVDA  per configurare l'unità di misura per il movimento del
  mouse e la lettura della posizione del mouse mentre si sposta.
* Modificati diversi messaggi di questo componente aggiuntivo.
* Durante la modifica delle impostazioni, non si udirà più il segnale
  acustico di attivazione e disattivazione.
* Ora è disponibile una nuova funzione,  movimento del mouse tramite frecce
  ; in questo modo sarà possibile spostare il puntatore direttamente con i
  tasti frecci.
* Modifiche alla finestra elenco posizioni, che comprendono un nuovo nome
  (ora si chiama posizioni mouse) e layout, la visualizzazione delle
  coordinate mouse per un'etichetta e l'inclusione del nome dell'app attiva
  come parte del titolo.
* Dalle impostazioni posizione mouse, premendo invio su un'etichetta, il
  mouse si sposterà alla posizione salvata.
* Quando si rinomina una posizione mouse, verrà mostrato un messaggio di
  errore nel caso in cui esista già un'etichetta con lo stesso nome.
* Quando si cancellano o si puliscono i settaggi delle posizioni mouse, sarà
  necessario confermare con un sì.
* Cambiamenti alla funzione "vai a posizione", tra cui un nuovo nome (ora si
  chiama Nuova posizione del mouse) e la capacità di inserire le coordinate
  X e Y separatamente o utilizzando i tasti freccia su o giù.
* La finestra di dialogo mostrata quando si salva la posizione corrente del
  mouse ora mostra le coordinate per la posizione corrente del mouse.
* When saving positions, resolved an issue where NVDA may play error tones
  if the positions folder does not exist.

## Novità nella versione 1.4

* Rimosse le dipendenze Win32Api per rendere il componente compatibile con
  versioni passate e future di NVDA.

## Novità nella versione 1.0

* Versione iniziale.

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
