import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from common import get_intro_panel,get_gnomehotk_panel,get_kdehotk_panel,get_terminalhotk_panel,get_intro_in_packages_panel,get_appimage_panel,get_deb_panel,get_rpm_panel,get_snap_panel,get_tar_panel,get_flatpack_panel,get_zst_panel, get_language_panel, get_auto_and_scripts_panel, get_files_and_directories_panel, get_intro_in_terminal_panel, get_lifehacks_panel, get_navigation_panel, get_network_panel, get_processes_panel, get_utils_panel, get_intro_in_files_panel, get_bouble_commander_panel, get_caja_panel, get_dolphin_panel, get_gnome_commander_panel, get_nautilus_panel, get_sunflower_panel, get_thunar_panel
from translations.main_titles import translations, current_language
from code.text import chapter_texts
from code.dynamic_refs import dynamic_labels, dynamic_main_labels, dynamic_main_buttons

# Создаём Stack для переключения панелей
stack = Gtk.Stack()
stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)  # Set animation
# Обработчики для кнопок
#Back_button_func
def on_back_clicked(button):
    stack.set_visible_child_name("main_panel")

def on_language_clicked(button):
    print("Language button clicked")

def on_button1_clicked(button):
    stack.set_visible_child_name("linux_terminal_panel")

def on_button2_clicked(button):
    stack.set_visible_child_name("hotkeys_panel")

