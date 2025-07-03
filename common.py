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
from linux_term_chapters.auto_and_scripts import get_auto_and_scripts_panel as _get_auto_and_scripts_panel
from linux_term_chapters.files_and_directories import get_files_and_directories_panel as _get_files_and_directories_panel
from linux_term_chapters.intro_in_terminal import get_intro_in_terminal_panel as _get_intro_in_terminal_panel
from linux_term_chapters.lifehacks import get_lifehacks_panel as _get_lifehacks_panel
from linux_term_chapters.navigation import get_navigation_panel as _get_navigation_panel
from linux_term_chapters.network import get_network_panel as _get_network_panel
from linux_term_chapters.processes import get_processes_panel as _get_processes_panel
from linux_term_chapters.utils import get_utils_panel as _get_utils_panel
from fileman_chapters.intro_in_files import get_intro_in_files_panel as _get_intro_in_files_panel
from fileman_chapters.bouble_commander import get_bouble_commander_panel as _get_bouble_commander_panel
from fileman_chapters.caja import get_caja_panel as _get_caja_panel
from fileman_chapters.dolphin import get_dolphin_panel as _get_dolphin_panel
from fileman_chapters.gnome_commander import get_gnome_commander_panel as _get_gnome_commander_panel
from fileman_chapters.nautilus import get_nautilus_panel as _get_nautilus_panel
from fileman_chapters.sunflower import get_sunflower_panel as _get_sunflower_panel
from fileman_chapters.thunar import get_thunar_panel as _get_thunar_panel
from gi.repository import Gtk
from language_panel import get_language_panel as _get_language_panel

def get_intro_panel():
    return _get_intro_panel()

def get_gnomehotk_panel():
    return _get_gnomehotk_panel()

def get_kdehotk_panel():
    return _get_kdehotk_panel()

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

def get_language_panel():
    return _get_language_panel()

def get_auto_and_scripts_panel():
    return _get_auto_and_scripts_panel()

def get_files_and_directories_panel():
    return _get_files_and_directories_panel()

def get_intro_in_terminal_panel():
    return _get_intro_in_terminal_panel()

def get_lifehacks_panel():
    return _get_lifehacks_panel()

def get_navigation_panel():
    return _get_navigation_panel()

def get_network_panel():
    return _get_network_panel()

def get_processes_panel():
    return _get_processes_panel()

def get_utils_panel():
    return _get_utils_panel()

def get_intro_in_files_panel():
    return _get_intro_in_files_panel()

def get_bouble_commander_panel():
    return _get_bouble_commander_panel()

def get_caja_panel():
    return _get_caja_panel()

def get_dolphin_panel():
    return _get_dolphin_panel()

def get_gnome_commander_panel():
    return _get_gnome_commander_panel()

def get_nautilus_panel():
    return _get_nautilus_panel()

def get_sunflower_panel():
    return _get_sunflower_panel()

def get_thunar_panel():
    return _get_thunar_panel()


