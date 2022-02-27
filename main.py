import logging
import cfg
from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = cfg.API_TOKEN

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Русский военный корабль, иди нахуй")


@dp.message_handler()
async def process_message(message: types.Message):

    if message.chat.id != cfg.TARGET_CHAT_ID:
        await message.forward(chat_id=cfg.TARGET_CHAT_ID)
    else:
        answer_text = message.text
        await bot.send_message(chat_id=message.reply_to_message.forward_from.id, text=answer_text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)