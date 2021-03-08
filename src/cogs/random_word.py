"""Get random word from list.

This script sends randomly chosen word from list
Also, especially for this command, checks for spam messages

This file can also be imported as a module and contains the following functions:
    * get_random_word - sends message with randomly chosen word
"""


from random import choice
from asyncio import sleep
from src.lib.database import get_data, modify_data
from src.lib.users import get_random_user
from src.lib.words_base import manage_word


WORDS_ARRAY = get_data(2, False, 'SELECT words FROM main_words_base')
DELAY_TIME = 3


async def get_random_word(msg, args):
    """Get random word from list and send it.

    Parameters:
        msg (discord.message.Message): Execute send to channel function
        args (list): List of arguments (Custom name or mode of function)
    """
    if not args:
        curr_user = msg.author.mention
    else:
        if args[0] == 'добавить':
            args.pop(0)
            word_to_add = " ".join(args)
            await msg.channel.send(manage_word(word_to_add, 'add'),
                                   delete_after=DELAY_TIME)
            await sleep(DELAY_TIME)
            await msg.delete()
            return

        if args[0] == 'удалить':
            if get_data(
                0,
                True,
                'SELECT * FROM admin_list WHERE admins_id = ?',
                msg.author.id
            ):
                args.pop(0)
                word_to_delete = " ".join(args)
                await msg.channel.send(manage_word(word_to_delete, 'del'),
                                       delete_after=DELAY_TIME)
                await sleep(DELAY_TIME)
                await msg.delete()
            return

        if args[0] == 'рандом':
            r_user = await get_random_user(msg)
            if r_user is None:
                return
            curr_user = r_user.mention
        else:
            curr_user = args[0]

    if len(WORDS_ARRAY) == 0:
        await msg.channel.send(f'{msg.author.mention}, я пока не знаю никаких слов, '
                               'однако вы можете добавить новые слова в мой словарь',
                               delete_after=DELAY_TIME)
        await sleep(DELAY_TIME)
        await msg.delete()
    elif _check_for_spam(msg):
        await msg.channel.send(f'{msg.author.mention} куда спамиш?',
                               delete_after=DELAY_TIME)
        await sleep(DELAY_TIME)
        await msg.delete()
    else:
        await msg.channel.send(f'{curr_user} {choice(WORDS_ARRAY)}')


def _check_for_spam(msg):
    """Get random word from list and send it.

    Parameters:
        msg (discord.message.Message): User ID to compare with database

    Returns:
        bool: True if user hit message in a row limit, False otherwise
    """
    spam_info = get_data(
        0,
        False,
        'SELECT spammer_ID, spammer_count FROM variables'
    )
    if spam_info[0] == msg.author.id:
        if spam_info[1] >= 3:
            modify_data(
                0,
                'UPDATE variables SET spammer_count = ?',
                0
            )
            return True
        modify_data(
            0,
            'UPDATE variables SET spammer_count = ?',
            spam_info[1] + 1
        )
        return False
    modify_data(
        0,
        'UPDATE variables SET spammer_ID = ?, spammer_count = ?',
        msg.author.id,
        1
    )
    return False
