import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from config_reader import config
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from modules.binance_currency import get_binance_currency
from modules.binance_rates import get_binance_rate
from modules.binance_p2p import get_p2p_rate, p2p_command_list
from modules.cb_rates import get_cb_rate
from modules.cb_currency import get_cb_currency
from modules.mos_rates import mos_command_list, get_mos_byn, get_mos_cny, get_mos_usd, get_mos_try, get_mos_eur
from modules.tinkoff_currency import get_tinkoff_currency
from modules.tinkoff_rates import get_tinkoff_rate
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value()) # Объект бота
dp = Dispatcher() # Диспетчер


# Хэндлер на команду /start
@dp.message(commands=["start"])
async def cmd_start(message: types.Message):
    buttons = [
        [types.KeyboardButton(text='💎 Курс критптовалюты Binance')],
        [types.KeyboardButton(text='💸 Курс на P2P Binance')],
        [types.KeyboardButton(text='💰 Курс МосБиржи')],
        [types.KeyboardButton(text='💰 Курс Тинькофф')],
        [types.KeyboardButton(text='💰 Курс ЦБ РФ')],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=buttons)
    await message.answer("Привет! Я бот бот от студентов HSE, который может помочь тебе быстро отследить крус разной инсторанной валюты и криптовалюты", reply_markup=keyboard)

@dp.message(content_types="text")
async def process_menu(message: types.Message):
    if message.chat.type == 'private':
        if message.text == '◀️Назад':
            buttons = [
                [types.KeyboardButton(text='💎 Курс критптовалюты Binance')],
                [types.KeyboardButton(text='💸 Курс на P2P Binance')],
                [types.KeyboardButton(text='💰 Курс МосБиржи')],
                [types.KeyboardButton(text='💰 Курс Тинькофф')],
                [types.KeyboardButton(text='💰 Курс ЦБ РФ')],

            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=buttons)
            await message.answer(
                 'Выберите действие',
                reply_markup=keyboard)
        elif (message.text == '💎 Курс критптовалюты Binance'):
            builder = ReplyKeyboardBuilder()
            builder.add(types.KeyboardButton(text=str('◀️Назад')))
            await bot.send_message(message.chat.id, '🕑 Загружаю курсы',
            reply_markup=builder.as_markup(resize_keyboard=True))
            for i in get_binance_currency.create_symbols_list():
                builder.add(types.KeyboardButton(text=str(i)))
            builder.adjust(2)
            await bot.send_message(message.chat.id, 'Выберете криптовалюту', reply_markup=builder.as_markup(resize_keyboard=True))
        elif (message.text == '💸 Курс на P2P Binance'):
            builder = ReplyKeyboardBuilder()
            builder.add(types.KeyboardButton(text=str('◀️Назад')))
            await bot.send_message(message.chat.id, '🕑 Загружаю курсы',
                                   reply_markup=builder.as_markup(resize_keyboard=True))
            for i in p2p_command_list:
                builder.add(types.KeyboardButton(text=str(i['name'])))
            builder.adjust(1)
            await bot.send_message(message.chat.id, 'Выберете вариант', reply_markup=builder.as_markup(resize_keyboard=True))
        elif (message.text == '💰 Курс ЦБ РФ'):
            builder = ReplyKeyboardBuilder()
            builder.add(types.KeyboardButton(text=str('◀️Назад')))
            await bot.send_message(message.chat.id, '🕑 Загружаю курсы',
                                   reply_markup=builder.as_markup(resize_keyboard=True))
            for i in get_cb_currency.create_currency_list():
                builder.add(types.KeyboardButton(text=str(i)))
            builder.adjust(1)
            await bot.send_message(message.chat.id, 'Выберете вариант',
                                   reply_markup=builder.as_markup(resize_keyboard=True))
        elif (message.text == '💰 Курс Тинькофф'):
            builder = ReplyKeyboardBuilder()
            builder.add(types.KeyboardButton(text=str('◀️Назад')))
            await bot.send_message(message.chat.id, '🕑 Загружаю курсы',
                                   reply_markup=builder.as_markup(resize_keyboard=True))
            for i in get_tinkoff_currency.create_currency_list():
                builder.add(types.KeyboardButton(text=str(i['method']+' '+i['currency'])))
            builder.adjust(1)
            await bot.send_message(message.chat.id, 'Выберете вариант',
                                   reply_markup=builder.as_markup(resize_keyboard=True))


        elif (message.text == '💰 Курс МосБиржи'):
            builder = ReplyKeyboardBuilder()
            builder.add(types.KeyboardButton(text=str('◀️Назад')))
            await bot.send_message(message.chat.id, '🕑 Загружаю курсы',
                                   reply_markup=builder.as_markup(resize_keyboard=True))
            for i in mos_command_list:
                builder.add(types.KeyboardButton(text=str(i['name'])))
            builder.adjust(1)
            await bot.send_message(message.chat.id, 'Выберете вариант',
                                   reply_markup=builder.as_markup(resize_keyboard=True))

        for i in get_tinkoff_currency.create_currency_list():
            if (message.text == i['method']+' '+i['currency']):
                res = get_tinkoff_rate.create_rate_list(i['currency'])
                await message.answer(res)


        for i in mos_command_list:
            if (message.text == i['name']):
                if (message.text == 'МосБиржа USD'):
                    res = get_mos_usd.create_rate_list()
                    await message.answer(res)
                if (message.text == 'МосБиржа EUR'):
                    res = get_mos_eur.create_rate_list()
                    await message.answer(res)
                if (message.text == 'МосБиржа TRY'):
                    res = get_mos_try.create_rate_list()
                    await message.answer(res)
                if (message.text == 'МосБиржа CNY'):
                    res = get_mos_cny.create_rate_list()
                    print(res)
                    await message.answer(res)
                if (message.text == 'МосБиржа BYN'):
                    res = get_mos_byn.create_rate_list()
                    await message.answer(res)
        for i in get_cb_currency.create_currency_list():
            if (message.text == i):
                response = get_cb_rate.create_rate_list(message.text)
                await message.answer(response)
        for i in p2p_command_list:
            if (message.text == i['name']):
                response = get_p2p_rate.create_rate_list(message.text)
                await message.answer(response)
        for i in get_binance_currency.create_symbols_list():
            if (message.text == i):
                response = get_binance_rate.create_rate_list(message.text)
                await message.answer(
                    response)






# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())