import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from code.text import chapter_texts
from translations.main_titles import current_language
from code.dynamic_refs import dynamic_labels
from translations.packages_chapters import packages_translations



scrolled_window_intro_in_packages_topic = Gtk.ScrolledWindow()
scrolled_window_intro_in_packages_topic.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

# Main Box in scrolled window
main_box_panel_intro_in_packages_topic = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
main_box_panel_intro_in_packages_topic.set_valign(Gtk.Align.START)
main_box_panel_intro_in_packages_topic.add_css_class("intro-list")

# Back button
back_button = Gtk.Button(label="‹")
back_button.add_css_class("back-button1")
back_button.set_size_request(50, 50)
back_button.set_halign(Gtk.Align.START)
back_button.set_hexpand(False)
main_box_panel_intro_in_packages_topic.append(back_button)

# Label
label = Gtk.Label(label=packages_translations[current_language]["intro_in_packages"])
label.set_use_markup(True)
dynamic_labels.append((label, "intro_in_packages"))
label.add_css_class("intro-label")
main_box_panel_intro_in_packages_topic.append(label)

scrolled_window_intro_in_packages_topic.set_child(main_box_panel_intro_in_packages_topic)

def get_intro_in_packages_panel():
    return scrolled_window_intro_in_packages_topic, "hotkeys_intro_panel", back_button

def get_intro_in_packages_text():
    return packages_translations[current_language]["intro_in_packages"]