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


        "flatpack": """<span size="24000" weight="bold">Формат пакета Flatpak: Простое объяснение</span>

<span color="#00B7EB"><b>Flatpak</b></span> — это современный формат пакетов для Linux, используемый в дистрибутивах, таких как Ubuntu, Fedora или Arch. Файл с расширением <b>.flatpak</b> содержит программу и её зависимости, что позволяет запускать приложение без сложной настройки. Это как контейнер, обеспечивающий работу программы в любой Linux-системе.

<span size="24000" weight="bold">Что такое Flatpak?</span>

<span color="#00B7EB"><b>Flatpak-пакет</b></span> — это архив, включающий приложение, библиотеки и настройки, необходимые для его работы. Он изолирован от системы, что повышает безопасность и упрощает установку на разных дистрибутивах. Управление <span color="#00B7EB"><b>flatpak-пакетами</b></span> осуществляется через утилиту <span color="#00B7EB"><b>latpak</b></span>, которая работает с онлайн-хранилищем <span color="#00B7EB"><b>Flathub</b></span>, где хранятся тысячи приложений.

<span size="24000" weight="bold">Плюсы и минусы</span>

<span color="#00B7EB"><b>Flatpak</b></span> удобен, так как работает на большинстве дистрибутивов, а утилита <span color="#00B7EB"><b>flatpak</b></span> автоматически устанавливает и обновляет программы. Изоляция пакетов снижает риск сбоев в системе. Однако <span color="#00B7EB"><b>flatpak-пакеты</b></span> могут занимать больше места из-за включённых зависимостей, а запуск иногда чуть медленнее. Некоторые пользователи предпочитают традиционные пакеты для скорости. Качайте <span color="#00B7EB"><b>flatpak</b></span> только из Flathub или проверенных источников, чтобы избежать вредоносного кода.

<span size="24000" weight="bold">Как установить Flatpak-пакеты</span>

Проще всего установить программу командой <span background="#010101"><span color="blue">flatpak</span> <span color="yellow">install</span> <span color="green">flathub</span> <b>имя_пакета</b></span> — утилита <span color="#00B7EB"><b>flatpak</b></span> скачает и настроит всё автоматически. Пакеты также можно найти в <span color="#00B7EB"><b>Flathub</b></span> через браузер или графические интерфейсы, такие как GNOME Software, где установка начинается одним кликом. Обновления <span color="#00B7EB"><b>flatpak-пакетов</b></span> происходят автоматически через <span background="#010101"><span color="blue">flatpak</span> <span color="yellow">update</span></span>.""",


        "rpm": """
<span size=\"24000\" weight=\"bold\">RPM package format: Simple explanation</span>

<span color=\"#00B7EB\"><b>RPM format</b></span> is a way to deliver programs in Linux distributions like Fedora, CentOS, or openSUSE. A file with the .rpm extension contains the program, its files, and everything needed for it to work. It's like a package ready to be installed on your system.

<span size=\"24000\" weight=\"bold\">What is an RPM package?</span>

A <span color=\"#00B7EB\"><b>RPM package</b></span> is an archive with the application, libraries, and installation instructions. It is created for a specific distribution to ensure everything works correctly. Package managers like dnf or yum take RPM files from online repositories and install them automatically.

<span size=\"24000\" weight=\"bold\">Pros and Cons</span>

<span color=\"#00B7EB\"><b>RPM packages</b></span> are convenient because managers like <b>dnf</b> automatically find and install the necessary files. They are reliable and tailored for your distribution. However, they do not work on systems like Ubuntu. If you download an RPM file separately, sometimes dependencies need to be added manually. Download files only from safe sources to avoid malware.

<span size=\"24000\" weight=\"bold\">How to install RPM packages</span>

The simplest way is to use the command <span background=\"#010101\"><span color=\"blue\">sudo</span> <span color=\"yellow\">dnf</span> <span color=\"green\">install</span> <b>package_name</b></span>, which downloads and installs the program with dependencies. For a separate RPM file, use <span background=\"#010101\"><span color=\"blue\">sudo</span> <span color=\"yellow\">dnf</span> <span color=\"green\">install</span></span> to help add dependencies. In graphical interfaces like <b>GNOME Software</b>, you can simply click the file to install.""",


        "snap": """
<span size='24000' weight='bold'>Формат пакета Snap: Простое объяснение</span>

<span color='#00B7EB'><b>Snap</b></span> — это современный формат пакетов для Linux, используемый в дистрибутивах, таких как Ubuntu, Fedora или Linux Mint. Файл с расширением <span color='#00B7EB'><b>.snap</b></span> содержит программу, её зависимости и всё необходимое для работы. Это как контейнер, который запускает приложение без сложной настройки.

<span size='24000' weight='bold'>Что такое Snap?</span>

<span color='#00B7EB'><b>Snap-пакет</b></span> — это архив, включающий приложение и все его зависимости, что позволяет запускать его на разных дистрибутивах. Управление <span color='#00B7EB'><b>snap-пакетами</b></span> осуществляется через утилиту <span color='#00B7EB'><b>snapd</b></span>, которая работает с онлайн-магазином <b>Snap Store</b>. Пакеты изолированы от системы, что повышает безопасность и упрощает установку.

<span size='24000' weight='bold'>Плюсы и минусы</span>

<span color='#00B7EB'><b>Snap</b></span> удобен, так как работает на многих дистрибутивах, а <span color='#00B7EB'><b>snapd</b></span> автоматически ставит и обновляет программы. Пакеты изолированы, что снижает риск сбоев системы. Однако <span color='#00B7EB'><b>snap-пакеты</b></span> могут быть больше по размеру, а запуск иногда чуть медленнее из-за изоляции. Некоторые пользователи предпочитают традиционные пакеты для большей скорости. Качайте <span color='#00B7EB'><b>snap</b></span> только из <b>Snap Store</b>, чтобы избежать вредоносного кода.

<span size='24000' weight='bold'>Как установить Snap-пакеты</span>

Проще всего установить программу командой <span background='#010101'><span color='blue'>sudo</span> <span color='yellow'>snap</span> <span color='green'>install</span> <b>имя_пакета</b></span> — утилита <span color='#00B7EB'><b>snapd</b></span> скачает и настроит всё автоматически. Пакеты также можно найти в <b>Snap Store</b> через браузер или графические интерфейсы, такие как <b>Ubuntu Software</b>, где установка начинается одним кликом. Обновления snap-пакетов происходят автоматически в фоновом режиме.
""",


        "tar": """<span size='24000' weight='bold'>Tar package format: Simple explanation</span>

<span color='#00B7EB'><b>Tar</b></span> is an archive format often used in Linux to package files and programs. Files with the <b>.tar</b>, <b>.tar.gz</b>, or <b>.tar.bz2</b> extensions contain a set of data, which may include source code or ready-to-install files. It's like a compressed folder that you need to unpack and set up manually.

<span size='24000' weight='bold'>What is Tar?</span>

<span color='#00B7EB'><b>Tar</b></span> is an archive that combines files into one. In Linux, it is often used to distribute source code or data that the user must compile or install themselves. The <b>.tar.gz</b> and <b>.tar.bz2</b> formats mean the archive is compressed to save space. <span color='#00B7EB'><b>Tar</b></span> is not a package like <span color='#00B7EB'><b>deb</b></span> or <span color='#00B7EB'><b>snap</b></span>, but rather a way to transfer files.

<span size='24000' weight='bold'>Pros and Cons</span>

<span color='#00B7EB'><b>Tar</b></span> is universal and works on any Linux distribution, making it flexible for developers and enthusiasts. It allows distributing programs not available in repositories. However, installation from <span color='#00B7EB'><b>tar archives</b></span> is more complex, often requiring compilation and manual setup of dependencies, which can be difficult for beginners. Security is also important: download <span color='#00B7EB'><b>tar files</b></span> only from trusted sources to avoid malware.

<span size='24000' weight='bold'>How to install programs from Tar</span>

To work with <span color='#00B7EB'><b>tar archives</b></span>, unpack the file with a command like <span background='#010101'><span color='yellow'>tar</span> <span color='green'>-xzf</span> <b>filename.tar.gz</b></span>. If it's source code, you need to compile the program by following the instructions (usually in a <b>README</b> or <b>INSTALL</b> file). This may include commands like <b>./configure</b>, <span background='#010101'><span color='yellow'>make</span></span>, and <span background='#010101'><span color='blue'>sudo</span> <span color='yellow'>make</span> <span color='green'>install</span></span>. If the archive contains a ready program, just move the files to the desired location. Graphical tools like File Roller allow you to unpack <span color='#00B7EB'><b>tar</b></span> with a simple click.""",


        "zst": """<span size='24000' weight='bold'>ZST package format: Simple explanation</span>

<span color='#00B7EB'><b>ZST</b></span> is an archive format mainly used in Linux distributions like Arch Linux and Manjaro for packaging programs. Files with the <b>.zst</b> extension contain compressed data, including programs or their source code, and are used together with the pacman package manager. It's like a compact folder that the system unpacks for installation.

<span size='24000' weight='bold'>What is ZST?</span>

<span color='#00B7EB'><b>ZST</b></span> is an archive created using the <b>Zstandard</b> compression algorithm, which provides high compression and fast decompression. In Arch-based systems, <span color='#00B7EB'><b>zst packages</b></span> contain the application, its dependencies, and installation instructions. They are managed by <b>pacman</b>, which works with repositories like the Arch User Repository (AUR) or local files.

<span size='24000' weight='bold'>Pros and Cons</span>

<span color='#00B7EB'><b>ZST</b></span> is convenient for Arch Linux because compression reduces file size, and pacman automates installation from repositories. The format is optimized for speed and efficiency. However, <span color='#00B7EB'><b>zst packages</b></span> are specific to Arch-based distributions and not suitable for Ubuntu or Fedora. Manual installation from <span color='#00B7EB'><b>zst files</b></span> may require setting up dependencies, which can be difficult for beginners. Download <span color='#00B7EB'><b>zst files</b></span> only from trusted sources like <b>AUR</b> to avoid malware.

<span size='24000' weight='bold'>How to install ZST packages</span>

The easiest way is to install a program with the command <span background='#010101'><span color='blue'>sudo</span> <span color='yellow'>pacman -S</span> <b>package_name</b></span>, so pacman downloads and installs the package from the repository. For a local <span color='#00B7EB'><b>zst file</b></span>, use <span background='#010101'><span color='blue'>sudo</span> <span color='yellow'>pacman -U</span> <b>filename.zst</b></span>, and the manager will handle the installation. For packages from <b>AUR</b>, use tools like <b>yay</b> to simplify the process. Graphical interfaces like Pamac allow you to install <span color='#00B7EB'><b>zst packages</b></span> with a single click.""",
    },



    "en": {
        "intro_in_packages": """
<span size="24000" weight="bold">What are packages and how to use them</span>

In the Linux world, <span color="#00B7EB"><b>packages</b></span> are special files containing programs, libraries, or other components required for the system or applications to work. Packages simplify the installation, updating, and removal of programs because they include everything needed: the program itself, its dependencies (other packages it relies on), and installation instructions.

<span size="24000" weight="bold">Why do you need packages?</span>

Imagine you want to install a text editor or a game. Instead of manually downloading files, searching for the necessary libraries, and configuring them, you use a package. The package contains everything ready for installation, and the package manager (a special program in Linux) automatically determines which additional components are needed and how to install them.

<span size="24000" weight="bold">How do packages work?</span>

In Linux, packages are managed by <span color="#00B7EB"><b>package managers</b></span>, which depend on your distribution. For example:

• Ubuntu and Debian use apt (packages with the .deb extension).
• Fedora and CentOS use dnf or yum (packages with the .rpm extension).
• Arch Linux uses pacman.

Package managers work with repositories—online storage locations containing thousands of packages. When you install a program, the package manager downloads the required package from the repository and installs it along with its dependencies.

In the following chapters, we will discuss different packages and see how to work with them!""",
        "appimage": """
<span size=\"24000\" weight=\"bold\">AppImage format: Simplicity and Universality</span>

<span color=\"#00B7EB\"><b>AppImage</b></span> is a package format for Linux that allows you to run programs without traditional installation. It is a single executable file containing the application and all its dependencies (libraries, configuration files), making it convenient for both beginners and experienced users.

<span size=\"24000\" weight=\"bold\">What is AppImage?</span>

<span color=\"#00B7EB\"><b>AppImage</b></span> is a <b>"portable"</b> format that works on most Linux distributions without the need to install via a package manager. You simply download a file with the <b>.AppImage</b> extension, make it executable, and run it. The program works immediately, without adding anything to the system.

<span size=\"24000\" weight=\"bold\">Advantages of this format</span>
It is universal and works on almost all popular Linux distributions. It is a monolithic file that contains all the necessary components to run the program; you just need to launch it. It is also fully isolated and does not interact with the system or file system, making its use quite safe.

<span size=\"24000\" weight=\"bold\">How to use AppImage?</span>
You can find this format in your Linux distribution's software store or download it from the developer's website. If you want to run it graphically, during installation right-click the file -> properties -> allow executing as a program, then just double-click the file.

If you prefer the terminal, use the following command:
<span background=\"#010101\"><span color=\"yellow\">chmod</span> <span color=\"#F34336\">+x</span> <b>filename.AppImage</b></span>""",
        "deb": """
<span size=\"24000\" weight=\"bold\">DEB package format: The essentials explained simply</span>

The DEB format is a way to deliver programs in Linux distributions like Ubuntu or Debian. A file with the .deb extension contains the program, its files, and everything needed for it to work. It's like a box with an application, ready to install.

<span size=\"24000\" weight=\"bold\">What is a DEB package?</span>

A <span color=\"#00B7EB\"><b>DEB package</b></span> is an archive containing the program, libraries, and installation instructions. It is created for a specific distribution to ensure everything works smoothly. Package managers like apt take DEB files from online repositories and install them automatically.

<span size=\"24000\" weight=\"bold\">Pros and Cons</span>

DEB packages are convenient because the <span color=\"#00B7EB\"><b>apt</b></span> manager finds and installs everything you need. They are reliable and tailored for your distribution. However, they do not work on other systems, like Fedora. If you download a DEB file separately, sometimes dependencies need to be added manually. Download files only from trusted sources to avoid malware.

<span size=\"24000\" weight=\"bold\">How to install DEB packages?</span>

The easiest way is to install a program with the command <span background=\"#010101\"><span color=\"blue\">sudo</span> <span color=\"yellow\">apt</span> <span color=\"green\">install</span> <b>package_name</b></span> — the manager will download and set up everything automatically. If you have a DEB file, use <span background=\"#010101\"><span color=\"blue\">sudo</span> <span color=\"yellow\">dpkg -i</span> <b>filename.deb</b></span>. If something is missing, the command <span background=\"#010101\"><span color=\"blue\">sudo</span> <span color=\"yellow\">apt</span> <span color=\"green\">install</span> -f</span> will help. You can also click the file in Ubuntu Software — installation will start automatically.""",
        "flatpack": """
<span size=\"24000\" weight=\"bold\">Flatpak package format: Simple explanation</span>

<span color=\"#00B7EB\"><b>Flatpak</b></span> is a modern package format for Linux, used in distributions like Ubuntu, Fedora, or Arch. A file with the <b>.flatpak</b> extension contains the application and its dependencies, allowing you to run the app without complex setup. It's like a container that ensures the program works on any Linux system.

<span size=\"24000\" weight=\"bold\">What is Flatpak?</span>

A <span color=\"#00B7EB\"><b>Flatpak package</b></span> is an archive that includes the application, libraries, and settings needed for it to work. It is isolated from the system, which increases security and makes installation easier across different distributions. Managing <span color=\"#00B7EB\"><b>flatpak packages</b></span> is done with the <span color=\"#00B7EB\"><b>flatpak</b></span> utility, which works with the online repository <span color=\"#00B7EB\"><b>Flathub</b></span>, where thousands of apps are stored.

<span size=\"24000\" weight=\"bold\">Pros and Cons</span>

<span color=\"#00B7EB\"><b>Flatpak</b></span> is convenient because it works on most distributions, and the <span color=\"#00B7EB\"><b>flatpak</b></span> utility automatically installs and updates apps. The isolation of packages reduces the risk of system issues. However, <span color=\"#00B7EB\"><b>flatpak packages</b></span> can take up more space due to included dependencies, and startup can sometimes be a bit slower. Some users prefer traditional packages for speed. Download <span color=\"#00B7EB\"><b>flatpak</b></span> only from Flathub or trusted sources to avoid malware.

<span size=\"24000\" weight=\"bold\">How to install Flatpak packages</span>

The easiest way is to install an app with the command <span background=\"#010101\"><span color=\"blue\">flatpak</span> <span color=\"yellow\">install</span> <span color=\"green\">flathub</span> <b>package_name</b></span> — the utility will download and set up everything automatically. Packages can also be found in <span color=\"#00B7EB\"><b>Flathub</b></span> via browser or graphical interfaces like GNOME Software, where installation starts with one click. Updates for <span color=\"#00B7EB\"><b>flatpak packages</b></span> happen automatically with <span background=\"#010101\"><span color=\"blue\">flatpak</span> <span color=\"yellow\">update</span></span>.""",
        "rpm": """
<span size=\"24000\" weight=\"bold\">RPM package format: Simple explanation</span>

<span color=\"#00B7EB\"><b>RPM format</b></span> is a way to deliver programs in Linux distributions like Fedora, CentOS, or openSUSE. A file with the .rpm extension contains the program, its files, and everything needed for it to work. It's like a package ready to be installed on your system.

<span size=\"24000\" weight=\"bold\">What is an RPM package?</span>

A <span color=\"#00B7EB\"><b>RPM package</b></span> is an archive with the application, libraries, and installation instructions. It is created for a specific distribution to ensure everything works correctly. Package managers like dnf or yum take RPM files from online repositories and install them automatically.

<span size=\"24000\" weight=\"bold\">Pros and Cons</span>

<span color=\"#00B7EB\"><b>RPM packages</b></span> are convenient because managers like <b>dnf</b> automatically find and install the necessary files. They are reliable and tailored for your distribution. However, they do not work on systems like Ubuntu. If you download an RPM file separately, sometimes dependencies need to be added manually. Download files only from safe sources to avoid malware.

<span size=\"24000\" weight=\"bold\">How to install RPM packages</span>

The simplest way is to use the command <span background=\"#010101\"><span color=\"blue\">sudo</span> <span color=\"yellow\">dnf</span> <span color=\"green\">install</span> <b>package_name</b></span>, which downloads and installs the program with dependencies. For a separate RPM file, use <span background=\"#010101\"><span color=\"blue\">sudo</span> <span color=\"yellow\">dnf</span> <span color=\"green\">install</span></span> to help add dependencies. In graphical interfaces like <b>GNOME Software</b>, you can simply click the file to install.""",
        "snap": """
<span size='24000' weight='bold'>Snap package format: Simple explanation</span>

<span color='#00B7EB'><b>Snap</b></span> is a modern package format for Linux, used in distributions like Ubuntu, Fedora, or Linux Mint. A file with the <b>.snap</b> extension contains the application, its dependencies, and everything needed for it to work. It's like a container that runs the app without complex setup.

<span size='24000' weight='bold'>What is Snap?</span>

A <span color='#00B7EB'><b>Snap package</b></span> is an archive that includes the application and all its dependencies, allowing it to run on different distributions. Snap packages are managed by the <span color='#00B7EB'><b>snapd</b></span> utility, which works with the online store <b>Snap Store</b>. Packages are isolated from the system, which increases security and simplifies installation.

<span size='24000' weight='bold'>Pros and Cons</span>

<span color='#00B7EB'><b>Snap</b></span> is convenient because it works on many distributions, and <span color='#00B7EB'><b>snapd</b></span> automatically installs and updates apps. Packages are isolated, reducing the risk of system issues. However, <span color='#00B7EB'><b>snap packages</b></span> can be larger, and startup can sometimes be slower due to isolation. Some users prefer traditional packages for speed. Download <span color='#00B7EB'><b>snap</b></span> only from the <b>Snap Store</b> to avoid malware.

<span size='24000' weight='bold'>How to install Snap packages</span>

The easiest way is to install an app with the command <span background='#010101'><span color='blue'>sudo</span> <span color='yellow'>snap</span> <span color='green'>install</span> <b>package_name</b></span> — the <span color='#00B7EB'><b>snapd</b></span> utility will download and set up everything automatically. Packages can also be found in the <b>Snap Store</b> via browser or graphical interfaces like <b>Ubuntu Software</b>, where installation starts with one click. Updates for snap packages happen automatically in the background.""",
        "tar": """
<span size='24000' weight='bold'>Tar package format: Simple explanation</span>

<span color='#00B7EB'><b>Tar</b></span> is an archive format often used in Linux to package files and programs. Files with the <b>.tar</b>, <b>.tar.gz</b>, or <b>.tar.bz2</b> extensions contain a set of data, which may include source code or ready-to-install files. It's like a compressed folder that you need to unpack and set up manually.

<span size='24000' weight='bold'>What is Tar?</span>

<span color='#00B7EB'><b>Tar</b></span> is an archive that combines files into one. In Linux, it is often used to distribute source code or data that the user must compile or install themselves. The <b>.tar.gz</b> and <b>.tar.bz2</b> formats mean the archive is compressed to save space. <span color='#00B7EB'><b>Tar</b></span> is not a package like <span color='#00B7EB'><b>deb</b></span> or <span color='#00B7EB'><b>snap</b></span>, but rather a way to transfer files.

<span size='24000' weight='bold'>Pros and Cons</span>

<span color='#00B7EB'><b>Tar</b></span> is universal and works on any Linux distribution, making it flexible for developers and enthusiasts. It allows distributing programs not available in repositories. However, installation from <span color='#00B7EB'><b>tar archives</b></span> is more complex, often requiring compilation and manual setup of dependencies, which can be difficult for beginners. Security is also important: download <span color='#00B7EB'><b>tar files</b></span> only from trusted sources to avoid malware.

<span size='24000' weight='bold'>How to install programs from Tar</span>

To work with <span color='#00B7EB'><b>tar archives</b></span>, unpack the file with a command like <span background='#010101'><span color='yellow'>tar</span> <span color='green'>-xzf</span> <b>filename.tar.gz</b></span>. If it's source code, you need to compile the program by following the instructions (usually in a <b>README</b> or <b>INSTALL</b> file). This may include commands like <b>./configure</b>, <span background='#010101'><span color='yellow'>make</span></span>, and <span background='#010101'><span color='blue'>sudo</span> <span color='yellow'>make</span> <span color='green'>install</span></span>. If the archive contains a ready program, just move the files to the desired location. Graphical tools like File Roller allow you to unpack <span color='#00B7EB'><b>tar</b></span> with a simple click.""",
        "zst": """
<span size='24000' weight='bold'>ZST package format: Simple explanation</span>

<span color='#00B7EB'><b>ZST</b></span> is an archive format mainly used in Linux distributions like Arch Linux and Manjaro for packaging programs. Files with the <b>.zst</b> extension contain compressed data, including programs or their source code, and are used together with the pacman package manager. It's like a compact folder that the system unpacks for installation.

<span size='24000' weight='bold'>What is ZST?</span>

<span color='#00B7EB'><b>ZST</b></span> is an archive created using the <b>Zstandard</b> compression algorithm, which provides high compression and fast decompression. In Arch-based systems, <span color='#00B7EB'><b>zst packages</b></span> contain the application, its dependencies, and installation instructions. They are managed by <b>pacman</b>, which works with repositories like the Arch User Repository (AUR) or local files.

<span size='24000' weight='bold'>Pros and Cons</span>

<span color='#00B7EB'><b>ZST</b></span> is convenient for Arch Linux because compression reduces file size, and pacman automates installation from repositories. The format is optimized for speed and efficiency. However, <span color='#00B7EB'><b>zst packages</b></span> are specific to Arch-based distributions and not suitable for Ubuntu or Fedora. Manual installation from <span color='#00B7EB'><b>zst files</b></span> may require setting up dependencies, which can be difficult for beginners. Download <span color='#00B7EB'><b>zst files</b></span> only from trusted sources like <b>AUR</b> to avoid malware.

<span size='24000' weight='bold'>How to install ZST packages</span>

The easiest way is to install a program with the command <span background='#010101'><span color='blue'>sudo</span> <span color='yellow'>pacman -S</span> <b>package_name</b></span>, so pacman downloads and installs the package from the repository. For a local <span color='#00B7EB'><b>zst file</b></span>, use <span background='#010101'><span color='blue'>sudo</span> <span color='yellow'>pacman -U</span> <b>filename.zst</b></span>, and the manager will handle the installation. For packages from <b>AUR</b>, use tools like <b>yay</b> to simplify the process. Graphical interfaces like Pamac allow you to install <span color='#00B7EB'><b>zst packages</b></span> with a single click.""",
    },
    "zh": {
        "intro_in_packages": """
<span size="24000" weight="bold">什么是包以及如何使用它们</span>

在Linux世界中，<span color="#00B7EB"><b>包</b></span>是包含程序、库或其他组件的特殊文件，这些组件对于系统或应用程序的运行是必需的。包简化了程序的安装、更新和删除，因为它们包含了所有必需的内容：程序本身、其依赖项（其他包，它们依赖于它）以及安装说明。

<span size="24000" weight="bold">为什么需要包？</span>

想象一下，您想安装文本编辑器或游戏。与其手动下载文件、搜索所需库并配置它们，您可以使用包。包包含所有准备就绪的安装内容，而包管理器（Linux中的特殊程序）会自动决定需要哪些额外的组件以及如何安装它们。

<span size="24000" weight="bold">包是如何工作的？</span>

在Linux中，包由<span color="#00B7EB"><b>包管理器</b></span>管理，这些管理器取决于您的发行版。例如：

• 在Ubuntu和Debian中使用apt（扩展名为.deb的包）。
• 在Fedora和CentOS中使用dnf或yum（扩展名为.rpm的包）。
• 在Arch Linux中使用pacman。

包管理器与<span color="#00B7EB"><b>仓库</b></span>（在线存储库）合作，其中包含数千个包。当您安装程序时，包管理器从仓库下载所需的包并与其依赖项一起安装。

在接下来的章节中，我们将讨论不同的包并研究如何使用它们！
""",


        "appimage": """<span size="24000" weight="bold">AppImage格式：简单性和通用性</span>

<span color="#00B7EB"><b>AppImage</b></span> — 这是Linux的包格式，它允许您在没有传统安装的情况下运行程序。这是一个包含应用程序及其所有依赖项（库、配置文件）的单一可执行文件，这使得它对新手和有经验的用户都很方便。

<span size="24000" weight="bold">什么是AppImage？</span>

<span color="#00B7EB"><b>AppImage</b></span> — 这是一个<b>「便携式」</b>格式，它可以在大多数Linux发行版上运行，而无需通过包管理器安装。您只需下载扩展名为<b>.AppImage</b>的文件，使其可执行，然后运行它。程序运行时不会添加任何内容到系统中。

<span size="24000" weight="bold">此格式的优点</span>
它非常通用，并且几乎可以在所有流行的Linux发行版上运行。这是一个包含所有必需组件的单一文件，只需运行它即可。它完全隔离，不会与系统或文件系统交互，这使得它的使用相当安全

<span size="24000" weight="bold">如何使用AppImage？</span>
您可以在您的Linux发行版的软件包管理器中找到此格式，或从程序开发者的网站下载。如果您想以图形方式运行它，则在安装时右键单击文件 -> 属性 -> 作为程序运行，然后只需双击文件即可。

如果您更喜欢终端，请使用以下命令：
<span background="#010101"><span color="yellow">chmod</span> <span color="#F34336">+x</span> <b>文件名.AppImage</b></span>""",


        "deb": """
<span size="24000" weight="bold">deb格式：简单说明</span>

deb 是Linux发行版（如Ubuntu或Debian）中用于分发程序的一种方式。扩展名为.deb的文件包含程序、其文件和所有必需的文件。这就像一个包含应用程序的盒子，准备就绪。

<span size="24000" weight="bold">什么是deb？</span>

<span color="#00B7EB"><b>Deb-包</b></span> — 这是一个包含程序、库和安装说明的存档。它为特定发行版创建，以确保一切正常工作。包管理器（如apt）从在线存储库（仓库）获取deb文件并自动安装它们。

<span size="24000" weight="bold">优点和缺点</span>

Deb-包很方便，因为包管理器<span color="#00B7EB"><b>apt</b></span>自己找到并安装所有必需的文件。它们可靠且适合您的发行版。但它们在其他系统（如Fedora）中不起作用。如果您单独下载deb文件，有时需要手动添加依赖项。请从可信来源下载文件，以避免恶意代码。

<span size="24000" weight="bold">如何安装deb包？</span>

最简单的方法是使用命令<span background="#010101"><span color="blue">sudo</span> <span color="yellow">apt</span> <span color="green">install</span> <b>包名</b></span> — 包管理器会自动下载并设置。如果您有deb文件，请使用<span background="#010101"><span color="blue">sudo</span> <span color="yellow">dpkg -i</span> <b>文件名.deb</b></span>。如果缺少某些内容，命令<span background="#010101"><span color="blue">sudo</span> <span color="yellow">apt</span> <span color="green">install</span> -f</span>会帮助您。您也可以在Ubuntu Software中点击文件进行安装，安装会自动开始。""",


        "flatpack": """<span size="24000" weight="bold">Flatpak格式：简单说明</span>

<span color="#00B7EB"><b>Flatpak</b></span> — 这是Linux的现代包格式，用于在Ubuntu、Fedora或Arch等发行版中运行应用程序。扩展名为<b>.flatpak</b>的文件包含程序及其依赖项，这使得无需复杂设置即可运行应用程序。这是一个包含应用程序的容器，确保在任何Linux系统上运行。

<span size="24000" weight="bold">什么是Flatpak？</span>

<span color="#00B7EB"><b>Flatpak-包</b></span> — 这是一个包含应用程序、库和设置的存档，以确保其正常工作。它与系统隔离，这提高了安全性并简化了在不同发行版上的安装。<span color="#00B7EB"><b>Flatpak-包</b></span>的管理通过<span color="#00B7EB"><b>latpak</b></span>工具完成，该工具与在线存储库<span color="#00B7EB"><b>Flathub</b></span>合作，其中包含数千个应用程序。

<span size="24000" weight="bold">优点和缺点</span>

<span color="#00B7EB"><b>Flatpak</b></span> 很方便，因为它几乎可以在所有发行版上运行，而<span color="#00B7EB"><b>latpak</b></span>工具会自动安装和更新程序。包隔离降低了系统故障的风险。然而，<span color="#00B7EB"><b>Flatpak-包</b></span>可能会占用更多空间，因为它们包含依赖项，并且运行速度稍慢。一些用户可能更喜欢传统包以获得速度。请从<span color="#00B7EB"><b>Flatpak</b></span>仅从Flathub或可信来源下载，以避免恶意代码。

<span size="24000" weight="bold">如何安装Flatpak包？</span>

最简单的方法是使用命令<span background="#010101"><span color="blue">flatpak</span> <span color="yellow">install</span> <span color="green">flathub</span> <b>包名</b></span> — <span color="#00B7EB"><b>latpak</b></span>工具会自动下载并设置所有内容。您还可以通过浏览器或图形界面（如GNOME Software）在<span color="#00B7EB"><b>Flathub</b></span>中找到包，安装只需一次点击。<span color="#00B7EB"><b>Flatpak-包</b></span>的更新通过<span background="#010101"><span color="blue">flatpak</span> <span color="yellow">update</span></span>自动进行。""",


        "rpm": """<span size="24000" weight="bold">RPM格式：简单说明</span>

<span color="#00B7EB"><b>RPM格式</b></span> — 这是在Fedora、CentOS或openSUSE等Linux发行版中分发程序的一种方式。扩展名为.rpm的文件包含程序、其文件和所有必需的文件。这是一个准备安装到您系统的盒子。

<span size="24000" weight="bold">什么是RPM？</span>

<span color="#00B7EB"><b>RPM-包</b></span> — 这是一个包含程序、库和安装说明的存档。它为特定发行版创建，以确保一切正常工作。包管理器（如dnf或yum）从在线存储库（仓库）获取RPM文件并自动安装它们。

<span size="24000" weight="bold">优点和缺点</span>

<span color="#00B7EB"><b>RPM-包很方便</b></span>，因为包管理器（如<b>dnf</b>）自己找到并安装所需文件。它们可靠且适合您的发行版。但它们在Ubuntu等系统中不起作用。如果您单独下载RPM文件，有时需要手动添加依赖项。请从安全来源下载文件，以避免恶意代码。

<span size="24000" weight="bold">如何安装RPM包？</span>

最简单的方法是使用命令<span background="#010101"><span color="blue">sudo</span> <span color="yellow">dnf</span> <span color="green">install</span> <b>包名</b></span>，它下载并安装带有依赖项的程序。对于单独的RPM文件，使用<span background="#010101"><span color="blue">sudo</span> <span color="yellow">dnf</span> <span color="green">install</span></span>会帮助添加依赖项。在图形界面（如<b>GNOME Software</b>）中，只需点击文件即可安装。""",


        "snap": """
<span size='24000' weight='bold'>Snap格式：简单说明</span>

<span color='#00B7EB'><b>Snap</b></span> — 这是Linux的现代包格式，用于在Ubuntu、Fedora或Linux Mint等发行版中运行应用程序。扩展名为<span color='#00B7EB'><b>.snap</b></span>的文件包含程序及其依赖项和所有必需的文件。这是一个无需复杂设置即可运行的容器。

<span size='24000' weight='bold'>什么是Snap？</span>

<span color='#00B7EB'><b>Snap-包</b></span> — 这是一个包含应用程序及其所有依赖项的存档，这使得它可以运行在不同的发行版上。<span color='#00B7EB'><b>Snap-包</b></span>的管理通过<span color='#00B7EB'><b>snapd</b></span>工具完成，该工具与在线商店<b>Snap Store</b>合作。包与系统隔离，这提高了安全性并简化了安装。

<span size='24000' weight='bold'>优点和缺点</span>

<span color='#00B7EB'><b>Snap</b></span> 很方便，因为它几乎可以在所有发行版上运行，而<span color='#00B7EB'><b>snapd</b></span>工具会自动安装和更新程序。包隔离降低了系统故障的风险。然而，<span color='#00B7EB'><b>Snap-包</b></span>可能会占用更多空间，因为它们包含依赖项，并且运行速度稍慢。一些用户可能更喜欢传统包以获得速度。请从<span color='#00B7EB'><b>Snap</b></span>仅从<b>Snap Store</b>或可信来源下载，以避免恶意代码。

<span size='24000' weight='bold'>如何安装Snap包？</span>

最简单的方法是使用命令<span background='#010101'><span color='blue'>sudo</span> <span color='yellow'>snap</span> <span color='green'>install</span> <b>包名</b></span> — <span color='#00B7EB'><b>snapd</b></span>工具会自动下载并设置所有内容。您还可以通过浏览器或图形界面（如<b>Ubuntu Software</b>）在<b>Snap Store</b>中找到包，安装只需一次点击。<span color='#00B7EB'><b>Snap-包</b></span>的更新通过<span background='#010101'><span color="blue">snap</span> <span color="yellow">update</span></span>自动进行。
""",


        "tar": """<span size='24000' weight='bold'>Tar格式：简单说明</span>

<span color='#00B7EB'><b>Tar</b></span> — 这是Linux用于打包文件和程序的存档格式。扩展名为<b>.tar</b>、<b>.tar.gz</b>或<b>.tar.bz2</b>的文件包含一组数据，这些数据可能包含程序的源代码或用于安装的成品文件。这是一个压缩的文件夹，需要解压并手动配置。

<span size='24000' weight='bold'>什么是Tar？</span>

<span color='#00B7EB'><b>Tar</b></span> — 这是一个将文件合并到一个文件中的存档。在Linux中，它经常用于分发程序的源代码或用户需要自行编译或安装的数据。<b>.tar.gz</b>和<b>.tar.bz2</b>格式表示存档已压缩以节省空间。<span color='#00B7EB'><b>Tar</b></span>不是一个包，如<span color='#00B7EB'><b>deb</b></span>或<span color='#00B7EB'><b>snap</b></span>，而是一个文件传输方式。

<span size='24000' weight='bold'>优点和缺点</span>

<span color='#00B7EB'><b>Tar</b></span> 非常通用，并且几乎可以在任何Linux发行版上运行，这使得它对开发人员和爱好者来说非常灵活。它允许分发不在仓库中的程序。然而，从<span color='#00B7EB'><b>tar-存档</b></span>安装更复杂，因为通常需要编译源代码并手动配置依赖项。这可能对新手来说很困难。安全性也很重要：请从安全来源下载<span color='#00B7EB'><b>tar-文件</b></span>，以避免恶意代码。

<span size='24000' weight='bold'>如何安装程序从Tar？</span>

对于<span color='#00B7EB'><b>tar-存档</b></span>，使用命令解压文件，例如<span background='#010101'><span color="yellow">tar</span> <span color="green">-xzf</span> <b>文件名.tar.gz.</b></span> 如果这是源代码，则需要按照说明（通常在<b>README</b>或<b>INSTALL</b>文件中）编译程序。这可能包括<b>./configure</b>、<span background='#010101'><span color="yellow">make</span></span>和<span background='#010101'><span color="blue">sudo</span> <span color="yellow">make</span> <span color="green">install</span></span>等命令。如果存档包含成品程序，只需将文件移动到所需位置即可。图形工具（如File Roller）允许您通过单击解压<span color='#00B7EB'><b>tar</b></span>。""",


        "zst": """<span size='24000' weight='bold'>ZST格式：简单说明</span>

<span color='#00B7EB'><b>ZST</b></span> — 这是Linux中主要用于Arch Linux和Manjaro等发行版中打包程序的存档格式。扩展名为<span color='#00B7EB'><b>.zst</b></span>的文件包含压缩数据，包括程序或其源代码，并与包管理器pacman一起使用。这是一个压缩的文件夹，系统会解压以进行安装。

<span size='24000' weight='bold'>什么是ZST？</span>

<span color='#00B7EB'><b>ZST</b></span> — 这是一个使用<b>Zstandard</b>压缩算法创建的存档，该算法提供高压缩率和快速解压。在Arch-based系统中，<span color='#00B7EB'><b>zst-包</b></span>包含应用程序、其依赖项和安装说明。管理通过<b>pacman</b>完成，它与仓库（如Arch User Repository (AUR)）或本地文件合作。

<span size='24000' weight='bold'>优点和缺点</span>

<span color='#00B7EB'><b>ZST</b></span> 对于Arch Linux来说很方便，因为压缩减少了文件大小，而pacman自动化了从仓库的安装。格式针对速度和效率进行了优化。然而，<span color='#00B7EB'><b>zst-包</b></span>是Arch-based发行版的特定，不适合Ubuntu或Fedora。手动安装<span color='#00B7EB'><b>zst-文件</b></span>可能需要手动配置依赖项，这可能对新手来说很困难。请从<span color='#00B7EB'><b>AUR</b></span>或可信来源下载<span color='#00B7EB'><b>zst-文件</b></span>，以避免恶意代码。

<span size='24000' weight='bold'>如何安装ZST包？</span>

最简单的方法是使用命令<span background='#010101'><span color="blue">sudo</span> <span color="yellow">pacman -S</span> <b>包名</b></span>，这将使pacman从仓库下载并安装包。对于本地<span color='#00B7EB'><b>zst-文件</b></span>，使用<span background='#010101'><span color="blue">sudo</span> <span color="yellow">pacman -U</span> <b>文件名.zst</b></span>，并且包管理器会自动处理安装。对于<b>AUR</b>中的包，使用<b>yay</b>等工具，这些工具简化了过程。图形界面（如Pamac）允许您通过单击安装<span color='#00B7EB'><b>zst-包</b></span>。""",
    },
    "ja": {
        "intro_in_packages": """
<span size='24000' weight='bold'>パッケージとは何か、そしてその使い方</span>

Linuxの世界では、<span color='#00B7EB'><b>パッケージ</b></span>は、システムやアプリケーションの動作に必要なプログラム、ライブラリ、その他のコンポーネントを含む特別なファイルです。パッケージは、プログラムのインストール、更新、削除を簡単にします。なぜなら、必要なもの（プログラム本体、依存関係、インストール手順）がすべて含まれているからです。

<span size='24000' weight='bold'>なぜパッケージが必要なのか？</span>

例えば、テキストエディタやゲームをインストールしたいとします。ファイルを手動でダウンロードし、必要なライブラリを探して設定する代わりに、パッケージを使えばすべてが揃っています。パッケージマネージャー（Linuxの特別なプログラム）が自動的に追加コンポーネントの有無やインストール方法を判断します。

<span size='24000' weight='bold'>パッケージはどのように動作するのか？</span>

Linuxでは、パッケージはディストリビューションごとに異なる<span color='#00B7EB'><b>パッケージマネージャー</b></span>で管理されます。例えば：

• UbuntuやDebianではapt（.deb拡張子のパッケージ）
• FedoraやCentOSではdnfまたはyum（.rpmパッケージ）
• Arch Linuxではpacman

パッケージマネージャーはリポジトリ（オンラインのパッケージ倉庫）と連携し、数千のパッケージを管理します。プログラムをインストールすると、必要なパッケージがリポジトリからダウンロードされ、依存関係とともにインストールされます。

次の章では、さまざまなパッケージとその使い方を解説します！
""",
        "appimage": """
<span size='24000' weight='bold'>AppImage</span>

AppImageは、Linux向けのポータブルなアプリケーションパッケージ形式です。インストール不要で、ダウンロードしたファイルに実行権限を与えるだけで使えます。システムに変更を加えずにアプリを試したい場合に便利です。
""",
        "deb": """
<span size='24000' weight='bold'>DEBパッケージ</span>

DEBは、DebianやUbuntuなどのディストリビューションで使われるパッケージ形式です。aptやdpkgコマンドで管理され、依存関係の自動解決や簡単なインストールが特徴です。
""",
        "flatpack": """
<span size='24000' weight='bold'>Flatpak</span>

Flatpakは、ディストリビューションに依存しないLinuxアプリの配布形式です。サンドボックス化されており、アプリごとに依存関係を分離して安全に動作します。Flathubリポジトリから多くのアプリを簡単にインストールできます。
""",
        "rpm": """
<span size='24000' weight='bold'>RPMパッケージ</span>

RPMは、FedoraやCentOSなどで使われるパッケージ形式です。dnfやyumコマンドで管理され、システムの一貫性を保ちながらソフトウェアのインストールや更新が行えます。
""",
        "snap": """
<span size='24000' weight='bold'>Snap</span>

Snapは、Canonicalが開発したパッケージ形式で、Ubuntuをはじめ多くのディストリビューションで利用できます。アプリとその依存関係を一つのパッケージにまとめ、隔離された環境で動作します。
""",
        "tar": """
<span size='24000' weight='bold'>Tarアーカイブ</span>

Tarは、ソースコードやアプリケーションを圧縮・配布するための伝統的な形式です。展開後、手動でビルドやインストールが必要な場合があります。
""",
        "zst": """
<span size='24000' weight='bold'>ZSTパッケージ</span>

ZSTは、Arch LinuxやManjaroで使われる圧縮パッケージ形式です。pacmanコマンドで管理され、高速なインストールとアップデートが可能です。
"""
    },
    "fr": {
        "intro_in_packages": """
<span size='24000' weight='bold'>Qu'est-ce qu'un paquet et comment les utiliser</span>

Dans le monde Linux, un <span color='#00B7EB'><b>paquet</b></span> est un fichier spécial contenant des programmes, des bibliothèques ou d'autres composants nécessaires au fonctionnement du système ou des applications. Les paquets simplifient l'installation, la mise à jour et la suppression des programmes, car ils incluent tout le nécessaire : le programme lui-même, ses dépendances (autres paquets dont il dépend) et les instructions d'installation.

<span size='24000' weight='bold'>Pourquoi les paquets sont-ils nécessaires ?</span>

Imaginez que vous souhaitez installer un éditeur de texte ou un jeu. Au lieu de télécharger manuellement les fichiers, de rechercher les bibliothèques nécessaires et de les configurer, vous utilisez un paquet. Le paquet contient tout ce qu'il faut pour l'installation, et le gestionnaire de paquets (un programme spécial sous Linux) décide automatiquement des composants supplémentaires nécessaires et de la façon de les installer.

<span size='24000' weight='bold'>Comment fonctionnent les paquets ?</span>

Sous Linux, les paquets sont gérés par des <span color='#00B7EB'><b>gestionnaires de paquets</b></span> qui dépendent de votre distribution. Par exemple :

• Ubuntu et Debian utilisent apt (paquets .deb).
• Fedora et CentOS utilisent dnf ou yum (paquets .rpm).
• Arch Linux utilise pacman.

Les gestionnaires de paquets travaillent avec des dépôts en ligne contenant des milliers de paquets. Lorsque vous installez un programme, le gestionnaire télécharge le paquet requis et l'installe avec ses dépendances.

Les chapitres suivants aborderont différents paquets et expliqueront comment les utiliser !
""",
        "appimage": """
<span size='24000' weight='bold'>AppImage</span>

AppImage est un format de paquet portable pour Linux. Il ne nécessite pas d'installation : il suffit de donner les droits d'exécution au fichier téléchargé pour l'utiliser. Pratique pour tester des applications sans modifier le système.
""",
        "deb": """
<span size='24000' weight='bold'>Paquet DEB</span>

DEB est le format de paquet utilisé par Debian, Ubuntu et leurs dérivés. Il est géré par les commandes apt ou dpkg, avec résolution automatique des dépendances et installation simplifiée.
""",
        "flatpack": """
<span size='24000' weight='bold'>Flatpak</span>

Flatpak est un format de distribution d'applications indépendant de la distribution Linux. Les applications sont isolées (sandbox) et leurs dépendances séparées, ce qui garantit sécurité et compatibilité. Le dépôt Flathub propose de nombreuses applications faciles à installer.
""",
        "rpm": """
<span size='24000' weight='bold'>Paquet RPM</span>

RPM est le format de paquet utilisé par Fedora, CentOS et d'autres distributions. Il est géré par les commandes dnf ou yum, permettant une installation et une mise à jour cohérentes du système.
""",
        "snap": """
<span size='24000' weight='bold'>Snap</span>

Snap est un format de paquet développé par Canonical, utilisé sur Ubuntu et d'autres distributions. Il regroupe l'application et ses dépendances dans un seul paquet, fonctionnant dans un environnement isolé.
""",
        "tar": """
<span size='24000' weight='bold'>Archive Tar</span>

Tar est un format traditionnel pour compresser et distribuer des sources ou des applications. Après extraction, il peut être nécessaire de compiler ou d'installer manuellement.
""",
        "zst": """
<span size='24000' weight='bold'>Paquet ZST</span>

ZST est un format de paquet compressé utilisé par Arch Linux et Manjaro. Il est géré par la commande pacman, permettant une installation et une mise à jour rapides.
"""
    },
    "de": {
        "intro_in_packages": """
<span size='24000' weight='bold'>Was sind Pakete und wie arbeitet man damit?</span>

In der Linux-Welt ist ein <span color='#00B7EB'><b>Paket</b></span> eine spezielle Datei, die Programme, Bibliotheken oder andere Komponenten enthält, die für das System oder Anwendungen erforderlich sind. Pakete vereinfachen die Installation, Aktualisierung und Entfernung von Programmen, da sie alles Notwendige enthalten: das Programm selbst, seine Abhängigkeiten (andere Pakete, von denen es abhängt) und Anweisungen für die richtige Installation.

<span size='24000' weight='bold'>Wozu braucht man Pakete?</span>

Stellen Sie sich vor, Sie möchten einen Texteditor oder ein Spiel installieren. Anstatt Dateien manuell herunterzuladen, die benötigten Bibliotheken zu suchen und zu konfigurieren, verwenden Sie ein Paket. Das Paket enthält alles für die Installation, und der Paketmanager (ein spezielles Programm unter Linux) entscheidet automatisch, welche zusätzlichen Komponenten benötigt werden und wie sie installiert werden.

<span size='24000' weight='bold'>Wie funktionieren Pakete?</span>

Unter Linux werden Pakete mit <span color='#00B7EB'><b>Paketmanagern</b></span> verwaltet, die von Ihrer Distribution abhängen. Zum Beispiel:

• In Ubuntu und Debian wird apt verwendet (Pakete mit der Endung .deb).
• In Fedora und CentOS dnf oder yum (Pakete .rpm).
• In Arch Linux pacman.

Paketmanager arbeiten mit Online-Repositorien, die Tausende von Paketen enthalten. Wenn Sie ein Programm installieren, lädt der Paketmanager das benötigte Paket aus dem Repository herunter und installiert es zusammen mit den Abhängigkeiten.

In den folgenden Kapiteln werden wir verschiedene Pakete besprechen und sehen, wie man mit ihnen arbeitet!
""",
        "appimage": """
<span size='24000' weight='bold'>AppImage</span>

AppImage ist ein portables Paketformat für Linux. Es erfordert keine Installation: Einfach die heruntergeladene Datei ausführbar machen und starten. Praktisch, um Programme zu testen, ohne das System zu verändern.
""",
        "deb": """
<span size='24000' weight='bold'>DEB-Paket</span>

DEB ist das Paketformat für Debian, Ubuntu und deren Derivate. Es wird mit apt oder dpkg verwaltet, bietet automatische Auflösung von Abhängigkeiten und eine einfache Installation.
""",
        "flatpack": """
<span size='24000' weight='bold'>Flatpak</span>

Flatpak ist ein distributionsunabhängiges Format zur Verteilung von Linux-Anwendungen. Die Anwendungen laufen in einer Sandbox, Abhängigkeiten sind getrennt, was Sicherheit und Kompatibilität erhöht. Über das Flathub-Repository lassen sich viele Apps einfach installieren.
""",
        "rpm": """
<span size='24000' weight='bold'>RPM-Paket</span>

RPM ist das Paketformat für Fedora, CentOS und andere Distributionen. Es wird mit dnf oder yum verwaltet und ermöglicht eine konsistente Installation und Aktualisierung von Software.
""",
        "snap": """
<span size='24000' weight='bold'>Snap</span>

Snap ist ein von Canonical entwickeltes Paketformat, das auf Ubuntu und vielen anderen Distributionen verwendet wird. Es bündelt die Anwendung und ihre Abhängigkeiten in einem Paket und läuft isoliert.
""",
        "tar": """
<span size='24000' weight='bold'>Tar-Archiv</span>

Tar ist ein traditionelles Format zum Komprimieren und Verteilen von Quellcode oder Anwendungen. Nach dem Entpacken ist oft eine manuelle Kompilierung oder Installation erforderlich.
""",
        "zst": """
<span size='24000' weight='bold'>ZST-Paket</span>

ZST ist ein komprimiertes Paketformat, das in Arch Linux und Manjaro verwendet wird. Es wird mit dem Befehl pacman verwaltet und ermöglicht eine schnelle Installation und Aktualisierung.
"""
    },
} 