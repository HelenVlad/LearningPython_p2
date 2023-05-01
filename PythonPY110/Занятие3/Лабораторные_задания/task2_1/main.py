import json


def task() -> str:
    dict_numbers = {key: value for key, value in enumerate(map(lambda x: x**2, range(1, 11)), 1)}  # TODO c помощью dict comprehension сформировать словарь
    json_string = json.dumps(dict_numbers, indent=4)
    return json_string  # TODO сеализовать словарь в JSON строку


if __name__ == "__main__":
    print(task())
