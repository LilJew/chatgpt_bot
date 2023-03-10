import logging
import os
import telebot
import openai
import settings

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Set up the OpenAI API client


openai.api_key = os.environ["OPENAI_API_KEY"]

# Create the TeleBot client
bot = telebot.TeleBot(os.environ["TG_TOKEN"])



# Define a function to handle all messages
@bot.message_handler(func=lambda message: True)
def chat(message):
    global response
    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='You said: ' + message.text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    
    # Send the response to the user
    if message.chat.type == "group":
        if f'@{bot.get_me().username}' in message.text:
            bot.reply_to(message, response)
    elif message.chat.type == "private":
        bot.reply_to(message, response)


# Start the Bot
bot.polling()
