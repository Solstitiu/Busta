import requests
import json
from copy import deepcopy
from bs4 import BeautifulSoup as bsoup
from urllib.request import urlopen as req
from urllib.request import Request
import urllib.request
import re
from discord_webhook import DiscordWebhook
import time

'''
Nike sb dunk
Jordan 1 high 
Jordan 1 mid
Jordan 1 low
Jordan 4 
Jordan 5
Yeezy 350
Yeezy 700
'''

sent = ["a"]
already = []

tike_token = 'https://discord.com/api/webhooks/805760747841257503/Sff7Q262gGbA89nmX0LfzX3APCzwgfO4Q5cQqDexFyn-94Bw3O85d5uxqRpHypJJLXTL'
rap_city_token = 'https://discord.com/api/webhooks/805769376007323659/SrmOIOi9XPAfxGM_HnmA6J7-IdcJShnfLne-HrRQ4UYoCj1BdC4ZHChOicR_cPi9ADrY'
sport_select_token = 'https://discord.com/api/webhooks/805886568950136833/Q6dERRbOaKXkKfb2XaQacsLGlHqw3ij_ZzuPp-WOHbN4hkhgh4OMuQ1wWi4cXGAGPEOj'
sneaker_industry_token = 'https://discord.com/api/webhooks/805892673763934278/-L8-nEaIcG8VPhRYeDmp-8nck28rSmz3S5_Z0dLehxTRZpZRNMsXS85IfSXcvQmLrutT'
u_man_token = 'https://discord.com/api/webhooks/816009839044984913/1jLjvKbm-dVGyb2mr5Si6Cg0yQu0D_Lk-BAKs4TuoJuqBXfyQWJ8qOJqQAlICaMQ-YA_'
buzz_token = 'https://discord.com/api/webhooks/816061924839260220/ySXgHYwlptPQ0YA_CRIjeDUVmk6MwsyU1fbkf0GQnwzYuqJ0s1JeWash7BFLnrZzouws'
bodo_token = 'https://discord.com/api/webhooks/816062293996863509/lQ2maNTglJ0iPKnS7aSutLlMoGNuKYcXIi-0wAgaXjejdK-USqX5EdLX1xjfUBSwX80l'
superstep_token = 'https://discord.com/api/webhooks/816062705983160392/MIG8GQOOVBBw9bEvRhzCsu2jFz-KiUPK2yrHBuu1RWh4vFaVceR1Ir2MgZdRGVQltBNk'
grid_token = 'https://discord.com/api/webhooks/816063064859475998/PJbHciMXMXjN1IKGfuCTDbf0POJaKDS5EGXt6J3AfoZt9hXIECNwHpgDolN3TdX7HlGE'
dunk_token = 'https://discord.com/api/webhooks/816063505371103302/TtN55iE8DklYwPzWPGsqE3RlIXHWo2RCm6-jYfnTNjMty92vqGRvFtNq2y9MmANAoE1Q'
world_token = 'https://discord.com/api/webhooks/816063824154329149/bqiZOhSYB75nRbUrX72fEEgXZ4aR2N6L7VFNVDYjAxsyttYz2WK17U7I_Ranvft0Yrt3'
bstn_token = 'https://discord.com/api/webhooks/816064113632477184/Gqei9JNDoZWsz4ToO_xamYNFI7_MGMEvuhgEv_nb7yZD7ZL18tvc73Mb16EMzI14qNXu'
vitak_token = 'https://discord.com/api/webhooks/816069210040041472/NouyKgtJ583WOofhKOiP5qXdM2WLkK5nJeVJNkKrF9q2NtzMdPSAzWQrgXwQwlp2DqP0'
impact_token = 'https://discord.com/api/webhooks/816069521563582494/Y9grBQEqluQcHF5TMXQDfX2UZkiHqXiu7anBv69OwBBRrqJsaK7S-6L2WFOjlX3-SQ-d'
horn_token = 'https://discord.com/api/webhooks/816069813335097426/r1pA0Na7dBrnnMYUraHzpLBD1XA4t-7eT43E1sp7oaqJJBiE9pb0vd-PVWoIk6YgHeqd'
queensG_token = 'https://discord.com/api/webhooks/816070325339029515/Kjfr78OD2U2b0e6HAuE6YgLMS-7PvkPLni_45454-8tRjdlfMisaZ34u18vjHWHwvV2j'
queenscz_token = 'https://discord.com/api/webhooks/816070622324719627/WxUD3bRUa-FdH2i-7T5vGEWcZDjw8fb9fI6Be30tH9jpMSOZjOX1dZIP6tG_p91dEjam'
noss_token = 'https://discord.com/api/webhooks/816070764766691338/pKK-ZsaWVrZ6FIE10LTfDRIkcK9-DPP4O936cWLtDcsvqrY8MQp0RJKiqLMSaJxqqG3y'
basket_token = 'https://discord.com/api/webhooks/816071015918338069/8lcxDPILtZzIX6ejs1wKcG7use0IhS7WW0Jyg2GgM_HCuZJ7b15a6jLN24rucYLELKGU'
nigra_token = 'https://discord.com/api/webhooks/816071355271086141/1y7eM2dfDDOM8TmJikG2ZPP2LsTtNmleOHU7aoxlj-FRRaO8pjD4apd4_jCVe3hM5Z7r'
streets_token = 'https://discord.com/api/webhooks/816072016977330177/rBjtssO-wyGKf26LDRKkj4tBVVHQU1zc6i1TMs_K_tXJOU8ShS_hGMzbkPgQGj5weSgV'
sneak_token = 'https://discord.com/api/webhooks/816072245348401172/76O2msbfXv8L2L3_XyIudXLYeASUKryUFlae7XuP4L0_XM1PI1vlj-vZ56h3kpzJG6sm'
shoe_token = 'https://discord.com/api/webhooks/816074383332212806/pIuMQaFlIZpVb7jmsIF_wdWo8NSy86sktZLXea6nxwW2z9bKZrbUNM1T3Ty3r6hMbAtw'
skate_token = 'https://discord.com/api/webhooks/816074720050282567/EWxmFIFiEVRErpsUbAuv-yXdV315bA85krI9VIkSTH2KK9Qus1nYVkxMcvJfOAmtsYyj'
shelta_token = 'https://discord.com/api/webhooks/816075204525948939/svpzMR4NXF7ATkIMDM7QWxELWYRH3bxx3LFv4I8iOOrfeOZHSfC8T4jmUSlSY6Xh436I'
slam_token = 'https://discord.com/api/webhooks/816395349794488360/5AY0YfNL7mNRqDwUbM6BSuqv3qP0aKrkKcsPuw681hJZ-qfY50ADTM84iFbnn_NEA600'
segos_token = 'https://discord.com/api/webhooks/816622169965723668/CQ6kpqbfwzLZ1hmXvcrb3xTu9xQI2Ys93HwvN5s-E374qk6cYtAZH2a6P1inF3Lx-rIe'
colective_token = 'https://discord.com/api/webhooks/816624308771094548/94o0SOxwLws5idLW7W6aJ8NQzEyw-u-s9iJn7Uru2D0JzXIllhO1ggeagIEs0BhgmfgN'
sizzer_token = 'https://discord.com/api/webhooks/816631804081078272/rtU2c7jIuZuuCZ_mzz2_aK2NpxOQeRZOhrR_Rc11AhF7HuUjMcVSR_humGBCwDy99vn0'
distance_token = 'https://discord.com/api/webhooks/816704115161432104/eJuU_DRzNqR0w4HUgTmcvWKVqZqC7VK5SyKANXDZhMDgHSYoy1Z7XZSzgKr1aq3bcAdf'
sportloft_token = 'https://discord.com/api/webhooks/816954551088447519/xbwszprfI-kXaMNYJU2zqx7B-x9vob5BFqUAf1perxswuDGD14lU47ODnFZ2K7DZP6pK'

