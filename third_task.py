import random

NOUNS = ["автомобиль", "лес", "огонь", "город", "дом"]
ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(number=1, unique=False):
    """
    Returns a list of random strings joined from NOUNS, ADVERBS and ADJECTIVES
    :param number: number of jokes returned (default is 1)
    :param unique: if words in jokes can be repeated (default is False)
    :return: list if strings
    """

    # Choose a random function if unique
    random_func = random.choices if unique else random.sample

    # Get a random word from each list
    nouns = random_func(NOUNS, k=number)
    adverbs = random_func(ADVERBS, k=number)
    adjectives = random_func(ADJECTIVES, k=number)
    return [' '.join((nouns[i], adverbs[i], adjectives[i])) for i in range(number)]


if __name__ == '__main__':
    print(get_jokes(3))
