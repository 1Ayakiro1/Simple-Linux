#Файл, который служит "прослойкой" между основным кодом main.py и модулями с панелями (например, introduction_topic.py).

from hotkeys_chapters.introduction_topic import get_intro_panel as _get_intro_panel
from hotkeys_chapters.gnomehotk import get_gnomehotk_panel as _get_gnomehotk_panel
from hotkeys_chapters.kdehotk import get_kdehotk_panel as _get_kdehotk_panel
from hotkeys_chapters.terminalhotk import get_terminalhotk_panel as _get_terminalhotk_panel
from packages_chapters.intro_in_packages import get_intro_in_packages_panel as _get_intro_in_packages_panel
from packages_chapters.appimage import get_appimage_panel as _get_appimage_panel
from packages_chapters.deb import get_deb_panel as _get_deb_panel
from packages_chapters.rpm import get_rpm_panel as _get_rpm_panel
from packages_chapters.snap import get_snap_panel as _get_snap_panel
from packages_chapters.tar import get_tar_panel as _get_tar_panel
from packages_chapters.flatpack import get_flatpack_panel as _get_flatpack_panel
from packages_chapters.zst import get_zst_panel as _get_zst_panel
from gi.repository import Gtk

def get_intro_panel():
    return _get_intro_panel()

def get_gnomehotk_panel():
    return _get_gnomehotk_panel()

def get_kdehotk_panel():
    return _get_gnomehotk_panel()

def get_terminalhotk_panel():
    return _get_terminalhotk_panel()

def get_intro_in_packages_panel():
    return _get_intro_in_packages_panel()

def get_appimage_panel():
    return _get_appimage_panel()

def get_deb_panel():
    return _get_deb_panel()

def get_rpm_panel():
    return _get_rpm_panel()

def get_snap_panel():   
    return _get_snap_panel()

def get_tar_panel():
    return _get_tar_panel()

def get_flatpack_panel():
    return _get_flatpack_panel()

def get_zst_panel():
    return _get_zst_panel()


