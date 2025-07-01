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

def on_button3_clicked(button, stack):
    stack.set_visible_child_name("file_manager_panel")

def on_button4_clicked(button, stack):
    stack.set_visible_child_name("packages_and_installing_panel") 