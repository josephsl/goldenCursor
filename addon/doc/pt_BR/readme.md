# Cursor de ouro #

* Autor: salah atair, Joseph Lee
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]

Este complemento possibilita mover o mouse usando o teclado e salvar
posições do mouse em aplicativos.

## Comandos de teclas

* Control+NVDA+L: ver as posições salvas do mouse para um aplicativo, se
  houver.
* Shift+NVDA+L: salva uma tag ou um rótulo para a posição atual do mouse no
  aplicativo atualmente focalizado.
* Windows+NVDA+C: muda a unidade de movimento do mouse.
* Windows+NVDA+R: Alterna a restrição do mouse.
* Windows+NVDA+S: alterna o anúncio da posição do mouse em pixels.
* Windows+NVDA+J: move o mouse para uma posição específica x e y.
* Windows+NVDA+P: anuncia a posição do mouse.
* Windows+NVDA+M: ativa ou desativa as setas do mouse.
* Windows+NVDA+setas (ou apenas as teclas de seta se as setas do mouse
  estiverem ativadas): move o mouse.

Nota: Estes gestos podem ser reatribuídos via diálogo de Gestos de Entrada —
Definir comandos — do NVDA na categoria Cursor Dourado.

## Notas

* Ao compartilhar posições (tags), cada parte — usuário — deve usar a mesma
  resolução de tela.
* Para maior compatibilidade, deve-se maximizar a janela pressionando
  Windows+seta acima.
* Ao compartilhar posições, os rótulos de posições existentes devem ser
  renomeados.
* Os formatos de posição do mouse da versão 1.x e 2.x são incompatíveis.
* Para executar funções que exigem o uso de teclas de seta, desative as
  setas do mouse primeiro.
* Ao excluir posições salvas, se não houver posições salvas, as posições do
  aplicativo serão apagadas.

## Versão 3.0

* Se estiver usando o NVDA 2018.2, configurações do complemento serão
  encontradas na nova tela de configurações de multicategorias na categoria
  "Cursor Dourado".

## Versão 2.1

* Corrigido erro de decodificação de unicode ao tentar excluir o nome da
  tag.
* Impede várias instâncias ao abrir várias caixas de diálogo de complemento.
* Melhor aparência da lista de posições do mouse e saltar para diálogos de
  posição.

## Versão 2.0

* Requer o NVDA 2017.3 e posteriores.
* O formato do arquivo de posição é incompatível com as versões 1.x. Se o
  formato de posição 1.x for encontrado, as posições antigas serão migradas
  para o novo formato durante a instalação.
* Adicionada uma nova caixa de diálogo Configurações do Cursor Dourado no
  menu Preferências do NVDA para configurar a unidade de movimento do mouse
  e o anúncio das posições do mouse à medida que o mouse se move.
* Várias mensagens deste complemento foram alteradas.
* Ao alternar várias configurações, o tom de alternância não será mais
  ouvido.
* Agora você pode entrar no modo de setas do mouse, onde você pode mover o
  mouse pressionando apenas as teclas de seta.
* Alterações na caixa de diálogo de lista de posições, incluindo novo nome
  (agora chamado de Posições do Mouse) e leiaute, exibindo as coordenadas do
  mouse para um rótulo e mostrando o nome do aplicativo ativo como parte do
  título.
* Na caixa de diálogo Mouse Positions, pressionar Enter em um rótulo salvo
  moverá o mouse para o local salvo.
* Ao renomear a posição do mouse, uma caixa de diálogo de erro será mostrada
  se houver um rótulo com o mesmo nome do novo nome.
* Ao excluir ou limpar posições do mouse, você deve responder Sim antes que
  as posições sejam excluídas e/ou apagadas.
* Altera o recurso de salto do mouse, incluindo um novo nome (agora chamado
  de Nova posição do mouse) e a capacidade de inserir as coordenadas X e Y
  separadamente ou usando as teclas de seta para cima ou para baixo.
* A caixa de diálogo mostrada ao salvar a posição atual do mouse agora
  mostra as coordenadas da localização atual do mouse.
* Ao salvar posições, resolveu um problema em que o NvDA pode reproduzir
  tons de erro se a pasta de posições não existir.

## Versão 1.4

* Removido dependência win32api para torná-lo compatível com versões
  passadas e futuras do NVDA.

## Versão 1.0

* Versão inicial.

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev
