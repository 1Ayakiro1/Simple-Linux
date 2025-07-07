packages_translations = {
    "ru": {
        "intro_in_packages": """
<span size="24000" weight="bold">Что такое пакеты и как с ними работать</span>

В мире Linux <span color="#00B7EB"><b>пакеты</b></span> — это специальные файлы, содержащие программы, библиотеки или другие компоненты, необходимые для работы системы или приложений. Пакеты упрощают установку, обновление и удаление программ, так как включают всё необходимое: саму программу, её зависимости (другие пакеты, от которых она зависит) и инструкции для правильной установки.

<span size="24000" weight="bold">Зачем нужны пакеты?</span>

Представьте, что вы хотите установить текстовый редактор или игру. Вместо того чтобы вручную скачивать файлы, искать нужные библиотеки и настраивать их, вы используете пакет. Пакет содержит всё готовое для установки, а менеджер пакетов (специальная программа в Linux) автоматически решает, какие дополнительные компоненты нужны и как их установить.

<span size="24000" weight="bold">Как работают пакеты?</span>

В Linux пакеты управляются с помощью <span color="#00B7EB"><b>менеджеров пакетов</b></span>, которые зависят от вашего дистрибутива. Например:

• В Ubuntu и Debian используется менеджер apt (пакеты с расширением .deb).
• В Fedora и CentOS — dnf или yum (пакеты .rpm).
• В Arch Linux — pacman.

Менеджеры пакетов работают с репозиториями — онлайн-хранилищами, где находятся тысячи пакетов. Когда вы устанавливаете программу, менеджер пакетов скачивает нужный пакет из репозитория и устанавливает его вместе с зависимостями.

В следующих главах будут разобраны различные пакеты и рассмотрим,как с ними работать!
""",


        "appimage": """<span size="24000" weight="bold">Формат пакета AppImage: Простота и универсальность</span>

<span color="#00B7EB"><b>AppImage</b></span> — это формат пакетов для Linux, который позволяет запускать программы без традиционной установки. Это единый исполняемый файл, содержащий приложение и все его зависимости (библиотеки, файлы настроек), что делает его удобным для новичков и опытных пользователей.

<span size="24000" weight="bold">Что такое AppImage?</span>

<span color="#00B7EB"><b>AppImage</b></span> — это <b>«портативный»</b> формат, который работает на большинстве дистрибутивов Linux без необходимости установки через менеджер пакетов. Вы просто скачиваете файл с расширением <b>.AppImage</b>, делаете его исполняемым и запускаете. Программа работает сразу, не добавляя ничего в систему.

<span size="24000" weight="bold">Преимущества данного формата</span>
Он универсален и работае буквально на всех популярных дистрибутивах Linux. Это монолитный файл,который сам содержит в себе все необходимые компоненты для запуска программы,достаточно его лишь запустить. Также он полностью изолирован и не взаимодействует с системой и файловой системой,что делает его использование достаточно безопасным

<span size="24000" weight="bold">Как работать с AppImage?</span>
Вы можете найти этот формат в магазине вашего дистрибутива Linux,или скачать на сайте разработчика программы. Если вы хотите его запустить графически,то при его установке кликните правой кнопкой мыши по файлу -> свойста -> запускать как программу и далее просто дважды кликните по самому файлу.

Если же вы предпочитаете терминал, то используйте данную команду:
<span background="#010101"><span color="yellow">chmod</span> <span color="#F34336">+x</span> <b>имя_файла.AppImage</b></span>""",


        "deb": """
<span size="24000" weight="bold">Формат пакета deb: Просто о главном</span>

Формат deb — это способ доставки программ в Linux-дистрибутивах, таких как Ubuntu или Debian. Файл с расширением .deb содержит программу, её файлы и всё, что нужно для работы. Это как коробка с приложением, готовым к установке.

<span size="24000" weight="bold">Что такое deb?</span>

<span color="#00B7EB"><b>Deb-пакет</b></span> — это архив, в котором лежат программа, библиотеки и инструкции для установки. Он создан для конкретного дистрибутива, чтобы всё работало без сбоев. Менеджеры пакетов, такие как apt, берут deb-файлы из онлайн-хранилищ (репозиториев) и устанавливают их автоматически.

<span size="24000" weight="bold">Плюсы и минусы</span>

Deb-пакеты удобны, потому что менеджер <span color="#00B7EB"><b>apt</b></span> сам находит и ставит всё нужное. Они надёжны и подходят для вашего дистрибутива. Но они не работают в других системах, например, Fedora. Если скачать deb-файл отдельно, зависимости иногда нужно добавлять вручную. Качайте файлы только из проверенных мест, чтобы не поймать вредоносный код.

<span size="24000" weight="bold">Как устанавливать deb-пакеты?</span>

Проще всего установить программу командой <span background="#010101"><span color="blue">sudo</span> <span color="yellow">apt</span> <span color="green">install</span> <b>имя_пакета</b></span> — менеджер сам всё скачает и настроит. Если у вас есть deb-файл, используйте <span background="#010101"><span color="blue">sudo</span> <span color="yellow">dpkg -i</span> <b>имя_файла.deb</b></span>. Если что-то не хватает, команда <span background="#010101"><span color="blue">sudo</span> <span color="yellow">apt</span> <span color="green">install</span> -f</span> поможет. Можно также кликнуть по файлу в Ubuntu Software — установка начнётся автоматически.""",


        "flatpack": "Flatpak — система для создания, распространения и запуска изолированных приложений на Linux...",
        "rpm": "RPM — формат пакетов, используемый в Red Hat, Fedora и других...",
        "snap": "Snap — универсальный формат пакетов для Linux, разработанный Canonical...",
        "tar": "TAR-архивы используются для распространения программ в исходном или бинарном виде...",
        "zst": "ZST (Zstandard) — быстрый алгоритм сжатия, используемый в некоторых дистрибутивах Linux...",
    },
    "en": {
        "intro_in_packages": "This section introduces you to package management in Linux...",
        "appimage": "AppImage is a universal package format for Linux...",
        "deb": "DEB is a package format used in Debian and Ubuntu...",
        "flatpack": "Flatpak is a system for building, distributing, and running sandboxed apps on Linux...",
        "rpm": "RPM is a package format used in Red Hat, Fedora, and others...",
        "snap": "Snap is a universal package format for Linux developed by Canonical...",
        "tar": "TAR archives are used to distribute programs in source or binary form...",
        "zst": "ZST (Zstandard) is a fast compression algorithm used in some Linux distributions...",
    },
    "zh": {
        "intro_in_packages": "TODO: translate",
        "appimage": "TODO: translate",
        "deb": "TODO: translate",
        "flatpack": "TODO: translate",
        "rpm": "TODO: translate",
        "snap": "TODO: translate",
        "tar": "TODO: translate",
        "zst": "TODO: translate",
    },
    "ja": {
        "intro_in_packages": "TODO: translate",
        "appimage": "TODO: translate",
        "deb": "TODO: translate",
        "flatpack": "TODO: translate",
        "rpm": "TODO: translate",
        "snap": "TODO: translate",
        "tar": "TODO: translate",
        "zst": "TODO: translate",
    },
    "fr": {
        "intro_in_packages": "TODO: translate",
        "appimage": "TODO: translate",
        "deb": "TODO: translate",
        "flatpack": "TODO: translate",
        "rpm": "TODO: translate",
        "snap": "TODO: translate",
        "tar": "TODO: translate",
        "zst": "TODO: translate",
    },
    "de": {
        "intro_in_packages": "TODO: translate",
        "appimage": "TODO: translate",
        "deb": "TODO: translate",
        "flatpack": "TODO: translate",
        "rpm": "TODO: translate",
        "snap": "TODO: translate",
        "tar": "TODO: translate",
        "zst": "TODO: translate",
    },
} 