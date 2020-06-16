from __app__.chatbot.base import bot

@bot.message_handler(func=lambda message: True, content_types=['text'])
def send_id(message):
    if message.chat.type == "private":
        if(message.forward_from):
            if(message.forward_from.is_bot):
                text = 'O ID do chatbot da mensagem encaminhada é ' + str(message.forward_from.id)
            else:
                text = 'O ID do usuário da mensagem encaminhada é ' + str(message.forward_from.id)
        elif(message.forward_from_chat):
                text = 'O ID do canal da mensagem encaminhada é ' + str(message.forward_from_chat.id)
        else:
            text = 'O seu ID é ' + str(message.chat.id)
        bot.reply_to(message, text)