# Это файл,где хранятся функции-обработчики для разных кнопок и событий интерфейса



def on_back_clicked(button, stack):
    stack.set_visible_child_name("main_panel")

def on_language_clicked(button):
    print("Language button clicked")

def on_button1_clicked(button, stack):
    stack.set_visible_child_name("linux_terminal_panel")

def on_button2_clicked(button, stack):
    stack.set_visible_child_name("hotkeys_panel")

def on_back_clicked_intro1(button, stack):
    stack.set_visible_child_name("hotkeys_panel")

def on_button_intro_topic_clicked(button, stack, get_intro_panel):
    intro_panel, panel_name = get_intro_panel()
    stack.add_named(intro_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_intro_gnomehotk_clicked(button, stack, get_gnomehotk_panel):
    gnomehotk_panel, panel_name = get_gnomehotk_panel()
    stack.add_named(gnomehotk_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_kdehotk_clicked(button, stack, get_kdehotk_panel):
    kdehotk_panel, panel_name = get_kdehotk_panel()
    stack.add_named(kdehotk_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_terminalhotk_clicked(button, stack, get_terminalhotk_panel):
    terminalhotk_panel, panel_name = get_terminalhotk_panel()
    stack.add_named(terminalhotk_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_intro_in_packages_clicked(button, stack, get_intro_in_packages_panel):
    intro_in_packages_panel, panel_name = get_intro_in_packages_panel()
    stack.add_named(intro_in_packages_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_appimage_clicked(button, stack, get_appimage_panel):
    appimage_panel, panel_name = get_appimage_panel()
    stack.add_named(appimage_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_deb_clicked(button, stack, get_deb_panel):
    deb_panel, panel_name = get_deb_panel()
    stack.add_named(deb_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_rpm_clicked(button, stack, get_rpm_panel):
    rpm_panel, panel_name = get_rpm_panel()
    stack.add_named(rpm_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_snap_clicked(button, stack, get_snap_panel):
    snap_panel, panel_name = get_snap_panel()
    stack.add_named(snap_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_tar_clicked(button, stack, get_tar_panel):
    tar_panel, panel_name = get_tar_panel()
    stack.add_named(tar_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_flatpack_clicked(button, stack, get_flatpack_panel):
    flatpack_panel, panel_name = get_flatpack_panel()
    stack.add_named(flatpack_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_zst_clicked(button, stack, get_zst_panel):
    zst_panel, panel_name = get_zst_panel()
    stack.add_named(zst_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_auto_and_scripts_clicked(button, stack, get_auto_and_scripts_panel):
    auto_and_scripts_panel, panel_name = get_auto_and_scripts_panel()
    stack.add_named(auto_and_scripts_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_files_and_directories_clicked(button, stack, get_files_and_directories_panel):
    files_and_directories_panel, panel_name = get_files_and_directories_panel()
    stack.add_named(files_and_directories_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_intro_in_terminal_clicked(button, stack, get_intro_in_terminal_panel):
    intro_in_terminal_panel, panel_name = get_intro_in_terminal_panel()
    stack.add_named(intro_in_terminal_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_lifehacks_clicked(button, stack, get_lifehacks_panel):
    lifehacks_panel, panel_name = get_lifehacks_panel()
    stack.add_named(lifehacks_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_navigation_clicked(button, stack, get_navigation_panel):
    navigation_panel, panel_name = get_navigation_panel()
    stack.add_named(navigation_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_network_clicked(button, stack, get_network_panel):
    network_panel, panel_name = get_network_panel()
    stack.add_named(network_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_processes_clicked(button, stack, get_processes_panel):
    processes_panel, panel_name = get_processes_panel()
    stack.add_named(processes_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_utils_clicked(button, stack, get_utils_panel):
    utils_panel, panel_name = get_utils_panel()
    stack.add_named(utils_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_intro_in_files_clicked(button, stack, get_intro_in_files_panel):
    intro_in_files_panel, panel_name = get_intro_in_files_panel()
    stack.add_named(intro_in_files_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_bouble_commander_clicked(button, stack, get_bouble_commander_panel):
    bouble_commander_panel, panel_name = get_bouble_commander_panel()
    stack.add_named(bouble_commander_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_caja_clicked(button, stack, get_caja_panel):
    caja_panel, panel_name = get_caja_panel()
    stack.add_named(caja_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_dolphin_clicked(button, stack, get_dolphin_panel):
    dolphin_panel, panel_name = get_dolphin_panel()
    stack.add_named(dolphin_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_gnome_commander_clicked(button, stack, get_gnome_commander_panel):
    gnome_commander_panel, panel_name = get_gnome_commander_panel()
    stack.add_named(gnome_commander_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_nautilus_clicked(button, stack, get_nautilus_panel):
    nautilus_panel, panel_name = get_nautilus_panel()
    stack.add_named(nautilus_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_sunflower_clicked(button, stack, get_sunflower_panel):
    sunflower_panel, panel_name = get_sunflower_panel()
    stack.add_named(sunflower_panel, panel_name)
    stack.set_visible_child_name(panel_name)

def on_button_thunar_clicked(button, stack, get_thunar_panel):
    thunar_panel, panel_name = get_thunar_panel()
    stack.add_named(thunar_panel, panel_name)
    stack.set_visible_child_name(panel_name)



def on_button3_clicked(button, stack):
    stack.set_visible_child_name("file_manager_panel")

def on_button4_clicked(button, stack):
    stack.set_visible_child_name("packages_and_installing_panel") 