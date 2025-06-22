import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

# Обработчики для кнопок
def on_button1_clicked(button):
    print("Кнопка 1 нажата!")

def on_button2_clicked(button):
    print("Кнопка 2 нажата!")

def on_button3_clicked(button):
    print("Кнопка 3 нажата!")

def on_button4_clicked(button):
    print("Кнопка 4 нажата!")

def on_activate(app):
    window = Gtk.ApplicationWindow(application=app)
    window.set_title("Simple Linux")
    window.set_default_size(1000, 700)

    # Dark theme
    style_manager = Adw.StyleManager.get_default()
    style_manager.set_color_scheme(Adw.ColorScheme.FORCE_DARK)

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
    button4 = Gtk.Button(label="File manager")
    button4.connect("clicked", on_button4_clicked)
    button4.add_css_class("custom-button3")
    box_horiz2.append(button4)

    # Создаём CSS-провайдер для стилей кнопок
    css_provider = Gtk.CssProvider()
    try:
        css_provider.load_from_path("./styles/main.css")
    except Exception as e:
        print(f"Ошибка загрузки CSS: {e}")

    # Применяем CSS
    try:
        Gtk.StyleContext.add_provider_for_display(
            window.get_display(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
    except Exception as e:
        print(f"Ошибка применения CSS: {e}")

    #Append boxes
    main_box.append(box_horiz1)
    main_box.append(box_horiz2)

    # Устанавливаем контейнер как содержимое окна
    scrolled_window.set_child(main_box)
    window.set_child(scrolled_window)

    # Показываем окно
    window.present()

def main():
    # Создаём приложение с валидным application_id
    app = Adw.Application(application_id="com.example.simpleapp")
    app.connect("activate", on_activate)
    app.run(None)

if __name__ == "__main__":
    main()