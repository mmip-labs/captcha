import requests
import json
from config import headers, my_cookies, url
from functions import get_cookies_from_cart


def run_task(wp_nonce_code, token):

    # Get new Word press once code
    nonce_code = wp_nonce_code


    cart = {"cart[4637]": [3, "https://ylilit.ru/wp-content/uploads/2023/11/Kebab-v-lavashe.webp", "300",
                        "Кебаб с тертым сыром в лаваше .(Фирменное блюдо)", "385"]}

    cart_json = json.dumps(cart,ensure_ascii=False)

    # Get random name
    name = '123'
    # Get random phone number
    phone = '+7 (962) 211-79-79'
    # Get random email
    email = 'email@mail.com'
    # Get random address
    address = 'address'

    # Form new order
    data = {
        'action': 'sendCart',
        'name': f'{name}',
        'tel': f'{phone}',
        'email': f'{email}',
        'adress': f'{address}',
        'nonce_code': nonce_code,
        'cart': cart_json,
        'g-recaptcha-response': token
    }

    not_bot_cooke = get_cookies_from_cart()
    my_cookies['icwp-wpsf-notbot'] = f'notbotZaltchaZexp-{not_bot_cooke}'


    #print(my_cookies)
    # print(name, phone, email, address, dish_name, dish_value, dish_price, nonce_code)
    print(data)


    # Make request and get responce
    try:
        responce = requests.post(url, headers=headers, cookies=my_cookies, data=data, timeout=20)
    except:
        print("Connection error...")
    else:
        print(responce.status_code, responce.text)
        print()

