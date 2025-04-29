from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = "7737694973:AAEnQ_Qkdxl6ROgHvkeh_rC9inelu9eiWT8"

async def start(update: Update, context: CallbackContext):
    # Создаём кнопки
    keyboard = [
        [InlineKeyboardButton("Как всё подключается:", url="https://telegra.ph/Kak-vsyo-podklyuchaetsya-akustika-bez-paniki-04-29")],
        [InlineKeyboardButton("Микшер без паники:", url="https://telegra.ph/Miksher-bez-paniki-zachem-stolko-razyomov-i-za-chto-otvechayut-polzunki-04-29")],
        [InlineKeyboardButton("Эквалайзер и обработка звука:", url="https://telegra.ph/Pokruti-vot-tut-budet-luchshe-ehkvalajzer-i-obrabotka-zvuka-na-mikshere-bez-boli-04-29")]
    ]
    
    # Создаём разметку с кнопками
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с кнопками
    await update.message.reply_text(
        "Привет! Тут ты можешь найти гайды по диджеингу и работе с аппаратурой:", 
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
