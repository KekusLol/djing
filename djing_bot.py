from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = "7737694973:AAEnQ_Qkdxl6ROgHvkeh_rC9inelu9eiWT8"

async def start(update: Update, context: CallbackContext):
    # Создаём кнопки
    keyboard = [
        [InlineKeyboardButton("Тема 1", url="https://example.com")],
        [InlineKeyboardButton("Тема 2", url="https://example.org")],
        [InlineKeyboardButton("Тема 3", url="https://example.net")]
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