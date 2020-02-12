#!/usr/bin/env python3

import sys
import os

create_project = False

def usage():
    return "Usage: $ ./euler.py [-c] <problem#>"

def get_problem(problem_num):
    problem_file = "resources/problems.txt"

    string = ""
    is_problem = False
    with open(problem_file) as file:
        for line in file:
            if "Problem {}".format(problem_num) in line:
                is_problem = True
            if is_problem:
                if ("Problem {}".format(problem_num + 1)) in line:
                    return string
                string += line
    return string

def parse_cmd():
    global create_project
    argv = sys.argv[:]

    if len(argv) == 3 and argv[1] == '-c':
        create_project = True
        argv = argv[1:]

    if len(argv) == 2 and str.isdigit(argv[1]):
        return get_problem(int(argv[1])), int(argv[1])

    return False, 0

def create(problem, problem_num):
    pstring = f"{problem_num:03d}"
    path = os.getcwd() + '/' + pstring

    # Create the directory
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

        # If successfull, create the readme as well:
        with open(path + '/README.md', 'w+') as f:
            f.write(problem)

        # And create a default python file
        with open(path + f"/p{pstring}.py", 'w+') as f:
            f.write(f'''#!/usr/bin/env python3

# Solution to Project Euler problem {problem_num}

def solve():
    pass

if __name__ == "__main__":
    print(solve())
            ''')

def main():
    problem, problem_num = parse_cmd()

    if problem:
        problem = (problem.strip() + '\n')
        print('\n' + problem)

        if create_project:
            create(problem, problem_num)
    else:
        print(usage())


main()
