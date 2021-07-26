# Golden Cursor #

* Autores: salah atair, Joseph Lee
* Descargar [versión de desarrollo][1]
* Compatibilidad con NVDA: 2019.3 y versiones posteriores

Este complemento te permite mover el ratón utilizando un teclado y guardar
las posiciones del ratón para las aplicaciones.

## Teclas de Órdenes

* Control+NVDA+L: ver posiciones guardadas del ratón para una aplicación si
  hay alguna.
* Shift+NVDA+l: guarda una marca o una etiqueta para la posición del ratón
  actual en la aplicación enfocada actualmente.
* Windows+NVDA+C: cambiar la unidad de movimiento del ratón.
* Windows+NVDA+R: conmuta la restricción del ratón.
* Windows+NVDA+S: conmuta el anunciado del ratón en píxeles.
* Windows+NVDA+J: mover el ratón a una posición x e y específica.
* Windows+NVDA+P: anunciar la posición del ratón.
* Windows+NVDA+M: activar o desactivar flechas del ratón.
* Windows+NVDA+teclas de flechas (o solo teclas de flechas si flechas de
  ratón está activado): mover ratón.

Nota: estos gestos pueden reasignarse desde el diálogo Gestos de Entrada en
el menú Preferencias de NVDA en la categoría  Golden Cursor.

## Notas

* Cuando se comparten posiciones(tags), cada parte debería utilizar la misma
  resolución de pantalla.
* Para compatibilidad máxima, deberías maximizar windows pulsando
  Windows+flecha arriba.
* Al compartir posiciones, las etiquetas de posiciones existentes deberían
  renombrarse.
* Los formatos de las versiones 1.x y 2.x de posiciones del ratón son
  incompatibles.
* Para realizar funciones que requieran utilizar teclas de flechas, primero
  desactiva flechas del ratón.
* Al eliminar posiciones guardadas, si no quedan más posiciones guardadas,
  se limpiarán las de la aplicación.

## Versión 5.0

* Se ha modernizado el código fuente del complemento para hacerlo compatible
  con NVDA 2021.1.
* Se han resuelto muchos problemas de estilo del código y fallos potenciales
  con Flake8.

## Versión 4.0

* Se requiere de NVDA 2019.3 o posterior.
* El diálogo de opciones de Golden Cursor se ha sustituido por el panel de
  opciones de Golden Cursor.

## Versión 3.3

* Cambios internos para dar soporte a versiones futuras de NVDA.

## Versión 3.2

* El complemento es compatible con NVDA 2018.3 (WXPython 4).

## Versión 3.0

* Si se utiliza NVDA 2018.2, la configuración del complemento se encontrará
  en la nueva pantalla multicategoría Opciones en la categoría "Golden
  Cursor".

## Versión 2.1

* Corregido un error de decodificación unicode al teclear para eliminar el
  nombre de tag.
* Se previenen instancias múltiples al abrir varios diálogos del
  complemento.
* Mejorada la apariencia de los diálogos listar posiciones del ratón y
  saltar a posición.

## Versión 2.0

* Se requiere de NVDA 2017.3 y posterior.
* El formato del fichero de posición es incompatible con el de las versiones
  1.x. Si se encuentra un formato de posición 1.x, las posiciones antiguas
  se migrarán al nuevo formato durante la instalación.
* Añadido un nuevo diálogo Opciones de Golden Cursor en el menú Preferencias
  de NVDA para configurar la unidad de movimiento del ratón y el anunciado
  de posiciones del ratón según éste se mueva.
* Se han cambiado varios mensajes de este complemento.
* Al conmutar varias opciones, el tono de conmutación ya no se escuchará.
* Ahora puedes entrar en el modo flechas del ratón donde puedes mover el
  ratón pulsando sólo teclas de flechas.
* Cambios al diálogo listar posiciones, incluyendo nombre nuevo (ahora
  llamado Posiciones del ratón) y diseño, mostrando coordenadas del ratón
  para una etiqueta, y mostrando el nombre de la aplicación activa como
  parte del título.
* Desde el diálogo posiciones del ratón, pulsando intro sobre una etiqueta
  guardada se moverá el ratón a la localización guardada.
* Al renombrar una posición del ratón, se mostrará un diálogo de error si
  existe una etiqueta con el mismo nombre  que el nombre nuevo.
* Al eliminar o limpiar posiciones del ratón, ahora debes responder sí antes
  de que las posiciones se eliminen y/o se limpien.
* Cambios en la característica salto del ratón, incluyendo un nuevo nombre
  (ahora llamada Nueva posición del ratón) y la capacidad de introducir
  coordenadas X e Y separadamente o utilizando las teclas de flecha arriba o
  abajo.
* El diálogo mostrado al guardar la posición actual del ratón ahora muestra
  las coordenadas para la posición actual del ratón.
* Al guardar posiciones, se resolvió un problema donde NVDA podría
  reproducir tonos de error si la carpeta de posiciones no existe.

## Versión 1.4

* Eliminada la dependencia win32api para hacerlo compatible con versiones
  pasadas y futuras de NVDA.

## Versión 1.0

* Versión inicial.

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
