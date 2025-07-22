import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    # 1. Геттеры для name_items и number_items
    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    # 2. Добавление товара в чек
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        self.__name_items.append(name)
        self.__number_items += 1

    # 3. Удаление товара из чека
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

    # 4. Подсчёт общей стоимости товаров
    def check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price[item])
        total_sum = sum(total)
        if self.__number_items > 10:
            total_sum *= 0.9
        return total_sum

    # 5. Расчёт НДС для товаров со ставкой 20%
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)

        total = []
        for item in twenty_percent_tax:
            total.append(self.__item_price[item])

        total_sum = sum(total)
        if self.__number_items > 10:
            total_sum *= 0.9
        return total_sum * 0.2

    # 6. Расчёт НДС для товаров со ставкой 10%
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)

        total = []
        for item in ten_percent_tax:
            total.append(self.__item_price[item])

        total_sum = sum(total)
        if self.__number_items > 10:
            total_sum *= 0.9
        return total_sum * 0.1

    # 7. Расчёт общей суммы налогов
    def total_tax(self):
        return self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()

    # 8. Получение номера телефона покупателя
    @staticmethod
    def get_telephone_number(telephone_number):
        try:
            number_int = int(telephone_number)
        except:
            raise ValueError('Необходимо ввести цифры')

        number_str = str(number_int)
        if len(number_str) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f'+7{number_str}'

    # *9. Получение даты и времени покупки
    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        date = [
            ['часы', lambda x: x.hour],
            ['минуты', lambda x: x.minute],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year],
        ]
        for item in date:
            date_and_time.append(f'{item[0]}: {item[1](now)}')
        return date_and_time