# Golden Cursor #

* Auteur : salah atair, Joseph Lee
* Télécharger [version stable][1]
* Compatibilité NVDA : 2019.3 et ultérieure

Cette extension vous permet de déplacer la souris à l'aide du clavier et de
sauvegarder la position de la souris pour les applications.

## Touche de commandes

* Contrôle+NVDA+L : afficher les positions de la souris sauvegardées pour
  une application, s'il y en a
* Maj+NVDA+l : sauvegarde un tag ou une étiquette pour la position actuelle
  de la souris dans l'application ayant actuellement le focus.
* Windows+NVDA+C : changer l'unité de mouvement de la souris.
* Windows+NVDA+R : basculer entre activer/désactiver la restriction de la
  souris.
* Windows+NVDA+S : basculer entre activer/désactiver l'annonce de la
  position de la souris en pixels.
* Windows+NVDA+J : déplacez la souris vers une position spécifique x et y.
* Windows+NVDA+P : annoncer la position de la souris.
* Windows+NVDA+M : basculer les flèches de souris entre activer ou
  désactiver.
* Windows+NVDA+touches fléchées (ou simplement les touches fléchées si les
  flèches de la souris sont activées) : déplacez la souris.

Remarque : ces gestes peuvent être réassignées via le dialogue Gestes de
commandes de NVDA sous la catégorie Golden Cursor.

## Notes

* Lors du partage des positions (tags), chaque partie doit utiliser la même
  résolution d'affichage.
* Pour une compatibilité maximale, vous devriez maximiser les fenêtres en
  appuyant sur Windows+flècheHaut.
* Lors du partage des positions, les étiquettes des positions existantes
  doivent être renommées.
* Les formats de position de la souris version 1.x et 2.x sont
  incompatibles.
* Pour exécuter les fonctions nécessitant l'utilisation des touches
  fléchées, désactivez d'abord les flèches de la souris.
* Lorsque vous supprimez des positions sauvegardées, s'il n'y a plus de
  positions sauvegardées, les positions de l'application seront effacées.

## Version 5.0

* Code source de l'extension modernisé pour le rendre compatible avec NVDA
  2021.1.
* Résolution de nombreux problèmes de style de code et de bugs potentiels
  avec Flake8.

## Version 4.0

* Nécessite NVDA 2019.3 ou ultérieure.
* Le dialogue des paramètres Golden Cursor a été remplacée par le panneau de
  paramètres Golden Cursor.

## Version 3.3

* Modifications internes pour prendre en charge les futures versions de
  NVDA.

## Version 3.2

* Cette extension est compatible avec NVDA 2018.3 (wxPython 4).

## Version 3.0

* Si vous utilisez NVDA 2018.2, les paramètres de l'extension seront trouvés
  dans le nouvel écran de paramètres multi-catégories sous la catégorie
  "Golden Cursor".

## Version 2.1

* Correction d'une erreur de décodage Unicode lors de la tentative de
  suppression du nom du tag.
* Empêcher plusieurs instances lors de l'ouverture de diverses boîtes de
  dialogue de l'extension.
* Amélioration de l'apparence de la liste des positions de la souris et des
  dialogues Sauter à la position.

## Version 2.0

* Nécessite NVDA 2017.3 et versions ultérieures.
* Le format de fichier de position est incompatible avec les versions
  1.x. Si le format de position 1.x est trouvé, les anciennes positions
  seront migrées vers le nouveau format lors de l'installation.
* Ajout d'une nouvelle boîte de dialogue dans les paramètres Golden Cursor
  dans le menu Préférences de NVDA pour configurer l'unité de mouvement de
  la souris et l'annonce des positions de la souris lors de ses
  déplacements.
* Divers messages de cette extension ont changé.
* Lorsque vous basculez entre différents paramètres, la tonalité de
  basculement ne sera plus entendue.
* Vous pouvez maintenant entrer dans le mode flèches de la souris où vous
  pouvez déplacer la souris en appuyant simplement sur les touches fléchées.
* Changements pour le dialogue de la liste des positions, y compris le
  nouveau nom (maintenant appelé Positions de la souris) et la disposition,
  affichant les coordonnées de la souris pour une étiquette et affichant le
  nom de l'application active dans le titre.
* À partir du dialogue Positions de la souris, appuyez sur Entrée sur une
  étiquette sauvegardée pour déplacer la souris vers l'emplacement
  sauvegardé.
* Lorsque vous renommez une position de la souris, un dialogue d'erreur
  s'affiche si une étiquette portant le même nom que le nouveau nom existe.
* Lorsque vous supprimez ou effacez les positions de la souris, vous devez
  maintenant répondre Oui avant que les positions ne soient supprimées et/ou
  effacées.
* Changements pour la fonction de saut de la souris, y compris un nouveau
  nom (maintenant appelé Nouvelle position de la souris) et sa capacité à
  entrer les coordonnées X et Y séparément ou en utilisant les touches
  flèche haut ou bas.
* Le dialogue affichée lors de la sauvegarde de la position actuelle de la
  souris affiche maintenant les coordonnées de l'emplacement actuel de la
  souris.
* Lors de l'enregistrement des positions, résolution d'un problème où NVDA
  peut émettre un son d'erreur si le dossier des positions n'existe pas.

## Version 1.4

* Suppression de la dépendance win32api pour le rendre compatible avec les
  versions passées et futures de NVDA.

## Version 1.0

* Première version.

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
