def task() -> str:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]
    tada = min(list_words, key=len)
    return tada  # используй ключевую у функции min, по которой она долна определять минимальный элемент


if __name__ == "__main__":
    print(task())
