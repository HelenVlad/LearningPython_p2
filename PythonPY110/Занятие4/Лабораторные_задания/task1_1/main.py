import json
import re

BOOKS_FILE = "books.md"
# TODO записать ругулярное выражения для поиска книги
BOOK_REGEX = r"(?P<position>(?<=#### )\d{2})\. \[" \
             r"(?P<book>(?<=\[).*?(?=\]))\]\(" \
             r"(?P<book_url>(?<=\()https:\/\/amzn\.to\/.*?(?=\)))\) by " \
             r"(?P<author>(?<=by ).*?(?= \()) \(" \
             r"(?P<recommended>(?<=\()[\d\.]+?%) recommended\)[\s\S]+?\(" \
             r"(?P<cover_url>(?<=\()https:\/\/www.daolf\.com\/.*?(?=\)))\)[\s\S]+?\"" \
             r"(?P<description>(?<=\")[^\[\]\\]*?(?=\"))\""


def task():
    book_pattern = re.compile(BOOK_REGEX,
                              re.DOTALL)
# флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE) as f:
        # for book in book_pattern.finditer(f.read()):
        #     print(json.dumps(book.groupdict(), indent=4))

        book_dict = sorted(map(lambda x: x.groupdict(), book_pattern.finditer(f.read())),
                           key=lambda x: float((x["recommended"]).strip("%")), reverse=True)
# так как в задании требовалось отсортировать по убыванию популярности,  в функции sorted использовался reverse=True
        print(json.dumps(book_dict, indent=4))


if __name__ == '__main__':
    task()