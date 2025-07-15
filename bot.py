from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, CallbackQueryHandler, filters
import os

# Mensaje de bienvenida con bold serif unicode
MENSAJE_BIENVENIDA = (
    "𝐇𝐎𝐋𝐀! {nombre}\n\n"
    "𝐏𝐚𝐫𝐚 𝐥𝐨𝐬 𝐧𝐮𝐞𝐯𝐨𝐬 𝐦𝐢𝐞𝐦𝐛𝐫𝐨𝐬 𝐞𝐥 𝐜𝐨𝐧𝐭𝐞𝐧𝐢𝐝𝐨 𝟏𝟖+ 𝐩𝐚𝐫𝐚 𝐚𝐝𝐮𝐥𝐭𝐨𝐬 𝐞𝐬𝐭𝐚́:\n\n"
    "🔐𝐁𝐋𝐎𝐐𝐔𝐄𝐀𝐃𝐎🔐\n\n"
    "𝐏𝐫𝐞𝐬𝐢𝐨𝐧𝐞 𝐞𝐥 𝐛𝐨𝐭𝐨́𝐧\n"
    "🔓𝐃𝐄𝐒𝐁𝐋𝐎𝐐𝐔𝐄𝐀𝐑🔓\n"
    "𝐩𝐚𝐫𝐚 𝐯𝐞𝐫 𝐭𝐨𝐝𝐨 𝐞𝐥 𝐜𝐨𝐧𝐭𝐞𝐧𝐢𝐝𝐨."
)

# Botonera
keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("🔓𝐃𝐄𝐒𝐁𝐋𝐎𝐐𝐔𝐄𝐀𝐑🔓", url="https://tinyurl.com/JOVENClTAS")],
    [
        InlineKeyboardButton("𝐄𝐒𝐓𝐔𝐃𝐈𝐀𝐍𝐓𝐄𝐒", url="https://tinyurl.com/ESCUELITACUBA"),
        InlineKeyboardButton("𝐂𝐔𝐁𝐀𝐍𝐈𝐓𝐀𝐒", url="https://tinyurl.com/CUBANITASPUTAS")
    ],
    [InlineKeyboardButton("¿𝐂𝐨́𝐦𝐨 𝐝𝐞𝐬𝐛𝐥𝐨𝐪𝐮𝐞𝐚𝐫?", callback_data="popup_ayuda")]
])

# Diccionario para rastrear el último mensaje de bienvenida
ultimo_mensaje_id = {}

# Función de bienvenida
async def bienvenida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    nombre = update.message.new_chat_members[0].first_name

    # Borra el mensaje anterior si existe
    if chat_id in ultimo_mensaje_id:
        try:
            await context.bot.delete_message(chat_id, ultimo_mensaje_id[chat_id])
        except:
            pass

    texto = MENSAJE_BIENVENIDA.format(nombre=nombre)
    mensaje = await update.message.reply_text(text=texto, reply_markup=keyboard)
    ultimo_mensaje_id[chat_id] = mensaje.message_id

# Maneja el botón "¿Cómo desbloquear?"
async def manejar_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "popup_ayuda":
        await query.message.reply_text(
            "𝐏𝐫𝐞𝐬𝐢𝐨𝐧𝐞 𝐞𝐥 𝐛𝐨𝐭𝐨́𝐧 𝐃𝐄𝐒𝐁𝐋𝐎𝐐𝐔𝐄𝐀𝐑 𝐲 𝐬𝐞𝐥𝐞𝐜𝐜𝐢𝐨𝐧𝐞 𝟑 𝐠𝐫𝐮𝐩𝐨𝐬 𝐆𝐑𝐀𝐍𝐃𝐄𝐒."
        )

# Main
if __name__ == '__main__':
    TOKEN = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, bienvenida))
    app.add_handler(CallbackQueryHandler(manejar_callback))
    app.run_polling()
