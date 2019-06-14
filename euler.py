import sys

def get_problem(problem_num):
    problem_file = "resources/problems2.txt"

    with open(problem_file) as file:
        for line in file:
            if "Problem {}".format(problem_num) in line:
                print(line[:-1])

def usage():
    return "Usage: > euler.py <eulerProblem>"

def main():
    if len(sys.argv) == 2 and str.isdigit(sys.argv[1]):
        problem = get_problem(int(sys.argv[1]))
        if problem:
            pass
    else:
        print(usage())


if __name__ == "__main__":
    main()
