from telegram.ext import MessageHandler, Filters, run_async

from backend.models import Message
from backend.tgbot.base import TelegramBotApi
from backend.tgbot.utils import logger


@run_async
def echo_handler(api: TelegramBotApi, update):
    logger.info('Got message {} from {}'.format(update.message.text, update.message.chat_id))
    Message.from_update(api, update)
    api.bot.send_message(update.message.chat_id, update.message.text)


handlers = [
    MessageHandler(Filters.text, echo_handler)
]
