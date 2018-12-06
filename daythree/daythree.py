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
            fd = defaultdict(tuple)
            for line in file.readlines():
                coord = line[line.index("@ ") + 2: line.index(":")]
                size = line[line.index(": ") + 2:len(line)]
                coord_set = set(coord)
                size_set = set(size)
                fd[line[line.index("#") + 1:line.index("@")]] = (coord_set, size_set)
            print(fd)


if __name__ == "__main__":
    print(get_result("daythreeinput.txt"))
