import logging
import cfg
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.router import Router

API_TOKEN = cfg.API_TOKEN

# Configure logging
logging.basicConfig(level=logging.DEBUG)
lgr = logging.getLogger('personal')


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)



@router.message(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Русский военный корабль, иди нахуй")



@router.message()
async def process_message(message: types.Message):
    lgr.debug('new message received in process method')
    lgr.debug(f'caption: {message.caption}')

    if message.chat.id != cfg.TARGET_CHAT_ID:
        await bot.forward_message(chat_id=cfg.TARGET_CHAT_ID, from_chat_id=message.chat.id, message_id=message.message_id)
    else:
        answer_text = message.text
        await bot.send_message(chat_id=message.reply_to_message.forward_from.id, text=answer_text)



async def start():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
