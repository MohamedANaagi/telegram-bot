from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7214791099:AAEIaImW5v5tqiG_rQFfdxoIr-Fx1Nh61Sc"

# دالة البداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [KeyboardButton("قدرات 🧠")],
        [KeyboardButton("تحصيلي 📚")],
        [KeyboardButton("رياضيات ➗")]
    ]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=False)
    await update.message.reply_text("👋 مرحبًا بك! اختر القسم من القائمة:", reply_markup=reply_markup)

# دالة التعامل مع الرسائل
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "قدرات" in text:
        await update.message.reply_text("🧠 قسم القدرات: استعد لأفضل التمارين!")
    elif "تحصيلي" in text:
        await update.message.reply_text("📚 قسم التحصيلي: معلومات قيمة ومفيدة.")
    elif "رياضيات" in text:
        await update.message.reply_text("➗ قسم الرياضيات: تمارين وأسئلة شيقة.")
    else:
        await update.message.reply_text("😅 لم أفهم ذلك. اختر من الأزرار تحت أو اكتب /start لإعادة القائمة.")

# تشغيل البوت
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ البوت شغال... روح على تليجرام وجرب /start")
    application.run_polling()

if __name__ == "__main__":
    main()
