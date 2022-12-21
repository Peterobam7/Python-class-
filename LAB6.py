
import telegram.ext

Token = '5621879944:AAFbyfsEobMCKQk_1j275LJ0vhdOC6zj9kE'

updater = telegram.ext.Updater("5621879944:AAFbyfsEobMCKQk_1j275LJ0vhdOC6zj9kE", use_context= True)
dispatcher = updater.dispatcher 
def start(update, context):
    update.message.reply_text("Этот бот предоставляет вам ссылки на видео YouTube о том, как решать различные виды кубиков Рубика. \n/S2-Для кубов 2X2\n/S3-Для кубов 3X3\n/SPoly-Для кубов многогранников\n/SSkewb-для кубов skewb\n/S6-для Кубов 6X6 ")

        
def help(update,context):
    update.message.reply_text(
    """
    /start ->  Welcome to peter's TelBot
    /S2 -> solution for 2X2 cube
    /S3 -> solution for 3X3 cube
    /S6 -> solution for 6X6 cube
    /SPoly -> solution for polyhedron cube
    /SSkewb -> solution for Sphere cube 
    """
    )

def S2(update, context):
    update.message.reply_text("Here is a solution for 2X2 cube: https://youtu.be/mSA0IZh1bMU")
def S3(update, context):
    update.message.reply_text("Here is a solution for 3X3 cube: https://youtu.be/KGvQRaK1mvs ")
def SPoly(update, context):
    update.message.reply_text("Here is a solution for polyhedron cube: https://youtu.be/oVRooYDvRqg ")
def SSkewb(update, context):
    update.message.reply_text("Here is a solution for Skewb cube: https://youtu.be/I6132yshkeU")
def S6(update, context):
    update.message.reply_text("Here is a solution for 6X6 cube: https://youtu.be/5Lw6GniCkUk")

dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('S2', S2))
dispatcher.add_handler(telegram.ext.CommandHandler('S3', S3))
dispatcher.add_handler(telegram.ext.CommandHandler('SPoly', SPoly))
dispatcher.add_handler(telegram.ext.CommandHandler('SSkewb', SSkewb))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.CommandHandler('S6', S6))

updater.start_polling()
updater.idle()
