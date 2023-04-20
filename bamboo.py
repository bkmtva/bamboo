import random
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN:Final = '5954406754:AAFaud-JuoC7UN62oJdbtKYm-ojjzKk504g'
BOT_USERNAME: '@bambboo_bot'

async def say_hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    short_hello_messages = [
        "Hey!",
        "Hi!",
        "Hello!",
        "Hey there!",
        "Hi there!",
        "Hello there!",
        "What's up?",
        "Howdy!",
        "Yo!",
        "Sup?",
        "G'day!",
        "Hey, hey!",
        "Hiya!",
        "Yo yo!",
        "Hey ho!",
        "Hello, hello!",
        "Hi, friend!",
        "Hey buddy!",
        "Hola!",
        "Bonjour!",
        "Ciao!",
        "Namaste!",
        "Salut!",
        "Aloha!",
        "Shalom!",
        "Salam!",
        "Konnichiwa!",
        "Ni hao!",
        "Guten tag!",
        "Sawasdee!"
    ]
   
    await update.message.reply_text(f"{random.choice(short_hello_messages)}")
    
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):   
    await update.message.reply_text("Я бот который поможет тебе следить за расходами :)")



def handel_response(text: str, NAME: str) -> str:
    biggest_hello_messages = [
        f"Hey there, {NAME}!",
        "Hello, my friend! It's great to see you again.",
        f"Greetings and salutations, dear {NAME}!",
        "Hey, stranger! Long time no see.",
        "Hi there!",
        f"Good morning/afternoon/evening, {NAME}! I hope you're doing well.",
        "Hey, howdy, hi there!",
        f"Well, hello, hello, {NAME}!",
        f"Hey, {NAME}, it's great to have a chance to catch up with you.",
        f"Hiya, {NAME}!",
        "Hello, my lovely friend! It's always a pleasure to see you.",
        "Hey there, stranger danger!",
        f"Good day to you, {NAME}!",
        f"Why, hello there, {NAME}! You're looking as fabulous as ever.",
        f"Greetings, {NAME}!",
        f"Hey, hey, hey, {NAME}!",
        f"Hello, my dear {NAME}! It's a pleasure to hear from you.",
        f"Hey, {NAME}, it's been too long!",
        "Good morning/afternoon/evening, sunshine!",
        "Hey, my friend!",
        f"Hi there, {NAME}, I hope you're having a great day so far!",
        f"Well, well, well, if it isn't {NAME}!",
        f"Hello there, {NAME}! I hope you're ready for a fantastic day.",
        f"Hey, stranger! It's great to finally put a face to the name.",
        f"Hiya, {NAME}! I hope your day is as wonderful as you are.",
        f"Hello, {NAME}, it's always a pleasure to see your smiling face.",
        f"Hey there, {NAME}, how's life treating you these days?",
        "Greetings, my friend!",
        f"Hey, {NAME}",
        f"Well, hello there, {NAME}, it's great to hear from you!"
    ]
    processed: str = text.lower()
    if 'hello' in processed or 'hi' in processed or "hey" in processed or 'sup' in processed:
        return f"{random.choice(biggest_hello_messages)}"

    return "I don't understand"
async def handel_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    NAME: str = update.message.chat.first_name
    message_type: str = update.message.chat.type
    text: str = update.message.text
   
    response: str = handel_response(text, NAME) 
    print("response:", response)
    await update.message.reply_text(response)
    
    
    
async def errors(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} error: {context.error}")


# def say_hi(name):
#     # Short Hello Messages
#     short_hello_messages = [
#     "Hey!",
#     "Hi!",
#     "Hello!",
#     "Hey there!",
#     "Hi there!",
#     "Hello there!",
#     "What's up?",
#     "Howdy!",
#     "Yo!",
#     "Sup?",
#     "G'day!",
#     "Hey, hey!",
#     "Hiya!",
#     "Yo yo!",
#     "Hey ho!",
#     "Hello, hello!",
#     "Hi, friend!",
#     "Hey buddy!",
#     "Hola!",
#     "Bonjour!",
#     "Ciao!",
#     "Namaste!",
#     "Salut!",
#     "Aloha!",
#     "Shalom!",
#     "Salam!",
#     "Konnichiwa!",
#     "Ni hao!",
#     "Guten tag!",
#     "Sawasdee!"
# ]

# # Biggest Hello Messages
#     biggest_hello_messages = [
#     "Hey there, [Name]! How's it going today?",
#     "Hello, my friend! It's great to see you again.",
#     "Greetings and salutations, dear [Name]!",
#     "Hey, stranger! Long time no see.",
#     "Hi there, how's your day treating you so far?",
#     "Good morning/afternoon/evening, [Name]! I hope you're doing well.",
#     "Hey, howdy, hi there! How have you been?",
#     "Well, hello, hello, [Name]! How's life treating you?",
#     "Hey, [Name], it's great to have a chance to catch up with you.",
#     "Hiya, [Name]! What's the latest and greatest with you?",
#     "Hello, my lovely friend! It's always a pleasure to see you.",
#     "Hey there, stranger danger! What brings you around these parts?",
#     "Good day to you, [Name]! How's everything in your world?",
#     "Why, hello there, [Name]! You're looking as fabulous as ever.",
#     "Greetings, [Name]! How's your week going so far?",
#     "Hey, hey, hey, [Name]! What's the haps?",
#     "Hello, my dear [Name]! It's a pleasure to hear from you.",
#     "Hey, [Name], it's been too long! What's new and exciting with you?",
#     "Good morning/afternoon/evening, sunshine! How are you today?",
#     "Hey, my friend! How are things in your neck of the woods?",
#     "Hi there, [Name], I hope you're having a great day so far!",
#     "Well, well, well, if it isn't [Name]! How have you been, my friend?",
#     "Hello there, [Name]! I hope you're ready for a fantastic day.",
#     "Hey, stranger! It's great to finally put a face to the name.",
#     "Hiya, [Name]! I hope your day is as wonderful as you are.",
#     "Hello, [Name], it's always a pleasure to see your smiling face.",
#     "Hey there, [Name], how's life treating you these days?",
#     "Greetings, my friend! How's everything in your neck of the woods?",
#     "Hey, [Name], what's the good word?",
#     "Well, hello there, [Name], it's great to hear from you!"
# ]

#     print(f"{random.choice(short_hello_messages)}, {name}")
    
if __name__ == '__main__':
    print("Starting...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', say_hi))
    app.add_handler(CommandHandler('help', help_command))
    
    app.add_handler(MessageHandler(filters.TEXT, handel_messages))
    
    
    app.add_error_handler(errors)
    print("Polling...")
    app.run_polling(poll_interval=3)