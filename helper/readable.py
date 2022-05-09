WORDS = [
    # Persian
    {'fa': {'originName': 'از مبدا',
            'destinationName': 'به مقصد',
            'trainNumber': 'شماره قطار',
            'departureDateTime': 'زمان حرکت',
            'arrivalDateTime': 'زمان رسیدن',
            'cost': 'هزینه(با تخفیف)',
            'fullPrice': 'قیمت کل',
            'seat': 'صندلی خالی', }
     },

    # English
    {'en': {}
     }
]


def translate(word: str, lang="fa") -> str:
    """
    Translate a word. The word must be translated in the dictionary (WORDS).
    """
    return [element for element in WORDS if list(element.keys())[0] == lang][0][lang][word]
