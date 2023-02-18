from typing import List
from time import time


PATH_OUTPUT = 'output'
PATHNAME = r'input.txt'


def read_input(pathname):
    with open(pathname, 'r') as f:
        input = list(f.readlines())
    return input



def make_elements_int(element):
    """
    To convert the elements in the input to integers
    """
    mod_element = element.replace('\n','')
    if mod_element != '':
        return int(mod_element)
    else:
        return mod_element
    


def solve(input:List):
    edited_input = list(map(make_elements_int, input))

    each_elf_calories = list()
    sum_each_elf_calories = list()

    for element in edited_input:
        if element != '':
            each_elf_calories.append(element)
        else:
            sum_calories = sum(each_elf_calories)
            sum_each_elf_calories.append(sum_calories)
            each_elf_calories = list()

    solution_1 = max(sum_each_elf_calories)
    
    sorted_calories = sorted(sum_each_elf_calories, reverse=True)
    solution_2 = sum(sorted_calories[:3])
    return solution_1, solution_2



def write_output(
                path_output,
                solution_1,
                solution_2,
                ):
    file = file = path_output + fr'/solutions.txt'
    with open(file, 'w') as f:
        f.write('==============================================================================\n\n')
        f.write('The solution, Section 1:\n')
        f.write('\n')
        f.write(f'--> {solution_1}')
        f.write('\n\n')
        f.write('The solution, Section 2:\n')
        f.write('\n')
        f.write(f'--> {solution_2}')
    pass


def main():
    
    start= time()
    INPUT = read_input(PATHNAME)
    SOLUTION_1, SOLUTION_2 = solve(INPUT)
    print(f'Maximum Calories --> {SOLUTION_1}')
    print(f'Maximum of Top 3 Calories --> {SOLUTION_2}')
    write_output(
                path_output=PATH_OUTPUT,
                solution_1=SOLUTION_1,
                solution_2=SOLUTION_2,
                )
    end = time()
    print(f'Elapsed time was {end - start:.7f}')


if __name__ == '__main__':main()