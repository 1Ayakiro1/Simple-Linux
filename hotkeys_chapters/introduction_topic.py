import gi
# --- GTK и Adwaita инициализация ---
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from handlers import on_back_clicked, on_back_clicked_intro1
from code.text import chapter_texts
from translations.main_titles import current_language
from code.dynamic_refs import dynamic_labels
from translations.hotkeys_chapters import hotkeys_translations

# --- Создаём скроллируемую панель для темы "Hotkeys" ---
scrolled_window_intro_topic = Gtk.ScrolledWindow()
scrolled_window_intro_topic.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

# --- Основной контейнер для содержимого панели ---
main_box_panel_intro_topic = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
main_box_panel_intro_topic.set_valign(Gtk.Align.START)
main_box_panel_intro_topic.add_css_class("intro-list")

# --- Кнопка "назад" (Back button) ---
# Обработчик для этой кнопки НЕ назначается здесь, чтобы избежать циклов и конфликтов с аргументами.
# Вместо этого, main.py получает экземпляр этой кнопки через get_intro_panel() и назначает обработчик сам.
back_button = Gtk.Button(label="‹")
back_button.add_css_class("back-button1")
back_button.set_size_request(50, 50)
back_button.set_halign(Gtk.Align.START)
back_button.set_hexpand(False)
main_box_panel_intro_topic.append(back_button)

# --- Текстовая метка с хоткеями ---
label = Gtk.Label(label=hotkeys_translations[current_language]["introduction_topic"])
dynamic_labels.append((label, "hotkeys"))
label.add_css_class("intro-label")
main_box_panel_intro_topic.append(label)

# --- Добавляем основной контейнер в скроллируемое окно ---
scrolled_window_intro_topic.set_child(main_box_panel_intro_topic)

# --- Функция-прокси ---
def get_intro_panel():
    """
    Возвращает:
        - панель (scrolled_window_intro_topic)
        - имя панели ("hotkeys_intro_panel")
        - экземпляр back_button
    Назначение обработчика для back_button происходит в main.py,
    чтобы можно было передать нужный stack и избежать циклических импортов.
    """
    return scrolled_window_intro_topic, "hotkeys_intro_panel", back_button

def get_introduction_topic_text():
    return hotkeys_translations[current_language]["introduction_topic"]
