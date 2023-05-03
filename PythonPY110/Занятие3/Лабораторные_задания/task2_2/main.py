import json


def task(input_filename: str, output_filename: str) -> None:
    with open(input_filename, "rt") as i_f, \
         open(output_filename, "wt") as o_f:  # TODO записать содержимое в json файл output.json с отступами
        i_f_load = json.load(i_f)
        json.dump(i_f_load, o_f, indent=4)

if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
