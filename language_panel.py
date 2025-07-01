import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

def get_language_panel():
    scrolled_window = Gtk.ScrolledWindow()
    scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

    main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    main_box.set_valign(Gtk.Align.START)

    # Back button
    back_button = Gtk.Button(label="‹")
    back_button.add_css_class("back-button1")
    main_box.append(back_button)

    # Языки
    languages = [
        ("English", "en"),
        ("Русский", "ru"),
        ("中文", "zh"),
        ("日本語", "ja"),
        ("Français", "fr"),
        ("Deutsch", "de"),
        ("Español", "es"),
    ]
    for lang_name, lang_code in languages:
        btn = Gtk.Button(label=lang_name)
        btn.add_css_class("button-intro-topic")
        btn.set_margin_bottom(10)
        # btn.connect("clicked", ...)  # обработчик смены языка
        main_box.append(btn)

    scrolled_window.set_child(main_box)
    return scrolled_window, "language_panel", back_button 