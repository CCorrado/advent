def get_result(file_path):
    try:
        file = open(file_path)
    except FileNotFoundError:
        print("File Not Found: " + str(file_path))
    except IsADirectoryError:
        print("This is a directory: " + str(file_path))
    else:
        with file:
            file_lines = set()
            for line in file.readlines():
                file_lines.add(line)

            for st in file_lines:
                dup_list = list(file_lines)
                dup_list.remove(st)

                for s in dup_list:
                    result = get_diff(s.strip(), st.strip())
                    if result is True:
                        print(s, st)
                        return s, st


def get_diff(st1, st2):
    results = list(zip(st1, st2))
    comp_results = 0
    for result in results:
        comp = result[0] == result[1]
        if not comp:
            comp_results += 1
    return comp_results == 1


if __name__ == "__main__":
    print(get_result("day2input.txt"))
