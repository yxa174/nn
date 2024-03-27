import logging  # Выводим лог на консоль и в файл
from datetime import datetime, timezone, timedelta  # Дата и время, временнАя зона, временной интервал
from time import time
import os.path

import pandas as pd

from FinamPy import FinamPy  # Работа с сервером TRANSAQ

from FinamPy.proto.tradeapi.v1.candles_pb2 import DayCandleTimeFrame, DayCandleInterval, IntradayCandleTimeFrame, IntradayCandleInterval
from google.type.date_pb2 import Date
from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.json_format import MessageToDict


logger = logging.getLogger('FinamPy.Bars')  # Будем вести лог. Определяем здесь, т.к. возможен внешний вызов ф-ии


# noinspection PyShadowingNames
def save_candles_to_file(fp_provider=FinamPy(),
                         security_board='TQBR', security_codes=('SBER',), intraday=False, time_frame=DayCandleTimeFrame.DAYCANDLE_TIMEFRAME_D1,
                         datapath=os.path.join('..', '..', 'Data', 'Finam', ''), delimiter='\t', dt_format='%d.%m.%Y %H:%M',
                         skip_first_date=False, skip_last_date=False, four_price_doji=False):
    """Получение бар, объединение с имеющимися барами в файле (если есть), сохранение бар в файл

    :param FinamPy fp_provider: Провайдер Finam
    :param str security_board: Код площадки
    :param tuple security_codes: Коды тикеров в виде кортежа
    :param bool intraday: Внутридневной интервал. Нужно указывать, т.к. DayCandleTimeFrame.DAYCANDLE_TIMEFRAME_D1 == IntradayCandleTimeFrame.INTRADAYCANDLE_TIMEFRAME_M1
    :param DayCandleTimeFrame|IntradayCandleTimeFrame time_frame: Временной интервал
    :param str datapath: Путь сохранения файла '..\\..\\Data\\Finam\\' - Windows, '../../Data/Finam/' - Linux
    :param str delimiter: Разделитель значений в файле истории. По умолчанию табуляция
    :param str dt_format: Формат представления даты и времени в файле истории. По умолчанию русский формат
    :param bool skip_first_date: Убрать бары на первую полученную дату
    :param bool skip_last_date: Убрать бары на последнюю полученную дату
    :param bool four_price_doji: Оставить бары с дожи 4-х цен
    """
    tf = fp_provider.finam_timeframe_to_timeframe(time_frame, intraday)  # Временной интервал для имени файла
    td = timedelta(days=(30 if intraday else 365))  # Максимальный запрос за 30 дней для внутридневных интервалов и 1 год (365 дней) для дневных и выше
    for security_code in security_codes:  # Пробегаемся по всем тикерам
        interval = IntradayCandleInterval(count=500) if intraday else DayCandleInterval(count=500)  # Нужно поставить максимальное кол-во бар. Максимум, можно поставить 500
        file_bars = None  # Дальше будем пытаться получить бары из файла
        file_name = f'{datapath}{security_board}.{security_code}_{tf}.txt'
        file_exists = os.path.isfile(file_name)  # Существует ли файл
        if file_exists:  # Если файл существует
            logger.info(f'Получение файла {file_name}')
            file_bars = pd.read_csv(file_name, sep=delimiter, parse_dates=['datetime'], date_format=dt_format, index_col='datetime')  # Считываем файл в DataFrame
            last_date: datetime = file_bars.index[-1]  # Дата и время последнего бара по МСК
            logger.info(f'Первый бар: {file_bars.index[0]}')
            logger.info(f'Последний бар: {last_date}')
            logger.info(f'Кол-во бар: {len(file_bars)}')
            next_bar_open_utc = fp_provider.msk_to_utc_datetime(last_date + timedelta(minutes=1), True) if intraday else \
                last_date.replace(tzinfo=timezone.utc) + timedelta(days=1)  # Смещаем время на возможный следующий бар по UTC
        else:  # Файл не существует
            logger.warning(f'Файл {file_name} не найден и будет создан')
            next_bar_open_utc = datetime(1990, 1, 1, tzinfo=timezone.utc)  # Берем дату, когда никакой тикер еще не торговался
        logger.info(f'Получение истории {security_board}.{security_code} {tf} из Finam')
        todate_utc = datetime.utcnow().replace(tzinfo=timezone.utc)  # Будем получать бары до текущей даты и времени UTC
        from_ = getattr(interval, 'from')  # Т.к. from - ключевое слово в Python, то получаем атрибут from из атрибута интервала
        to_ = getattr(interval, 'to')  # Аналогично будем работать с атрибутом to для единообразия
        first_request = not file_exists  # Если файл не существует, то первый запрос будем формировать без даты окончания. Так мы в первом запросе получим первые бары истории
        new_bars_list = []  # Список новых бар
        while True:  # Будем получать бары пока не получим все
            todate_min_utc = min(todate_utc, next_bar_open_utc + td)  # До какой даты можем делать запрос
            if intraday:  # Для интрадея datetime -> Timestamp
                from_.seconds = Timestamp(seconds=int(next_bar_open_utc.timestamp())).seconds  # Дата и время начала интервала UTC
                if not first_request:  # Для всех запросов, кроме первого
                    to_.seconds = Timestamp(seconds=int(todate_min_utc.timestamp())).seconds  # Дата и время окончания интервала UTC
                    if from_.seconds == to_.seconds:  # Если дата и время окончания интервала совпадает с датой и временем начала
                        break  # то выходим из цикла получения бар
            else:  # Для дневных интервалов и выше datetime -> Date
                date_from = Date(year=next_bar_open_utc.year, month=next_bar_open_utc.month, day=next_bar_open_utc.day)  # Дата начала интервала UTC
                from_.year = date_from.year
                from_.month = date_from.month
                from_.day = date_from.day
                if not first_request:  # Для всех запросов, кроме первого
                    date_to = Date(year=todate_min_utc.year, month=todate_min_utc.month, day=todate_min_utc.day)  # Дата окончания интервала UTC
                    if date_to == date_from:  # Если дата окончания интервала совпадает с датой начала
                        break  # то выходим из цикла получения бар
                    to_.year = date_to.year
                    to_.month = date_to.month
                    to_.day = date_to.day
            if first_request:  # Для первого запроса
                first_request = False  # далее будем ставить в запросы дату окончания интервала
            logger.debug(f'Запрос с {next_bar_open_utc} по {todate_min_utc}')
            response = (fp_provider.get_intraday_candles(security_board, security_code, time_frame, interval) if intraday else
                        fp_provider.get_day_candles(security_board, security_code, time_frame, interval))  # Получаем ответ на запрос бар
            if not response:  # Если в ответ ничего не получили
                return  # то возникла ошибка. Ее получим в логе FinamPy. Выходим, дальше не продолжаем
            response_dict = MessageToDict(response, including_default_value_fields=True)  # Переводим в словарь из JSON
            if 'candles' not in response_dict:  # Если бар нет в словаре
                logger.error(f'Ошибка при получении истории: {response_dict}')
                return  # то выходим, дальше не продолжаем
            new_bars_dict = response_dict['candles']  # Получаем все бары из Finam
            if len(new_bars_dict) > 0:  # Если пришли новые бары
                # Дату/время UTC получаем в формате ISO 8601. Пример: 2023-06-16T20:01:00Z
                # В статье https://stackoverflow.com/questions/127803/how-do-i-parse-an-iso-8601-formatted-date описывается проблема, что Z на конце нужно убирать
                first_bar_open_dt = fp_provider.utc_to_msk_datetime(datetime.fromisoformat(new_bars_dict[0]['timestamp'][:-1])) if intraday else\
                    datetime(new_bars_dict[0]['date']['year'], new_bars_dict[0]['date']['month'], new_bars_dict[0]['date']['day'])  # Дату и время первого полученного бара переводим из UTC в МСК
                last_bar_open_dt = fp_provider.utc_to_msk_datetime(datetime.fromisoformat(new_bars_dict[-1]['timestamp'][:-1])) if intraday else \
                    datetime(new_bars_dict[-1]['date']['year'], new_bars_dict[-1]['date']['month'], new_bars_dict[-1]['date']['day'])  # Дату и время последнего полученного бара переводим из UTC в МСК
                logger.debug(f'Получены бары с {first_bar_open_dt} по {last_bar_open_dt}')
                for new_bar in new_bars_dict:  # Пробегаемся по всем полученным барам
                    dt = fp_provider.utc_to_msk_datetime(datetime.fromisoformat(new_bar['timestamp'][:-1])) if intraday else \
                        datetime(new_bar['date']['year'], new_bar['date']['month'], new_bar['date']['day'])  # Дату и время переводим из UTC в МСК
                    open_ = round(int(new_bar['open']['num']) * 10 ** -int(new_bar['open']['scale']), int(new_bar['open']['scale']))
                    high = round(int(new_bar['high']['num']) * 10 ** -int(new_bar['high']['scale']), int(new_bar['high']['scale']))
                    low = round(int(new_bar['low']['num']) * 10 ** -int(new_bar['low']['scale']), int(new_bar['low']['scale']))
                    close = round(int(new_bar['close']['num']) * 10 ** -int(new_bar['close']['scale']), int(new_bar['close']['scale']))
                    volume = new_bar['volume']
                    new_bars_list.append({'datetime': dt, 'open': open_, 'high': high, 'low': low, 'close': close, 'volume': volume})
                last_bar_open_utc = fp_provider.msk_to_utc_datetime(last_bar_open_dt, True) if intraday else\
                    last_bar_open_dt.replace(tzinfo=timezone.utc)  # Дата и время открытия последнего бара UTC
                next_bar_open_utc = last_bar_open_utc + timedelta(minutes=1) if intraday else last_bar_open_utc + timedelta(days=1)  # Смещаем время на возможный следующий бар UTC
            else:  # Если новых бар нет
                next_bar_open_utc = todate_min_utc + timedelta(minutes=1) if intraday else todate_min_utc + timedelta(days=1)  # то смещаем время на возможный следующий бар UTC
            if next_bar_open_utc > todate_utc:  # Если пройден весь интервал
                break  # то выходим из цикла получения бар
        if len(new_bars_list) == 0:  # Если новых бар нет
            logger.info('Новых записей нет')
            continue  # то переходим к следующему тикеру, дальше не продолжаем
        pd_bars = pd.DataFrame(new_bars_list)  # Список новых бар -> DataFrame
        pd_bars.index = pd_bars['datetime']  # В индекс ставим дату/время
        pd_bars = pd_bars[['datetime', 'open', 'high', 'low', 'close', 'volume']]  # Отбираем нужные колонки. Дата и время нужна, чтобы не удалять одинаковые OHLCV на разное время
        logger.info(f'Первый бар: {pd_bars.index[0]}')
        logger.info(f'Последний бар: {pd_bars.index[-1]}')
        logger.info(f'Кол-во бар: {len(pd_bars)}')
        if not file_exists and skip_first_date:  # Если файла нет, и убираем бары на первую дату
            len_with_first_date = len(pd_bars)  # Кол-во бар до удаления на первую дату
            first_date = pd_bars.index[0].date()  # Первая дата
            pd_bars.drop(pd_bars[(pd_bars.index.date == first_date)].index, inplace=True)  # Удаляем их
            logger.warning(f'Удалено бар на первую дату {first_date}: {len_with_first_date - len(pd_bars)}')
        if skip_last_date:  # Если убираем бары на последнюю дату
            len_with_last_date = len(pd_bars)  # Кол-во бар до удаления на последнюю дату
            last_date = pd_bars.index[-1].date()  # Последняя дата
            pd_bars.drop(pd_bars[(pd_bars.index.date == last_date)].index, inplace=True)  # Удаляем их
            logger.warning(f'Удалено бар на последнюю дату {last_date}: {len_with_last_date - len(pd_bars)}')
        if not four_price_doji:  # Если удаляем дожи 4-х цен
            len_with_doji = len(pd_bars)  # Кол-во бар до удаления дожи
            pd_bars.drop(pd_bars[(pd_bars.high == pd_bars.low)].index, inplace=True)  # Удаляем их по условия High == Low
            logger.warning(f'Удалено дожи 4-х цен: {len_with_doji - len(pd_bars)}')
        if len(pd_bars) == 0:  # Если нечего объединять
            logger.info('Новых записей нет')
            continue  # то переходим к следующему тикеру, дальше не продолжаем
        logger.info(f'Первый бар: {pd_bars.index[0]}')
        logger.info(f'Последний бар: {pd_bars.index[-1]}')
        logger.info(f'Кол-во бар: {len(pd_bars)}')
        if file_exists:  # Если файл существует
            pd_bars = pd.concat([file_bars, pd_bars]).drop_duplicates(keep='last').sort_index()  # Объединяем файл с данными из Finam, убираем дубликаты, сортируем заново
        pd_bars = pd_bars[['open', 'high', 'low', 'close', 'volume']]  # Отбираем нужные колонки. Дата и время будет экспортирована как индекс
        logger.info(f'Сохранение файла ')
        pd_bars.to_csv(file_name, sep=delimiter, date_format=dt_format)
        logger.info(f'Первый бар: {pd_bars.index[0]}')
        logger.info(f'Последний бар: {pd_bars.index[-1]}')
        logger.info(f'Кол-во бар: {len(pd_bars)}')
        logger.info(f'В файл {file_name} сохранено записей: {len(pd_bars)}')


