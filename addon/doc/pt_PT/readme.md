# Cursor Dourado #

* Autores: salah atair, Joseph Lee
* Baixar [versão estável] [1]
* Compatibilidade com o NVDA: 2019.3 e seguintes

Este extra permite mover o rato usando um teclado e guardar as posições do
rato para cada aplicação, individualmente.

## Comandos:

* Control+NVDA+L: mostra as posições do rato guardadas para uma aplicação,
  se as houver.
* Shift+NVDA+l: Guarda uma etiqueta ou um nível para a posição actual do
  rato, na aplicação actualmente focada. 
* Windows+NVDA+C: altera a unidade de movimento do rato.
* Windows+NVDA+R: alterna a restrição do rato.
* Windows+NVDA+S: alterna entre indicação de coordenadas da posição do rato.
* Windows+NVDA+J: move o rato para uma posição específica x e y.
* Windows+NVDA+P: informa a posição do rato.
* Windows+NVDA+M: activa ou desactiva o rato.
* Windows+NVDA+teclas de seta (ou apenas teclas de seta se as setas do rato
  estiverem activadas): move o rato.

Nota: estes comandos podem ser reatribuídos através do diálogo definir
comandos do NVDA sob a categoria Cursor Dourado.

## Notas

* Ao compartilhar ficheiros de posições (etiquetas), cada máquina deve usar
  a mesma resolução de ecrã.
* Para compatibilidade máxima, deve maximizar a janela, pressionando Windows
  + Seta para cima.
* Ao compartilhar ficheiros de posições, os rótulos de posição existentes
  devem ser renomeados.
* Os formatos de ficheiros de posição do rato 1.x e 2.x são incompatíveis.
* Para executar funções que exijam o uso das teclas de seta, desactive,
  primeiro, as setas do rato.
* Ao apagar posições guardadas, se não houver quaisquer outras para a mesma
  aplicação, o respectivo ficheiro de posições será excluído.

## Versão 5.0

* Código-fonte modernizado para o tornar compatível com o NVDA 2021.1.
* Resolvidos vários problemas de estilo de codificação e potenciais bugs com
  Flake8.

## Versão 4.0

* Requer o NVDA 2019.3 ou posterior.
* O diálogo de configurações do Cursor Dourado foi substituído pelo painel
  de configurações do Cursor Dourado.

## Versão 3.3

* Alterações internas para apoiar futuros lançamentos do NVDA.

## Versão 3.2

* O Extra é compatível com o  NVDA 2018.3 (wxPython 4).

## Versão 3.0

* Se estiver a usar o NVDA 2018.2, configurações adicionais serão
  encontradas no novo ecrã de configurações de várias categorias na
  categoria "Golden Cursor".

## Versão 2.1

* Corrigido o erro de decodificação unicode ao tentar apagar o nome da
  etiqueta.
* Impediu-se a abertura de várias instâncias do mesmo extra.
* Melhorou-se a aparência da lista de posições do rato e do diálogo de
  saltar para posições. 

## Versão 2.0

* Requer o NVDA 2017.3 ou posterior.
* O formato do ficheiro de posições é incompatível com as versões 1.x. Se o
  formato do ficheiro de posições 1.x for encontrado, as posições antigas
  serão migradas para o novo formato durante a instalação.
* Adicionada uma nova caixa de diálogo de Configurações do Cursor de Ouro no
  menu Preferências do NVDA para configurar a unidade de movimento do rato e
  o anúncio das posições do rato, quando este se move.
* Várias mensagens deste extra foram modificadas.
* Quando alternar entre várias configurações, o tom alternativo não será
  mais ouvido.
* Agora pode usar o modo setas do rato, através do qual pode mover o rato
  pressionando apenas as teclas de seta.
* Alterações na caixa de diálogo da lista de posições, incluindo o novo nome
  (agora chamado de Posições do rato) e layout, mostrando as coordenadas do
  rato para uma etiqueta e mostrando o nome da aplicação activa como parte
  do título.
* A partir da caixa de diálogo Posições do rato, pressionar Enter sobre uma
  etiqueta guardada moverá o rato para o local guardado.
* Ao renomear uma posição do rato, será mostrada uma caixa de diálogo de
  erro se já existir uma etiqueta com o mesmo nome.
* Ao apagar ou limpar as posições do rato, deve agora responder Sim antes
  que as posições sejam excluídas e / ou desmarcadas.
* Alterações no recurso de salto do rato, incluindo um novo nome (agora
  chamado de nova posição do rato) e capacidade de inserir as coordenadas X
  e Y separadamente ou usando as teclas de seta para cima ou para baixo.
* A caixa de diálogo mostrada ao guardar a posição actual do rato agora
  mostra as coordenadas para a localização atual do rato.
* Ao guardar as posições, resolveu-se  um problema em que o NVDA reproduzia
  tons de erro se a pasta de posições não existisse.

## Versão 1.4

* Foi removida a dependência win32api para torná-lo compatível com as
  versões passadas e futuras do NVDA.

## Versão 1.0

* Lançamento inicial.

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
