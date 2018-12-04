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
            result = 0
            freqs = defaultdict(int)

            for index, line in enumerate(file.readlines()):
                operation = 1
                if int(line) < 0:
                    operation = -1

                for oper in range(0, int(line), operation):
                    current = operation + result
                    if current in freqs.values():
                        print(current)
                        return current
                    result = current

                if result in freqs.values():
                    print(result)
                    return result
                else:
                    freqs[index + 1] = result

            print(result)
            return result


if __name__ == "__main__":
    get_result("day1input.txt")
