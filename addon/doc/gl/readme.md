# Golden Cursor #

* Autores: salah atair, Joseph Lee
* Descargar [versión de desenvolvemento][1]
* Compatibilidade con NVDA: 2019.3 en diante

Este complemento permíteche mover o rato usando un teclado e gardar as
posicións do rato para as aplicacións.

## Teclas de Ordes

* Control+NVDA+L: ver posicións gardadas do rato para unha aplicación se hai
  algunha.
* Shift+NVDA+l: garda unha tag ou unha etiqueta para a posición do rato
  actual na aplicación enfocada actualmente.
* Windows+NVDA+C: cambiar a unidade de movemento do rato.
* Windows+NVDA+R: conmuta a restricción do rato.
* Windows+NVDA+S: conmuta o anunciamento da posición do rato en pixeis.
* Windows+NVDA+J: mover o rato a unha posición x e y específica.
* Windows+NVDA+P: anunciar a posición do rato.
* Windows+NVDA+M: activar ou desactivar frechas do rato.
* Windows+NVDA+teclas de frechas (ou so teclas de frechas se frechas do rato
  está aceso): mover o rato.

Nota: estos xestos poden reasignarse dende o diálogo Xestos de Entrada no
menú Preferencias do NVDA na categoría Golden Cursor.

## Notas

* Cando se comparten posicións (tags), cada parte debería usar a mesma
  resolución de pantalla.
* Para compatibilidade máxima, deberías maximizar windows premendo
  Windows+frecha arriba.
* Ó compartiren posicións, as etiquetas de posicións existentes deberían
  renomearse.
* Os formatos das versións 1.x e 2.x de posicións do rato son incompatibles.
* Para realizar funcións que requiran usar teclas de frechas, primeiro
  desactiva frechas do rato.
* Ao se borrar posicións gardadas, se non quedan máis posicións gardadas,
  limparanse as da aplicación.

## Versión 5.0

* ´Modernizado o código fonte do complemento para facelo compatible con NVDA
  2021.1.
* Resoltos varios problemas e erros potenciais no estilo do código con
  flake8.

## Versión 4.0

* Require do NVDA 2019.3 ou posterior.
* O diálogo de opcións de Golden Cursor reemprazouse polo panel de opcións
  de Golden Cursor.

## Versión 3.3

* Trocos internos para soportar versións futuras de NVDA.

## Versión 3.2

* O complemento é compatible con NVDA 2018.3 (WxPython 4).

## Versión 3.0

* Se se usa o NVDA 2018.2, a configuración do complemento atoparase na nova
  pantalla multicategoría Opcións na categoría "Golden Cursor".

## Versión 2.1

* Arranxado un erro de decodificación unicode ao se teclear para borrar o
  nome de tag.
* Prevéñense instancias múltiples ao se abrir varios diálogos do
  complemento.
* Mellorada a aparienza dos diálogos listar posicións do rato e saltar a
  posición.

## Versión 2.0

* Requírese do NVDA 2017.3 e posterior.
* O formato do ficheiro de posición é incompatible co das versións 1.x. Se
  se atopa un formato de posición 1.x, as posicións vellas migraranse ao
  novo formato durante a instalación.
* Engadido un novo diálogo Opcións de Golden Cursor no menú Preferencias do
  NVDA para configurar a unidade de movemento do rato e o anunciado de
  posicións do rato segundo este se mova.
* Cambiáronse varias mensaxes deste complemento.
* Ao se conmutar varias opcións, o ton de conmutación xa non se escoitará.
* Agora podes entrar no modo frechas do rato onde podes mover o rato
  premendo só teclas de frechas.
* Cambios ao diálogo listar posicións, incluindo nome novo (agora chamado
  Posicións do rato) e deseño, amosando coordenadas do rato para unha
  etiqueta, e amosando o nome da aplicación activa coma parte do título.
* Dende o diálogo posicións do rato, premendo intro sobre unha etiqueta
  gardada moverase o rato á localización gardada.
* Ao se renomear unha posición do rato, amosarase un diálogo de erro se
  existe unha etiqueta co mesmo nome  que o nome novo.
* Ao se borrar e limpar posicións do rato, agora debes responder si antes de
  que as posicións se borren e/ou se limpen.
* Cambios na característica salto do rato, incluindo un novo nome (agora
  chamada Nova posición do raton) e a capacidade de introducir coordenadas X
  e Y separadamente ou usando as teclas de frecha arriba ou abaixo.
* O diálogo amosado ao se gardar a posición actual do rato agora amosa as
  coordenadas para a posición actual do rato.
* Ao se gardar posicións, resolveuse un problema onde o NVDA podería
  reproducir tons de erro se o cartafol de posicións non existe.

## Versión 1.4

* Quitada a dependencia win32api para facelo compatible con versións pasadas
  e futuras de NVDA.

## Versión 1.0

* Versión inicial.

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
