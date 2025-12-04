import logging
import qrcode
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = '8023296312:AAFZvasvkaPKwvmfkPHXf5Q7AmoDaJLSvNg'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Отправьте мне ссылку или текст, и я создам для вас QR-код !")

@dp.message_handler()
async def generate_qr_code(message: types.Message):
    data = message.text
    img = qrcode.make(data)
    img.save('qrcode.png')
    with open('qrcode.png', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo, caption="Ваш QR-код готов !")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
