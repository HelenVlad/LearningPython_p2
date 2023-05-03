OUTPUT_FILE = "output.txt"


def task():
    # with open(OUTPUT_FILE, "r+") as file: # TODO записать лесенку в файл
    #     text = "".join([line for line in file][::-1])
    #     file.seek(0)
    #     file.write(str(text))

    with open(OUTPUT_FILE, "w") as file:
        for star in range(1, 11):
            file.write(f"{star * '*':>10}\n")

if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
