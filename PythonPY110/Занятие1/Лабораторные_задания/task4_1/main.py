from itertools import count


def task():
    counter = count(100, 10)
    cou = 0
    while cou < 10:
        cou += 1
        yield next(counter)

    # TODO распечатать с столбик первые 10 чисел бесконечного итератора


if __name__ == "__main__":

    for num in task():
        print(num)


