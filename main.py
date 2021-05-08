from pyrogram import Client
from pyrogram.filters import command, private, text
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent

from function import transliterate

app = Client("tilon", api_id=2424010, api_hash='9fb173ded391c8aca77667709be270e3',
             bot_token="bot_tokeni")


@app.on_message(private & command(['start']))
async def _start(_, message):
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Inlineda sinab ko'rish", switch_inline_query="Salom")]])

    await message.reply_text("Salom, men kirill harflarini lotinga yoki lotin harflarini kirillga o‘tkazib beraman."
                             "Shunchaki matningizni yuboring", reply_markup=keyboard)


@app.on_message(private & text)
async def hello(_, message):
    await message.reply_text(transliterate(message.text))


@app.on_inline_query()
async def _inline(_, query):
    try:
        await query.answer(results=[
            InlineQueryResultArticle(
                title="Yuborish",
                input_message_content=InputTextMessageContent(
                    transliterate(query.query)
                ),
            )
        ], cache_time=0)
    except:
        await query.answer(results=[
            InlineQueryResultArticle(
                title="Xatolik",
                input_message_content=InputTextMessageContent(
                    "Qandaydir xatolik bo'ldi\n@TILON bilan bog'laning."
                ),
            )
        ], cache_time=0)
    else:
        await query.answer(results=[])


app.run()
