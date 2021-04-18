ENG_TO_RUS = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'дестять',
    'zero': 'ноль',
}


def num_translate_avd(number):
    to_capitalize = number and ('A' <= number[0] <= 'Z')
    result = ENG_TO_RUS.get(number.lower())
    return result.capitalize() if (result and to_capitalize) else result
