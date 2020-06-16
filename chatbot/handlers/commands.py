from __app__.chatbot.base import bot

@bot.message_handler(commands=['start', 'ajuda'])
def start(message):
    if message.chat.type == "private":
        text = 'Olá, ' + message.from_user.first_name + '!'
        text += '\n\nEu sou o Identify Bot e posso te ajuda a encontrar os IDs aqui do Telegram.'
        text += '\n\nO seu ID de usuário é ' + str(message.chat.id) + '.'
        text += '\n\nVocê também pode me enviar texto, mídia ou mensagens de outros usuários.'
        bot.send_message(message.chat.id, text)