import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)
        sort = sorted(json_data, key= lambda x: x["length"])
    return sort  # TODO отсортировать список словарей


if __name__ == "__main__":
    data = task()
    print(json.dumps(data, indent=4))

    # TODO дополнительно записать отсортированный список в JSON файл
