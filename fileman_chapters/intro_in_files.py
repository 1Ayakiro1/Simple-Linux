import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, Gdk
from code.text import chapter_texts
from translations.main_titles import current_language
from code.dynamic_refs import dynamic_labels
from translations.fileman_chapters import fileman_translations
import os

# --- CSS connetcton start ---
css_provider = Gtk.CssProvider()
css_path = os.path.join(os.path.dirname(__file__), "../styles/fileman.css")
try:
    css_provider.load_from_path(css_path)
    Gtk.StyleContext.add_provider_for_display(
        Gdk.Display.get_default(),
        css_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )
except Exception as e:
    print(f"[CSS ERROR] {e}")
# --- CSS connection end ---



scrolled_window_intro_in_files = Gtk.ScrolledWindow()
scrolled_window_intro_in_files.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

# Main Box in scrolled window
main_box_panel_intro_in_files = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
main_box_panel_intro_in_files.set_valign(Gtk.Align.START)
main_box_panel_intro_in_files.add_css_class("intro-list")

# Back button
back_button = Gtk.Button(label="‹")
back_button.add_css_class("back-button1")
back_button.set_size_request(50, 50)
back_button.set_halign(Gtk.Align.START)
back_button.set_hexpand(False)
main_box_panel_intro_in_files.append(back_button)

# Label
label = Gtk.Label(label=fileman_translations[current_language]["intro_in_files"])
label.set_use_markup(True)
dynamic_labels.append((label, "intro_in_files"))
label.add_css_class("introduction")
label.set_wrap(True)
label.set_xalign(0)
main_box_panel_intro_in_files.append(label)

scrolled_window_intro_in_files.set_child(main_box_panel_intro_in_files)

def get_intro_in_files_panel():
    return scrolled_window_intro_in_files, "intro_in_files_panel", back_button

def get_intro_in_files_text():
    return fileman_translations[current_language]["intro_in_files"]