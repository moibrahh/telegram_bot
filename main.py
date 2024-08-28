from typing import Final
from telegram import Update # type: ignore
from telegram.ext import Application, CommandHANdler, MessageHAndler, filters, ContextTypes # type: ignore

TOKEN: Final = '555712669:AAGAg9cVB19dD27_hyTLAuiQMF4R6s1FR74'
BOT_USERNAME: Final = '@B_man1bot'

#commands
async def start_command (update: Update, context: ContextTypes.DEFAULT_TYPES):
    await update.message.reply_text("Hello, Mr.Mo welcomes you")

async def help_command (update: Update, context: ContextTypes.DEFAULT_TYPES):
    await update.message.reply_text("Kindly let me know how I may assist you")

async def custom_command (update: Update, context: ContextTypes.DEFAULT_TYPES):
    await update.message.reply_text("Hello, Mr.Mo welcomes you")

#response handling
def handle_response(text: str) -> str:
    processed: str = text.lower()
    if "hello" in processed:
        return "Hey there"
    if "how are you " in processed:
        return "I am doing great"
    
    return "I do not understand your command"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME  in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

        print('Bot:', response)
        await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot....')
    app = Application.builder().token(TOKEN).build()


    #commands
    app.add_handler(CommandHANdler('start', start_command))
    app.handler(CommandHANdler('help', help_command))
    app.handler(CommandHANdler('custom', custom_command))

    #messages
    app.add_handler(MessageHAndler(filters.TEXT, handle_message))


    #errors
    app.add_error_handler(error)

    #polling
    print('polling.....')
    app.run_polling(poll_interval=3)

