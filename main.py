# main.py — Kira BlackFox Bot v4
# Требует: pip install pytelegrambotapi
# Поместите изображения в папку "images" (опционально)

import telebot
from telebot import types
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# ==============================
# 🔐 TOKEN — вставлен ваш токен
# ==============================
TOKEN = "8517148151:AAHGkLOO5b4OeRkVojI-rEfEvD2h26fL-BA"

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# ==============================
# 📁 ПУТИ К ИЗОБРАЖЕНИЯМ (опционально)
# ==============================
IMAGES_DIR = "images"
IMAGE_FILES = {
    "Разработка Telegram-ботов": os.path.join(IMAGES_DIR, "bots.png"),
    "Сценарии для сторис и постов": os.path.join(IMAGES_DIR, "stories.png"),
    "Таблицы и системы учёта": os.path.join(IMAGES_DIR, "tables.png"),
    "Копирайтинг": os.path.join(IMAGES_DIR, "copywriting.png"),
    "Переводы RU ↔ EN": os.path.join(IMAGES_DIR, "translate.png"),
    "Разработка логотипов": os.path.join(IMAGES_DIR, "logos.png"),
    "Статьи": os.path.join(IMAGES_DIR, "articles.png"),
    "Универсальные услуги": os.path.join(IMAGES_DIR, "universal.png"),
}

# ==============================
# 🔥 ORDER URL (переход в ваш чат)
# ==============================
ORDER_URL = "https://t.me/kira_blackfox"

# ==============================
# 📝 ОПИСАНИЯ УСЛУГ (вариант B — красиво отформатировано)
# ==============================
SERVICES = {
     "Разработка Telegram-ботов": 
        "Разработаю Telegram-бота или мини-приложение под ключ.\n\n"
        "📌 <b>Что я делаю:</b>\n"
        "— Боты для бизнеса, консультаций, онлайн-магазинов\n"
        "— Мини-приложения Telegram (анкеты, каталоги, бронирование)\n"
        "— Приём заявок, квизы, калькуляторы\n"
        "— Интеграции: CRM, Google Sheets, оплата, email\n"
        "— Многоуровневые меню, FAQ, логика переходов\n"
        "— Настройка хостинга и запуск «под ключ»\n\n"
        "⭐ <b>Почему со мной удобно:</b>\n"
        "— Объясняю простым языком\n"
        "— Быстрая работа\n"
        "— Всегда на связи\n"
        "— Делаю так, как нужно вам — и подсказываю лучшее решение",

    "Сценарии для сторис и постов":
        "Напишу живые, динамичные и цепляющие сценарии, которые удерживают внимание.\n\n"
        "📌 <b>Что входит:</b>\n"
        "— Сценарии под любой формат\n"
        "— Stories с удержанием внимания\n"
        "— Reels-сценарии\n"
        "— Контент-план (по запросу)\n"
        "— Готовые фразы + структура\n\n"
        "💬 Подходит: блогерам, экспертам, мастерам красоты, психологам, продажникам.",

    "Таблицы и системы учёта":
        "Разработаю простую и удобную систему учёта в Google Sheets.\n\n"
        "📌 <b>Что могу создать:</b>\n"
        "— Таблица прибыли\n"
        "— Учёт расходов и доходов\n"
        "— Мини-CRM\n"
        "— Личная финансовая таблица\n"
        "— Автоматические формулы и графики\n\n"
        "Работаю аккуратно, объясняю, как пользоваться.",

    "Копирайтинг":
        "Создам текст, который работает на вашу цель: продажи, доверие или экспертность.\n\n"
        "📌 <b>Что пишу:</b>\n"
        "— Посты\n"
        "— Лонгриды\n"
        "— Статьи\n"
        "— Описания товаров\n"
        "— Тексты для сайтов\n"
        "— Продающие тексты\n\n"
        "Пишу в вашем стиле, соблюдаю сроки, даю корректировки.",

    "Переводы RU ↔ EN":
        "Сделаю качественный перевод: аккуратный, точный и адаптированный.\n\n"
        "📌 <b>Что делаю:</b>\n"
        "— Перевод + вычитка\n"
        "— Сохранение авторского стиля\n"
        "— Адаптация под ЦА\n\n"
        "Подходит для магазинов, статей, писем, блогов и бизнеса.",

    "Разработка логотипов":
        "Сделаю стильный и продуманный логотип.\n\n"
        "📌 <b>Что получаете:</b>\n"
        "— 3 варианта логотипа\n"
        "— Цветной + монохром\n"
        "— PNG без фона\n"
        "— Палитра и шрифты\n\n"
        "Идеально для бизнеса и личного бренда.",

    "Статьи":
        "Подготовлю глубокую, структурную и аккуратную статью.\n\n"
        "📌 <b>Подойдёт для:</b>\n"
        "— Блогов\n"
        "— Сайтов\n"
        "— Медиа\n"
        "— Личных страниц\n\n"
        "Пишу быстро, качественно и в срок.",

    "Универсальные услуги":
        "Помогу выполнить задачу любой сложности: текст, дизайн, таблица, перевод, сценарий, бот.\n"
        "Работаю быстро, внимательно и на результат."
}

# ==============================
# 🔧 Keyboards
# ==============================
def main_menu_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton("🔥 Услуги"))
    kb.add(types.KeyboardButton("📞 Контакты"), types.KeyboardButton("🦊 О нас"))
    return kb

