# Golden Cursor #

* Tekijät: Salah Atair ja Joseph Lee
* Lataa [vakaa versio][1]
* Yhteensopivuus: NVDA 2019.3 ja uudemmat

Tämän lisäosan avulla voit siirtää hiirtä näppäimistöä käyttäen sekä
tallentaa hiiren sijainteja sovelluksille.

## Näppäinkomennot

* Ctrl+NVDA+L: näytä sovellukselle tallennetut hiiren sijainnit.
* Vaihto+NVDA+L: tallenna tunniste tai selite nykyiselle hiiren sijainnille
  aktiivisessa sovelluksessa.
* Win+NVDA+C: muuta hiiren siirtämisen yksikköä.
* Win+NVDA+R: Ota hiiren rajoittaminen käyttöön tai poista se käytöstä.
* Win+NVDA+S: Ota hiiren sijainnin puhuminen pikseleinä käyttöön tai poista
  se käytöstä.
* Win+NVDA+J: siirrä hiiri tiettyyn x- ja y-sijaintiin.
* Win+NVDA+P: ilmoita hiiren sijainti.
* Win+NVDA+M: ota hiirinuolet käyttöön tai poista ne käytöstä.
* Win+NVDA+Nuolinäppäimet (tai pelkät nuolinäppäimet, mikäli hiirinuolet
  ovat käytössä): siirrä hiirtä.

Huom: Näiden komentojen uudelleenmäärittäminen on mahdollista
Syötekomennot-valintaikkunasta Golden Cursor -kategorian alta.

## Huomautuksia

* Käyttäjien tulisi sijainteja (tunnisteita) jakaessaan käyttää samaa näytön
  tarkkuutta.
* Ikkunat tulisi suurentaa parhaimman yhteensopivuuden varmistamiseksi
  painamallla Win+Nuoli ylös.
* Olemassa olevat sijainnit tulisi nimetä uudelleen sijainteja jaettaessa.
* Versio 1.x ja 2.x:n hiirisijaintien muodot eivät ole yhteensopivia
  keskenään.
* Suorita nuolinäppäinten käyttöä edellyttäviä toimintoja poistamalla ensin
  hiirinuolet käytöstä.
* Mikäli tallennettuja sijainteja ei ole jäljellä niitä poistettaessa,
  sovelluksen sijainnit tyhjennetään.

## Versio 5.0

* Lisäosa tehty yhteensopivaksi NVDA 2021.1:n kanssa lähdekoodia
  uudistamalla.
* Ratkaistu useita koodaustyylin ongelmia ja mahdollisia bugeja Flake8:lla.

## Versio 4.0

* Vaatii NVDA 2019.3:n tai uudemman.
* Lisäosan asetusvalintaikkuna on korvattu asetuspaneelilla.

## Versio 3.3

* Sisäisiä muutoksia tulevien NVDA-versioiden tukemiseksi.

## Versio 3.2

* Lisäosa on NVDA 2018.3 (wxPython 4) -yhteensopiva.

## Versio 3.0

* NVDA 2018.2:ta käytettäessä lisäosan asetukset löytyvät uudesta
  monikategoriaisesta asetusruudusta kohdasta "Golden Cursor".

## Versio 2.1

* Korjattu Unicode-dekoodausvirhe yritettäessä poistaa tunnisteen nimeä.
* Estetty lisäosan valintaikkunoiden avaaminen useaan kertaan.
* Paranneltu hiiren sijaintiluettelo- sekä sijaintiin siirtymisen
  valintaikkunoiden ulkoasua.

## Versio 2.0

* Edellyttää NVDA 2017.3:a tai uudempaa.
* Sijaintitiedoston muoto ei ole yhteensopiva 1.x-versioiden kanssa. Mikäli
  vanhoja sijainteja löytyy, ne päivitetään uuteen muotoon lisäosan
  asennuksen aikana.
* Lisätty NVDA:n Asetukset-valikkoon uusi Golden Cursorin
  asetusvalintaikkuna, josta on mahdollista määrittää hiiren siirtämisen
  yksikkö sekä sijainnin puhuminen hiirtä siirrettäessä.
* Useat tämän lisäosan ilmoituksista ovat muuttuneet.
* Äänimerkkiä ei enää kuulu eri asetuksia muutettaessa.
* Voit nyt siirtyä hiirinuolet-tilaan, jossa hiirtä on mahdollista siirtää
  pelkkiä nuolinäppäimiä käyttäen.
* Muutoksia Sijainnit-valintaikkunaan, mukaan lukien uusi nimi (Hiiren
  sijainnit), ulkoasu, hiiren koordinaattien näyttäminen selitteelle sekä
  aktiivisen sovelluksen nimen näyttäminen osana ikkunan nimeä.
* Enterin painaminen tallennetun selitteen kohdalla Hiiren sijainnit
  -valintaikkunassa siirtää hiiren tallennettuun sijaintiin.
* Hiiren sijaintia uudelleennimettäessä näytetään virhevalintaikkuna, mikäli
  samanniminen selite on jo olemassa.
* Hiiren sijainteja poistettaessa tai tyhjennettäessä on vastattava Kyllä,
  ennen kuin sijainnit poistetaan ja/tai tyhjennetään.
* Muutoksia Siirry sijaintiin -valintaikkunaan, mukaan lukien uusi nimi
  (Uusi hiiren sijainti) sekä mahdollisuus syöttää X- ja Y-koordinaatit
  erikseen tai Nuoli ylös/alas-näppäimiä käyttäen.
* Nykyistä hiiren sijaintia tallennettaessa näytettävä valintaikkuna näyttää
  nyt sijainnin koordinaatit.
* Ratkaistu ongelma, jossa NVDA saattaa toistaa virheääniä sijainteja
  tallennettaessa, mikäli sijaintien kansiota ei ole olemassa.

## Versio 1.4

* Lisäosa tehty yhteensopivaksi vanhempien ja tulevien NVDA-versioiden
  kanssa poistamalla win32api-riippuvuus.

## Versio 1.0

* Ensimmäinen versio.

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
