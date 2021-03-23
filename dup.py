#!/bin/python3
import sys
def main()
    file_name = sys.argv[1]

    with open(file_name, 'r') as f:
        l_file_name = f.readlines()

    r_dup = list(set(l_file_name))

    new_file = "non-dup-file.txt"
    for srv in r_dup:
        with open(new_file, 'a') as f:
            f.write(srv)
    print('file created successfully after removing duplicates ' + new_file)


if __name__ == '__main__':
    main()