def services_menu_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in SERVICES.keys():
        kb.add(types.KeyboardButton(name))
    kb.add(types.KeyboardButton("⬅️ Назад в меню"))
    return kb

def inline_service_kb():
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("🔥 Заказать", url=ORDER_URL))
    kb.add(types.InlineKeyboardButton("⬅️ Назад к услугам", callback_data="cb_services"))
    return kb

# ==============================
# 🟢 HANDLERS
# ==============================
@bot.message_handler(commands=["start", "help"])
def cmd_start(message):
    chat_id = message.chat.id

    try:
        # Эффект "печатает"
        bot.send_chat_action(chat_id, "typing")
        import time
        time.sleep(0.8)

        # Первое короткое сообщение
        bot.send_message(
            chat_id,
            "🦊 Привет! Лисичка уже здесь — сейчас всё покажу…",
            parse_mode="HTML"
        )

        # Небольшая пауза для атмосферы
        bot.send_chat_action(chat_id, "typing")
        time.sleep(2.1)

        # Основное приветствие
        bot.send_message(
            chat_id,
            "<b>🦊 Привет! Я Kira BlackFox</b>\n\n"
            "⚡Выполню задачи быстро, чётко и недорого...",
            parse_mode="HTML",
            reply_markup=main_menu_kb(),
        )

    except Exception as e:
        logging.exception("start error: %s", e)


@bot.message_handler(func=lambda m: True)
def handle_text(message):
    text = message.text or ""
    chat_id = message.chat.id

    try:
        # Главное меню
        if text == "🔥 Услуги":
            bot.send_message(chat_id, "<b>🔥 Услуги</b>\nВыберите услугу:", reply_markup=services_menu_kb())
            return

        if text == "📞 Контакты":
            # используем HTML, ссылки кликабельны
            contacts_html = (
                "<b>📞 Контакты</b>\n\n"
                "Telegram: <a href='https://t.me/kira_blackfox'>@kira_blackfox</a>\n"
                "Instagram: <a href='https://www.instagram.com/kira_blackfox?igsh=c2Z3cGE4ZXo1bzV3'>kira_blackfox</a>\n"
                "Kwork: <a href='https://kwork.ru/user/kira_blackfox'>kwork.ru/user/kira_blackfox</a>\n"
                "Email: <a href='mailto:kvbfox@gmail.com'>kvbfox@gmail.com</a>"
            )
            bot.send_message(chat_id, contacts_html, reply_markup=main_menu_kb())
            return

        if text == "🦊 О нас":
            bot.send_message(
    chat_id,
    "<b>🦊 О нас</b>\n\n"
    "Добро пожаловать в мастерскую Kira BlackFox!\n\n"
    "<b>КТО Я:</b>\n"
    "Начинающий специалист с огромным желанием расти вместе с вами. "
    "Сейчас я учусь, пробую и набираюсь опыта, поэтому предлагаю услуги по доступным ценам. "
    "Но помните: каждая работа выполняется с максимальной отдачей!\n\n"
    "<b>ЧТО ПРЕДЛАГАЮ:</b>\n"
    "• Создание продающих текстов и контента\n"
    "• Разработка стильного дизайна\n"  
    "• Настройка базовой автоматизации\n"
    "• Помощь в продвижении соцсетей\n\n"
    "<b>ПОЧЕМУ СТОИТ РАБОТАТЬ СО МНОЙ:</b>\n"
    "▪️ Цены ниже рынка (пока!)\n"
    "▪️ Индивидуальный подход к каждому проекту\n"
    "▪️ Быстрая обратная связь и исполнение\n\n"
    "Kira BlackFox — контент, дизайн и автоматизация под ключ.",
    parse_mode="HTML",
    reply_markup=main_menu_kb()
)
            return

        if text == "⬅️ Назад в меню":
            bot.send_message(chat_id, "Главное меню загружено!", reply_markup=main_menu_kb())
            return

        # Если нажали конкретную услугу — показываем карточку
        if text in SERVICES:
            desc = SERVICES[text]
            img_path = IMAGE_FILES.get(text)
            if img_path and os.path.exists(img_path):
                with open(img_path, "rb") as f:
                    bot.send_photo(chat_id, f, caption=desc, reply_markup=inline_service_kb())
            else:
                bot.send_message(chat_id, desc, reply_markup=inline_service_kb())
            return

        # по умолчанию — подсказка
        bot.send_message(chat_id,
                         "Не поняла тебя 😼. Выбери пункт меню ниже.",
                         reply_markup=main_menu_kb())

    except Exception as e:
        logging.exception("handle_text error: %s", e)
        try:
            bot.send_message(chat_id, "Произошла ошибка. Попробуй ещё раз.", reply_markup=main_menu_kb())
        except Exception:
            pass

# ==============================
# 🔁 CALLBACK (inline back)
# ==============================
@bot.callback_query_handler(func=lambda c: True)
def callback(c):
    data = c.data
    chat_id = c.message.chat.id
    try:
        if data == "cb_services":
            bot.answer_callback_query(c.id)
            bot.send_message(chat_id, "🔥 Выберите услугу:", reply_markup=services_menu_kb())
            return
        bot.answer_callback_query(c.id)
    except Exception as e:
        logging.exception("callback error: %s", e)

# ==============================
# ▶️ RUN
# ==============================
if __name__ == "__main__":
    print("Bot v4 running...")
    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except KeyboardInterrupt:
        print("Stopped by user")
    except Exception as e:
        logging.exception("Bot crashed: %s", e)
        
import os
port = int(os.environ.get("PORT", 5000))
