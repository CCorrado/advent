from collections import defaultdict


def get_result(file_path):
    try:
        file = open(file_path)
    except FileNotFoundError:
        print("File Not Found: " + str(file_path))
    except IsADirectoryError:
        print("This is a directory: " + str(file_path))
    else:
        with file:
            twos = 0
            threes = 0
            for line in file.readlines():
                wd = defaultdict(int)
                for st in line:
                    wd[st] += 1
                plus_three = False
                plus_two = False
                for val in wd.values():
                    if val == 3:
                        plus_three = True
                    if val == 2:
                        plus_two = True
                    if plus_three and plus_two:
                        break
                if plus_two:
                    twos += 1
                if plus_three:
                    threes += 1

            return twos * threes


if __name__ == "__main__":
    print(get_result("day2input.txt"))
