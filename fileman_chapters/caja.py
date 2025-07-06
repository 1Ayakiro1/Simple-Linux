import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from code.text import chapter_texts
from translations.main_titles import current_language
from code.dynamic_refs import dynamic_labels
from translations.fileman_chapters import fileman_translations



scrolled_window_caja = Gtk.ScrolledWindow()
scrolled_window_caja.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

# Main Box in scrolled window
main_box_panel_caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
main_box_panel_caja.set_valign(Gtk.Align.START)
main_box_panel_caja.add_css_class("intro-list")

# Back button
back_button = Gtk.Button(label="‹")
back_button.add_css_class("back-button1")
back_button.set_size_request(50, 50)
back_button.set_halign(Gtk.Align.START)
back_button.set_hexpand(False)
main_box_panel_caja.append(back_button)

# Label
label = Gtk.Label(label=fileman_translations[current_language]["caja"])
label.set_use_markup(True)
dynamic_labels.append((label, "caja"))
label.add_css_class("intro-label")
main_box_panel_caja.append(label)

scrolled_window_caja.set_child(main_box_panel_caja)

def get_caja_panel():
    return scrolled_window_caja, "caja_panel", back_button

def get_caja_text():
    return fileman_translations[current_language]["caja"]