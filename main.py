from settings.SETTINGSGOLD import *

from parse.ParseCheif import ParseGold, ParseUsd, ParseCrip, ParseSP500
from parse.dataPygold import Data, DataCrip, DataSP
#from parse.ParseSP import messagesp              #  ЭТОТ ПАРС ТОРМОЗИТ ВСЕ ОСТАЛЬНЫЕ ( selenium )

sitegold = ParseGold(URLGOLD).get_content()
valuesgold = Data(sitegold)
#print(valuesgold.get_all_list())   # ВЫВОДИТ ДРАГМЕТАЛЛЫ

siteusd = ParseUsd(URLGOLD).get_content_usd()
usdvalue = Data(siteusd)
#print(siteusd)    # ВЫВОДИТ ДОЛЛАР И ЕВРО

sitebit = ParseCrip(URLBIT).get_content_bit()
valuescrip = DataCrip(sitebit)
#print(valuescrip.get_all_list_crip())    # ВЫВОДИТ КРИПТОВАЛЮТЫ


sitesp = ParseSP500(URLSP500).get_content_sp()
valuesp = DataSP(sitesp)
#print(messagesp)          # ВЫВОДИТ ИНДЕКС SP 500



@BOT.message_handler(commands = ['start'])
def start_message(message):
    BOT.send_message(message.chat.id, 'Выбери интересующий тебя актив', reply_markup = KEYBOARD_START)


@BOT.message_handler(content_types = ['text'])
def get_text_messages(message):

    if message.text == BUTTON_METALL:
        BOT.send_message(message.chat.id, 'Какая информация нужна?', reply_markup = KEYBOARD_CHOICE)

    elif message.text == BUTTON_GET_ALL_GOLD:
        BOT.send_message(message.chat.id, valuesgold.get_all_list(), reply_markup = KEYBOARD_CHOICE) 

    elif message.text == BUTTON_GET_GOLD:
        BOT.send_message(message.chat.id, valuesgold.get_gold_value(), reply_markup = KEYBOARD_CHOICE)

    elif message.text == BUTTON_GET_SER:
        BOT.send_message(message.chat.id, valuesgold.get_ser_value(), reply_markup = KEYBOARD_CHOICE)

    elif message.text == BUTTON_GET_PLAT:
        BOT.send_message(message.chat.id, valuesgold.get_plat_value(), reply_markup = KEYBOARD_CHOICE)

    elif message.text == BUTTON_GET_PALL:
        BOT.send_message(message.chat.id, valuesgold.get_pallad_value(), reply_markup = KEYBOARD_CHOICE) 


    elif message.text == BUTTON_CURREBCY:
        BOT.send_message(message.chat.id, 'Какая информация нужна?', reply_markup = KEYBOARD_CHOICE_USD)   

    elif message.text == BUTTON_GET_ALL_USD:
        BOT.send_message(message.chat.id, siteusd, reply_markup = KEYBOARD_CHOICE_USD)

    elif message.text == BUTTON_GET_USD:
        BOT.send_message(message.chat.id, usdvalue.get_usd_value(), reply_markup = KEYBOARD_CHOICE_USD)

    elif message.text == BUTTON_GET_EUR:
        BOT.send_message(message.chat.id, usdvalue.get_eur_value(), reply_markup = KEYBOARD_CHOICE_USD)


    elif message.text == BUTTON_CRIPTA:
        BOT.send_message(message.chat.id, 'Какая информация нужна?', reply_markup = KEYBOARD_CHOICE_CRIPTA)   ###########

    elif message.text == BUTTON_GET_ALL_CRIP:
        BOT.send_message(message.chat.id, valuescrip.get_all_list_crip(), reply_markup = KEYBOARD_CHOICE_CRIPTA)

    elif message.text == BUTTON_GET_BIT:
        BOT.send_message(message.chat.id, valuescrip.get_bit_value(), reply_markup = KEYBOARD_CHOICE_CRIPTA)

    elif message.text == BUTTON_GET_ETH:
        BOT.send_message(message.chat.id, valuescrip.get_eth_value(), reply_markup = KEYBOARD_CHOICE_CRIPTA)

    elif message.text == BUTTON_GET_MONERO:
        BOT.send_message(message.chat.id, valuescrip.get_monero_value(), reply_markup = KEYBOARD_CHOICE_CRIPTA)

    elif message.text == BUTTON_GET_DOG:
        BOT.send_message(message.chat.id, valuescrip.get_dog_value(), reply_markup = KEYBOARD_CHOICE_CRIPTA)


    elif message.text == BUTTON_SP:
        BOT.send_message(message.chat.id, valuesp.get_all_list_sp(), reply_markup = KEYBOARD_START)


    elif message.text == BUTTON_START:
        start_message(message)

    else:
        BOT.send_message(message.chat.id, 'Я тебя не понимаю! Напиши пожалуйста /start')

BOT.polling()


