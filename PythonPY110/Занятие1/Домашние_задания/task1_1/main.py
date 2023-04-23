if __name__ == "__main__":
    def my_enumerate(lst:list):
        my_enu = zip(range(0, len(lst)), lst)
        return my_enu

    # a = [15, 5, 6, 4, 8, 79, 16, 3, 0, 3, 5]
    # for x, y in my_enumerate(a):
    #     print(x, y)
    #####