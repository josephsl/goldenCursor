# 金色光标 #

* 作者: salah atair, Joseph Lee
* 下载[稳定版][1]
* NVDA compatibility: 2019.3 and beyond
* Download [older version][3] compatible with NVDA 2019.2.1 and earlier

该附加插件允许您使用键盘移动鼠标并为应用程序保存鼠标位置。

## 快捷键

* Control+NVDA+L: 查看应用程序保存的鼠标位置（如果有）。
* Shift+NVDA+l: 保存当前焦点应用程序中鼠标位置的标签。
* Windows+NVDA+C: 改变鼠标移动单位。
* Windows+NVDA+R: 切换鼠标限制。
* Windows+NVDA+S: 以像素为单位报告切换鼠标的位置。
* Windows+NVDA+J: 将鼠标移动到特定的x和y位置。
* Windows+NVDA+P: 报告鼠标位置。
* Windows+NVDA+M: sswitch鼠标箭头打开或关闭。
* Windows + NVDA +箭头键（当鼠标箭头打开时只是方向键）：关闭则移动鼠标。

注意: 这些手势可以通过Golden Cursor类别下的NVDA输入手势对话框重新设置。

## 注意

* 在共享位置（标签）时，每个用户应使用相同的显示分辨率。
* 为了获得最大的兼容性，您应该通过按Windows +向上箭头来最大化窗口。
* 分享位置时，现有位置标签应重新命名。
* * 版本1.x和2.x鼠标位置格式不兼容。
* 要执行需要使用箭头键的功能，请先关闭鼠标箭头。
* 删除保存的位置时，如果没有保存的位置，应用程序的位置将被清除。

## Version 4.0

* Requires NVDA 2019.3 or later.
* Golden Cursor settings dialog has been replaced by Golden Cursor settings
  panel.

## Version 3.3

* Internal changes to support future NVDA releases.

## 版本3.2

* 现在插件与NVDA 2018.3（wxPython 4）兼容。

## 版本3.0

* 如果使用NVDA 2018.2，则可以在“金色光标”类别下的新的设置见面中找到附加设置。

## 版本2.1

* 修正试图删除标签名称时的unicode解码错误。
* 打开各种附加对话框时防止出现多个实例。
* 改进了鼠标位置列表的窗口并跳转到位置对话框。

## 版本2.0

* 需要NVDA 2017.3及更高版本。
* 位置文件格式与1.x版本不兼容。如果找到1.x位置格式，则旧位置将在安装期间迁移到新格式。
* 在NVDA的“首选项”菜单中添加了一个新的金色光标设置对话框，用于配置鼠标移动单位以及鼠标移动时鼠标位置的项目。
* 来自此附加组件的各种消息已更改。
* 切换各种设置时，切换音将不再被听到。
* 您现在可以进入鼠标箭头模式，只需按方向键即可移动鼠标。
* 位置列表对话框的更改，包括新名称（现称为“鼠标位置”）和布局，显示标签的鼠标坐标以及将活动应用程序的名称显示为标题的一部分。
* 从鼠标位置对话框中，按保存的标签上的Enter键将鼠标移动到保存的位置。
* 重命名鼠标位置时，如果存在与新名称相同名称的标签，则会显示错误对话框。
* 删除或清除鼠标位置时，现在必须在删除和/或清除位置之前回答是。
* 改变鼠标跳跃功能，包括一个新名称（现在称为新鼠标位置）和分别输入X和Y坐标或使用向上或向下箭头键的能力。
* 保存当前鼠标位置时显示的对话框现在显示当前鼠标位置的坐标。
* 保存位置时，解决了位置文件夹不存在时NvDA可能播放错误提示音的问题。

## 版本1.4

* 删除了win32api的依赖，使其与过去和未来版本的NVDA兼容。

## 版本1.0

* 发布初始版本。

[[!tag stable dev]]

[1]: https://addons.nvda-project.org/files/get.php?file=gc

[2]: https://addons.nvda-project.org/files/get.php?file=gc-dev

[3]: https://addons.nvda-project.org/files/get.php?file=gc-2019
