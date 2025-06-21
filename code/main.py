import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

# Обработчики для кнопок
def on_button1_clicked(button):
    print("Кнопка 1 нажата!")

def on_button2_clicked(button):
    print("Кнопка 2 нажата!")

def on_activate(app):
    window = Gtk.ApplicationWindow(application=app)
    window.set_title("Simple Linux")
    window.set_default_size(1000, 700)

    # Dark theme
    style_manager = Adw.StyleManager.get_default()
    style_manager.set_color_scheme(Adw.ColorScheme.FORCE_DARK)

    # Box for buttons
    box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    box.set_margin_top(20)
    box.set_margin_start(20)
    box.set_margin_end(20)
    box.set_halign(Gtk.Align.CENTER)
    box.set_valign(Gtk.Align.CENTER)

    # Создаём первую кнопку
    button1 = Gtk.Button(label="Кнопка 1")
    button1.connect("clicked", on_button1_clicked)
    button1.add_css_class("custom-button1")
    box.append(button1)

    # Создаём вторую кнопку
    button2 = Gtk.Button(label="Кнопка 2")
    button2.connect("clicked", on_button2_clicked)
    button2.add_css_class("custom-button2")
    box.append(button2)

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

    # Устанавливаем контейнер как содержимое окна
    window.set_child(box)

    # Показываем окно
    window.present()

def main():
    # Создаём приложение с валидным application_id
    app = Adw.Application(application_id="com.example.simpleapp")
    app.connect("activate", on_activate)
    app.run(None)

if __name__ == "__main__":
    main()