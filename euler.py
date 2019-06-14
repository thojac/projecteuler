#!/usr/bin/env python

import sys

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

def usage():
    return "Usage: > euler.py <eulerProblem>"

def main():
    if len(sys.argv) == 2 and str.isdigit(sys.argv[1]):
        problem_num = int(sys.argv[1])
        problem = get_problem(problem_num)
        if problem:
            print("\n" + problem.strip())
        else:
            print("Problem number {} not found".format(problem_num))
    else:
        print(usage())


if __name__ == "__main__":
    main()
