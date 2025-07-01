from hotkeys_chapters.introduction_topic import get_intro_panel as _get_intro_panel
from hotkeys_chapters.gnomehotk import get_gnomehotk_panel as _get_gnomehotk_panel
from gi.repository import Gtk

def get_intro_panel():
    return _get_intro_panel()

def get_gnomehotk_panel():
    return _get_gnomehotk_panel()

