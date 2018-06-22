import requests
import argparse


def create_parser():
    """
    Функция, реализующая утилиту командной строки и принимающая два аргумента валюту и сумму в USD
    :return: parser
    """
    input_parser = argparse.ArgumentParser(description='Утилита командной строки '
                                                       'для обработки кода валюты и суммы в USD')
    input_parser.add_argument('currency', default='UAH',
                        help='Введите код одной из трех валют: UAH, EUR, GBP')
    input_parser.add_argument('sum', default=0,
                        help='Укажите сумму в USD, которую необходимо конвертировать'
                             ' в виде целого или дробного (через точку) числа')
    return input_parser


def convert_currency(cost, code):
    """
    Функция принимает сумму в USD и валюту, в которую нужно конвертировать (тип string).
    Функция запрашивает актуальный курс валют со стороннего сервиса (https://free.currencyconverterapi.com).
    Функция возвращает цену в нужной валюте и/ или ошибку.
    """
    in_currency = 'USD'

    pair_currency = in_currency + '_' + code

    url = "https://free.currencyconverterapi.com/api/v5/convert"
    query_params = {'q': pair_currency,
                    'compact': 'ultra'}
    response = requests.get(url, params=query_params)
    exchange_rate = response.json()[pair_currency]
    calculation = float(cost) * exchange_rate
    result = float(f'{calculation:.{2}f}')

    return result


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    code_currency = args.currency
    sum_in_USD = args.sum


try:
    out = convert_currency(sum_in_USD, code_currency)
    print(f'Цена за товар ({args.sum} USD) по актуальному курсу обмена составляет {out} {code_currency}')
except ImportError:
    print('У Вас не установлен модуль requests, обратитесь за справкой '
          'http://docs.python-requests.org/en/master/user/install/#pipenv-install-requests')
except (KeyError, NameError):
    print('Проверьте правильность введеного Вами кода валюты!'
          ' Должен быть один из следующих вариантов: UAH, EUR, GBP')
except (TypeError, ValueError):
    print('Проверьте правильность указания суммы валюты в USD, должно быть указано число; '
          ' возможно Вы поставили запятую вместо точки в дробном значении суммы;'
          ' либо Вы указали более двух аргументов')
