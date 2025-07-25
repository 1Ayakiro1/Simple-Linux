import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, Gdk
from code.text import chapter_texts
from translations.main_titles import current_language
from code.dynamic_refs import dynamic_labels
from translations.packages_chapters import packages_translations
import os

# --- CSS connetcton start ---
css_provider = Gtk.CssProvider()
css_path = os.path.join(os.path.dirname(__file__), "../styles/packages.css")
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



scrolled_window_deb_topic = Gtk.ScrolledWindow()
scrolled_window_deb_topic.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

# Main Box in scrolled window
main_box_panel_deb_topic = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
main_box_panel_deb_topic.set_valign(Gtk.Align.START)
main_box_panel_deb_topic.add_css_class("intro-list")

# Back button
back_button = Gtk.Button(label="‹")
back_button.add_css_class("back-button1")
back_button.set_size_request(50, 50)
back_button.set_halign(Gtk.Align.START)
back_button.set_hexpand(False)
main_box_panel_deb_topic.append(back_button)

# Label
label = Gtk.Label(label=packages_translations[current_language]["deb"])
label.set_use_markup(True)
dynamic_labels.append((label, "deb"))
label.add_css_class("debchik") #Why not xd
label.set_wrap(True)
label.set_xalign(0)
main_box_panel_deb_topic.append(label)

scrolled_window_deb_topic.set_child(main_box_panel_deb_topic)

def get_deb_panel():
    return scrolled_window_deb_topic, "hotkeys_intro_panel", back_button

def get_deb_text():
    return packages_translations[current_language]["deb"]