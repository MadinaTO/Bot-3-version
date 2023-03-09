from aiogram import types, Dispatcher
from config import bot


async def echo(message: types.Message):
    bad_words = ['java', 'html', 'дурак', 'дура']
    username = '{message.from_user.username}' \
        if message.from_user.username is not None else message.from_user.first_name
    for word in bad_words:
        if word in message.text.lower().replace(' ', ''):
           await message.answer(f'Ne materis {username} '
                                f'Sam ty {word}!')

        if message.text.startswith('.'):
            await bot.pin_chat_message(message.chat.id, message.message_id)

        if message.text == 'dice':
            a = await bot.send_dice(message.chat.id, emoji='⚽')
            print(a.dice.value)

        if message.text == 'python':
            b = await bot.send_dice(message.chat.id, emoji='🎰')
            print(b.dice.value)

async def user_ban(massage: types.Message):
    user_name = massage.from_user.username
    if user_name:
        user_name = user_name
    else:
        user_name = massage.from_user.first_name
    if massage.from_user.username is not users:
        users[f'@{user_name}'] = massage.from_user.id
        print(users)
    else:
        pass


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
    dp.register_message_handler(user_ban)