tike_token_flt = 'https://discord.com/api/webhooks/822754280603385886/duUrti5fdn_SDBOQAGTSXKHORnx9BkeVdSw85bKaEXnsDXUa4DuiFeCvYgMze7EZMT6K'
rapcity_token_flt = 'https://discord.com/api/webhooks/822756625357340682/MofhbsEqYGyA1Wl_j2IzK9Kudeem46vvS9im_nEmy_51lFKEXpBc6kFrBpVtckPMiJsp'
sneaker_indutry_token_flt = 'https://discord.com/api/webhooks/822755663302230017/pixRhW_9Q99ZB7O-I66j180e3NDF5qIUHsih0vWz3ctQmyLAE9KC4BIAwhfD6mVcB7ek'
sizzer_flt = 'https://discord.com/api/webhooks/822756869738332160/4J00UsWgwtZfgb_5kDuZTAucczwp9mhGq4nynNnOcKj23ZT-LBL4J6u0ELgDcct7ieKC'
distance_flt = 'https://discord.com/api/webhooks/822757450116497408/wGbC8ThucQ0hdtg9h4ulQNgek6UtbXQ9Y143nkGkTyC6jWG8XCCQRIkdIubXiX019osx'
uman_token_flt = 'https://discord.com/api/webhooks/822757848022646804/56UCHuuMd-Tnispnhr5GmJ0PflbISSLWeXYSh4w5fzOsIq5KmQ9yB6Dho3tFh3ro66yn'
buzz_token_flt = 'https://discord.com/api/webhooks/822758088947400754/7qmouLB-latVdG0Z2XqEUeeP3ovgRzjLysG0bzJG3Zb-ZIXg1jkENHfiSu39DJa2wj7D'
bodo_token_flt = 'https://discord.com/api/webhooks/822758478233600061/r3n6oBAOqEfSOnRiRVU160P2ulzjaDnGYUU-LiUzJXPA0hNibxxV7EV89C3Icj4DSiox'
superstep_toke_flt = 'https://discord.com/api/webhooks/822758903191175218/fOHx2mAIQ0IZjRwuVwbZfGJzs1xIrAAPBNgr1Ku_U6-kS-MmKDZ1RbCDqzfDJ-YNMbjS'
grid_token_flt = 'https://discord.com/api/webhooks/822759374249918524/vV3m7fa8cEJli1KYDVSILsDqcUHmCdUnwWinjcwnB8uMGyhaAUzcbxizD7CTfjj7Coih'
colective_token_flt = 'https://discord.com/api/webhooks/822759758930771968/6z2kGnWoIYVhj1KBks0SHN48GZatk7EoEQS-KI9P8BfdmyGmYMt8Q_yAFUwSWgBGwNU7'
sportloft_token_flt = 'https://discord.com/api/webhooks/822760048592683008/PWamF9Hi-mIdA1Y-9d4W0vi8zf9Iq28gV6eRDrk127YGxrlrzzR5DATWeFSiOC_biOIW'
sport_select_token_flt = 'https://discord.com/api/webhooks/822760255167528960/HXamhN7P5SpIjk4QZ0BH0Om_XFU0vOdtBjmFclIvU0-E3HRZh5Y6ULYdvs7iW52MS-vG'
segos_token_flt = 'https://discord.com/api/webhooks/822760727223599124/ulnHE3mY73-B3tXv0iaLIR4pFS5iyi5AhzLKPNkG1GxbFmp_MI15k4HABYeX5R23gwsL'
dunk_token_flt = 'https://discord.com/api/webhooks/822760935366066177/J-Qh0gLl3ibTVfWOWj-pj-Mghnu61vRZdjAPrurMMz4EQYbmsLbC7btckJrWmd0p4dCV'
bstn_token_flt = 'https://discord.com/api/webhooks/822761541240881192/HwSB5oVdEBqF_79ID-zuGswBv6E1__efx-wNTwx0JIzfrYiUMGeFCcD2nt84Y8zr2Nen'
vitkac_token_flt = 'https://discord.com/api/webhooks/822762113952645130/7jkeuJIVmFCa5Kmg4SJ55lP6AxCF79fHM78TfoGNVzTIOO3udwHBFL6mfDnpOUAN5I2j'
impact_token_flt = 'https://discord.com/api/webhooks/822764740349657109/jdd0A1RNSEDRi7q-NhrUI0z6fJ_IkQUQaVUZ1_RbbTv4-2Pr6nMH4TPwjN408JXM0NWQ'
horn_token_flt = 'https://discord.com/api/webhooks/822765129464414208/351V_Elq_DlxgXtqu6m6Mj4eW26CZj3rYR7_KEyzrKZ5V1auJ4AZuKBv_jzeExyRRMdX'
queenG_token_flt = 'https://discord.com/api/webhooks/822765468456714240/rjS0Q6VfLORPZ6yAJCNUeX_sX3LOfyne7-KTkp9kHEV6QOShCEd_CqPUf9-3POXcfEiv'
queencz_token_flt = 'https://discord.com/api/webhooks/822775541761179668/iUXpm2yMiWPCywfrVp66Q4dZCWlJqfwn9OuGYZ9vDd0wE6aedh6qCNCEMyTwUynEUaBc'
noss_toke_flt = 'https://discord.com/api/webhooks/822775877938970624/rPzfXIhlfkuSRnMonTjaee7mTAK3uei1k0EeRdmwH6DewXB6uBDASVXThgJZXGSW2x6f'
basket_token_flt = 'https://discord.com/api/webhooks/822776030372167692/sn3gYmpqgKkKxYoc7M00TKewQY1_qEfTM-CduGshSBY9CXu6dp3jTbKVdBZ67A_KHxBV'
streets_token_flt = 'https://discord.com/api/webhooks/822776271796305950/DzfDNwmplkWRRbqperYTru26wZvE8tp0VY0TaD7iL4pYwmWeMAyGwIdl31r02nX882za'
sneak_token_flt = 'https://discord.com/api/webhooks/822776498485592115/HXavS13S8bah_SSTnElsSxoVJ8FhUGlDyLycB3RI0L1PiXdoXF0OCMcBpJdUfYJmCBGk'
shoe_token_flt = 'https://discord.com/api/webhooks/822776826061389825/FSoTrmgINzn4vsyWse5th8swHjVrzHEjztqTw6zqkUK_MVwxTmbmk6lKaKNcaC-kca1f'
slam_token_flt = 'https://discord.com/api/webhooks/822776963269001216/-cbOoSq6y1-j7vhuKl2pAAhvGSBw4N5MYDwNFXU9oKE2mqS2WC_9Fa0zUmU7sPafirzd'
shelta_token_flt = 'https://discord.com/api/webhooks/822777221248843776/pX5B_a05soiSbLv-3D5fEwDrAAixFhMLi-tEd4XGg3zVVfDsOsMagQktj5_zxATVA7Us'

