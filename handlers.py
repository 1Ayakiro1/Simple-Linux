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




def on_button3_clicked(button, stack):
    stack.set_visible_child_name("file_manager_panel")

def on_button4_clicked(button, stack):
    stack.set_visible_child_name("packages_and_installing_panel") 