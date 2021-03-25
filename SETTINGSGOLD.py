import telebot

URLGOLD = 'http://mfd.ru/centrobank/preciousmetals/'

URLBIT = 'https://coinmarketcap.com/ru/'

URLSP500 = 'https://www.finanz.ru/indeksi/s&p_500'

TOKEN = '1730286171:AAF2CNdHXrn-O_mdaMZqsqD6XjZdKu9U2Zc'

BOT = telebot.TeleBot(TOKEN)

BUTTON_START = 'В начало'
BUTTON_METALL = 'ДРАГМЕТАЛЛЫ'
BUTTON_CURREBCY = 'ВАЛЮТЫ'
BUTTON_CRIPTA = 'КРИПТОВАЛЮТЫ'
BUTTON_SP = 'S&P 500 (SPX)'


BUTTON_GET_ALL_GOLD = 'Вывести все драгметаллы'
BUTTON_GET_GOLD = 'Вывести курс Золота'
BUTTON_GET_SER = 'Вывести курс Серебра'
BUTTON_GET_PLAT = 'Вывести курс Платины'
BUTTON_GET_PALL = 'Вывести курс Палладия'


BUTTON_GET_ALL_USD = 'Вывести все Валюты'
BUTTON_GET_USD = 'Вывести курс Доллара'
BUTTON_GET_EUR = 'Вывести курс Евро'

BUTTON_GET_ALL_CRIP = 'Вывести все Криптовалюты'
BUTTON_GET_BIT = 'Вывести курс Биткоина'
BUTTON_GET_ETH = 'Вывести курс Эфира'
BUTTON_GET_MONERO = 'Вывести курс Монеро'
BUTTON_GET_DOG = 'Вывести курс Догекоина'

def create_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    return keyboard


KEYBOARD_START = create_keyboard()
KEYBOARD_START.row(BUTTON_METALL, BUTTON_CURREBCY)
KEYBOARD_START.row(BUTTON_CRIPTA, BUTTON_SP)


KEYBOARD_CHOICE = create_keyboard()
KEYBOARD_CHOICE.row(BUTTON_GET_ALL_GOLD, BUTTON_GET_GOLD,)
KEYBOARD_CHOICE.row(BUTTON_GET_SER, BUTTON_GET_PLAT,)
KEYBOARD_CHOICE.row(BUTTON_GET_PALL, BUTTON_START)  


KEYBOARD_CHOICE_USD = create_keyboard()
KEYBOARD_CHOICE_USD.row(BUTTON_GET_ALL_USD, BUTTON_GET_USD)
KEYBOARD_CHOICE_USD.row(BUTTON_GET_EUR, BUTTON_START)


KEYBOARD_CHOICE_CRIPTA = create_keyboard()
KEYBOARD_CHOICE_CRIPTA.row(BUTTON_GET_ALL_CRIP, BUTTON_GET_BIT)
KEYBOARD_CHOICE_CRIPTA.row(BUTTON_GET_ETH, BUTTON_GET_MONERO)
KEYBOARD_CHOICE_CRIPTA.row(BUTTON_GET_DOG, BUTTON_START)