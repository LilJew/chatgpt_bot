import logging
import telebot
import openai

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Set up the OpenAI API client
openai.api_key = "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"

# Create the TeleBot client
bot = telebot.TeleBot("5562426530:AAE09FoIxWIWRbGdL4ToJgDeqKh0YTY6esA")

# Define a function to handle all messages
@bot.message_handler(func=lambda message: True)
def chat(message):
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
    bot.reply_to(message, response)

# Start the Bot
bot.polling()
