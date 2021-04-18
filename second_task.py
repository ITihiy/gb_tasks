import pprint


def thesaurus_adv(*args):
    result = dict()
    for arg in args:
        name, surname = arg.split()
        first_name = name[0]
        first_surname = surname[0]
        if first_surname not in result:
            result[first_surname] = dict()
        if first_name not in result[first_surname]:
            result[first_surname][first_name] = []
        result[first_surname][first_name].append(arg)
    return result


if __name__ == '__main__':
    pprint.pprint(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
