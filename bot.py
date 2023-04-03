from aiogram import Bot, Dispatcher, executor, types
import databaser

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('Здравствуйте!\nЯ - Academic Bot. Сообщу информацию об успеваемости вашего ребёнка по любой дисциплине.\n\nПожалуйста, напишите мне сообщение в форме: Фамилия Имя Дисциплина, чтобы получить информацию. \n\nПример: Михайлов Михаил Математика.\n\nЧтобы получить информацию по всем предметам, напишите \"Все\" на месте пункта \"Дисциплина\".')

@dp.message_handler()
async def send_info(message: types.Message):
    message_text = message.text.split()
    if len(message_text) >= 3: # Потому что формат ожидаемого сообщения = Фамилия Имя Дисциплина
        pupil_name = f'{message_text[0]} {message_text[1]}' # Первые два слова всегда фамилия и имя ученика
        subject = ' '.join(message_text[2:]) # Всё остальное - название дисциплины
        pupil_info = databaser.find_in_database(pupil_name, subject)
        if pupil_info != []:
            answer = ''
            for row in pupil_info:
                answer += f'{row[3]}: {row[4]}\n'
            await message.reply(f'Оценки ученика \"{pupil_name}\":\n{answer}')
        else:
            await message.reply(f'Не удалось найти данного ученика или дисциплину. Проверьте правильность ввода данных.')
    else:
        await message.reply('К сожалению, мне не знакома данная команда...\n\nВоспользуйтесь /start или /help, чтобы получить доступные команды.')

def start():
    executor.start_polling(dp, skip_updates=True)
