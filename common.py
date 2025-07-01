#Файл, который служит "прослойкой" между основным кодом main.py и модулями с панелями (например, introduction_topic.py).

from hotkeys_chapters.introduction_topic import get_intro_panel as _get_intro_panel
from hotkeys_chapters.gnomehotk import get_gnomehotk_panel as _get_gnomehotk_panel
from hotkeys_chapters.kdehotk import get_kdehotk_panel as _get_kdehotk_panel
from gi.repository import Gtk

def get_intro_panel():
    return _get_intro_panel()

def get_gnomehotk_panel():
    return _get_gnomehotk_panel()

def get_kdehotk_panel():
    return _get_gnomehotk_panel()


