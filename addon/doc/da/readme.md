# Golden Cursor #

* Forfatter: Salah Atair, Joseph Lee
* Download [stabil version][1]
* NVDA-kompatibilitet: 2019.3 og derefter

Denne tilføjelse giver dig mulighed for at flytte musen ved hjælp af et
tastatur og gemme musepositioner til applikationer.

## Tastaturkommandoer:

* Ctrl+NVDA+L: Få vist gemte musepositioner for et program, hvis der er
  nogen.
* Skift+NVDA+L: Gem et tag eller en etiket for den aktuelle museposition i
  den aktuelt fokuserede applikation.
* Windows+NVDA+C: Skift musens bevægelsesenhed.
* Windows+NVDA+R: Skift tilstand for musebegrænsning.
* Windows+NVDA+S: Skifte rapportering af musens position i pixels.
* Windows+NVDA+J: Flyt musen til bestemte X og Y koordinater.
* Windows+NVDA+P: Rapportér musens aktuelle position.
* Windows+NVDA+M: Slå musepile til og fra.
* Windows+NVDA+Piletaster (eller blot piletasterne alene, hvis musepile er
  slået til): Flyt mus.

Bemærk: Disse kommandoer kan ændres ved brug af NVDA-dialogen
"Inputbevægelser" under kategorien "Golden Cursor".

## Bemærkninger

* Når der deles positioner (tags), skal hver part anvende samme
  skærmopløsning.
* For maksimal kompatibilitet bør du maksimere vinduer ved at trykke på
  Windows+Pil op.
* Når man deler positioner, skal eksisterende positionetiketter omdøbes.
* Version 1.x og 2.x muspositionsformater er inkompatible.
* For at udføre funktioner, der kræver brug af piletasterne, skal du først
  slå musepilene fra.
* Når der slettes gemte positioner, vil alle positioner for den aktuelle
  applikation ryddes, hvis der ikke længere eksistere gemte positioner.

## Version 5.0

* Moderniserede tilføjelsens kildekode for at gøre den kompatibel med NVDA
  2021.1.
* Løst mange problemer med kodningstil og potentielle fejl med Flake8.

## Version 4.0

* Kræver NVDA 2019.3 eller nyere.
* Golden Cursor-indstillingsdialogen er blevet erstattet af Golden
  Cursor-indstillingspanelet.

## Version 3.3

* Interne ændringer for at bedre kunne understøtte fremtidige versioner af
  NVDA.

## Version 3.2

* Tilføjelse er kompatibel med NVDA 2018.3 (wxPython 4).

## Version 3.0

* Hvis du bruger NVDA 2018.2, findes yderligere indstillinger i det nye
  indstillingspanel under kategorien "Golden Cursor".

## Version 2.1

* Rettede Unicode-afkodningsfejl, når du forsøger at slette tagnavne.
* Forhindre flere forekomster, når du åbner forskellige tilføjelsesdialoger.
* Forbedret udseende af muspositionsliste og hoppe til positionsdialoger.

## Version 2.0

* Kræver NVDA 2017.3 og senere.
* Positionfilformat er ukompatibelt med 1.x versioner. Hvis 1.x
  positionsformat er fundet, vil gamle positioner blive migreret til det nye
  format under installationen.
* Tilføjet en ny Golden Cursor-indstillingsdialog i NVDAs indstillingsmenu
  for at konfigurere musens bevægelsesenhed og annoncering af museposition,
  når musen bevæges.
* Forskellige meddelelser fra denne tilføjelse er ændret.
* Når du skifter forskellige indstillinger, bliver tonen ikke længere
  afspillet.
* Du kan nu indtaste musepile-tilstanden, hvor du kan flytte musen ved blot
  at trykke på piletasterne.
* Ændringer i positionslistedialog, herunder nyt navn (nu kaldet
  Musepositioner) og layout, der viser musekoordinater for en etiket og
  viser navnet på den aktive app som en del af titellinjen.
* Fra dialogboksen Musepositioner flyttes musen til den gemte placering ved
  at trykke på Enter på en gemt etiket.
* Når du omdøber en museposition, vises en fejldialog, hvis der findes en
  etiket med samme navn som det nye navn.
* Når du sletter eller rydder musepositioner, skal du nu svare Ja før
  positioner slettes og/eller ryddes.
* Ændringer i musehopfunktionen, herunder et nyt navn (nu kaldet Ny
  museposition) og evne til at indtaste X- og Y-koordinater hver for sig
  eller ved hjælp af pilene op og ned.
* Dialogboksen, der vises, når du gemmer den aktuelle museposition, viser nu
  koordinater for den aktuelle museplacering.
* Løst et problem der udløste en fejltone, når du gemmer positioner, hvis
  positionsmappen ikke findes.

## Version 1.4

* Fjernet win32api afhængighed for at gøre den kompatibel med tidligere og
  fremtidige versioner af NVDA.

## Version 1.0

* Første udgivelse.

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
