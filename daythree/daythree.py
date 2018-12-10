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
            hits: defaultdict(tuple) = calculate_coverage(fd)
            return len(hits)


def calculate_coverage(fd: dict) -> defaultdict(tuple):
    """
    Method to calculate the coverage of a single entry.

    :param fd: dictionary containing a reference to the ID with the associated coord and size.
    :return: tuple containing the (Coordinate, List<Int> of covered coordinates).
    """
    hits = defaultdict(tuple)
    dups = defaultdict(tuple)
    x_hits = defaultdict(list)
    y_hits = defaultdict(list)
    x_coords = set()
    y_coords = set()
    for key, value in fd.items():
        # x values first
        for x_coord in range(value[0][0], value[0][0] + value[1][0]):
            x_hits[x_coord] += [key]
            x_coords.add(x_coord)
        for y_coord in range(value[0][1], value[0][1] + value[1][1]):
            y_hits[y_coord] += [key]
            y_coords.add(y_coord)

    max_x = max(x_coords)
    max_y = max(y_coords)

    for x in range(0, max_x):
        for y in range(0, max_y):
            if x_hits[x] != [] and y_hits[y] != []:
                for x_hit, y_hit in zip(x_hits[x], y_hits[y]):
                    if x_hit == y_hit:
                        hits[(x, y)] += tuple(x_hit)
    for key, hit in hits.items():
        if len(hit) > 1:
            dups[key] += hit
    return dups


if __name__ == "__main__":
    print(get_result("daythreeinput.txt"))