def _on_button_intro_topic_clicked(button):
    panel_name = "introduction_topic_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_intro_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_gnomehotk_topic_clicked(button):
    panel_name = "gnomehotk_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_gnomehotk_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_kdehotk_topic_clicked(button):
    panel_name = "kdehotk_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_kdehotk_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_terminalhotk_topic_clicked(button):
    panel_name = "terminalhotk_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_terminalhotk_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_intro_in_packages_clicked(button):
    panel_name = "intro_in_packages_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_intro_in_packages_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_appimage_clicked(button):
    panel_name = "appimage_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_appimage_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_deb_clicked(button):
    panel_name = "deb_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_deb_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_rpm_clicked(button):
    panel_name = "rpm_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_rpm_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_snap_clicked(button):
    panel_name = "snap_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_snap_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_tar_clicked(button):
    panel_name = "tar_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_tar_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_flatpack_clicked(button):
    panel_name = "flatpack_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_flatpack_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_zst_clicked(button):
    panel_name = "zst_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_zst_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_auto_and_scripts_clicked(button):
    panel_name = "auto_and_scripts_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_auto_and_scripts_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_files_and_directories_clicked(button):
    panel_name = "files_and_directories_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_files_and_directories_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_intro_in_terminal_clicked(button):
    panel_name = "intro_in_terminal_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_intro_in_terminal_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_lifehacks_clicked(button):
    panel_name = "lifehacks_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_lifehacks_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_navigation_clicked(button):
    panel_name = "navigation_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_navigation_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_network_clicked(button):
    panel_name = "network_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_network_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_processes_clicked(button):
    panel_name = "processes_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_processes_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_utils_clicked(button):
    panel_name = "utils_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_utils_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_intro_in_files_clicked(button):
    panel_name = "intro_in_files_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_intro_in_files_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_bouble_commander_clicked(button):
    panel_name = "bouble_commander_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_bouble_commander_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_caja_clicked(button):
    panel_name = "caja_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_caja_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_dolphin_clicked(button):
    panel_name = "dolphin_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_dolphin_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_gnome_commander_clicked(button):
    panel_name = "gnome_commander_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_gnome_commander_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_nautilus_clicked(button):
    panel_name = "nautilus_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_nautilus_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_sunflower_clicked(button):
    panel_name = "sunflower_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_sunflower_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def _on_button_thunar_clicked(button):
    panel_name = "thunar_panel"
    if stack.get_child_by_name(panel_name):
        stack.set_visible_child_name(panel_name)
        return
    panel, _, back_button = get_thunar_panel()
    back_button.connect("clicked", on_back_clicked)
    stack.add_named(panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button3_clicked(button):
    stack.set_visible_child_name("file_manager_panel")

def on_button4_clicked(button):
    stack.set_visible_child_name("packages_and_installing_panel")

def on_activate(app):
    global window
    window = Gtk.ApplicationWindow(application=app)
    window.set_title("Simple Linux")
    window.set_default_size(1000, 700)

    # Dark theme
    style_manager = Adw.StyleManager.get_default()
    style_manager.set_color_scheme(Adw.ColorScheme.FORCE_DARK)


    ##############MAIN PANEL###############

    # Scrolled window
    scrolled_window = Gtk.ScrolledWindow()
    scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

    # Main Box in scrolled window
    main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    main_box.set_valign(Gtk.Align.START)

    # --- Новый top bar на CenterBox ---
    center_box = Gtk.CenterBox()
    center_box.set_hexpand(True)
    center_box.set_halign(Gtk.Align.FILL)
    center_box.set_valign(Gtk.Align.START)
    center_box.set_margin_top(0)
    center_box.set_margin_bottom(0)
    center_box.set_margin_start(0)
    center_box.set_margin_end(0)

    # Top label
    label = Gtk.Label()
    label.set_markup(translations[current_language]["main_title"])
    label.add_css_class("custom-label")
    label.set_halign(Gtk.Align.CENTER)
    label.set_hexpand(True)
    center_box.set_center_widget(label)
    dynamic_main_labels.append((label, "main_title"))

    # Switch lang button
    lang_button = Gtk.MenuButton(label="En")
    lang_button.add_css_class("lang-button")
    lang_button.set_halign(Gtk.Align.END)
    lang_button.set_valign(Gtk.Align.START)
    lang_button.set_hexpand(False)
    lang_button.set_vexpand(False)

    # --- Popover for language selection ---
    popover = Gtk.Popover()
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    languages = [
        ("English", "en"),
        ("Русский", "ru"),
        ("中文", "zh"),
        ("日本語", "ja"),
        ("Français", "fr"),
        ("Deutsch", "de"),
        ("Español", "es"),
    ]
    def set_language(lang_code):
        global current_language
        current_language = lang_code
        lang_button.set_label(lang_code.upper())
        update_all_texts()
        print(f"Language changed to: {lang_code}")
        popover.popdown()

    for lang_name, lang_code in languages:
        btn = Gtk.Button(label=lang_name)
        btn.add_css_class("lang-choice-btn")
        btn.set_size_request(120, 32)
        btn.set_margin_bottom(2)
        btn.set_halign(Gtk.Align.CENTER)
        btn.set_valign(Gtk.Align.CENTER)
        btn.connect("clicked", lambda b, code=lang_code: set_language(code))
        box.append(btn)
    popover.set_child(box)
    popover.set_has_arrow(True)
    popover.set_size_request(180, 240)
    box.set_halign(Gtk.Align.CENTER)
    box.set_valign(Gtk.Align.CENTER)
    lang_button.set_popover(popover)

    center_box.set_end_widget(lang_button)

    main_box.append(center_box)

    # Box for buttons
    box_horiz1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    box_horiz1.set_margin_top(20)
    box_horiz1.set_margin_start(20)
    box_horiz1.set_margin_end(20)
    box_horiz1.set_halign(Gtk.Align.CENTER)
    box_horiz1.set_valign(Gtk.Align.CENTER)

    # Next box
    box_horiz2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    box_horiz2.set_margin_top(20)
    box_horiz2.set_margin_start(20)
    box_horiz2.set_margin_end(20)
    box_horiz2.set_halign(Gtk.Align.CENTER)
    box_horiz2.set_valign(Gtk.Align.CENTER)

    # Terminal button
    button1 = Gtk.Button(label=translations[current_language]["terminal"])
    button1.connect("clicked", on_button1_clicked)
    button1.add_css_class("custom-button1")
    box_horiz1.append(button1)
    dynamic_main_buttons.append((button1, "terminal"))

    # Hotkeys button
    button2 = Gtk.Button(label=translations[current_language]["hotkeys"])
    button2.connect("clicked", on_button2_clicked)
    button2.add_css_class("custom-button2")
    box_horiz1.append(button2)
    dynamic_main_buttons.append((button2, "hotkeys"))

    # File manager button
    button3 = Gtk.Button(label=translations[current_language]["file_manager"])
    button3.connect("clicked", on_button3_clicked)
    button3.add_css_class("custom-button3")
    box_horiz2.append(button3)
    dynamic_main_buttons.append((button3, "file_manager"))

    # Packages & installing button
    button4 = Gtk.Button(label=translations[current_language]["packages"])
    button4.connect("clicked", on_button4_clicked)
    button4.add_css_class("custom-button3")
    box_horiz2.append(button4)
    dynamic_main_buttons.append((button4, "packages"))

    # Append boxes to main_box
    main_box.append(box_horiz1)
    main_box.append(box_horiz2)

    # Устанавливаем main_box как дочерний элемент scrolled_window
    scrolled_window.set_child(main_box)

    # Добавляем scrolled_window в stack
    stack.add_named(scrolled_window, "main_panel")


    ##############LINUX TERMINAL PANEL###############

    # Scrolled window
    scrolled_window_panel2 = Gtk.ScrolledWindow()
    scrolled_window_panel2.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

    #Main Box in scrolled window
    main_box_panel2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    main_box_panel2.set_halign(Gtk.Align.START)
    # main_box_panel2.set_margin_top(10)
    main_box_panel2.set_valign(Gtk.Align.START)

    #Back button
    back_button = Gtk.Button(label="‹")
    back_button.connect("clicked", on_back_clicked)
    back_button.add_css_class("back-button1")
    back_button.set_size_request(50, 50)
    back_button.set_halign(Gtk.Align.START)
    back_button.set_hexpand(False)
    main_box_panel2.append(back_button)

    button_intro_in_terminal_topic = Gtk.Button(label=translations[current_language]["intro_in_terminal"])
    button_intro_in_terminal_topic.connect("clicked", _on_button_intro_in_terminal_clicked)
    button_intro_in_terminal_topic.add_css_class("button-intro-topic")
    main_box_panel2.append(button_intro_in_terminal_topic)
    dynamic_main_labels.append((button_intro_in_terminal_topic, "intro_in_terminal"))

    button_auto_and_scripts_topic = Gtk.Button(label=translations[current_language]["auto_and_scripts"])
    button_auto_and_scripts_topic.connect("clicked", _on_button_auto_and_scripts_clicked)
    button_auto_and_scripts_topic.add_css_class("button-intro-topic")
    main_box_panel2.append(button_auto_and_scripts_topic)
    dynamic_main_labels.append((button_auto_and_scripts_topic, "auto_and_scripts"))

    button_files_and_directories_topic = Gtk.Button(label=translations[current_language]["files_and_directories"])
    button_files_and_directories_topic.connect("clicked", _on_button_files_and_directories_clicked)
    button_files_and_directories_topic.add_css_class("button-intro-topic")
    main_box_panel2.append(button_files_and_directories_topic)
    dynamic_main_labels.append((button_files_and_directories_topic, "files_and_directories"))

    button_lifehacks_topic = Gtk.Button(label=translations[current_language]["file_manager"])
    button_lifehacks_topic.connect("clicked", _on_button_lifehacks_clicked)
    button_lifehacks_topic.add_css_class("button-intro-topic")
    main_box_panel2.append(button_lifehacks_topic)
    dynamic_main_labels.append((button_lifehacks_topic, "lifehacks"))

    button_navigation_topic = Gtk.Button(label=translations[current_language]["navigation"])
    button_navigation_topic.connect("clicked", _on_button_navigation_clicked)
    button_navigation_topic.add_css_class("button-intro-topic")
    main_box_panel2.append(button_navigation_topic)
    dynamic_main_labels.append(( button_navigation_topic, "navigation"))

    button_network_topic = Gtk.Button(label=translations[current_language]["network"])
    button_network_topic.connect("clicked", _on_button_network_clicked)
    button_network_topic.add_css_class("button-intro-topic")
    main_box_panel2.append(button_network_topic)
    dynamic_main_labels.append((button_network_topic, "network"))

    button_processes_topic = Gtk.Button(label=translations[current_language]["processes"])
    button_processes_topic.connect("clicked", _on_button_processes_clicked)
    button_processes_topic.add_css_class("button-intro-topic")
    main_box_panel2.append(button_processes_topic)
    dynamic_main_labels.append((button_processes_topic, "processes"))

    button_utils_topic = Gtk.Button(label=translations[current_language]["utils"])
    button_utils_topic.connect("clicked", _on_button_utils_clicked)
    button_utils_topic.add_css_class("button-intro-topic")
    main_box_panel2.append(button_utils_topic)
    dynamic_main_labels.append((button_utils_topic, "utils"))

    stack.add_named(main_box_panel2, "linux_terminal_panel")


    ##############HOTKEYS PANEL###############

    # Scrolled window
    scrolled_window_panel3 = Gtk.ScrolledWindow()
    scrolled_window_panel3.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
    scrolled_window_panel3.set_min_content_height(100)
    scrolled_window_panel3.set_max_content_height(200)

    # Main Box in scrolled window
    main_box_panel3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    main_box_panel3.set_halign(Gtk.Align.START)
    main_box_panel3.set_valign(Gtk.Align.START)

    # Back button
    back_button = Gtk.Button(label="‹")
    back_button.connect("clicked", on_back_clicked)
    back_button.add_css_class("back-button1")
    back_button.set_size_request(50, 50)
    back_button.set_halign(Gtk.Align.START) 
    back_button.set_hexpand(False)
    main_box_panel3.append(back_button)

    # intro button topic
    button_intro_topic = Gtk.Button(label=translations[current_language]["hotkeys"])
    button_intro_topic.connect("clicked", _on_button_intro_topic_clicked)
    button_intro_topic.add_css_class("button-intro-topic")
    main_box_panel3.append(button_intro_topic)
    dynamic_main_labels.append((button_intro_topic, "hotkeys"))

    button_gnomehotk_topic = Gtk.Button(label=translations[current_language]["gnome_hotkeys"])
    button_gnomehotk_topic.connect("clicked", _on_button_gnomehotk_topic_clicked)
    button_gnomehotk_topic.add_css_class("button-intro-topic")
    main_box_panel3.append(button_gnomehotk_topic)
    dynamic_main_labels.append((button_gnomehotk_topic, "gnome_hotkeys"))

    button_kdehotk_topic = Gtk.Button(label=translations[current_language]["kde_hotkeys"])
    button_kdehotk_topic.connect("clicked", _on_button_kdehotk_topic_clicked)
    button_kdehotk_topic.add_css_class("button-intro-topic")
    main_box_panel3.append(button_kdehotk_topic)
    dynamic_main_labels.append((button_kdehotk_topic, "kde_hotkeys"))

    button_terminalhotk_topic = Gtk.Button(label=translations[current_language]["terminal_hotkeys"])
    button_terminalhotk_topic.connect("clicked", _on_button_terminalhotk_topic_clicked)
    button_terminalhotk_topic.add_css_class("button-intro-topic")
    main_box_panel3.append(button_terminalhotk_topic)
    dynamic_main_labels.append((button_terminalhotk_topic, "terminal_hotkeys"))

    scrolled_window_panel3.set_child(main_box_panel3)
    stack.add_named(scrolled_window_panel3, "hotkeys_panel")

    

    ##############FILE MANAGER PANEL###############

    # Scrolled window
    scrolled_window_panel4 = Gtk.ScrolledWindow()
    scrolled_window_panel4.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

    #Main Box in scrolled window
    main_box_panel4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    main_box_panel4.set_halign(Gtk.Align.START)
    main_box_panel4.set_valign(Gtk.Align.START)

    #Back button
    back_button = Gtk.Button(label="‹")
    back_button.connect("clicked", on_back_clicked)
    back_button.add_css_class("back-button1")
    back_button.set_size_request(50, 50)
    back_button.set_halign(Gtk.Align.START)
    back_button.set_hexpand(False)
    main_box_panel4.append(back_button)

    button_intro_in_files_topic = Gtk.Button(label=translations[current_language]["introduction"])
    button_intro_in_files_topic.connect("clicked", _on_button_intro_in_files_clicked)
    button_intro_in_files_topic.add_css_class("button-intro-topic")
    main_box_panel4.append(button_intro_in_files_topic)
    dynamic_main_labels.append((button_intro_in_files_topic, "introduction"))

    button_bouble_commander_topic = Gtk.Button(label=translations[current_language]["double_commander"])
    button_bouble_commander_topic.connect("clicked", _on_button_bouble_commander_clicked)
    button_bouble_commander_topic.add_css_class("button-intro-topic")
    main_box_panel4.append(button_bouble_commander_topic)
    dynamic_main_labels.append((button_bouble_commander_topic, "double_commander"))

    button_caja_topic = Gtk.Button(label=translations[current_language]["caja"])
    button_caja_topic.connect("clicked", _on_button_caja_clicked)
    button_caja_topic.add_css_class("button-intro-topic")
    main_box_panel4.append(button_caja_topic)
    dynamic_main_labels.append((button_caja_topic, "caja"))

    button_dolphin_topic = Gtk.Button(label=translations[current_language]["dolphin"])
    button_dolphin_topic.connect("clicked", _on_button_dolphin_clicked)
    button_dolphin_topic.add_css_class("button-intro-topic")
    main_box_panel4.append(button_dolphin_topic)
    dynamic_main_labels.append((button_dolphin_topic, "dolphin"))

    button_gnome_commander_topic = Gtk.Button(label=translations[current_language]["gnome_commander"])
    button_gnome_commander_topic.connect("clicked", _on_button_gnome_commander_clicked)
    button_gnome_commander_topic.add_css_class("button-intro-topic")
    main_box_panel4.append(button_gnome_commander_topic)
    dynamic_main_labels.append((button_gnome_commander_topic, "gnome_commander"))

    button_nautilus_topic = Gtk.Button(label=translations[current_language]["nautilus"])
    button_nautilus_topic.connect("clicked", _on_button_nautilus_clicked)
    button_nautilus_topic.add_css_class("button-intro-topic")
    main_box_panel4.append(button_nautilus_topic)
    dynamic_main_labels.append((button_nautilus_topic, "nautilus"))

    button_sunflower_topic = Gtk.Button(label=translations[current_language]["sunflower"])
    button_sunflower_topic.connect("clicked", _on_button_sunflower_clicked)
    button_sunflower_topic.add_css_class("button-intro-topic")
    main_box_panel4.append(button_sunflower_topic)
    dynamic_main_labels.append((button_sunflower_topic, "sunflower"))

    button_thunar_topic = Gtk.Button(label=translations[current_language]["thunar"])
    button_thunar_topic.connect("clicked", _on_button_thunar_clicked)
    button_thunar_topic.add_css_class("button-intro-topic")
    main_box_panel4.append(button_thunar_topic)
    dynamic_main_labels.append((button_thunar_topic, "thunar"))

    stack.add_named(main_box_panel4, "file_manager_panel")


    ##############PACKAGES & INSTALLING PANEL###############

    # Scrolled window
    scrolled_window_panel5 = Gtk.ScrolledWindow()
    scrolled_window_panel5.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

    #Main Box in scrolled window
    main_box_panel5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    main_box_panel5.set_halign(Gtk.Align.START)
    main_box_panel5.set_valign(Gtk.Align.START)

    #Back button
    back_button = Gtk.Button(label="‹")
    back_button.connect("clicked", on_back_clicked)
    back_button.add_css_class("back-button1")
    back_button.set_size_request(50, 50)  # Фиксированная ширина и высота
    back_button.set_halign(Gtk.Align.START)  # Прижимаем к левому краю
    back_button.set_hexpand(False) 
    main_box_panel5.append(back_button)

    button_intro_in_packages_topic = Gtk.Button(label=translations[current_language]["intro_in_packages"])
    button_intro_in_packages_topic.connect("clicked", _on_button_intro_in_packages_clicked)
    button_intro_in_packages_topic.add_css_class("button-intro-topic")
    main_box_panel5.append(button_intro_in_packages_topic)
    dynamic_main_labels.append((button_intro_in_packages_topic, "intro_in_packages"))

    button_appimage_topic = Gtk.Button(label=translations[current_language]["appimage"])
    button_appimage_topic.connect("clicked", _on_button_appimage_clicked)
    button_appimage_topic.add_css_class("button-intro-topic")
    main_box_panel5.append(button_appimage_topic)
    dynamic_main_labels.append((button_appimage_topic, "appimage"))

    button_deb_topic = Gtk.Button(label=translations[current_language]["deb"])
    button_deb_topic.connect("clicked", _on_button_deb_clicked)
    button_deb_topic.add_css_class("button-intro-topic")
    main_box_panel5.append(button_deb_topic)
    dynamic_main_labels.append((button_deb_topic, "deb"))

    button_rpm_topic = Gtk.Button(label=translations[current_language]["rpm"])
    button_rpm_topic.connect("clicked", _on_button_rpm_clicked)
    button_rpm_topic.add_css_class("button-intro-topic")
    main_box_panel5.append(button_rpm_topic)
    dynamic_main_labels.append((button_rpm_topic, "rpm"))

    button_snap_topic = Gtk.Button(label=translations[current_language]["snap"])
    button_snap_topic.connect("clicked", _on_button_snap_clicked)
    button_snap_topic.add_css_class("button-intro-topic")
    main_box_panel5.append(button_snap_topic)
    dynamic_main_labels.append((button_snap_topic, "snap"))

    button_tar_topic = Gtk.Button(label=translations[current_language]["tar"])
    button_tar_topic.connect("clicked", _on_button_tar_clicked)
    button_tar_topic.add_css_class("button-intro-topic")
    main_box_panel5.append(button_tar_topic)
    dynamic_main_labels.append((button_tar_topic, "tar"))

    button_flatpack_topic = Gtk.Button(label=translations[current_language]["flatpack"])
    button_flatpack_topic.connect("clicked", _on_button_flatpack_clicked)
    button_flatpack_topic.add_css_class("button-intro-topic")
    main_box_panel5.append(button_flatpack_topic)
    dynamic_main_labels.append((button_flatpack_topic, "flatpack"))

    button_zst_topic = Gtk.Button(label=translations[current_language]["zst"])
    button_zst_topic.connect("clicked", _on_button_zst_clicked)
    button_zst_topic.add_css_class("button-intro-topic")
    button_zst_topic.set_margin_bottom(20)
    main_box_panel5.append(button_zst_topic)
    dynamic_main_labels.append((button_zst_topic, "zst"))

    stack.add_named(main_box_panel5, "packages_and_installing_panel")
    
    
    
    
    # Создаём CSS-провайдер для стилей кнопок
    css_provider = Gtk.CssProvider()
    try:
        css_provider.load_from_path("./styles/main.css")
    except Exception as e:
        pass

    # Применяем CSS
    try:
        Gtk.StyleContext.add_provider_for_display(
            window.get_display(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
    except Exception as e:
        pass


    # Устанавливаем контейнер как содержимое окна
    window.set_child(stack)

    # Показываем окно
    window.present()

def update_all_texts():
    from translations.main_titles import translations
    # Updating Labels
    for label, chapter in dynamic_labels:
        # Hotkeys chapters
        if chapter == "gnomehotk":
            from translations.hotkeys_chapters import hotkeys_translations
            label.set_markup(hotkeys_translations[current_language]["gnomehotk"])
        elif chapter == "kdehotk":
            from translations.hotkeys_chapters import hotkeys_translations
            label.set_markup(hotkeys_translations[current_language]["kdehotk"])
        elif chapter == "terminalhotk":
            from translations.hotkeys_chapters import hotkeys_translations
            label.set_markup(hotkeys_translations[current_language]["terminalhotk"])
        elif chapter == "introduction_topic":
            from translations.hotkeys_chapters import hotkeys_translations
            label.set_markup(hotkeys_translations[current_language]["introduction_topic"])
        # Fileman chapters
        elif chapter == "bouble_commander":
            from translations.fileman_chapters import fileman_translations
            label.set_markup(fileman_translations[current_language]["bouble_commander"])
        elif chapter == "caja":
            from translations.fileman_chapters import fileman_translations
            label.set_markup(fileman_translations[current_language]["caja"])
        elif chapter == "dolphin":
            from translations.fileman_chapters import fileman_translations
            label.set_markup(fileman_translations[current_language]["dolphin"])
        elif chapter == "gnome_commander":
            from translations.fileman_chapters import fileman_translations
            label.set_markup(fileman_translations[current_language]["gnome_commander"])
        elif chapter == "intro_in_files":
            from translations.fileman_chapters import fileman_translations
            label.set_markup(fileman_translations[current_language]["intro_in_files"])
        elif chapter == "nautilus":
            from translations.fileman_chapters import fileman_translations
            label.set_markup(fileman_translations[current_language]["nautilus"])
        elif chapter == "sunflower":
            from translations.fileman_chapters import fileman_translations
            label.set_markup(fileman_translations[current_language]["sunflower"])
        elif chapter == "thunar":
            from translations.fileman_chapters import fileman_translations
            label.set_markup(fileman_translations[current_language]["thunar"])
        # Linux term chapters
        elif chapter == "auto_and_scripts":
            from translations.linux_term_chapters import linux_term_translations
            label.set_markup(linux_term_translations[current_language]["auto_and_scripts"])
        elif chapter == "files_and_directories":
            from translations.linux_term_chapters import linux_term_translations
            label.set_markup(linux_term_translations[current_language]["files_and_directories"])
        elif chapter == "intro_in_terminal":
            from translations.linux_term_chapters import linux_term_translations
            label.set_markup(linux_term_translations[current_language]["intro_in_terminal"])
        elif chapter == "lifehacks":
            from translations.linux_term_chapters import linux_term_translations
            label.set_markup(linux_term_translations[current_language]["lifehacks"])
        elif chapter == "navigation":
            from translations.linux_term_chapters import linux_term_translations
            label.set_markup(linux_term_translations[current_language]["navigation"])
        elif chapter == "network":
            from translations.linux_term_chapters import linux_term_translations
            label.set_markup(linux_term_translations[current_language]["network"])
        elif chapter == "processes":
            from translations.linux_term_chapters import linux_term_translations
            label.set_markup(linux_term_translations[current_language]["processes"])
        elif chapter == "utils":
            from translations.linux_term_chapters import linux_term_translations
            label.set_markup(linux_term_translations[current_language]["utils"])
        # Packages chapters
        elif chapter == "appimage":
            from translations.packages_chapters import packages_translations
            label.set_markup(packages_translations[current_language]["appimage"])
        elif chapter == "deb":
            from translations.packages_chapters import packages_translations
            label.set_markup(packages_translations[current_language]["deb"])
        elif chapter == "flatpack":
            from translations.packages_chapters import packages_translations
            label.set_markup(packages_translations[current_language]["flatpack"])
        elif chapter == "intro_in_packages":
            from translations.packages_chapters import packages_translations
            label.set_markup(packages_translations[current_language]["intro_in_packages"])
        elif chapter == "rpm":
            from translations.packages_chapters import packages_translations
            label.set_markup(packages_translations[current_language]["rpm"])
        elif chapter == "snap":
            from translations.packages_chapters import packages_translations
            label.set_markup(packages_translations[current_language]["snap"])
        elif chapter == "tar":
            from translations.packages_chapters import packages_translations
            label.set_markup(packages_translations[current_language]["tar"])
        elif chapter == "zst":
            from translations.packages_chapters import packages_translations
            label.set_markup(packages_translations[current_language]["zst"])
        # Fallback for main_titles
        else:
            label.set_markup(translations[current_language].get(chapter, chapter))
    # Updating Chapters
    for label, key in dynamic_main_labels:
        if key == "main_title":
            label.set_markup(translations[current_language][key])
        else:
            label.set_label(translations[current_language][key])
    # Updating main btns
    for button, key in dynamic_main_buttons:
        button.set_label(translations[current_language][key])

def main():
    app = Adw.Application(application_id="com.example.simpleapp")
    app.connect("activate", on_activate)
    app.run(None)

if __name__ == "__main__":
    main()