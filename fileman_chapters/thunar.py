import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from code.text import hotkeys_text



scrolled_window_thunar = Gtk.ScrolledWindow()
scrolled_window_thunar.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

# Main Box in scrolled window
main_box_panel_thunar = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
main_box_panel_thunar.set_valign(Gtk.Align.START)
main_box_panel_thunar.add_css_class("intro-list")

# Back button
back_button = Gtk.Button(label="‹")
back_button.add_css_class("back-button1")
back_button.set_size_request(50, 50)
back_button.set_halign(Gtk.Align.START)
back_button.set_hexpand(False)
main_box_panel_thunar.append(back_button)

# Label
label = Gtk.Label(label=hotkeys_text)
label.add_css_class("intro-label")
main_box_panel_thunar.append(label)

scrolled_window_thunar.set_child(main_box_panel_thunar)

def get_thunar_panel():
    return scrolled_window_thunar, "thunar_panel", back_button