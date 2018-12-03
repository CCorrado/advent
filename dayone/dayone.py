def get_result():
    filepath = "day1input.txt"
    try:
        file = open(filepath)
    except FileNotFoundError:
        print("File Not Found: " + str(filepath))
    except IsADirectoryError:
        print("This is a directory: " + str(filepath))
    else:
        with file:
            result = 0
            for line in file.readlines():
                current = int(line) + result
                result = current
            print(result)


if __name__ == "__main__":
    get_result()
