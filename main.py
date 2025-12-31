import requests
import json
import random
from config import headers, my_cookies, url
from functions import get_wp_nonce, generate_phone_number, make_menu, generate_random_email
from functions import random_russian_name, get_random_yaroslavl_address, get_cookies_from_cart


def run_task(wp_nonce_code):

    # Get new Word press once code
    nonce_code = wp_nonce_code


    cart = {"cart[4637]": [3, "https://ylilit.ru/wp-content/uploads/2023/11/Kebab-v-lavashe.webp", "300",
                        "Кебаб с тертым сыром в лаваше .(Фирменное блюдо)", "385"]}

    cart_json = json.dumps(cart,ensure_ascii=False)

    # Get random name
    name = random_russian_name()
    # Get random phone number
    phone = generate_phone_number()
    # Get random email
    email = generate_random_email()
    # Get random address
    address = get_random_yaroslavl_address()

    token = '0cAFcWeA5hxLxKPQpqlzJ7WFDMJ-TLMVVnU9SkwvL0LmbiJrf5Poo6U0DAi-FhPTRN1zLLiBYVOhxu63ayFKr56XG14KQHP-Apb2hqHSYe_A4CFwlSEpv2XV0ZgA_HnHuSuwIjblPwaFd2vm9MB24tYzfKr_SdYVpr_Bu2db1sn342aqnZja-iL3iRQSXNj_ZzSUZYFfejVrv4aJ7hY5rgpmUTKbtw5why10KMShvqrU5Xv5fCQN_NWOe6YYcMNjp-Ju8njQoI-qk3-Hjxb0cO_yo6fTdSMVIz6no_gpV5uW7BSRzxfhnGxK46drw9KnoHmxniO7i0CTrgx1-xm6KfnUZk92DkBBBu00Bxp1fpxGfHsofBEYz9dl4PLhMHsbJ_ZmmUoAXZ3D36-VaMpkGO3vN8esYVrsIQE5c4qyFuo14rjm_QBprSAZlPG8iwAkdpEqPBR8sGoymEhh1zgWqj14Nv0mVKokiI0i3Mjzb0Z2kDkPcs2vF-0sNLqm23Qm3p4jpqHHH8PTQqcT-hU5Ord6s_pojSE5J5Qd7tCoOv1Le2wpeY-0hTHZE5udOMps4xa8SMJ1Jd0gET7eH7oV2K1eEksunuhs-ojmgCXiLihetHELgRfRvpHtRzAF9sBqIIqKbt-6F1uUL9JdjCNl84fhDjETvHjMTxj5rwmtiR4zyr5ZYC3eeLOcz8p_RXUYofD4S2-52Hh2UzOS8v9ETEmIIO2LdOWMtin85reaNYdXanmj9HAwzZKaKlDgSed5X1QQZ1rfj1NNL1NrQQLESujqQb_CzfT86kaQXdeSiVOXHgeNcKdbBZdCFRg-medzWGWYXpO4W1vBTuOV40GCF6TZiujzt3O-Dte2m9cwtxvNNM4HBExI6e71TvXg7UOb1XlIi9SMO6lQ0QmtazOl5e76ZLhre1-FbrryvUa-REw0_GpFtz1_KSu0w2iJPSMXRMmEWAbGEE4tuYfAY5oA0zOp08iCqIesgFNAL88lQRMMwESPosXtjRs6LM1xfSriImgVkAPWzpBfivYXuzwyXBVAp4Pjr59ImpgnO3M1PXsTkASSF5zdX4RB2eM7knNIQ4mVvuVE3pKw_qZA0XpWe1hZry5JibbQYf_dSMQReqlFqfVj69VDBkJ2qzGfM7ll3rFm3Yrfb_mf2QTbRJwgbmEWdNvaBq_SZoNthLjJa1M7wLsQzZFNtYPvM-1WpwVznj-aQpWWYw56JjTowf5_fzq-UXVLS9XrHokGXzdapeeIiXp4QnnbmhrcYAkjWqRj2bYWDFV0W7ahAEU8ES-MJUGL5tsh6w6_hpsQkW9wVZdnvgDFuHG-7I7RwONyXty5EQ8ILDVK8dXKI2_0MO1wuL6eE2XtfaQjNOCMRwexWo0SkO9ikTTaN7lMSKGSjH8UPKi3PRQso414B7DZm-ot7yN6wH6ASHBXs4K5Kmp_hyW1-1rR6XagMMEWAVVp_tEAJXD5Oml_gVyOpA-yXZyLT8Xc5C9b_k6W1rbEpOZ0lV3SzuqBn5i0QdyzxF2ygbWYLxf4uV4t9PEySdE8JI-lE_Yci_diSBT85HMb3s6ye3ejmfAWod2Pmi0mtfikTxOWir4lluxsueMH22g7PwVmQWNNLM9r9vNI1RxqsVGnpKLBV7CPD0NntzkK0e6EDS7qcdN7DjpUSBheQPrR68T6sZuT3VJct-JrvG7ig08WRsKNe15qAWgSBjvjblfx4QkFfqGNmr36B85UP2WFsyJ1hFC5GOU0so-HojMw'

    # Form new order
    data = {
        'action': 'sendCart',
        'name': f'{name}',
        'tel': f'{phone}',
        'email': f'{email}',
        'adress': f'{address}',
        'nonce_code': nonce_code,
        'cart': cart_json,
        '\'g-recaptcha-response\'': token
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

nonce_code = get_wp_nonce()
run_task(nonce_code)

