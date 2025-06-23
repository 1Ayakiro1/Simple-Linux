import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from text import hotkeys_text



# Создаём Stack для переключения панелей
stack = Gtk.Stack()
stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)  # Set animation
# Обработчики для кнопок
#Back_button_func
def on_back_clicked(button):
    stack.set_visible_child_name("main_panel")
def on_button1_clicked(button):
    stack.set_visible_child_name("linux_terminal_panel")

def on_button2_clicked(button):
    stack.set_visible_child_name("hotkeys_panel")

def on_button3_clicked(button):
    stack.set_visible_child_name("file_manager_panel")

def on_button4_clicked(button):
    stack.set_visible_child_name("packages_and_installing_panel")

def on_activate(app):
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

    #Main Box in scrolled window
    main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    main_box.set_halign(Gtk.Align.CENTER)
    main_box.set_valign(Gtk.Align.START)


    #Top label in main box
    label = Gtk.Label(label="Let's Begin!")
    label.add_css_class("custom-label")  # Для стилизации в styles.css
    main_box.append(label)

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
    button1 = Gtk.Button(label="Linux Terminal")
    button1.connect("clicked", on_button1_clicked)
    button1.add_css_class("custom-button1")
    box_horiz1.append(button1)

    # Hotkeys button
    button2 = Gtk.Button(label="Hotkeys")
    button2.connect("clicked", on_button2_clicked)
    button2.add_css_class("custom-button2")
    box_horiz1.append(button2)

    # File manager button
    button3 = Gtk.Button(label="File manager")
    button3.connect("clicked", on_button3_clicked)
    button3.add_css_class("custom-button3")
    box_horiz2.append(button3)

    # File manager button
    button4 = Gtk.Button(label="Packages & installing")
    button4.connect("clicked", on_button4_clicked)
    button4.add_css_class("custom-button3")
    box_horiz2.append(button4)
    
    stack.add_named(main_box, "main_panel")  # Добавляем основную панель
    
    #Append boxes
    main_box.append(box_horiz1)
    main_box.append(box_horiz2)


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
    main_box_panel2.append(back_button)

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
    back_button.set_size_request(50, 50)  # Фиксированная ширина и высота
    back_button.set_halign(Gtk.Align.START)  # Прижимаем к левому краю
    back_button.set_hexpand(False)  # Отключаем растяжение кнопки
    main_box_panel3.append(back_button)

    # Hotkeys Label
    hotkeys_label1 = Gtk.Label(label=hotkeys_text)
    hotkeys_label1.add_css_class("hotkeys-label")
    hotkeys_label1.set_wrap(True)
    main_box_panel3.append(hotkeys_label1)

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
    main_box_panel4.append(back_button)

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
    main_box_panel5.append(back_button)

    stack.add_named(main_box_panel5, "packages_and_installing_panel")
    
    
    
    
    # Создаём CSS-провайдер для стилей кнопок
    css_provider = Gtk.CssProvider()
    try:
        css_provider.load_from_path("./styles/main.css")
    except Exception as e:
        print(f"Error to load CSS: {e}")

    # Применяем CSS
    try:
        Gtk.StyleContext.add_provider_for_display(
            window.get_display(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
    except Exception as e:
        print(f"Application Error CSS: {e}")


    # Устанавливаем контейнер как содержимое окна
    window.set_child(stack)

    # Показываем окно
    window.present()

def main():
    # Создаём приложение с валидным application_id
    app = Adw.Application(application_id="com.example.simpleapp")
    app.connect("activate", on_activate)
    app.run(None)

if __name__ == "__main__":
    main()