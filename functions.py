import requests
import random
import re
from config import male_names, female_names
import base64
import time

def get_cookies_from_cart():
    """
    Заходит на страницу корзины https://ylilit.ru
    и выводит все cookies, полученные от сайта.
    """
    url = "https://ylilit.ru"

    # Создаём сессию (чтобы cookies сохранялись)
    session = requests.Session()


    # Выполняем GET-запрос
    response = session.get(url)

    # Проверяем успешность запроса
    response.raise_for_status()

    if session.cookies:
        for name, value in session.cookies.items():
            cookie = session.cookies.get_dict().get(name)
            # Получаем дополнительные атрибуты, если доступны
            jar = session.cookies
            for c in jar:
                cookie_vaulue = c.value

    return cookie_vaulue.split("-")[-1]

def get_wp_nonce():

    # 1. Define the URL
    url = "https://ylilit.ru"

    pattern_lengh = 192

    # 2. Send an HTTP GET request to the URL
    response = requests.get(url)

    # 3. Check if the request was successful (optional but recommended)
    if response.status_code == 200:
        # 4. Access the page content as a string (decoded Unicode)
        page_content_text = response.text

        for i in page_content_text.split(" "):
            pattern = r'src="data:text/javascript;base64,([^"]+)"></script>'
            match = re.search(pattern, i)
            if match:
                base64_str = match.group(1)
                if len(base64_str) == pattern_lengh:

                    decoded_bytes = base64.b64decode(base64_str)
                    decoded_text = decoded_bytes.decode('utf-8')

                    decoded_text2 = decoded_text.replace('/* <![CDATA[ */','')
                    decoded_text2 = decoded_text2.replace('//# sourceURL=cart-js-extra','')
                    decoded_text2 = decoded_text2.replace('/* ]]> */','')
                    decoded_text2 = decoded_text2.strip()

                    pattern2 = r'var dataAjax = {"url":"https://ylilit.ru/wp-admin/admin-ajax.php","nonce":"(.*)"};'
                    match2 = re.search(pattern2, decoded_text2)
                    if match2:
                        nonce = match2.group(1)
                        return nonce


def generate_phone_number():
    # Генерируем случайные числа для телефона
    operator_code = random.choice([910, 911, 915, 980, 989,  920, 922, 923, 924, 925, 926,
                                   927, 928, 929, 930, 939, 999, 903, 905, 906, 909, 960,
                                   961, 962, 963, 967, 900, 901, 902, 904, 908, 950, 953,
                                   977, 995, 996])  # Пример операторских кодов
    part1 = random.randint(100, 999)
    part2 = random.randint(10, 99)
    part3 = random.randint(10, 99)

    # Формируем номер телефона
    phone_number = f"+7 ({operator_code}) {part1}-{part2}-{part3}"

    return phone_number

# Make dish list
def make_menu():
    menu = {}

    with open('data2.txt', encoding='utf8') as src:
        for str1 in src:

            if 'data-id' in str1:
                data_id = str1.strip().split('=')[1].replace("\"","")
                menu[data_id] = []

            if 'data-name' in str1:
                data_name = str1.strip().split('=')[1].replace("\"","")
                menu[data_id].append(data_name)

            if 'data-heft' in str1:
                data_heft = str1.strip().split('=')[1].replace("\"","")
                menu[data_id].append(data_heft)

            if 'data-img' in str1:
                data_img = str1.strip().split('=')[1].replace("\"","")
                menu[data_id].append(data_img)

            if 'data-price' in str1:
                match = re.search(r'data-price="(\d+)"', str1)
                data_price = match.group(1)
                menu[data_id].append(data_price)
    return menu

# Function generates random email
def generate_random_email():
    """
    Генерирует реалистичный случайный email с осмысленным логином,
    похожим на имя/фамилию человека.
    Домены: mail.ru, gmail.com, yandex.ru, rambler.ru, list.ru, vk.com, yahoo.com
    """

    # Популярные русские и международные имена
    first_names = [
        "alex", "alexander", "alexandra", "andrey", "anna", "artem", "dmitry",
        "ekaterina", "elena", "ivan", "maria", "maxim", "mikhail", "natalia",
        "nikita", "olga", "pavel", "roman", "sergey", "svetlana", "victor",
        "vladimir", "yulia", "denis", "evgeny", "irina", "kirill", "oksana",
        "stepan", "tatyana", "viktoriya", "john", "mike", "david", "james",
        "emma", "sophia", "olivia", "liam", "noah"
    ]

    # Популярные русские и международные фамилии (в транслите)
    last_names = [
        "ivanov", "petrov", "sidorov", "smirnov", "kuznetsov", "popov",
        "vasilyev", "sokolov", "mikhaylov", "novikov", "fedorov", "morozov",
        "volkov", "alekseev", "lebedev", "semenov", "egorov", "pavlov",
        "kozlov", "stepanov", "nikolaev", "orlov", "andreev", "makarov",
        "nikitin", "zakharov", "zaytsev", "solovev", "borisov", "yakolev",
        "smith", "johnson", "williams", "brown", "jones", "garcia", "miller",
        "davis", "rodriguez", "martinez", "hernandez", "lopez"
    ]

    domains = [
        "mail.ru", "gmail.com", "yandex.ru", "rambler.ru",
        "list.ru", "vk.com", "yahoo.com"
    ]

    # Варианты формирования логина
    choice = random.choice([
        # Просто имя
        lambda: random.choice(first_names),

        # Просто фамилия
        lambda: random.choice(last_names),

        # Имя.Фамилия
        lambda: f"{random.choice(first_names)}.{random.choice(last_names)}",

        # Фамилия.Имя
        lambda: f"{random.choice(last_names)}.{random.choice(first_names)}",

        # Имя_Фамилия
        lambda: f"{random.choice(first_names)}_{random.choice(last_names)}",

        # Имя + цифры (год рождения или случайные)
        lambda: f"{random.choice(first_names)}{random.randint(1970, 2005)}",

        # Инициалы + фамилия (например, a.ivanov)
        lambda: f"{random.choice(first_names)[0]}.{random.choice(last_names)}",

        # Фамилия + цифры
        lambda: f"{random.choice(last_names)}{random.randint(10, 999)}",

        # Имя + короткая цифра в конце
        lambda: f"{random.choice(first_names)}{random.randint(1, 99):02d}",
    ])

    local_part = choice().lower()  # Всегда в нижнем регистре

    domain = random.choice(domains)

    return f"{local_part}@{domain}"
