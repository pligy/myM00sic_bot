from aiogram import Bot, Dispatcher, executor, types
from start import bot, dp
from my_parser import start_main, main

@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    await message.answer("hello")

@dp.message_handler(commands=["hello"])
async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, f"Привет, {message.from_user.full_name}")

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Искать музыку", "Создать плейлист", "Мои плейлисты"]
    keyboard.add(*buttons)
    await message.answer("Что вы хотите сделать?", reply_markup=keyboard)

async def create_playlist():
    pass

async def add_playlist():
    pass

async def get_playlists():
    pass

@dp.message_handler(lambda message: message.text == "Мои плейлисты")
async def playlist_output(message: types.Message):
    playlists = await get_playlists()

    if playlists == []:
        await message.reply("У вас нет ни одного плейлиста! Попробуйте создать плейлист")
    #else:
        #for i in range(len(playlists)):

@dp.message_handler(lambda message: message.text == "Искать музыку")
async def find_music(message: types.Message):
    await message.reply("Введите название музыки")

@dp.message_handler(lambda message: message.text == "Создать плейлист")
async def create_playlist(message: types.Message):
    await message.reply("Список ваших аудио")

@dp.callback_query_handler(lambda message: message.text == "➕")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("Успех")

inkb = types.InlineKeyboardMarkup(row_width=5)
inButton = types.InlineKeyboardButton(text="➕", callback_data="➕")
inButton2 = types.InlineKeyboardButton(text="⏮", callback_data="⏮")
inButton3 = types.InlineKeyboardButton(text="⏯", callback_data="⏯")
inButton4 = types.InlineKeyboardButton(text="⏭", callback_data="⏭")
#inButton5 = types.InlineKeyboardButton(text="⏯", callback_data="⏯")
inkb.add(inButton2, inButton3, inButton4, inButton)

@dp.message_handler()
async def echo(message: types.Message):
    text = message.text
    lst = await main(text)

    print(lst)
    for i in range(len(lst)):
        await message.answer(str(i + 1) + ". " + lst[i]) # message.text
        await message.answer("Выберите действие:", reply_markup=inkb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
