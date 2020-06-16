from __app__.chatbot.base import bot

@bot.message_handler(content_types=['photo'])
def handle_photo_files(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id, 'Não posso interpretar imagens.')