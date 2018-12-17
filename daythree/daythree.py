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
                line = line.strip()
                coord = line[line.index("@ ") + 2: line.index(":")]
                size = line[line.index(": ") + 2:len(line)]
                wh = (int(size[:size.index("x")]), int(size[size.index("x") + 1:]))
                xy = (int(coord[coord.index(",") + 1:]) + 1, int(coord[:coord.index(",")]) + 1)
                coord_set_set = (xy, wh)
                fd[line[line.index("#") + 1:line.index("@") - 1]] = coord_set_set
            hits: int = calculate_coverage(fd)
            return hits


def calculate_coverage(fd: dict) -> int:
    """
    Method to calculate the coverage of a single entry.

    :param fd: dictionary containing a reference to the ID with the associated coord and size.
    :return: tuple containing the (Coordinate, List<Int> of covered coordinates).
    """
    hits = defaultdict(list)
    dups = defaultdict(list)
    miss = defaultdict(list)
    for key, value in fd.items():
        for x in range(value[0][0], value[0][0] + value[1][0]):
            for y in range(value[0][1], value[0][1] + value[1][1]):
                if (x, y) in hits:
                    dups[(x, y)] += hits[(x, y)] + [key]

                if key in dups.values():
                    miss[key] = []
                else:
                    miss[key] += [key]

                hits[(x, y)] += [key]

    return len(dups)


if __name__ == "__main__":
    print(get_result("daythreeinput.txt"))
