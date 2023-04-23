def task() -> int:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]
    mml = max(map(len, list_words))
    return mml # TODO найти длину самого длинного слова


if __name__ == "__main__":
    print(task())
