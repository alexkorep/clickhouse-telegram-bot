import os
from clickhouse_driver import Client
from src.clickhouse import (
    CLICKHOUSE_HOST,
    CLICKHOUSE_PORT,
    CLICKHOUSE_USER,
    CLICKHOUSE_PASSWORD,
    CLICKHOUSE_SECURE,
)
from src.messages import MSG_WELCOME


CLICKHOUSE_ADMIN_DATABASE = os.environ.get(
    "CLICKHOUSE_ADMIN_DATABASE", "clickhouse_telegram_bot"
)

admin_client = Client(
    host=CLICKHOUSE_HOST,
    port=CLICKHOUSE_PORT,
    user=CLICKHOUSE_USER,
    password=CLICKHOUSE_PASSWORD,
    database=CLICKHOUSE_ADMIN_DATABASE,
    secure=CLICKHOUSE_SECURE,
)


def check_invite(user_msg):
    result = admin_client.execute(
        "SELECT * FROM invites WHERE invite = %(invite)s",
        {"invite": user_msg},
    )
    if len(result) > 0:
        return True

    return False


def check_authentication(user_username, bot, chat_dest, user_msg):
    """Check if the request is authenticated.
    :returns: True if the request is authenticated, False otherwise.
    """
    result = admin_client.execute(
        "SELECT * FROM users WHERE username = %(user_username)s",
        {"user_username": user_username},
    )

    print("result", result)
    if len(result) > 0:
        return True

    if check_invite(user_msg):
        # Create an account
        admin_client.execute(
            "insert into users (username) values (%(user_username)s)",
            {"user_username": user_username},
        )
        bot.send_message(
            chat_dest,
            "Invite is accepted.\n\n" + MSG_WELCOME,
        )
        return False

    bot.send_message(
        chat_dest,
        "This bot is invite only. Please send me your invite code to get access.",
    )
    return False
