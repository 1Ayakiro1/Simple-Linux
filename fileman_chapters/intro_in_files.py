import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from code.text import chapter_texts
from translations import current_language
from code.dynamic_refs import dynamic_labels



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
label = Gtk.Label(label=chapter_texts["hotkeys"][current_language])
dynamic_labels.append((label, "hotkeys"))
label.add_css_class("intro-label")
main_box_panel_intro_in_files.append(label)

scrolled_window_intro_in_files.set_child(main_box_panel_intro_in_files)

def get_intro_in_files_panel():
    return scrolled_window_intro_in_files, "intro_in_files_panel", back_button