# Автоматически добавляю недостающие ключи из ru во все языки (en, zh, ja, fr, de), копируя значения. Существующие переводы не трогаю.
hotkeys_translations = {
    # ----- ENGLISH TRANSLATE -----
    "en": {
        "introduction_topic": """
<span size='18000' weight='bold'>Introduction to Hotkeys</span>

Linux hotkeys help you work faster and more efficiently. This section covers the most important shortcuts for beginners and how to use them in different environments.
""",
        "gnomehotk": """
<span size='18000' weight='bold'>GNOME Hotkeys</span>

• <span color='#00B7EB'><b>Super</b></span>: Open Activities Overview to search for apps, windows, or workspaces.
• <span color='#00B7EB'><b>Alt + Tab</b></span>: Switch between open applications.
• <span color='#00B7EB'><b>Alt + `</b></span>: Switch between windows of the same application.
• <span color='#00B7EB'><b>Super + Tab</b></span>: Switch between applications with visual effect.
• <span color='#00B7EB'><b>Alt + F2</b></span>: Open the quick command input bar.
• <span color='#00B7EB'><b>Super + L</b></span>: Lock the screen.
• <span color='#00B7EB'><b>Ctrl + Alt + Delete</b></span>: Open the logout/restart/shutdown menu.
• <span color='#00B7EB'><b>Print Screen</b></span>: Take a screenshot (saved to Pictures or clipboard).
• <span color='#00B7EB'><b>Super + Print Screen</b></span>: Open the area selection screenshot tool.

<span size='large' weight='bold'>Window Management</span>

• <span color='#00B7EB'><b>Super + ←/→</b></span>: Snap window to left/right half of the screen.
• <span color='#00B7EB'><b>Super + ↑</b></span>: Maximize window.
• <span color='#00B7EB'><b>Super + ↓</b></span>: Minimize/restore window.
• <span color='#00B7EB'><b>Alt + F4</b></span>: Close the active window.
• <span color='#00B7EB'><b>Alt + Space</b></span>: Open the window menu.
• <span color='#00B7EB'><b>Super + M</b></span>: Show/hide notifications and calendar.

<span size='large' weight='bold'>Workspaces</span>

• <span color='#00B7EB'><b>Super + Page Up/Page Down</b></span>: Switch between workspaces.
• <span color='#00B7EB'><b>Ctrl + Alt + ←/→</b></span>: Switch between workspaces (in some distributions).
• <span color='#00B7EB'><b>Super + Shift + Page Up/Page Down</b></span>: Move window to another workspace.
• <span color='#00B7EB'><b>Super + T</b></span>: Open a new terminal (Ubuntu).

<span size='large' weight='bold'>Search and Apps</span>

• <span color='#00B7EB'><b>Super + A</b></span>: Show the list of applications.
• <span color='#00B7EB'><b>Super + S</b></span>: Open search (find files, apps, settings).
• <span color='#00B7EB'><b>Super + number (1–9)</b></span>: Launch or switch to a pinned app on the panel.
""",
        "kdehotk": """
<span size='18000' weight='bold'>KDE Hotkeys</span>

• <span color='#00B7EB'><b>Super</b></span>: Open the application menu.
• <span color='#00B7EB'><b>Alt + Tab</b></span>: Switch between windows (with visual effect).
• <span color='#00B7EB'><b>Alt + `</b></span>: Switch between windows of the same app.
• <span color='#00B7EB'><b>Alt + F2</b></span>: Open Krunner (search apps/files/commands).
• <span color='#00B7EB'><b>Super + L</b></span>: Lock the screen.
• <span color='#00B7EB'><b>Ctrl + Alt + Delete</b></span>: Open the session end menu.
• <span color='#00B7EB'><b>Print Screen</b></span>: Take a screenshot with Spectacle.
• <span color='#00B7EB'><b>Super + Print Screen</b></span>: Screenshot the active window.
• <span color='#00B7EB'><b>Ctrl + Alt + T</b></span>: Open terminal (Konsole).

<span size='large' weight='bold'>Window Management</span>

• <span color='#00B7EB'><b>Alt + F3</b></span>: Open the window menu.
• <span color='#00B7EB'><b>Alt + F4</b></span>: Close the active window.
• <span color='#00B7EB'><b>Super + ←/→</b></span>: Snap window to left/right.
• <span color='#00B7EB'><b>Super + ↑</b></span>: Maximize window.
• <span color='#00B7EB'><b>Super + ↓</b></span>: Minimize window.
• <span color='#00B7EB'><b>Ctrl + F10</b></span>: Minimize/restore all windows.
• <span color='#00B7EB'><b>Super + T</b></span>: Tile window layout (if enabled).

<span size='large' weight='bold'>Workspaces and Activities</span>

• <span color='#00B7EB'><b>Ctrl + F1/F2/F3/F4</b></span>: Switch between virtual desktops (up to 4).
• <span color='#00B7EB'><b>Super + Tab</b></span>: Switch desktops with effect.
• <span color='#00B7EB'><b>Super + Q</b></span>: Open activities overview.
• <span color='#00B7EB'><b>Ctrl + Alt + ←/→</b></span>: Switch between workspaces.
• <span color='#00B7EB'><b>Super + Shift + arrow</b></span>: Move window to another desktop.

<span size='large' weight='bold'>Search and Apps</span>

• <span color='#00B7EB'><b>Super + number (1–9)</b></span>: Launch/switch to a pinned app on the taskbar.
• <span color='#00B7EB'><b>Alt + F1</b></span>: Open an alternative app menu (if set).
• <span color='#00B7EB'><b>Super + R</b></span>: Quickly run a command via Krunner.
• <span color='#00B7EB'><b>Super + E</b></span>: Open file manager (Dolphin).

<span size='large' weight='bold'>KDE Unique Features</span>

• <span color='#00B7EB'><b>Super + V</b></span>: Open clipboard history.
• <span color='#00B7EB'><b>Super + D</b></span>: Show/hide desktop.
• <span color='#00B7EB'><b>Ctrl + Alt + Shift</b></span>: Enable effect overview mode.
• <span color='#00B7EB'><b>Super + G</b></span>: Enable/disable gaming window layout.
""",
        "terminalhotk": """
<span size='18000' weight='bold'>Terminal Hotkeys</span>

Key operations for efficient work in the Linux terminal: command editing, navigation, process control, and more.
"""
    },

    # ----- RUSSIAN TRANSLATE -----
    "ru": {
        "introduction_topic": """Добро пожаловать в главу по работе с горячими клавишами в операционной системе Linux!

В данной главе будут подсказки по использованию горячих клавиш в различных графических окружениях,программах и утилитах первой необходимости. Все необходимые сочетания клавиш всегда будут под рукой и в любой момент вы сможете подсмотреть,заучивать необязательно!""",


        "gnomehotk": """• <span color="#00B7EB"><b>Super</b></span>: Открыть обзор (Activities Overview) для поиска приложений, окон или рабочих столов.
• <span color="#00B7EB"><b>Alt + Tab</b></span>: Переключение между открытыми приложениями.
• <span color="#00B7EB"><b>Alt + `</b></span>: Переключение между окнами одного приложения.
• <span color="#00B7EB"><b>Super + Tab</b></span>: Переключение между приложениями с визуальным эффектом.
• <span color="#00B7EB"><b>Alt + F2</b></span>: Открыть строку для быстрого ввода команды.
• <span color="#00B7EB"><b>Super + L</b></span>: Заблокировать экран.
• <span color="#00B7EB"><b>Ctrl + Alt + Delete</b></span>: Открыть меню выхода (выход, перезагрузка, выключение).
• <span color="#00B7EB"><b>Print Screen</b></span>: Сделать скриншот (сохранение в «Изображения» или буфер обмена).
• <span color="#00B7EB"><b>Super + Print Screen</b></span>: Открыть инструмент для выбора области скриншота.

<span size="large" weight="bold"> Управление окнами </span>

• <span color="#00B7EB"><b>Super + стрелка влево/вправо</b></span>: Прикрепить окно к левой/правой половине экрана.
• <span color="#00B7EB"><b>Super + стрелка вверх</b></span>: Развернуть окно на весь экран.
• <span color="#00B7EB"><b>Super + стрелка вниз</b></span>: Свернуть/восстановить окно.
• <span color="#00B7EB"><b>Alt + F4</b></span>: Закрыть активное окно.
• <span color="#00B7EB"><b>Alt + Space</b></span>: Открыть меню окна (свернуть, закрыть и т.д.).
• <span color="#00B7EB"><b>Super + M</b></span>: Показать/скрыть уведомления и календарь.

<span size="large" weight="bold"> Рабочие столы </span>

• <span color="#00B7EB"><b>Super + Page Up/Page Down</b></span>: Переключение между рабочими столами.
• <span color="#00B7EB"><b>Ctrl + Alt + ←/→</b></span>: Переключение между рабочими столами (в некоторых дистрибутивах).
• <span color="#00B7EB"><b>Super + Shift + Page Up/Page Down</b></span>: Переместить окно на другой рабочий стол.
• <span color="#00B7EB"><b>Super + T</b></span>: Открыть новый терминал (в Ubuntu).

<span size="large" weight="bold"> Поиск и приложения </span>

• <span color="#00B7EB"><b>Super + A</b></span>: Показать список приложений в обзоре.
• <span color="#00B7EB"><b>Super + S</b></span>: Открыть поиск (вводите запрос для поиска файлов, приложений, настроек).
• <span color="#00B7EB"><b>Super + цифра (1–9)</b></span>: Запустить или переключиться на приложение, закрепленное в панели (по порядку).
""",
        
        
        "kdehotk": """<span size="large" weight="bold"> Общие действия</span>

• <span color="#00B7EB"><b>Super</b></span>: Открыть меню приложений (Kicker или Kickoff).
• <span color="#00B7EB"><b>Alt + Tab</b></span>: Переключение между открытыми окнами (с визуальным эффектом).
• <span color="#00B7EB"><b>Alt + `</b></span> (тильда): Переключение между окнами одного приложения.
• <span color="#00B7EB"><b>Alt + F2</b></span>: Открыть Krunner (поиск приложений, файлов, команд).
• <span color="#00B7EB"><b>Super + L</b></span>: Заблокировать экран.
• <span color="#00B7EB"><b>Ctrl + Alt + Delete</b></span>: Открыть меню завершения сеанса (выход, перезагрузка, выключение).
• <span color="#00B7EB"><b>Print Screen</b></span>: Открыть Spectacle для создания скриншота.
• <span color="#00B7EB"><b>Super + Print Screen</b></span>: Сделать скриншот активного окна.
• <span color="#00B7EB"><b>Ctrl + Alt + T</b></span>: Открыть терминал (Konsole по умолчанию).

<span size="large" weight="bold"> Управление окнами </span>

• <span color="#00B7EB"><b>Alt + F3</b></span>: Открыть меню окна (свернуть, закрыть, прикрепить).
• <span color="#00B7EB"><b>Alt + F4</b></span>: Закрыть активное окно.
• <span color="#00B7EB"><b>Super + стрелка влево/вправо</b></span>: Прикрепить окно к левой/правой половине экрана.
• <span color="#00B7EB"><b>Super + стрелка вверх</b></span>: Развернуть окно на весь экран.
• <span color="#00B7EB"><b>Super + стрелка вниз</b></span>: Свернуть окно.
• <span color="#00B7EB"><b>Ctrl + F10</b></span>: Свернуть/развернуть все окна (показать рабочий стол).
• <span color="#00B7EB"><b>Super + T</b></span>: Плиточное расположение окон (если включено).

<span size="large" weight="bold"> Рабочие столы и активности </span>

• <span color="#00B7EB"><b>Ctrl + F1/F2/F3/F4</b></span>: Переключение между виртуальными рабочими столами (по умолчанию до 4).
• <span color="#00B7EB"><b>Super + Tab</b></span>: Переключение между рабочими столами с эффектом (аналог Alt + Tab для окон).
• <span color="#00B7EB"><b>Super + Q</b></span>: Открыть обзор активностей (Activities).
• <span color="#00B7EB"><b>Ctrl + Alt + стрелки влево/вправо</b></span>: Переключение между рабочими столами.
• <span color="#00B7EB"><b>Super + Shift + стрелки</b></span>: Переместить окно на другой рабочий стол.

<span size="large" weight="bold"> Поиск и приложения </span>

• <span color="#00B7EB"><b>Super + цифра (1–9)</b></span>: Запустить/переключиться на приложение, закрепленное в панели задач.
• <span color="#00B7EB"><b>Alt + F1</b></span>: Открыть альтернативное меню приложений (если настроено).
• <span color="#00B7EB"><b>Super + R</b></span>: Быстрый запуск команды через Krunner (аналог Alt + F2).
• <span color="#00B7EB"><b>Super + E</b></span>: Открыть файловый менеджер (Dolphin).

<span size="large" weight="bold"> Уникальные функции KDE </span>

• <span color="#00B7EB"><b>Super + V</b></span>: Открыть буфер обмена (история скопированного текста).
• <span color="#00B7EB"><b>Super + D</b></span>: Показать/скрыть рабочий стол.
• <span color="#00B7EB"><b>Ctrl + Alt + Shift</b></span>: Включить режим обзора эффектов (настраиваемые анимации).
• <span color="#00B7EB"><b>Super + G</b></span>: Включить/выключить игровую компоновку окон (для минимизации задержек).""",


        "terminalhotk": """ <span size="24000" weight="bold">Работа с терминалом</span>
        
<span size="24000" weight="bold">  Вкладки</span>

В программе "Терминал Gnome" предусмотрены вкладки, и работают они аналогично вкладкам в веб-браузере или файловом менеджере. Иными словами, если вам нужно несколько терминалов, вовсе не обязательно открывать _несколько окон_. Достаточно одного окна с _несколькими вкладками_. Ниже приведены горячие клавиши, относящиеся ко вкладкам:

• <span color="#00B7EB"><b>Ctrl+Shift+T</b></span> — открыть новую вкладку;

• <span color="#00B7EB"><b>Ctrl+Shift+W или Ctrl+D</b></span> — закрыть текущую вкладку (или весь терминал, если вкладка одна);

• <span color="#00B7EB"><b>Ctrl+Shift+N</b></span> — открыть новое окно терминала из текущего.

Со временем вы можете оказаться в ситуации, когда вкладок станет действительно много, и тогда возникнет вопрос о навигации между ними. Вам пригодятся следующие сочетания клавиш:

• <span color="#00B7EB"><b>Ctrl+PgDn</b></span> — перейти на следующую (справа) вкладку;

• <span color="#00B7EB"><b>Ctrl+PgDn</b></span> — перейти на предыдущую (слева) вкладку;

• <span color="#00B7EB"><b>Ctrl+Shift+PgDn</b></span> — сдвинуть вкладку вправо;

• <span color="#00B7EB"><b>Ctrl+Shift+PgUp</b></span> — сдвинуть вкладку влево.

• <span color="#00B7EB"><b>Alt+1</b></span> — перейти на первую по счёту вкладку. Подставьте другую цифру для нужной вам вкладки. Данный способ позволяет «дотянуться» максимум до _десятой_ по счёту вкладки.

<span size="24000" weight="bold"> Навигация</span>

Три очень часто используемые комбинации для копирования и вставки текста, а также отмены выполняющейся команды:

• <span color="#00B7EB"><b>Ctrl+Shift+С</b></span> — копирование в буфер обмена;

• <span color="#00B7EB"><b>Ctrl+Shift+V</b></span> — вставка из буфера обмена;

• <span color="#00B7EB"><b>Ctrl+C</b></span> — прерывание выполняющейся команды или очистка текущей строки.

Для того чтобы выделить нужный текст в терминале, вам потребуется воспользоваться мышью. Тем не менее, в программе "Терминал Gnome" имеется встроенное средство поиска текста, которое позволяет искать как по обычному фрагменту, так и по регулярному выражению:

• <span color="#00B7EB"><b>Ctrl+Shift+F</b></span> — вызов встроенного поиска по любому тексту в терминале.

Если команда в терминале слишком длинная, или вы сделали опечатку в начале и не сразу это заметили, вы можете вернуться в начало строки. А затем — снова в конец. Вот как это сделать:

• <span color="#00B7EB"><b>Ctrl+A</b></span> — переместиться в начало строки;

• <span color="#00B7EB"><b>Ctrl+E</b></span> — переместиться в конец строки.

В терминале Linux можно перемещаться внутри строки также по словам и по отдельным символам (в последнем случае, это аналогично использованию клавиш с боковыми стрелками):

• <span color="#00B7EB"><b>Ctrl+F</b></span> — переместиться на 1 символ вперед;

• <span color="#00B7EB"><b>Ctrl+B</b></span> — переместиться на 1 символ назад;

• <span color="#00B7EB"><b>Alt+F</b></span> — переместиться к следующему слову;

• <span color="#00B7EB"><b>Alt+B</b></span> — переместиться в начало предыдущего слова.

<span size="24000" weight="bold"> Управление командами и процессами</span>

• <span color="#00B7EB"><b>Ctrl+Z</b></span> — приостановка процесса;

• <span color="#00B7EB"><b>Ctrl+S</b></span> — прекратить обновление вывода команды;

• <span color="#00B7EB"><b>Ctrl+Q</b></span> — возобновить вывод команды.

• <span color="#00B7EB"><b>Ctrl+P</b></span> — вывести предыдущую команду;

• <span color="#00B7EB"><b>Ctrl+N</b></span> — вывести следующую команду.

<span size="24000" weight="bold"> Редактирование команд</span>

Самое время рассмотреть средства редактирования команд — они в Bash весьма продвинутые. Удобное перемещение в начало и конец строки, выборочное удаление символов и слов — это лишь часть возможностей, которые могут пригодиться пользователю. За редактирование команд отвечают следующие сочетания клавиш:

• <span color="#00B7EB"><b>Ctrl+U</b></span> — удалить весь текст слева от курсора;

• <span color="#00B7EB"><b>Ctrl+K</b></span> — удалить весь текст справа от курсора;

• <span color="#00B7EB"><b>Ctrl+W</b></span> — удалить 1 слово или параметр слева от курсора;

• <span color="#00B7EB"><b>Ctrl+D</b></span> — удаление текущего символа (аналогично <b>Del</b>);

• <span color="#00B7EB"><b>Ctrl+H</b></span> — удаление предыдущего символа (аналогично <b>Backspace</b>);

• <span color="#00B7EB"><b>Alt+D</b></span> — удалить всё справа от курсора до ближайшего пробела;

• <span color="#00B7EB"><b>Alt+Backspace</b></span> — удалить всё слева от курсора до ближайшего пробела;

• <span color="#00B7EB"><b>Alt+T</b></span> — поменять местами текущее слово с предыдущем;

• <span color="#00B7EB"><b>Esc+T</b></span> — поменять местами два предыдущих слова;

• <span color="#00B7EB"><b>Tab</b></span> — автодополнение команды после ввода её первых символов.""",

        
    },
    "zh": {
        "introduction_topic": """
<span size='18000' weight='bold'>Linux 快捷键简介</span>

Linux 快捷键帮助您更快、更高效地工作。本节介绍最重要的快捷键及其在不同环境下的用法，适合初学者。
""",
        "gnomehotk": """
<span size='18000' weight='bold'>GNOME 快捷键</span>

• <span color='#00B7EB'><b>Super</b></span>：打开活动概览，搜索应用、窗口或工作区。
• <span color='#00B7EB'><b>Alt + Tab</b></span>：在打开的应用间切换。
• <span color='#00B7EB'><b>Alt + `</b></span>：在同一应用的窗口间切换。
• <span color='#00B7EB'><b>Super + Tab</b></span>：以视觉效果切换应用。
• <span color='#00B7EB'><b>Alt + F2</b></span>：打开快速命令输入栏。
• <span color='#00B7EB'><b>Super + L</b></span>：锁定屏幕。
• <span color='#00B7EB'><b>Ctrl + Alt + Delete</b></span>：打开注销/重启/关机菜单。
• <span color='#00B7EB'><b>Print Screen</b></span>：截图（保存到图片文件夹或剪贴板）。
• <span color='#00B7EB'><b>Super + Print Screen</b></span>：打开区域截图工具。

<span size='large' weight='bold'>窗口管理</span>

• <span color='#00B7EB'><b>Super + ←/→</b></span>：窗口左右分屏。
• <span color='#00B7EB'><b>Super + ↑</b></span>：窗口最大化。
• <span color='#00B7EB'><b>Super + ↓</b></span>：窗口最小化/还原。
• <span color='#00B7EB'><b>Alt + F4</b></span>：关闭活动窗口。
• <span color='#00B7EB'><b>Alt + Space</b></span>：打开窗口菜单。
• <span color='#00B7EB'><b>Super + M</b></span>：显示/隐藏通知和日历。

<span size='large' weight='bold'>工作区</span>

• <span color='#00B7EB'><b>Super + Page Up/Page Down</b></span>：切换工作区。
• <span color='#00B7EB'><b>Ctrl + Alt + ←/→</b></span>：切换工作区（部分发行版）。
• <span color='#00B7EB'><b>Super + Shift + Page Up/Page Down</b></span>：将窗口移动到其他工作区。
• <span color='#00B7EB'><b>Super + T</b></span>：打开新终端（Ubuntu）。

<span size='large' weight='bold'>搜索与应用</span>

• <span color='#00B7EB'><b>Super + A</b></span>：显示应用列表。
• <span color='#00B7EB'><b>Super + S</b></span>：打开搜索（查找文件、应用、设置）。
• <span color='#00B7EB'><b>Super + 数字(1–9)</b></span>：启动或切换到面板固定应用。
""",
        "kdehotk": """
<span size='18000' weight='bold'>KDE 快捷键</span>

• <span color='#00B7EB'><b>Super</b></span>：打开应用菜单。
• <span color='#00B7EB'><b>Alt + Tab</b></span>：窗口间切换（带视觉效果）。
• <span color='#00B7EB'><b>Alt + `</b></span>：同一应用窗口间切换。
• <span color='#00B7EB'><b>Alt + F2</b></span>：打开 Krunner（应用/文件/命令搜索）。
• <span color='#00B7EB'><b>Super + L</b></span>：锁定屏幕。
• <span color='#00B7EB'><b>Ctrl + Alt + Delete</b></span>：打开会话结束菜单。
• <span color='#00B7EB'><b>Print Screen</b></span>：用 Spectacle 截图。
• <span color='#00B7EB'><b>Super + Print Screen</b></span>：截取活动窗口。
• <span color='#00B7EB'><b>Ctrl + Alt + T</b></span>：打开终端（Konsole）。

<span size='large' weight='bold'>窗口管理</span>

• <span color='#00B7EB'><b>Alt + F3</b></span>：打开窗口菜单。
• <span color='#00B7EB'><b>Alt + F4</b></span>：关闭活动窗口。
• <span color='#00B7EB'><b>Super + ←/→</b></span>：窗口左右分屏。
• <span color='#00B7EB'><b>Super + ↑</b></span>：窗口最大化。
• <span color='#00B7EB'><b>Super + ↓</b></span>：窗口最小化。
• <span color='#00B7EB'><b>Ctrl + F10</b></span>：最小化/还原所有窗口。
• <span color='#00B7EB'><b>Super + T</b></span>：平铺窗口布局（启用时）。

<span size='large' weight='bold'>工作区与活动</span>

• <span color='#00B7EB'><b>Ctrl + F1/F2/F3/F4</b></span>：切换虚拟桌面（最多4个）。
• <span color='#00B7EB'><b>Super + Tab</b></span>：带特效切换桌面。
• <span color='#00B7EB'><b>Super + Q</b></span>：打开活动概览。
• <span color='#00B7EB'><b>Ctrl + Alt + ←/→</b></span>：切换工作区。
• <span color='#00B7EB'><b>Super + Shift + 方向键</b></span>：将窗口移动到其他桌面。

<span size='large' weight='bold'>搜索与应用</span>

• <span color='#00B7EB'><b>Super + 数字(1–9)</b></span>：启动/切换任务栏固定应用。
• <span color='#00B7EB'><b>Alt + F1</b></span>：打开备用应用菜单（如已设置）。
• <span color='#00B7EB'><b>Super + R</b></span>：用 Krunner 快速运行命令。
• <span color='#00B7EB'><b>Super + E</b></span>：打开文件管理器（Dolphin）。

<span size='large' weight='bold'>KDE 独有功能</span>

• <span color='#00B7EB'><b>Super + V</b></span>：打开剪贴板历史。
• <span color='#00B7EB'><b>Super + D</b></span>：显示/隐藏桌面。
• <span color='#00B7EB'><b>Ctrl + Alt + Shift</b></span>：启用特效概览模式。
• <span color='#00B7EB'><b>Super + G</b></span>：启用/禁用游戏窗口布局。
""",
        "terminalhotk": """
<span size='18000' weight='bold'>终端快捷键</span>

在 Linux 终端高效工作的按键操作：命令编辑、导航、进程控制等。
"""
    },
    "ja": {
        "introduction_topic": """
<span size='18000' weight='bold'>ホットキー入門</span>

Linuxのホットキーは、作業をより速く、効率的に行うのに役立ちます。このセクションでは、初心者向けの最も重要なショートカットと、さまざまな環境での使い方を解説します。
""",
        "gnomehotk": """
<span size='18000' weight='bold'>GNOMEホットキー</span>

• <span color='#00B7EB'><b>Super</b></span>: アクティビティ概要を開き、アプリやウィンドウ、ワークスペースを検索。
• <span color='#00B7EB'><b>Alt + Tab</b></span>: 開いているアプリ間を切り替え。
• <span color='#00B7EB'><b>Alt + `</b></span>: 同じアプリのウィンドウ間を切り替え。
• <span color='#00B7EB'><b>Super + Tab</b></span>: アプリ間をビジュアル効果で切り替え。
• <span color='#00B7EB'><b>Alt + F2</b></span>: クイックコマンド入力バーを開く。
• <span color='#00B7EB'><b>Super + L</b></span>: 画面をロック。
• <span color='#00B7EB'><b>Ctrl + Alt + Delete</b></span>: ログアウト/再起動/シャットダウンメニューを開く。
• <span color='#00B7EB'><b>Print Screen</b></span>: スクリーンショットを撮る（画像フォルダまたはクリップボードに保存）。
• <span color='#00B7EB'><b>Super + Print Screen</b></span>: 範囲選択スクリーンショットツールを開く。

<span size='large' weight='bold'>ウィンドウ管理</span>

• <span color='#00B7EB'><b>Super + ←/→</b></span>: ウィンドウを左右半分にスナップ。
• <span color='#00B7EB'><b>Super + ↑</b></span>: ウィンドウを最大化。
• <span color='#00B7EB'><b>Super + ↓</b></span>: ウィンドウを最小化/復元。
• <span color='#00B7EB'><b>Alt + F4</b></span>: アクティブウィンドウを閉じる。
• <span color='#00B7EB'><b>Alt + Space</b></span>: ウィンドウメニューを開く。
• <span color='#00B7EB'><b>Super + M</b></span>: 通知とカレンダーを表示/非表示。

<span size='large' weight='bold'>ワークスペース</span>

• <span color='#00B7EB'><b>Super + Page Up/Page Down</b></span>: ワークスペース間を切り替え。
• <span color='#00B7EB'><b>Ctrl + Alt + ←/→</b></span>: ワークスペース間を切り替え（一部ディストリビューション）。
• <span color='#00B7EB'><b>Super + Shift + Page Up/Page Down</b></span>: ウィンドウを他のワークスペースに移動。
• <span color='#00B7EB'><b>Super + T</b></span>: 新しいターミナルを開く（Ubuntu）。

<span size='large' weight='bold'>検索とアプリ</span>

• <span color='#00B7EB'><b>Super + A</b></span>: アプリ一覧を表示。
• <span color='#00B7EB'><b>Super + S</b></span>: 検索を開く（ファイル、アプリ、設定を検索）。
• <span color='#00B7EB'><b>Super + 数字(1–9)</b></span>: パネルにピン留めされたアプリを起動/切り替え。
""",
        "kdehotk": """
<span size='18000' weight='bold'>KDEホットキー</span>

• <span color='#00B7EB'><b>Super</b></span>: アプリケーションメニューを開く。
• <span color='#00B7EB'><b>Alt + Tab</b></span>: ウィンドウ間を切り替え（ビジュアル効果付き）。
• <span color='#00B7EB'><b>Alt + `</b></span>: 同じアプリのウィンドウ間を切り替え。
• <span color='#00B7EB'><b>Alt + F2</b></span>: Krunner（アプリ/ファイル/コマンド検索）を開く。
• <span color='#00B7EB'><b>Super + L</b></span>: 画面をロック。
• <span color='#00B7EB'><b>Ctrl + Alt + Delete</b></span>: セッション終了メニューを開く。
• <span color='#00B7EB'><b>Print Screen</b></span>: Spectacleでスクリーンショット。
• <span color='#00B7EB'><b>Super + Print Screen</b></span>: アクティブウィンドウのスクリーンショット。
• <span color='#00B7EB'><b>Ctrl + Alt + T</b></span>: ターミナル（Konsole）を開く。

<span size='large' weight='bold'>ウィンドウ管理</span>

• <span color='#00B7EB'><b>Alt + F3</b></span>: ウィンドウメニューを開く。
• <span color='#00B7EB'><b>Alt + F4</b></span>: アクティブウィンドウを閉じる。
• <span color='#00B7EB'><b>Super + ←/→</b></span>: ウィンドウを左右半分にスナップ。
• <span color='#00B7EB'><b>Super + ↑</b></span>: ウィンドウを最大化。
• <span color='#00B7EB'><b>Super + ↓</b></span>: ウィンドウを最小化。
• <span color='#00B7EB'><b>Ctrl + F10</b></span>: すべてのウィンドウを最小化/復元。
• <span color='#00B7EB'><b>Super + T</b></span>: タイルウィンドウ配置（有効時）。

<span size='large' weight='bold'>ワークスペースとアクティビティ</span>

• <span color='#00B7EB'><b>Ctrl + F1/F2/F3/F4</b></span>: 仮想デスクトップ間を切り替え（最大4つ）。
• <span color='#00B7EB'><b>Super + Tab</b></span>: デスクトップ間を効果付きで切り替え。
• <span color='#00B7EB'><b>Super + Q</b></span>: アクティビティ概要を開く。
• <span color='#00B7EB'><b>Ctrl + Alt + ←/→</b></span>: ワークスペース間を切り替え。
• <span color='#00B7EB'><b>Super + Shift + 矢印</b></span>: ウィンドウを他のデスクトップに移動。

<span size='large' weight='bold'>検索とアプリ</span>

• <span color='#00B7EB'><b>Super + 数字(1–9)</b></span>: タスクバーにピン留めされたアプリを起動/切り替え。
• <span color='#00B7EB'><b>Alt + F1</b></span>: 代替アプリメニューを開く（設定時）。
• <span color='#00B7EB'><b>Super + R</b></span>: Krunnerでコマンドを素早く実行。
• <span color='#00B7EB'><b>Super + E</b></span>: ファイルマネージャー（Dolphin）を開く。

<span size='large' weight='bold'>KDE独自機能</span>

• <span color='#00B7EB'><b>Super + V</b></span>: クリップボード履歴を開く。
• <span color='#00B7EB'><b>Super + D</b></span>: デスクトップを表示/非表示。
• <span color='#00B7EB'><b>Ctrl + Alt + Shift</b></span>: エフェクト概要モードを有効化。
• <span color='#00B7EB'><b>Super + G</b></span>: ゲーム用ウィンドウレイアウトを有効/無効化。
""",
        "terminalhotk": """
<span size='18000' weight='bold'>ターミナルホットキー</span>

Linuxターミナルで効率的に作業するためのキー操作：コマンド編集、ナビゲーション、プロセス制御など。
"""
    },
    "fr": {
        "introduction_topic": """
<span size='18000' weight='bold'>Introduction aux raccourcis clavier</span>

Les raccourcis clavier sous Linux vous aident à travailler plus rapidement et efficacement. Cette section présente les combinaisons les plus importantes pour les débutants et leur utilisation dans différents environnements.
""",
        "gnomehotk": """
<span size='18000' weight='bold'>Raccourcis GNOME</span>

• <span color='#00B7EB'><b>Super</b></span> : Ouvrir l'aperçu des activités pour rechercher des applications, fenêtres ou espaces de travail.
• <span color='#00B7EB'><b>Alt + Tab</b></span> : Passer d'une application ouverte à une autre.
• <span color='#00B7EB'><b>Alt + `</b></span> : Passer d'une fenêtre à l'autre d'une même application.
• <span color='#00B7EB'><b>Super + Tab</b></span> : Passer d'une application à l'autre avec effet visuel.
• <span color='#00B7EB'><b>Alt + F2</b></span> : Ouvrir la barre de saisie rapide de commande.
• <span color='#00B7EB'><b>Super + L</b></span> : Verrouiller l'écran.
• <span color='#00B7EB'><b>Ctrl + Alt + Delete</b></span> : Ouvrir le menu de session (déconnexion, redémarrage, arrêt).
• <span color='#00B7EB'><b>Print Screen</b></span> : Capture d'écran (enregistrement dans Images ou presse-papiers).
• <span color='#00B7EB'><b>Super + Print Screen</b></span> : Ouvrir l'outil de capture de zone.

<span size='large' weight='bold'>Gestion des fenêtres</span>

• <span color='#00B7EB'><b>Super + Flèche gauche/droite</b></span> : Ancrer la fenêtre à gauche/droite.
• <span color='#00B7EB'><b>Super + Flèche haut</b></span> : Maximiser la fenêtre.
• <span color='#00B7EB'><b>Super + Flèche bas</b></span> : Réduire/restaurer la fenêtre.
• <span color='#00B7EB'><b>Alt + F4</b></span> : Fermer la fenêtre active.
• <span color='#00B7EB'><b>Alt + Espace</b></span> : Ouvrir le menu de la fenêtre.
• <span color='#00B7EB'><b>Super + M</b></span> : Afficher/masquer les notifications et le calendrier.

<span size='large' weight='bold'>Espaces de travail</span>

• <span color='#00B7EB'><b>Super + Page Up/Page Down</b></span> : Changer d'espace de travail.
• <span color='#00B7EB'><b>Ctrl + Alt + Flèches gauche/droite</b></span> : Changer d'espace de travail (selon la distribution).
• <span color='#00B7EB'><b>Super + Shift + Page Up/Page Down</b></span> : Déplacer la fenêtre vers un autre espace de travail.
• <span color='#00B7EB'><b>Super + T</b></span> : Ouvrir un nouveau terminal (Ubuntu).

<span size='large' weight='bold'>Recherche et applications</span>

• <span color='#00B7EB'><b>Super + A</b></span> : Afficher la liste des applications.
• <span color='#00B7EB'><b>Super + S</b></span> : Ouvrir la recherche (fichiers, applications, paramètres).
• <span color='#00B7EB'><b>Super + chiffre (1–9)</b></span> : Lancer ou basculer vers une application épinglée à la barre.
""",
        "kdehotk": """
<span size='18000' weight='bold'>Raccourcis KDE</span>

• <span color='#00B7EB'><b>Super</b></span> : Ouvrir le menu des applications.
• <span color='#00B7EB'><b>Alt + Tab</b></span> : Passer d'une fenêtre à l'autre (avec effet visuel).
• <span color='#00B7EB'><b>Alt + `</b></span> : Passer d'une fenêtre à l'autre d'une même application.
• <span color='#00B7EB'><b>Alt + F2</b></span> : Ouvrir Krunner (recherche d'applications, fichiers, commandes).
• <span color='#00B7EB'><b>Super + L</b></span> : Verrouiller l'écran.
• <span color='#00B7EB'><b>Ctrl + Alt + Delete</b></span> : Ouvrir le menu de fin de session.
• <span color='#00B7EB'><b>Print Screen</b></span> : Ouvrir Spectacle pour la capture d'écran.
• <span color='#00B7EB'><b>Super + Print Screen</b></span> : Capture d'écran de la fenêtre active.
• <span color='#00B7EB'><b>Ctrl + Alt + T</b></span> : Ouvrir le terminal (Konsole).

<span size='large' weight='bold'>Gestion des fenêtres</span>

• <span color='#00B7EB'><b>Alt + F3</b></span> : Ouvrir le menu de la fenêtre.
• <span color='#00B7EB'><b>Alt + F4</b></span> : Fermer la fenêtre active.
• <span color='#00B7EB'><b>Super + Flèche gauche/droite</b></span> : Ancrer la fenêtre à gauche/droite.
• <span color='#00B7EB'><b>Super + Flèche haut</b></span> : Maximiser la fenêtre.
• <span color='#00B7EB'><b>Super + Flèche bas</b></span> : Réduire la fenêtre.
• <span color='#00B7EB'><b>Ctrl + F10</b></span> : Réduire/restaurer toutes les fenêtres.
• <span color='#00B7EB'><b>Super + T</b></span> : Disposition en mosaïque (si activée).

<span size='large' weight='bold'>Espaces de travail et activités</span>

• <span color='#00B7EB'><b>Ctrl + F1/F2/F3/F4</b></span> : Changer de bureau virtuel (jusqu'à 4).
• <span color='#00B7EB'><b>Super + Tab</b></span> : Changer de bureau avec effet.
• <span color='#00B7EB'><b>Super + Q</b></span> : Ouvrir l'aperçu des activités.
• <span color='#00B7EB'><b>Ctrl + Alt + Flèches</b></span> : Changer d'espace de travail.
• <span color='#00B7EB'><b>Super + Shift + Flèches</b></span> : Déplacer la fenêtre vers un autre bureau.

<span size='large' weight='bold'>Recherche et applications</span>

• <span color='#00B7EB'><b>Super + chiffre (1–9)</b></span> : Lancer/basculer vers une application épinglée à la barre des tâches.
• <span color='#00B7EB'><b>Alt + F1</b></span> : Ouvrir un menu d'applications alternatif.
• <span color='#00B7EB'><b>Super + R</b></span> : Lancer rapidement une commande via Krunner.
• <span color='#00B7EB'><b>Super + E</b></span> : Ouvrir le gestionnaire de fichiers (Dolphin).

<span size='large' weight='bold'>Fonctionnalités uniques KDE</span>

• <span color='#00B7EB'><b>Super + V</b></span> : Ouvrir l'historique du presse-papiers.
• <span color='#00B7EB'><b>Super + D</b></span> : Afficher/masquer le bureau.
• <span color='#00B7EB'><b>Ctrl + Alt + Shift</b></span> : Activer le mode aperçu des effets.
• <span color='#00B7EB'><b>Super + G</b></span> : Activer/désactiver la disposition de jeu.
""",
        "terminalhotk": """
<span size='18000' weight='bold'>Raccourcis du terminal</span>

Combinaisons de touches pour travailler efficacement dans le terminal Linux : édition de commandes, navigation, contrôle des processus, etc.
"""
    },
    "de": {
        "introduction_topic": """
<span size='18000' weight='bold'>Einführung in Tastenkombinationen</span>

Tastenkombinationen in Linux helfen Ihnen, schneller und effizienter zu arbeiten. In diesem Abschnitt werden die wichtigsten Shortcuts für Einsteiger erklärt und deren Nutzung in verschiedenen Umgebungen gezeigt.
""",
        "gnomehotk": """
<span size='18000' weight='bold'>GNOME-Tastenkombinationen</span>

• <span color='#00B7EB'><b>Super</b></span>: Aktivitätenübersicht öffnen, um nach Anwendungen, Fenstern oder Arbeitsflächen zu suchen.
• <span color='#00B7EB'><b>Alt + Tab</b></span>: Zwischen geöffneten Anwendungen wechseln.
• <span color='#00B7EB'><b>Alt + `</b></span>: Zwischen Fenstern einer Anwendung wechseln.
• <span color='#00B7EB'><b>Super + Tab</b></span>: Zwischen Anwendungen mit visuellen Effekten wechseln.
• <span color='#00B7EB'><b>Alt + F2</b></span>: Schnellbefehlsleiste öffnen.
• <span color='#00B7EB'><b>Super + L</b></span>: Bildschirm sperren.
• <span color='#00B7EB'><b>Ctrl + Alt + Delete</b></span>: Sitzungsmenü öffnen (Abmelden, Neustart, Herunterfahren).
• <span color='#00B7EB'><b>Print Screen</b></span>: Screenshot erstellen (in "Bilder" oder Zwischenablage speichern).
• <span color='#00B7EB'><b>Super + Print Screen</b></span>: Bereichsauswahl für Screenshot öffnen.

<span size='large' weight='bold'>Fensterverwaltung</span>

• <span color='#00B7EB'><b>Super + Links/Rechts</b></span>: Fenster an die linke/rechte Bildschirmhälfte andocken.
• <span color='#00B7EB'><b>Super + Oben</b></span>: Fenster maximieren.
• <span color='#00B7EB'><b>Super + Unten</b></span>: Fenster minimieren/wiederherstellen.
• <span color='#00B7EB'><b>Alt + F4</b></span>: Aktives Fenster schließen.
• <span color='#00B7EB'><b>Alt + Leertaste</b></span>: Fenstermenü öffnen.
• <span color='#00B7EB'><b>Super + M</b></span>: Benachrichtigungen und Kalender anzeigen/ausblenden.

<span size='large' weight='bold'>Arbeitsflächen</span>

• <span color='#00B7EB'><b>Super + Bild auf/ab</b></span>: Zwischen Arbeitsflächen wechseln.
• <span color='#00B7EB'><b>Ctrl + Alt + Links/Rechts</b></span>: Zwischen Arbeitsflächen wechseln (in manchen Distributionen).
• <span color='#00B7EB'><b>Super + Shift + Bild auf/ab</b></span>: Fenster auf andere Arbeitsfläche verschieben.
• <span color='#00B7EB'><b>Super + T</b></span>: Neues Terminal öffnen (Ubuntu).

<span size='large' weight='bold'>Suche und Anwendungen</span>

• <span color='#00B7EB'><b>Super + A</b></span>: Anwendungsübersicht anzeigen.
• <span color='#00B7EB'><b>Super + S</b></span>: Suche öffnen (Dateien, Anwendungen, Einstellungen).
• <span color='#00B7EB'><b>Super + Zahl (1–9)</b></span>: Anwendung in der Leiste starten/wechseln.
""",
        "kdehotk": """
<span size='18000' weight='bold'>KDE-Tastenkombinationen</span>

• <span color='#00B7EB'><b>Super</b></span>: Anwendungsmenü öffnen.
• <span color='#00B7EB'><b>Alt + Tab</b></span>: Zwischen Fenstern wechseln (mit Effekt).
• <span color='#00B7EB'><b>Alt + `</b></span>: Zwischen Fenstern einer Anwendung wechseln.
• <span color='#00B7EB'><b>Alt + F2</b></span>: Krunner öffnen (Suche nach Apps, Dateien, Befehlen).
• <span color='#00B7EB'><b>Super + L</b></span>: Bildschirm sperren.
• <span color='#00B7EB'><b>Ctrl + Alt + Delete</b></span>: Sitzungsende-Menü öffnen.
• <span color='#00B7EB'><b>Print Screen</b></span>: Spectacle für Screenshots öffnen.
• <span color='#00B7EB'><b>Super + Print Screen</b></span>: Screenshot des aktiven Fensters.
• <span color='#00B7EB'><b>Ctrl + Alt + T</b></span>: Terminal (Konsole) öffnen.

<span size='large' weight='bold'>Fensterverwaltung</span>

• <span color='#00B7EB'><b>Alt + F3</b></span>: Fenstermenü öffnen.
• <span color='#00B7EB'><b>Alt + F4</b></span>: Aktives Fenster schließen.
• <span color='#00B7EB'><b>Super + Links/Rechts</b></span>: Fenster an linke/rechte Seite andocken.
• <span color='#00B7EB'><b>Super + Oben</b></span>: Fenster maximieren.
• <span color='#00B7EB'><b>Super + Unten</b></span>: Fenster minimieren.
• <span color='#00B7EB'><b>Ctrl + F10</b></span>: Alle Fenster minimieren/wiederherstellen.
• <span color='#00B7EB'><b>Super + T</b></span>: Kachelmodus (wenn aktiviert).

<span size='large' weight='bold'>Arbeitsflächen und Aktivitäten</span>

• <span color='#00B7EB'><b>Ctrl + F1/F2/F3/F4</b></span>: Zwischen virtuellen Desktops wechseln (bis zu 4).
• <span color='#00B7EB'><b>Super + Tab</b></span>: Zwischen Desktops mit Effekt wechseln.
• <span color='#00B7EB'><b>Super + Q</b></span>: Aktivitätenübersicht öffnen.
• <span color='#00B7EB'><b>Ctrl + Alt + Pfeile</b></span>: Zwischen Arbeitsflächen wechseln.
• <span color='#00B7EB'><b>Super + Shift + Pfeile</b></span>: Fenster auf anderen Desktop verschieben.

<span size='large' weight='bold'>Suche und Anwendungen</span>

• <span color='#00B7EB'><b>Super + Zahl (1–9)</b></span>: Anwendung in der Taskleiste starten/wechseln.
• <span color='#00B7EB'><b>Alt + F1</b></span>: Alternatives Anwendungsmenü öffnen.
• <span color='#00B7EB'><b>Super + R</b></span>: Schnellbefehl über Krunner ausführen.
• <span color='#00B7EB'><b>Super + E</b></span>: Dateimanager (Dolphin) öffnen.

<span size='large' weight='bold'>KDE-spezifische Funktionen</span>

• <span color='#00B7EB'><b>Super + V</b></span>: Zwischenablage öffnen.
• <span color='#00B7EB'><b>Super + D</b></span>: Desktop anzeigen/verbergen.
• <span color='#00B7EB'><b>Ctrl + Alt + Shift</b></span>: Effektübersicht aktivieren.
• <span color='#00B7EB'><b>Super + G</b></span>: Gaming-Layout aktivieren/deaktivieren.
""",
        "terminalhotk": """
<span size='18000' weight='bold'>Terminal-Tastenkombinationen</span>

Tastenkombinationen für effizientes Arbeiten im Linux-Terminal: Befehlsbearbeitung, Navigation, Prozesssteuerung usw.
"""
    },
}