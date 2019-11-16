#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shodan

api = shodan.Shodan('<shodanapikeyiniz>')
kelime = input("[ ? ] Aranacak Anahtar Kelimeyi veya Hostu Gir : ")

def kelimeyegoreara():
    try:
            ara = api.search(kelime)
            print('Sonuclar Bulundu : {}'.format(ara['total']))
            print("")
            for sonuc in ara['matches']:
                    print('IP: {}'.format(sonuc['ip_str']))
                    print(sonuc['data'])
                    print("")
    except shodan.APIError as e:
            print('Hata: {}'.format(e))

def hostagoreara():
    host = api.host(kelime)
    print("""
        IP: {}
        Organizasyon: {}
        İşletim Sistemi: {}
    """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

    for item in host['data']:
            print("""
                Port: {}
                Banner: {}

            """.format(item['port'], item['data']))

secim = input("""[ ? ] Anahtar Kelimeye Göre Arama Yapacaksanız 1'i
      Host'a Göre Arama Yapacaksanız 2'yi Seçiniz : """)

if secim == "1":
    kelimeyegoreara()
if secim == "2":
    hostagoreara()