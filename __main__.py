from telebot import TeleBot, types
from pyshorteners import Shortener
from random import choice
from time import time

bot = TeleBot("1837589842:AAFD6qYea1U4uKBFdGtzgNlV61BNoUv5S8A")
category = 'bdsm', 'в лесу', 'в школе', 'веб', 'гарем', 'гей', 'групповой секс', 'инцест', 'лезби', 'переодевание', 'повседневность', 'эротика'
StrList = """Список бесплатно доступной детской порнографии!! Доступен в /help
Перед работой с ботом ознакомтесь с /help 
Вы можете выбрать один из вариантов введя команду /see [id|name]
Вы так же можете получить доступ к VIP контенту, всего за 70$/месяц!
Для этого обратитесь к администратору бота!
"""
FH = "mega.nz", "yadi.sk", "dropbox.com", "cloud.mail.ru"


def is_in_cat(arg) -> tuple:
    if not arg:
        return False, ""
    text: str = arg[0].strip()
    if text.isdigit():
        id_ = int(text)
        if len(category) >= id_ > 0:
            return id_, category[id_ - 1]
    else:
        if text in category:
            return category.index(text), text
    return False, text


def gen_help():
    return """Список категорий:
""" + "\n".join((f"{i}. {v}" for i, v in enumerate(category, 1))) \
        + f"""Если у вас проблемы с доступом к материалам, попробуйте через {round(time() % 60)} секунд.
Так как наш бот обнавляет ссылку на категорию каждые 60 секунд.
Сейчас из файлообенников на которых лежит наш материал, мы можем предложить вам {' / '.join(FH)}
При формировании ссылки (/see) бот выбирает рандомный ФО, а все наши файлы лежат на всех ФО, 
так что можете повторно отправить запрос на ссылку чтобы получить другой ФО.
"""


@bot.message_handler(["start"])
def start_handler(message: types.Message):
    bot.send_message(message.chat.id, StrList)


@bot.message_handler(["see"])
def start_handler(message: types.Message):
    cat = is_in_cat(message.text.split()[1:])
    if cat[0]:
        ans = f"Получаю ссылку на категорию {cat[1]} [{cat[0]}] (Все файлы лежат на различных популярных файлообменниках!)"
        bot.send_message(message.chat.id, ans)
        ans = "Ваша ссылка на категорию {0} [{1}]: {2}\n(Перейдя по ссылке вы увидете несколько сек рекламы, но не пугайтесь, в итоге вы попадёте на ФО {3})".format(
            cat[1], cat[0], Shortener().qpsru.short("https://galaxy-link.space/st?api=106a61983212472df50e1a4c7d069fb40a92a7f9&url=" + Shortener().qpsru.short("https://galaxy-link.space/st?api=106a61983212472df50e1a4c7d069fb40a92a7f9&url=https://is.gd/OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")), choice(FH))
        bot.send_message(message.chat.id, ans)
    else:
        ans = f"Не известная категория {cat[1]}."
        bot.send_message(message.chat.id, ans)


@bot.message_handler(["help"])
def help_(message: types.Message):
    bot.send_message(message.chat.id, gen_help())


@bot.message_handler()
def any_(message: types.Message):
    bot.send_message(message.chat.id, "Воспользуйтесь - /help")


bot.polling(True)
