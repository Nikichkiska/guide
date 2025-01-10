from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Ваш токен (замените на тот, что вы получили от BotFather)
API_TOKEN = '7926369822:AAH5y76DGlvgV-leksoYe-J01DqzwWtBzJ4'

# Функция, которая будет отвечать на команду /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Ответ бота пользователю
    await update.message.reply_text('Привет! Я твой бот!')

# Основная функция для запуска бота
def main():
    # Создаем приложение с переданным токеном
    application = Application.builder().token(API_TOKEN).build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем polling (прослушивание сообщений от пользователей)
    print("Бот запущен. Ожидание команд...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
