from aiogram import types, Dispatcher
from config import bot, ADMINS


async def ban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMINS:
            await message.answer('You are not my boss')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение!')
        else:
            await bot.kick_chat_member(message.chat.id,
                                       message.reply_to_message.from_user.id)
            await message.answer(f'{message.from_user.first_name} bratan kicknul '
                                 f'{message.reply_to_message.from_user.first_name}')
    else:
        await message.answer('Пиши в группу')


async def ban_username(message: types.Message):
    try:
        if message.chat.type != 'private':
            message_words = message.text.split()
            username = message_words[1]
            await bot.kick_chat_member(message.chat.id, user_id=users[f'{username}'])
            await message.answer('Он вышел сам!')
        else:
            await message.answer('пиши в группе!')
    except KeyError:
        await  message.answer(f'{username} ничего не написал зачем его кикать?')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(ban_username, commands=['banban'], commands_prefix='!/')
