translations = {
    "en": {
        "hello": "Hello!",
        "main_title": "Let's Begin!",
        "hotkeys": "Hotkeys",
        "file_manager": "File manager",
        "packages": "Packages & installing",
    },
    "ru": {
        "hello": "Привет!",
        "main_title": "Начнем!",
        "hotkeys": "Горячие клавиши",
        "file_manager": "Файловый менеджер",
        "packages": "Пакеты и установка",
    },
    "zh": {
        "hello": "你好！",
        "main_title": "让我们开始吧！",
        "hotkeys": "快捷键",
        "file_manager": "文件管理器",
        "packages": "软件包与安装",
    },
    "ja": {
        "hello": "こんにちは！",
        "main_title": "始めましょう！",
        "hotkeys": "ホットキー",
        "file_manager": "ファイルマネージャー",
        "packages": "パッケージとインストール",
    },
    "fr": {
        "hello": "Bonjour!",
        "main_title": "Commençons!",
        "hotkeys": "Raccourcis clavier",
        "file_manager": "Gestionnaire de fichiers",
        "packages": "Paquets et installation",
    },
    "de": {
        "hello": "Hallo!",
        "main_title": "Los geht's!",
        "hotkeys": "Tastenkombinationen",
        "file_manager": "Dateimanager",
        "packages": "Pakete & Installation",
    },
    "es": {
        "hello": "¡Hola!",
        "main_title": "¡Empecemos!",
        "hotkeys": "Atajos de teclado",
        "file_manager": "Administrador de archivos",
        "packages": "Paquetes e instalación",
    },
}

current_language = "en"

def get_translation(key, lang=None):
    if lang is None:
        lang = current_language
    return translations.get(lang, {}).get(key, key) 