if __name__ == '__main__':  # Точка входа при запуске этого скрипта
    start_time = time()  # Время начала запуска скрипта
    fp_provider = FinamPy()  # Подключаемся ко всем торговым счетам
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Формат сообщения
                        datefmt='%d.%m.%Y %H:%M:%S',  # Формат даты
                        level=logging.DEBUG,  # Уровень логируемых событий NOTSET/DEBUG/INFO/WARNING/ERROR/CRITICAL
                        handlers=[logging.FileHandler('Bars.log'), logging.StreamHandler()])  # Лог записываем в файл и выводим на консоль
    logging.Formatter.converter = lambda *args: datetime.now(tz=fp_provider.tz_msk).timetuple()  # В логе время указываем по МСК

    security_board = 'TQBR'  # Акции ММВБ
    # security_codes = ('SBER', 'VTBR', 'GAZP', 'NMTP', 'LKOH', 'BSPB', 'FESH', 'ALRS', 'YNDX', 'BELU',
    #                   'GMKN', 'MTLR', 'HYDR', 'MAGN', 'SNGSP', 'NVTK', 'ROSN', 'TATN', 'SBERP', 'CHMF',
    #                   'MGNT', 'RTKM', 'TRNFP', 'MTSS', 'FEES', 'SNGS', 'NLMK', 'PLZL', 'RNFT', 'MOEX',
    #                   'DVEC', 'TGKA', 'MTLRP', 'RUAL', 'TRMK', 'IRAO', 'SMLT', 'AFKS', 'AFLT', 'PIKK')  # TOP 40 акций ММВБ
    security_codes = ('SBER',)  # Для тестов
    # security_board = 'FUT'  # Фьючерсы
    # security_codes = ('SiH4', 'RIH4')  # Формат фьючерса: <Тикер><Месяц экспирации><Последняя цифра года> Месяц экспирации: 3-H, 6-M, 9-U, 12-Z

    skip_last_date = True  # Если получаем данные внутри сессии, то не берем бары за дату незавершенной сессии
    # skip_last_date = False  # Если получаем данные, когда рынок не работает, то берем все бары
    save_candles_to_file(fp_provider, security_board, security_codes, four_price_doji=True, skip_last_date=skip_last_date)  # Дневные бары
    # save_candles_to_file(fp_provider, security_board, security_codes, True, IntradayCandleTimeFrame.INTRADAYCANDLE_TIMEFRAME_H1, skip_last_date=skip_last_date)  # Часовые бары
    # save_candles_to_file(fp_provider, security_board, security_codes, True, IntradayCandleTimeFrame.INTRADAYCANDLE_TIMEFRAME_M15, skip_last_date=skip_last_date)  # 15-и минутные бары
    # save_candles_to_file(fp_provider, security_board, security_codes, True, IntradayCandleTimeFrame.INTRADAYCANDLE_TIMEFRAME_M5, skip_last_date=skip_last_date)  # 5-и минутные бары
    # save_candles_to_file(fp_provider, security_board, security_codes, True, IntradayCandleTimeFrame.INTRADAYCANDLE_TIMEFRAME_M1, skip_last_date=skip_last_date, four_price_doji=True)  # Минутные бары

    fp_provider.close_channel()  # Закрываем канал перед выходом

    logger.info(f'Скрипт выполнен за {(time() - start_time):.2f} с')
