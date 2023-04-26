INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():# TODO перезаписать содержимое одного файла в другой
    with open(INPUT_FILE, "r") as inpuut,\
        open(OUTPUT_FILE, "w") as outpuut:
        outpuut.write(''.join(x for x in map(str.upper, inpuut)))


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
