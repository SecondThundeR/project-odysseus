"""User Handler Library (Beta).

This script allows to select user from list of server users
and get his information

This file can also be imported as a module and contains the following functions:
    * get_random_user - returns info of randomly chosen user
    * get_shipping_users - returns info of two randomly chosen users
    * get_members_name - returns nickname or name of member as a string
    * add_member_to_db - adds member to database
    * rem_member_from_db - removes member from database
    * is_user_admin - returns True, if user is admin of bot
    * is_user_blocked - returns True, if user is in blacklist of bot
"""


from random import choice
from src.lib.database import get_data, modify_data


async def get_random_user(msg):
    """Get a random user from an list and return it's info.

    Parameters:
        msg (discord.message.Message): Info about guild from message

    Returns:
        discord.member.Member: Object with info about member
            which was randomly chosen.
        None for empty array of users
    """
    users = get_data(0, False, 'SELECT users FROM users_id')
    try:
        member = await msg.guild.fetch_member(choice(users))
        return member
    except IndexError:
        return None


async def get_shipping_users(msg):
    """Get two random users from an list and return their info.

    Parameters:
        msg (discord.message.Message): Info about guild from message

    Returns:
        list: Users objects with their info which was randomly chosen.
        None for empty array of users
    """
    users = get_data(0, False, 'SELECT users FROM users_id')
    try:
        first_member = await msg.guild.fetch_member(choice(users))
        second_member = await msg.guild.fetch_member(choice(users))
        while second_member == first_member:
            second_member = await msg.guild.fetch_member(choice(users))
        return [first_member, second_member]
    except IndexError:
        return None


def get_members_name(member):
    """Check if member has a nickname on server.

    Parameters:
        member (discord.member.Member): Info about member of guild

    Returns:
        str: User's name, if user doesn't have a nickname and otherwise
    """
    if member.nick is None:
        return member.name
    return member.nick


def add_member_to_db(member):
    """Add member to database.

    Used for adding members on startup or when member is getting
    on the server

    Parameters:
        member (discord.member.Member): Info about member of guild
    """
    if member.bot:
        return modify_data(0, 'INSERT INTO bots VALUES (?)', member.id)
    return modify_data(0, 'INSERT INTO users VALUES (?)', member.id)


def rem_member_from_db(member):
    """Remove member from database.

    Used for removing members from database in certain cases
    (Ignoring in shipping and etc.)

    **Noteworthy:** This makes sense until the bot reboots. In future there are plans
    for adding ignore list for shipping and other commands

    Parameters:
        member (discord.member.Member): Info about member of guild
    """
    if member.bot:
        return modify_data(0, 'DELETE FROM bots WHERE bots_id = ?', member.id)
    return modify_data(0, 'DELETE FROM users WHERE users_id = ?', member.id)


def is_user_admin(user_id):
    """Check if user is an admin of bot.

    Parameters:
        user_id (int): ID of user to check

    Returns:
        bool: True, if user is admin of bot. False otherwise
    """
    db_id = get_data(0,
                     True,
                     'SELECT admins_id FROM admin_list WHERE admins_id = ?',
                     user_id)
    return user_id == db_id


def is_user_blocked(user_id):
    """Check if user is in blacklist of bot.

    Parameters:
        user_id (int): ID of user to check

    Returns:
        bool: True, if user is banned. False otherwise
    """
    db_id = get_data(0,
                     True,
                     'SELECT blocked_id FROM block_list WHERE blocked_id = ?',
                     user_id)
    return user_id == db_id