keywords = [   "NIKE", "JORDAN+1",  
                "JORDAN+3" 
           ]

#"JORDAN+4", "JORDAN+5", "JORDAN+6", "JORDAN+11",
#                "JORDAN+12", "NIKE+DUNK+LOW", "NIKE+SB+DUNK", "AIR+FORCE+1"

filt =  [   "air", "force", "yeezy", "jordan"
            "nike", "low", "sb", "dunk"
        ]


kkeys = ['name', 'price', 'prices', 'url', 'names', 'urls']

def init():
    hashes = []
    f = open("DB.txt", "r")
    lines = f.read()
    hashes = lines.split('**!*!!***!!')
    f.close()
    return hashes

def scrap_slamdunk():

    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    global sent
    # For each keyword a querry will be created
    new_items = []
    
    url = 'https://www.slamdunk.gr/el/32843-papoutsia?brand=nike,jordan'
    urls = []

    try:
        response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
        urls = re.findall('<a class="product_img_link" href="(.*)" ', response)
    except Exception:
        return []
    
    for i in range(0, len(urls)):
        if urls[i] not in hashes:
            try:
                aux = {}
                aux['url'] = urls[i]
                response = requests.get(url=urls[i], headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text.replace(">", "\n")
                aux['prices'] = re.findall('class="price" content="(.*)"', response)[0] + ' Euros'
                response = requests.get(url=urls[i], headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
                aux['name'] = re.findall('<title>(.*)</title>', response)[0]
                new_items.append(aux)
                f.write(urls[i] + '**!*!!***!!')
                hashes.append(urls[i])
            except Exception:
                break
        
    return new_items

def scrap_shelta():
    
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://shelta.eu/searchresults?pagesize=20&searchstring="

    # For each keyword a querry will be created
    new_items = []
    for keyword in keywords:
        # Launch request and store it's response
        url = main_url + keyword.replace("+", "%20")
        try:
            response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
            urls = re.findall('href="(.*)"><span>More info</span></a>', response)
            prices = re.findall('class="SearchPriceAmount">(.*) EUR</span></span><span', response)
            names = re.findall('title="(.*)" href=', response)
            names.remove(names[0])
        except Exception:
            return []

        for i in range(0, len(urls)):
            if urls[i] not in hashes:
                aux = {}
                aux['url'] = 'https://shelta.eu/' + urls[i]
                aux['prices'] = prices[i] + ' euros'
                aux['name'] = names[i][0:names[i].index('(')]
                new_items.append(aux)
                f.write(urls[i] + '**!*!!***!!')
                hashes.append(urls[i])

    return new_items

def scrap_shoe():
    
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # For each keyword a querry will be created
    new_items = []
    
    # Launch request and store it's response
    url = 'https://shoegallerymiami.com/collections/mens-shoes'
    try:
        response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
        urls = re.findall('<h3 class="standard-index search-result-title"><a href="(.*)" title', response)
    except Exception:
        return []

    for i in range(0, len(urls)):
        if urls[i] not in hashes:
            try:
                aux = {}
                aux['url'] = 'https://shoegallerymiami.com/' + urls[i]
                response = requests.get(url=aux['url'], headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
                
                aux['prices'] = re.findall('<meta property="og:price:amount" content="(.*)">', response)
                if aux['prices'] != []:
                    aux['name'] = re.findall('<meta name="twitter:title" content="(.*)">', response)[0]
                    aux['prices'] = aux['prices'][0]
                    new_items.append(aux)
                    f.write(urls[i] + '**!*!!***!!')
                    hashes.append(urls[i])
            except Exception:
                break
    return new_items

def scrap_sneak():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://www.sneak-a-venue.com/search?searchstring="

    # For each keyword a querry will be created
    new_items = []
    for keyword in keywords:
        # Launch request and store it's response
        url = main_url + keyword 

        try:
            response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
            urls = re.findall('<a class="plink image" href="(.*)">', response)
        except Exception:
            return []

        for i in range(0, len(urls)):
            if urls[i] not in hashes:
                try:
                    aux = {}
                    aux['url'] = 'https://www.sneak-a-venue.com' + urls[i]
                    response = requests.get(url=aux['url'], headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
                    aux['name'] = re.findall('<span class="productname">(.*)</span>', response)[0]
                    aux['prices'] = re.findall("'total_value': (.*),", response)[0]
                    cat = re.findall("'category': '(.*)'", response)[0]
                    if cat == 'Footwear' or cat == 'Sneaker':
                        new_items.append(aux)
                        f.write(urls[i] + '**!*!!***!!')
                        hashes.append(urls[i])
                except Exception:
                    break

    return new_items

def scrap_streets():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    url = "https://www.thestreets.eu/mens-sneakers/c,d,12,0,f:m-5_6/"

    # For each keyword a querry will be created
    new_items = []
    
    try:
        # Launch request and store it's response
        response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
        urls = re.findall('href="(.*)"></a></div>', response.replace("class", '\n'))
        prices = re.findall('data-tax="incl. tax">(.*)€</span>', response.replace("class", '\n'))
        names = re.findall('<a class="product_full_link" title="(.*)"', response.replace("href", '\n'))
    except Exception:
        return []

    for i in range(1, min(len(urls), 12)):
        if urls[i] not in hashes:
            try:
                response = requests.get(url=urls[i], headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
                aux = {}
                aux['url'] = urls[i]
                aux['name'] = names[i]
                aux['prices'] = prices[i]
                new_items.append(aux)
                f.write(urls[i] + '**!*!!***!!')
                hashes.append(urls[i])
            except Exception:
                break
    return new_items

def scrap_basket():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://www.baskets-store.com/nl/search/"

    # For each keyword a querry will be created
    new_items = []
    for keyword in keywords:
        # Launch request and store it's response
        url = main_url + keyword
        try:
            response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
            urls = re.findall('href="https://www.baskets-store.com/nl/(.*)" title=', response.replace("class", '\n'))
        except Exception:
            return []

        for i in range(1, len(urls)):
            if urls[i] not in hashes:
                try:
                    aux = {}
                    if urls[i] != '':
                        aux['url'] = 'https://www.baskets-store.com/nl/' + urls[i]
                        response = requests.get(url=aux['url'], headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
                        aux['name'] = re.findall("<title>(.*)</title>", response)[0]
                        aux['price'] = re.findall("'price': '(.*)',", response)[0]
                        new_items.append(aux)
                        f.write(urls[i] + '**!*!!***!!')
                        hashes.append(urls[i])
                except Exception:
                    break
    return new_items

def scrap_noss():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://www.noss.hr/hr/filter/type_44/?q="

    # For each keyword a querry will be created
    new_items = []
    for keyword in keywords:
        # Launch request and store it's response
        url = main_url + keyword
        try:
            response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
            urls = re.findall(' href="(.*)"><img id="', response.replace("'", '\n'))
        except Exception:
            return []

        for i in range(0, len(urls)):
            if urls[i] not in hashes:
                try:
                    aux = {}
                    aux['url'] = urls[i]
                    response = requests.get(url=aux['url'], headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
                    aux['name'] = re.findall('<meta name="title" content="(.*)" ', response.replace("/><meta name", "\n"))[0]
                    aux['price'] = re.findall('">(.*)KN</strong>', response)[0] + 'KN'
                    new_items.append(aux)
                    f.write(urls[i] + '**!*!!***!!')
                    hashes.append(urls[i])
                except Exception:
                    break
    return new_items

def scrap_queenscz():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    new_items = []
    
    # Launch request and store it's response
    url = 'https://www.queens.cz/kat/2/boty-tenisky-panske/?filtr[]=156&filtr[]=1&filtr[]=658'
    try:
        response = requests.get(url='url', headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
        urls = re.findall('<a href="https://www.queens.cz(.*)" >', response.replace("'", '\n'))
    except Exception:
        return []

    for i in range(0, len(urls) - 2):
        if urls[i] not in hashes:
            try:
                aux = {}
                aux['url'] = 'https://www.queens.cz' + urls[i]
                response = requests.get(url=aux['url'], headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
                aux['price'] = re.findall('value: (.*),', response)[0] + " currency: 'CZK'"
                aux['name'] = re.findall('<title>(.*) ', response.replace('/', '\n'))[0]
                new_items.append(aux)
                f.write(urls[i] + '**!*!!***!!')
                hashes.append(urls[i])
            except Exception:
                break
    return new_items

def scrap_queensG():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    special = [ 'https://www.queens.global/men-sneakers-nike-acg/',
                'https://www.queens.global/men-sneakers-jordan/',
                'https://www.queens.global/men-sneakers-nike/']

    # For each keyword a querry will be created
    new_items = []
    for url in special:
        try:
            response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
            urls = re.findall('"><a href="(.*)" data-name=', response.replace("'", '\n'))
            prices = re.findall('class="price">(.*)</span><div', response.replace(" ", '\n'))
            names = re.findall('alt="(.*)"></noscri', response.replace("pt>", '\n'))
        except Exception:
            return []

        for i in range(0, len(prices)):
            if urls[i] not in hashes:
                aux = {}
                aux['url'] = 'https://www.queens.global/' + urls[i]
                aux['price'] = prices[i].replace('€', 'Euros: ')
                aux['name'] = names[i]
                new_items.append(aux)
                f.write(urls[i] + '**!*!!***!!')
                hashes.append(urls[i])
    f.close()
    return new_items


def scrap_horn():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://www.engelhorn.de/suche?q="

    # For each keyword a querry will be created
    new_items = []

    url = 'https://www.engelhorn.de/sport/herren/sportschuhe/basketballschuhe?srule=Neuheiten'
    
    try:
        response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
        urls = re.findall('<a href="(.*)" class="quickview-button">', response)
    except Exception:
        return []

    for i in range(0, len(urls)):
        if urls[i] not in hashes:
            try:
                r = requests.get(url=urls[i], headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text.lower()
                k = 0
                for word in filt:
                    if word in r:
                        k += 1
                if k != 0:
                    aux = {}
                    aux['url'] = urls[i]
                    response = requests.get(url=urls[i], headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
                    aux['price'] = re.findall("data-listprice='(.*) ", response)[0] + 'euros'
                    aux['name'] = re.findall("<title>(.*)</title>", response)[0]
                    f.write(urls[i] + '**!*!!***!!')
                    hashes.append(urls[i])
                    new_items.append(aux)
            except Exception:
                break
    f.close()
    return new_items

def scrap_impact():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # For each keyword a querry will be created
    new_items = []
    try:
        response = requests.get(url='https://www.impact-premium.com/86-shoes', headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
    except Exception:
        return []

    urls = re.findall('<a class="product_img_link"(.*)"', response.replace("title=", "\n"))
 
    for i in range(0, len(urls)):
        if urls[i] not in hashes:
            try:
                aux = {}
                aux['url'] = urls[i].replace('href="', '')
                response = requests.get(url=aux['url'], headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
                aux['price'] = re.findall('class="price" content="(.*)"> ', response)[0][:re.findall('class="price" content="(.*)"> ', response)[0].index('"> ')]
                aux['name'] = re.findall('"name":"(.*)","itemCondition":', response.replace('http', '\n'))[0]
                new_items.append(aux)
                f.write(urls[i] + '**!*!!***!!')
                hashes.append(urls[i])
            except Exception:
                break
    return new_items

def scrap_vitkac():

    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://www.vitkac.com/us/shop/men?targets=topFilter%2CproductList%2Coffsets_bottom&params%5B0%5D%5Bname%5D=cat%5B440%5D&params%5B0%5D%5Bvalue%5D=on&main_category=&undefined=&q="

    # For each keyword a querry will be created
    new_items = []
    for keyword in keywords:
        # Launch request and store it's response
        url = main_url + keyword
        
        try:
            response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
        except Exception:
            return []

        names = re.findall('data-seoname="(.*)"', response)
        urls = re.findall('href="https://www.vitkac.com/us/p/(.*)"', response)
        prices = re.findall('data-seoprice="(.*)"', response)

        for i in range(0, len(urls)):
            if urls[i] not in hashes:
                aux = {}
                aux['url'] = 'href="https://www.vitkac.com/us/p/' + urls[i]
                aux['price'] = prices[i].replace('€', 'Euros: ')
                aux['name'] = names[i]
                new_items.append(aux)
                f.write(urls[i] + '**!*!!***!!')
                hashes.append(urls[i])

    f.close()
    return new_items


def scrap_bstn():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://www.bstn.com/eu_en/catalogsearch/result/?q="

    # For each keyword a querry will be created
    new_items = []
    for keyword in keywords:
        # Launch request and store it's response
        url = main_url + keyword.replace('+', '%20') + '&categories=Men~Footwear'
        try:
            response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
            names = re.findall("<h3> <strong> (.*) </strong> </h3>", response)
            urls = re.findall('<a class="catalog-grid-item__name-link" href="(.*)">', response)
            prices = re.findall('<span itemprop="lowPrice" class="after_special price "> (.*) </span>', response)
        except Exception:
            return []

        for i in range(0, len(urls)):
            if urls[i] not in hashes:
                aux = {}
                aux['url'] = urls[i]
                aux['price'] = prices[i].replace('€', 'Euros: ')
                aux['name'] = names[i]
                new_items.append(aux)
                f.write(urls[i] + '**!*!!***!!')
                hashes.append(urls[i])

    f.close()
    return new_items

def scrap_worldbox():

    req = [ 'https://worldbox.pl/products/air-force-1/keyword,air%20force%201?keyword=air%20force%201', 
            'https://worldbox.pl/products/jordan-1/keyword,jordan%201',
            'https://worldbox.pl/products/jordan-3/keyword,jordan%203?keyword=jordan%203',
            'https://worldbox.pl/products/jordan-4/keyword,jordan%204?keyword=jordan%204',
            'https://worldbox.pl/products/jordan-5/keyword,jordan%205?keyword=jordan%205',
            'https://worldbox.pl/products/jordan-6/keyword,jordan%206?keyword=jordan%206',
            'https://worldbox.pl/products/jordan-11/keyword,jordan%2011?keyword=jordan%2011',
            'https://worldbox.pl/products/jordan-12/keyword,jordan%2012?keyword=jordan%2012',
            'https://worldbox.pl/products/nike-sb-low/keyword,nike%20sb%20low?keyword=nike%20sb%20low'
    ]

    # Acts as a backup
    old_items = (json.load(open("worldbox.json")))

    # Main url must add search querry before request
    main_url = "https://worldbox.pl/products/"

    # Will be used to see if there are new entries
    urls2 = []
    for backup in old_items:
        urls2.append(backup.get("url", None))

    # For each keyword a querry will be created
    new_items = []
    for keyword in req:
        # Launch request and store it's response
        response = requests.get(url=keyword, headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
        
        names = re.findall("'name': '(.*)',", response)
        urls = re.findall("'url' : '(.*)',", response)
        prices = re.findall("'unit_sale_price' : '(.*)',", response)

        for i in range(0, len(prices)):
            aux = {}
            aux['url'] = urls[i]
            aux['price'] = prices[i]
            aux['name'] = names[i]
            new_items.append(aux)

    nn = []
    new_bool = False
    # Compare old items with new ones and see if there really are new items
    for item in new_items:
        if item['url'] not in urls2:
            nn.append(item)
            new_bool = True

    # Write the new items to the file
    if new_bool:
        old_items += nn
        with open('worldbox.json', 'w') as file:
            json.dump(old_items, file, indent=4)
        # Return just the new added items
        return nn

# Permisions
def scrap_distance():

    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # For each keyword a querry will be created
    new_items = []

    file = open('distance.txt', 'r', encoding='utf-8')
    response = file.read()
    file = open('distance.txt', 'r', encoding='utf-8')
    lines = file.readlines()

    
    t = response.replace('class="product photo', '\n')

    urls = re.findall('div> <a href="(.*)" ', t)
    prices = []
    names = re.findall('"name":"(.*)"', response.replace(",", "\n"))

    for line in lines:
        if 'RON' in line:
            a = line[line.index('RON') - 7 :line.index('RON')]
            if '=' not in a and 'Code' not in a and 'LA' not in a:
                prices.append(a.replace('\u00a0', ' RON'))

    for i in range(0, len(names)):
        if urls[i] not in hashes:
            aux = {}
            aux['url'] = urls[i]
            aux['price'] = prices[i]
            aux['name'] = names[i]
            new_items.append(aux)
            f.write(urls[i] + '**!*!!***!!')
            hashes.append(urls[i])

    f.close()
    return new_items

def scrap_dunkshop():

    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://dunkshop.eu/catalogsearch/result/index/?cat=3&q="

    # For each keyword a querry will be created
    new_items = []
    for keyword in keywords:
        # Launch request and store it's response
        url = main_url + keyword
        try:
            response = requests.get(url=url,headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
        except Exception:
            return []
        prices = re.findall('<span class="price">€(.*)</span>                                    </span>', response)
        names = re.findall('title="(.*)" cl', response.replace('ass="', '\n'))
        lines = list(iter(response.splitlines()))
        urls = []
        for i in range(0, len(lines) - 7):
            if '<div class="price-box">' in lines[i+6]:
                urls.append(re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", lines[i])[0])
        for i in range(0, len(prices)):
            if urls[i] not in hashes:
                aux = {}
                aux['url'] = urls[i]
                aux['price'] = prices[i]
                aux['name'] = names[i+2]
                new_items.append(aux)
                f.write(urls[i] + '**!*!!***!!')
                hashes.append(urls[i])
    
    f.close()
    return new_items

# Not done permissions
def scrap_segos():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # For each keyword a querry will be created
    new_items = []

    file = open('segos1.txt', 'r')
    response = file.read()

    urls = re.findall("<a itemprop=\"url\" href='(.*)'>", response)
    prices = re.findall('<span class="price precio">(.*)</span>', response.replace('$.ajax({url:', '\n'))

    for i in range(0, len(urls)):
        if urls[i] not in hashes:
            aux = {}
            aux['url'] = urls[i]
            aux['price'] = prices[i][:prices[i].index(',')] + '€'
            aux['name'] = urls[i][urls[i].index('ct/')+ 3 :].replace('-', ' ')
            new_items.append(aux)
            f.write(urls[i] + '**!*!!***!!')
            hashes.append(urls[i])

    f.close()
    return new_items

#Not done permissions
def scrap_colective():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # For each keyword a querry will be created
    new_items = []

    # Launch request and store it's response
    file = open('colectiv.txt', 'r', encoding='utf-8')
    response = file.read()

    prices = re.findall('<span class="original-price"><b>(.*)</b></span> ', response)
    prices2 = re.findall('<span class="current-price red">(.*) lei</span>', response)
    urls = re.findall('<a class="frame ecommerce" href="(.*)" onclick="', response.replace('$.ajax({url:', '\n'))
    names = re.findall('<img class="absImg absImg1" src=(.*)', response.replace('$.ajax({url:', '\n'))

    for i in range(0, len(prices)):
        if urls[i] not in hashes:
            aux = {}
            aux['url'] = urls[i]
            aux['price'] = prices2[i]
            aux['name'] = names[i][86:]
            new_items.append(aux)
            f.write(urls[i] + '**!*!!***!!')
            hashes.append(urls[i])

    f.close()
    return new_items

def scrap_boarders():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://www.boarders.ro/search?word="

    # For each keyword a querry will be created
    new_items = []
    for keyword in keywords:
        # Launch request and store it's response
        url = main_url + keyword.replace("+", "%20") + "&categories[]=10&price[min]=&price[max]="

        try:
            response = requests.get(url=url,headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
        except Exception:
            return []

        prices = re.findall('<div class="price">(.*) Lei</div>', response)
        urls = re.findall('a href="(.*)" class="product-name">', response)
        names = list()
        for url in urls:
            names.append(re.findall(' <a class="product-name" href="' + url +'">(.*)</a>', response)[0])
        for i in range(0, len(names)):
            if urls[i] not in hashes:
                aux = {}
                aux['name'] = names[i]
                aux['url'] = urls[i]
                aux['price'] = prices[i]
                new_items.append(aux)
                f.write(urls[i] + '**!*!!***!!')
                hashes.append(urls[i])

    f.close()
    return new_items

# NOT DONE PERMISIONS
def scrap_sportloft():
    # Acts as a backup
    old_items = (json.load(open("sportloft.json")))

    return old_items

    # Will be used to see if there are new entries
    urls2 = []
    for backup in old_items:
        urls2.append(backup.get("url", None))

    # For each keyword a querry will be created
    new_items = []

    # Launch request and store it's response
    file = open('sportloft.txt', 'r', encoding='utf-8')
    lines = file.readlines()

    '''
    #names = re.findall('<p>(.*)</p>', response)
    prices1 = re.findall('<span class="current-price red">(.*) lei</span> ', response)
    prices2 = re.findall('<span class="original-price"><b>(.*) lei</b></span> ', response)
    urls = re.findall('<h2 class="h5"><a class="ecommerce" href="(.*)"', response)

    input(len(urls))
    input(len(prices1))
    input(len(prices2))
    '''
    
    for i in range(0, len(prices)):
        aux = {}
        aux['url'] = urls[i]
        aux['price'] = prices[i]
        new_items.append(aux)

    new_bool = False
    nn = []
    # Compare old items with new ones and see if there really are new items
    for item in new_items:
        if item['url'] not in urls2:
            nn.append(item)
            new_bool = True

    # Write the new items to the file
    if new_bool:
        old_items += nn
        with open('sportloft.json', 'w') as file:
            json.dump(old_items, file, indent=4)
        # Return just the new added items
        return nn

def scrap_superstep():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    special = ['https://superstep.ro/index.php?route=product/category&path=430&fm=5',
                'https://superstep.ro/index.php?route=product/category&path=430&fm=41',
              ]

    # For each keyword a querry will be created
    new_items = []
    for url in special:
        try:
            response = requests.get(url=url,headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text.replace(",", "\n")
        except Exception:
            return []
        names = re.findall('"name":"(.*)"', response)
        prices = re.findall('"price":"(.*)"', response)
        ids = re.findall('"id":"(.*)"', response)
        for i in range(0, len(names)):
            if ids[i] not in hashes:
                aux = {}
                aux['name'] = names[i]
                aux['url'] = 'https://superstep.ro/index.php?route=product/product&product_id=' + ids[i]
                aux['price'] = prices[i]
                new_items.append(aux)
                f.write(ids[i] + '**!*!!***!!')
                hashes.append(ids[i])

    f.close()
    return new_items


def scrap_bodosport():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://www.bodosport.ro/index.php?route=product/search&search="

    # For each keyword a querry will be created
    new_items = []
    for keyword in keywords:
        # Launch request and store it's response
        url = main_url + keyword.replace("+","%20") + '&category_id=518'
        try:
            response = requests.get(url=url, timeout=25, headers={'User-Agent': 'Mozilla/5.0'}).text
        except Exception:
            return []
        names = re.findall('<div class="item-img-info"><a title="(.*)" class=', response)
        old_prices = re.findall('<span class="old-price"><span class="price">(.*)</span></span>', response)
        new_prices = re.findall(' <span class="special-price"><span class="price">(.*)</span></span>', response)
        urls = re.findall('class="product-image" href="https://www.bodosport.ro(.*)">', response)

        for i in range(0, len(names)):
            if urls[i] not in hashes:
                aux = {}
                aux['name'] = names[i]
                aux['url'] = 'https://www.bodosport.ro' + urls[i]
                new_items.append(aux)
                f.write(urls[i] + '**!*!!***!!')
                hashes.append(urls[i])

    f.close()
    return new_items

def scrap_buzz():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    url = 'https://www.buzzsneakers.com/RON_ro/incaltaminte/barbati/nike/'

    # For each keyword a querry will be created
    new_items = []
    try:
        response = requests.get(url=url,  headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
    except Exception:
        return []
    names = re.findall('data-productName="(.*)"', response)
    category = re.findall('data-productCat="(.*)"', response)
    prices = re.findall('data-productPrice="(.*)" >', response)
    urls = re.findall('data-remote-modal-quick-wiew-product-permalink="(.*) ', response.replace("?", " \n"))
    
    for i in range(0, len(names)):
        if urls[i*3] not in hashes:
            aux = {}
            aux['name'] = names[i]
            aux['price'] = prices[i]
            aux['url'] = urls[i*3]
            new_items.append(aux)
            f.write(urls[i*3] + '**!*!!***!!')
            hashes.append(urls[i*3])

    f.close()
    return new_items

def scrap_uman():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://www.u-man.ro/toate-produsele/filtru-categorie:2?q="

    # For each keyword a querry will be created
    new_items = []
    for keyword in keywords:
        # Launch request and store it's response
        url = main_url + keyword
        try:
            response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text.replace(',', "\n").replace(';', "\n")
        except Exception:
            return []
        names = re.findall('"name":"(.*)"', response)
        prices = re.findall('"price":"(.*)"', response)
        urls = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",response)
        trim = []
        for url in urls:
            trim.append(url)
        for i in range( len(names)-1, -1, -1):
            if trim[-1] not in hashes:
                aux = {}
                aux['name'] = names[i]
                aux['price'] = prices[i]
                aux['url'] = trim[-1]
                f.write(trim[-1] + '**!*!!***!!')
                hashes.append(trim[-1])
                trim.remove(trim[-1])
                new_items.append(aux)
                already.append(trim[-1])
                
    f.close()
    return new_items

def scrap_11teamsport():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://11teamsports.ro/s/"

    # For each keyword a querry will be created
    new_items = []
    for keyword in keywords:
        # Add keyword to url
        url = main_url + keyword.replace('+',"%20") + '/type2-28'
        # Launch request and store it's response
        try:
            response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
        except Exception:
            return []
        names = re.findall('"name": " (.*)", "price":', response)
        prices = re.findall('"price": (.*), "brand":', response)
        ids = re.findall('"id": "(.*)", "name": ',response)
        urls = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",response)
        for i in range(0, len(names)):
            if ids[i] not in hashes:
                aux = {}
                aux['name'] = names[i]
                aux['price'] = prices[i]
                for url in urls:
                    if ids[i] in url and 'jpg' not in url:
                        aux['url'] = url
                new_items.append(aux)
                f.write(ids[i] + '**!*!!***!!')
                hashes.append(ids[i])

    f.close()
    return new_items

def scrap_sportselect():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://www.sportselect.ro/produse?c="

    # For each keyword a querry will be created
    new_items = []
    for keyword in keywords:
        # Add keyword to url
        url = main_url + keyword
        # Launch request and store it's response
        try:
            response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
        except Exception:
            return []
        # Extract valuable information
        names = re.findall('"name": "(.*)",', response)
        prices = re.findall('"price": "(.*)",', response)
        urls2 = re.findall('"url": "https://(.*)",', response)
        # Create a dict with the information
        for i in range(0, len(prices)):
            if urls2[2*i] not in hashes:
                aux = {}
                aux['name'] = names[i*2]
                aux['price'] = prices[i]
                aux['url'] = "https://" + urls2[i*2]
                new_items.append(aux)
                f.write(urls2[2*i] + '**!*!!***!!')
                hashes.append(urls2[2*i])

    f.close()
    return new_items

def scrap_skates():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://www.skates.ro/index.php?main_page=advanced_search_result&search_in_description=1&keyword="

    # For each keyword a querry will be created
    new_items = []
    for keyword in keywords:
        # Add keyword to url
        url = main_url + keyword + '&inc_subcat=0&sort=20a&fltCategorie%5B%5D=87'
        # Launch request and store it's response
        try:
            response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
        except Exception:
            return []
        names = re.findall('data-name="(.*)" data-discount=', response)
        aux = re.findall('ice">(.*)&nbsp;lei</span><', response)
        prices = []
        for price in aux:
            if '>' in price:
                prices.append(price[price.find('">')+2:])
            else:
                prices.append(price)
        urls = re.findall('class="product-link clearfix" href="(.*)"><img src=', response)
        for i in range(0, len(names)):
            if names[i] not in hashes:
                aux = {}
                aux['name'] = names[i]
                aux['price'] = prices[i]
                aux['url'] = urls[i]
                new_items.append(aux)
                f.write(names[i] + '**!*!!***!!')
                hashes.append(names[i])
    
    f.close()
    return new_items


def scrap_sizzer():
    
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://sizeer.ro/"
        
    file = open('sizzer.txt', 'r', encoding='utf-8')
    response = file.read()
    
    prices = re.findall('<span itemprop="price">(.*)</span>', response)
    urls = re.findall('<a class="b-itemList_photoLink" href="(.*)" ', response)
    names = re.findall('data-ga-name="(.*)"', response)

    new_items = []
    
    for i in range(0, len(urls)):
        if urls[i] not in hashes:
            aux = {}
            aux['price'] = prices[i]
            aux['url'] = 'https://sizeer.ro' + urls[i]
            aux['name'] = names[i]
            new_items.append(aux)
            f.write(urls[i] + '**!*!!***!!')
            hashes.append(urls[i])
    
    f.close()
    return new_items
    

def scrap_tike():
    """
        Scrapes tike.ro for new items added that contains keywords from keywords list
    """
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://www.tike.ro/incaltaminte/?search="
    
    # For each keyword a querry will be created
    new_items = []
    for keyword in keywords:
        # Add keyword to url
        url = main_url + keyword.replace('+', '%20')
        # Launch request and store it's response
        try: 
            response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15).text
        except Exception:
            return []
        names = re.findall('data-productName="(.*)"', response)
        ids2 = re.findall('data-productid="(.*)"', response)
        category = re.findall('data-productCat="(.*)"', response)
        prices = re.findall('data-productPrice="(.*)"', response)

        for i in range(0, len(names)):
            if ids2[i] not in hashes:
                aux = {}
                aux['name'] = names[i]
                aux['id'] = ids2[i]
                aux['category'] = category[i]
                aux['price'] = prices[i]
                aux['url'] = re.search('<a href="(.*)" title="'+names[i], response).group(1)
                new_items.append(aux)
                f.write(ids2[i] + '**!*!!***!!')
                hashes.append(ids2[i])
    
    f.close()
    return new_items

def scrap_rap_city():
    """
        Scrapes rap-city.ro for new items added that contains keywords from keywords list
    """
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://www.rapcity.ro/kereses/?SZURES="

    # For each keyword a querry will be created
    new_items = []
    for keyword in keywords:
        # Add keyword to url
        url = main_url + keyword

        try:
            # Launch request and store it's response
            response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15).text
        except Exception:
            return []

        urls = re.findall('<a href="../Utcai(.*)" ', response.replace('class','\n'))
        names = re.findall("<h2 title='(.*)' ", response.replace('class','\n'))
        prices = re.findall('<span class="price-normal"><span>(.*)</span> ', response.replace('<span>RON', '\n'))

        for i in range(0, len(urls)):
            if urls[i] not in hashes:
                aux = {}
                aux['name'] = names[i]
                aux['price'] = prices[i]
                aux['url'] = 'https://www.rapcity.ro/Utcai' + urls[i]
                new_items.append(aux)
                f.write(urls[i] + '**!*!!***!!')
                hashes.append(urls[i])

    f.close()
    return new_items

def scrap_sneakerindustry():
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://sneakerindustry.ro/ro/cautare?s="
    
    # For each keyword a querry will be created
    new_items = []
    for keyword in keywords:
        # Add keyword to url
        url = main_url + keyword
        # Launch request and store it's response
        try:
            response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15).text
        except Exception:
            return []

        urls = re.findall('<h2 class="h2" itemprop="name"><a href="(.*)">', response)
        prices = re.findall('<span itemprop="price" class="price">(.*) RON</span>', response)

        for i in range(0, len(urls)):
            if urls[i] not in hashes:
                try:
                    aux = {}
                    res = requests.get(url=urls[i], headers={'User-Agent': 'Mozilla/5.0'}, timeout=15).text
                    aux['name'] = re.findall('<title>(.*)Sn', res)
                    if aux['name'] == []:
                        break
                    aux['name'] = aux['name'][0]
                    aux['price'] = prices[i]
                    aux['url'] = urls[i]
                    new_items.append(aux)
                    f.write(urls[i] + '**!*!!***!!')
                    hashes.append(urls[i])
                except Exception:
                    break

    f.close()
    return new_items

def scrap_grid():
    """
        Scrapes grid-sport.ro for new items added that contains keywords from keywords list
    """
    try:
        hashes = init()
        f = open("DB.txt", "a")
    except Exception:
        return []

    # Main url must add search querry before request
    main_url = "https://grid-sport.ro/catalogsearch/result/index/?cat=286&q="

    # For each keyword a querry will be created
    new_items = []
    for keyword in keywords:
        # Add keyword to url
        url = main_url + keyword
        # Launch request and store it's response
        try:
            response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15).text
        except Exception:
            return []
        urls = re.findall('https://(.*)" class="product photo"',response)
        names = re.findall('alt="(.*)"></sp',response.replace('an>', '\n'))
        
        for i in range(0, len(urls)):
            if urls[i] not in hashes:
                try:
                    aux = {}
                    res = requests.get(url='https://' + urls[i], headers={'User-Agent': 'Mozilla/5.0'}, timeout=25).text
                    aux['price'] = re.findall('<meta property="product:price:amount" content="(.*)"/>',res)
                    aux['url'] = 'https://' + urls[i]
                    aux['name'] = names[i]
                    new_items.append(aux)
                    f.write(urls[i] + '**!*!!***!!')
                    hashes.append(urls[i])
                except Exception:
                    break
        return new_items
        f.close()


def send_to_discord(result, token, token_flt):

    filters =   ['nike sb dunk', 'jordan 1', 'jordan 1 high', 'jordan 1 mid', 'jordan 1 low',
                'jordan 4', 'jordan 5', 'yeezy 350', 'yeezy 700', 'jordan 3'
                ]
    
    filters2 = [
                ['yeezy', '350 '], ['nike', 'sb', 'dunk'], ['jordan', '1 '],
                ['jordan', '4 '], ['jordan', '5 '],  ['yeezy', '700 ']
               ]
    
    global sent
    if result != None and result !=[]:
        for item in result:
            if item['url'] not in sent:
                sent.append(item['url'])
                s = ""
                #resp = requests.get(url=item['url'], timeout=25, headers={'User-Agent': 'Mozilla/5.0'}).text.lower()
                ok = 0
                trimis = 0
                for flt in filters:
                    if flt in item.get('name','').lower() or flt in item.get('names','').lower():
                        for key in item.keys():
                            if str(key) in kkeys:
                                s += str(key) + " : " + str(item[key]) + "\n"
                        webhook = DiscordWebhook(url=token_flt, content= '@here, @everyone, take a look here')
                        response = webhook.execute()
                        webhook = DiscordWebhook(url=token_flt, content=s)
                        response = webhook.execute()
                        ok = 1
                        trimis = 1
                        break
                if trimis == 0:
                    for flt in filters2:
                        count = 0
                        for f in flt:
                            if f in item.get('name','').lower() or f in item.get('names','').lower():
                                count += 1
                        if count == len(flt):
                            for key in item.keys():
                                if str(key) in kkeys:
                                    s += str(key) + " : " + str(item[key]) + "\n"
                            webhook = DiscordWebhook(url=token_flt, content= '@@here, @everyone, take a look here')
                            response = webhook.execute()
                            webhook = DiscordWebhook(url=token_flt, content=s)
                            response = webhook.execute()
                            ok = 1
                            break
                if ok == 0:
                    for key in item.keys():
                        if str(key) in kkeys:
                            s += str(key) + " : " + str(item[key]) + "\n"
                    webhook = DiscordWebhook(url=token, content= '@@here, @everyone, take a look here')
                    response = webhook.execute()
                    webhook = DiscordWebhook(url=token, content=s)
                    response = webhook.execute()


if __name__ == "__main__":

    for i in range(0,2):
        print("Scraping bodosport")
        output = scrap_bodosport()
        send_to_discord(output, bodo_token, bodo_token_flt)
        print(output)
        print("Scraping tike")
        output = scrap_tike()
        send_to_discord(output, tike_token, tike_token_flt)
        print(output)
        print("Scraping rap_city")
        output = scrap_rap_city()
        send_to_discord(output, rap_city_token, rapcity_token_flt)
        print(output)
        print("Scraping sneakerindustry")
        output = scrap_sneakerindustry()
        send_to_discord(output, sneaker_industry_token, sneaker_indutry_token_flt)
        print(output)
        print("Scraping sizzer")
        output = scrap_sizzer()
        send_to_discord(output, sizzer_token, sizzer_flt)
        print(output)
        print("Scraping distance")
        output = scrap_distance()
        send_to_discord(output, distance_token, distance_flt)
        print(output)
        print("Scraping uman")
        output = scrap_uman()
        send_to_discord(output, u_man_token, uman_token_flt)
        print(output)
        print("Scraping buzz")
        output = scrap_buzz()
        send_to_discord(output, buzz_token, buzz_token_flt)
        print(output)
        print("Scraping superstep")
        output = scrap_superstep()
        send_to_discord(output, superstep_token, superstep_toke_flt)
        print(output)
        print("Scraping grid")
        output = scrap_grid()
        send_to_discord(output, grid_token, grid_token_flt)
        print(output)
        print("Scraping colective")
        output = scrap_colective()
        send_to_discord(output, colective_token, colective_token_flt)
        #print(output)
        #output = scrap_sportloft()
        #send_to_discord(output, sportloft_token, sportloft_token_flt)
        print(output)
        print("Scraping sportselect")
        output = scrap_sportselect()
        send_to_discord(output, sport_select_token, sport_select_token_flt)
        print(output)
        print("Scraping segos")
        output = scrap_segos()
        send_to_discord(output, segos_token, segos_token_flt)
        print(output)
        print("Scraping dunkshop")
        output = scrap_dunkshop()
        send_to_discord(output, dunk_token, dunk_token_flt)
        print(output)
        print("Scraping bstn")
        output = scrap_bstn()
        send_to_discord(output, bstn_token, bstn_token_flt)
        print(output)
        print("Scraping vitkac")
        output = scrap_vitkac()
        send_to_discord(output, vitak_token, vitkac_token_flt)
        print(output)
        print("Scraping impact")
        output = scrap_impact()
        send_to_discord(output, impact_token, impact_token_flt)
        print(output)
        print("Scraping horn")
        output = scrap_horn()
        send_to_discord(output, horn_token, horn_token_flt)
        print(output)
        print("Scraping queensG")
        output = scrap_queensG()
        send_to_discord(output, queensG_token, queenG_token_flt)
        print(output)
        print("Scraping queenscz")
        output = scrap_queenscz()
        send_to_discord(output, queenscz_token, queencz_token_flt)
        print(output)
        print("Scraping noss")
        output = scrap_noss()
        send_to_discord(output, noss_token, noss_toke_flt)
        print(output)
        print("Scraping basket")
        output = scrap_basket()
        send_to_discord(output, basket_token, basket_token_flt)
        print(output)
        print("Scraping streets")
        output = scrap_streets()
        send_to_discord(output, streets_token, streets_token_flt)
        print(output)
        print("Scraping sneak")
        output = scrap_sneak()
        send_to_discord(output, sneak_token, sneak_token_flt)
        print(output)
        print("Scraping shoe")
        output = scrap_shoe()
        send_to_discord(output, shoe_token, shoe_token_flt)
        print(output)
        print("Scraping slamdunk")
        output = scrap_slamdunk()
        send_to_discord(output, slam_token, slam_token_flt)
        print(output)
        print("Scraping shelta")
        output = scrap_shelta()
        send_to_discord(output, shelta_token, shelta_token_flt)
        print(output)
        time.sleep(100)
            



'''
    times = 0
    while True:
        

        output = scrap_bodosport()
        send_to_discord(output, bodo_token, bodo_token_flt)

        output = scrap_tike()
        send_to_discord(output, tike_token, tike_token_flt)

        output = scrap_rap_city()
        send_to_discord(output, rap_city_token, rapcity_token_flt)

        output = scrap_sneakerindustry()
        send_to_discord(output, sneaker_industry_token, sneaker_indutry_token_flt)

        output = scrap_sizzer()
        send_to_discord(output, sizzer_token, sizzer_flt)

        output = scrap_distance()
        send_to_discord(output, distance_token, distance_flt)

        output = scrap_uman()
        send_to_discord(output, u_man_token, uman_token_flt)

        output = scrap_buzz()
        send_to_discord(output, buzz_token, buzz_token_flt)

        output = scrap_superstep()
        send_to_discord(output, superstep_token, superstep_toke_flt)

        output = scrap_grid()
        send_to_discord(output, grid_token, grid_token_flt)

        output = scrap_colective()
        send_to_discord(output, colective_token, colective_token_flt)

        output = scrap_sportselect()
        send_to_discord(output, sport_select_token, sport_select_token_flt)

        output = scrap_segos()
        send_to_discord(output, segos_token, segos_token_flt)

        output = scrap_dunkshop()
        send_to_discord(output, dunk_token, dunk_token_flt)

        output = scrap_bstn()
        send_to_discord(output, bstn_token, bstn_token_flt)

        output = scrap_vitkac()
        send_to_discord(output, vitak_token, vitkac_token_flt)

        output = scrap_impact()
        send_to_discord(output, impact_token, impact_token_flt)

        output = scrap_horn()
        send_to_discord(output, horn_token, horn_token_flt)

        output = scrap_queensG()
        send_to_discord(output, queensG_token, queenG_token_flt)

        output = scrap_queenscz()
        send_to_discord(output, queenscz_token, queencz_token_flt)

        output = scrap_noss()
        send_to_discord(scrap_noss(), noss_token, noss_toke_flt)

        output = scrap_basket()
        send_to_discord(output, basket_token, basket_token_flt)

        output = scrap_streets()
        send_to_discord(output, streets_token, streets_token_flt)

        output = scrap_sneak()
        send_to_discord(output, sneak_token, sneak_token_flt)

        output = scrap_shoe()
        send_to_discord(output, shoe_token, shoe_token_flt)

        output = scrap_slamdunk()
        send_to_discord(output, slam_token, slam_token_flt)

        output = scrap_shelta()
        send_to_discord(output, shelta_token, shelta_token_flt)
        
        times += 1
        print("Still working... times -> ", str(times*60))
        time.sleep(3600)
    '''
