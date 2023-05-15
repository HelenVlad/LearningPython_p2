def pow_gen(base: int):
    counter = 0
    while True:  # TODO записать функцию-генератор
        exp = base ** counter
        yield exp
        counter += 1

if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
