import json


def task():
    filename = "input.json"
    # TODO считать содержимое JSON файла
    with open(filename) as f:
        f_load = json.load(f)
        f_max = max(*f_load, key= lambda x: x["score"])
    return f_max  # TODO найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
