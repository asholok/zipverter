#!/usr/bin/python
# -*- coding: utf-8 -*-

BRAZILIAN_STATE_CODES_REAL = {
    'AC': '01',
    'AL': '02',
    'AP': '03',
    'AM': '04',
    'BA': '05',
    'CE': '06',
    'DF': '07',
    'ES': '08',
    'MS': '11',
    'MA': '13',
    'MT': '14',
    'MG': '15',
    'PA': '16',
    'PB': '17',
    'PR': '18',
    'PI': '20',
    'RJ': '21',
    'RN': '22',
    'RO': '24',
    'RS': '23',
    'RR': '25',
    'SC': '26',
    'SP': '27',
    'SE': '28',
    'GO': '29',
    'PE': '30',
    'TO': '31'
}

BRAZILIAN_STATE_CODES_REVERCE = dict(zip(
                                    BRAZILIAN_STATE_CODES_REAL.values(),
                                    BRAZILIAN_STATE_CODES_REAL.keys()
                                ))

SUITABLE_CITY_NAMES = {
    u'Washington D.C.': u'Washington, D.C.',
    u'New York': u'New York City',
    u'Ciudad de México': u'Mexico City',
    u'Teotihuacán': u'Teotihuac\xe1n de Arista',
    u'Bielsko-Biała': u'Bielsko-Biala'
}
