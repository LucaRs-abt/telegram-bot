
import telebot
import time

# Inserisci qui il tuo token di BotFather
TOKEN = '8137640593:AAEV7rbmgBG6T2tZ6zPnrShRibqKjNV5HU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Ciao Luca! Il bot è attivo 🚀")

# Loop di protezione: riavvia il bot se si blocca
while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(f"⚠️ Errore: {e}")
        print("🔁 Riavvio tra 5 secondi...")
        time.sleep(5)