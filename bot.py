import logging
from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8733529051:AAGFHdDbpYqhjUuTIAO79879mhE9ENmFt2s"
WEB_APP_URL = "https://schrodinger-box.vercel.app"  # Пока можно localhost

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(
        [[KeyboardButton("🎁 Играть", web_app=WebAppInfo(url=WEB_APP_URL))]],
        resize_keyboard=True
    )
    
    await update.message.reply_text(
        "🎁 <b>SCHRÖDINGER'S BOX</b>\n\n"
        "Купи коробку за 5 USDT\n"
        "Внутри может быть до 25,000 USDT\n\n"
        "🎮 Нажми кнопку чтобы начать!",
        parse_mode="HTML",
        reply_markup=keyboard
    )

async def demo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎁 <b>ДЕМО-РЕЖИМ</b>\n\n"
        "Твой баланс: 100 виртуальных USDT\n"
        "3 бесплатных коробки\n\n"
        "🔥 Выиграл: 1,000 USDT!\n\n"
        "Хочешь на реальные? 💰",
        parse_mode="HTML"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('demo', demo))
    
    print("✅ Бот запущен!")
    app.run_polling()

if __name__ == '__main__':
    main()