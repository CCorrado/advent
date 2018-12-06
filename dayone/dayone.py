def get_result(file_path):
    try:
        file = open(file_path)
    except FileNotFoundError:
        print("File Not Found: " + str(file_path))
    except IsADirectoryError:
        print("This is a directory: " + str(file_path))
    else:
        with file:
            adjustments = list()
            for _, line in enumerate(file.readlines()):
                adjustments.append(int(line))

            freqs = set()
            freqs.add(0)
            current = 0
            while True:
                for adjustment in adjustments:
                    current += adjustment
                    if current in freqs:
                        return current
                    freqs.add(current)


if __name__ == "__main__":
    print(get_result("day1input.txt"))