def random_russian_name():
    """
    Возвращает случайное русское имя (мужское или женское).
    """
    all_names = male_names + female_names

    return random.choice(all_names)

def get_random_yaroslavl_address():
    """
    Возвращает случайный адрес в г. Ярославль, Россия.
    Список состоит из 200 уникальных сгенерированных адресов.
    """
    streets = [
        "Ленина", "Свободы", "Кирова", "Советская", "Московская", "Толбухина", "Республиканская", "Большая Октябрьская",
        "Ушинского", "Чайковского", "Некрасова", "Гагарина", "Победы", "Первомайская", "Волкова", "Фрунзе",
        "Свердлова", "Титова", "Комсомольская", "Яковлевская", "Депутатская", "Нахимсона", "Революционная",
        "Трефолева", "Чкалова", "Белинского", "Добролюбова", "Гоголя", "Пушкина", "Тургенева", "Лермонтова",
        "Маяковского", "Есенина", "Блока", "Андропова", "Строителей", "Автозаводская", "Тутаевское шоссе",
        "Ленинградский проспект", "Московский проспект", "Фрунзенская", "Доронина", "Суздальская", "Костромская",
        "Рыбинская", "Угличская", "Даниловская", "Пошехонская", "Гаврилов-Ямская", "Большая Федоровская",
        "Малая Федоровская", "Носкова", "Павлика Морозова", "Загородный сад", "Богдановича", "Салтыкова-Щедрина"
    ]

    districts = ["Кировский район", "Ленинский район", "Фрунзенский район", "Заволжский район", "Дзержинский район",
                 "Красноперекопский район"]

    #prefixes = ["ул.", "пр-кт", "пер.", "пл.", "б-р"]
    prefixes = ["ул."]

    # Генерация 200 уникальных адресов (один раз при первом вызове)
    if not hasattr(get_random_yaroslavl_address, "addresses"):
        addresses = set()
        while len(addresses) < 200:
            street_name = random.choice(streets)
            prefix = random.choice(prefixes)
            if prefix == "ул.":
                full_street = f"{prefix} {street_name}"
            elif prefix == "пр-кт":
                full_street = f"{prefix} {street_name}"
            elif prefix == "б-р":
                full_street = f"бульвар {street_name}"
            elif prefix == "пл.":
                full_street = f"площадь {street_name}"
            else:
                full_street = f"{prefix} {street_name}"

            house = random.randint(1, 45)
            house_str = str(house)
            if random.random() < 0.3:  # Корпус/строение/литер
                corpus = random.choice(["к", "стр", "литер"]) + random.choice(["1", "2", "3", "4", "А", "Б"])
                house_str += corpus

            if random.random() < 0.5:  # Квартира
                apt = random.randint(1, 300)
                house_str += f", кв. {apt}"

            district = random.choice(districts)

            address = f"{full_street}, д. {house_str}"
            addresses.add(address)

        get_random_yaroslavl_address.addresses = list(addresses)

    # Возврат случайного адреса из списка
    return random.choice(get_random_yaroslavl_address.addresses)

# def generate_email(name: str):
#     # Трансляция имени на латиницу
#     name_lat = translit(name, 'ru', reversed=True)
#
#     # Генерация случайного года рождения в диапазоне от 1960 до 2005
#     birth_year = random.randint(1960, 2005)
#
#     # Список доступных доменов
#     domains = ['mail.ru', 'gmail.com', 'yandex.ru', 'rambler.ru', 'list.ru', 'vk.com', 'yahoo.com']
#
#     # Генерация случайного домена
#     domain = random.choice(domains)
#
#     # Формирование email-адреса
#     email = f"{name_lat.lower()}{birth_year}@{domain}"
#
#     return email

def get_token():

    # 1. Define the URL
    url = "https://ylilit.ru/cart"


    # 2. Send an HTTP GET request to the URL
    response = requests.get(url)

    # 3. Check if the request was successful (optional but recommended)
    if response.status_code == 200:
        # 4. Access the page content as a string (decoded Unicode)
        page_content_text = response.text

        for i in page_content_text.split(" "):
            pattern = r'sitekey="(.*)"'
            match = re.search(pattern, i)
            if match:
                token_str = match.group(1)
                return token_str

