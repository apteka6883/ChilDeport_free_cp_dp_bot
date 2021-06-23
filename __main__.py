
from random import choice
from time import time
from string import ascii_letters, digits

from telebot import TeleBot, types
from pyshorteners import Shortener

bot = TeleBot("1837589842:AAFD6qYea1U4uKBFdGtzgNlV61BNoUv5S8A")
category = 'bdsm (10)', 'в лесу (2)', 'в школе (5)', 'веб (21)', 'гарем (1)', 'гей (22)', 'групповой секс (3)', 'инцест (13)', 'лезби (17)', 'переодевание (4)', 'повседневность (1)', 'эротика (30)'
StrList = """Список бесплатно доступной детской порнографии!! Доступен в /help
Перед работой с ботом ознакомтесь с /help 
Вы можете выбрать один из вариантов введя команду /see [id|name]
Вы так же можете получить доступ к VIP контенту, команда /buy
Для этого обратитесь к администратору бота!
"""
FH = "mega.nz", "yadi.sk", "cloud.mail.ru"


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
Так же тут показан только бесплатно доступный контент, с VIP вы получаете в 5 раз больше видео,
и НИКАКОЙ РЕКЛАМЫ! Плюс вы будете получать не ссылку на ФО а прямую ссылку на выдео с наших серверов (И на ФО тоже)!
Чтобы получить VIP введите команду /buy и оплатите на биткоин кашелёк. Покупаете вы один раз и на всегда.

Весь контент предоставляется студией ChilDeport, мы распологаемся в России, так что все видео на русском.
Но, когда вы покупаете VIP, мы предоставляем так же видео партнёров.
"""


def rand_str(l: int):
    return "".join((choice(ascii_letters + digits) for _ in range(l)))


def rand_url(serv: str):
    if serv == "mega.nz":
        url = f"https://{serv}/folder/{rand_str(8)}#{rand_str(22)}"
    elif serv == "yadi.sk":
        url = f"https://{serv}/d/{rand_str(14)}"
    elif serv == "cloud.mail.ru":
        url = f"https://{serv}/public/{rand_str(4)}/{rand_str(9)}"
    else:
        url = "https://is.gd/OOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    stn = Shortener()
    return stn.qpsru.short(
        f"https://galaxy-link.space/st?api=106a61983212472df50e1a4c7d069fb40a92a7f9&url={stn.qpsru.short(url)}")


@bot.message_handler(["start"])
def start_handler(message: types.Message):
    bot.send_message(message.chat.id, StrList)


@bot.message_handler(["see"])
def start_handler(message: types.Message):
    cat = is_in_cat(message.text.split()[1:])
    if cat[0]:
        ans = f"Получаю ссылку на категорию {cat[1]} [{cat[0]}]\n(Все файлы лежат на различных популярных файлообменниках!)"
        bot.send_message(message.chat.id, ans)
        ans = "Ваша ссылка на категорию {0} [{1}]: {2}\n(Перейдя по ссылке вы увидете несколько секунд рекламы, но не пугайтесь, в итоге вы попадёте на ФО {3})".format(
            cat[1], cat[0], rand_url(rs := choice(FH)), rs)
        bot.send_message(message.chat.id, ans, disable_web_page_preview=True)
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
