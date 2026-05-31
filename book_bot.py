"""Telegram bot main package."""

import os
import sys
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Read token from environment variable
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    print("Error: BOT_TOKEN environment variable not set.")
    sys.exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with a 2-button reply keyboard layout."""
    keyboard = [
        [KeyboardButton("Favorite Book")],
        [KeyboardButton("About the Book")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Choose an option from the keyboard below:", 
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Answers based on the specific keyboard button pressed."""
    user_text = update.message.text

    if user_text == "Favorite Book":
        response = "Chemistry coursebook, 7th grade"
    elif user_text == "About the Book":
        response = "A school coursebook on itroduction to Chemistry"
    else:
        response = "Please use the menu buttons to ask a question."

    await update.message.reply_text(response)

def main():
    """Starts the bot application."""
    # Build the application using the token
    app = Application.builder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))

    # Add text message handler to process button clicks
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()
