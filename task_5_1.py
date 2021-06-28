def odd_nums(count):
    for i in range(0, count + 1):
        if i % 2 != 0:
            yield i


def main(argv):
    program, *count = argv
    if count:
        for item in count:
            print(*odd_nums(int(item)))


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))

    # odd_to_5 = odd_nums(5)
    # print(next(odd_to_5))