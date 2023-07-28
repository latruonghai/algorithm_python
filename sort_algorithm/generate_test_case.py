import random
from modules.decorator_for_algorithm import sort_algo


@sort_algo
def generate_test_case(num_of_test_case: int, root_folder="test_cases"):
    for i in range(num_of_test_case):
        len_of_arr = 100000
        result = [random.randint(1, len_of_arr) for _ in range(len_of_arr)]
        with open("{}/test_case_sort_algorithm{}.txt".format(root_folder, i+1), "w+") as file:
            file.write(" ".join(map(str, result)))


if __name__ == "__main__":

    generate_test_case(1000)
