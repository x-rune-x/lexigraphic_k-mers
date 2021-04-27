import itertools


def organise_strings(symbol_list, n):
    string_list = []
    # Want to get the Cartesian product, basically permutations including repetitions.
    for product in itertools.product(symbol_list, repeat=n):
        k_mer = ''
        for char in product:
            k_mer += char
        string_list.append(k_mer)
    return string_list


# My own recursive function that can be used instead of itertools.product. Arguments are: the symbols to be arranged
# into strings, the desired length of the strings, the current length the string (start at 0 when calling the function),
# the current k_mer that is being built up and the list that k_mer strings will be stored in when the reach the required
# length.
def self_cartesion(symbol_list, n, length, k_mer, string_list):
    if length == n:
        string_list.append(k_mer)
    else:
        for i in range(len(symbol_list)):
            self_cartesion(symbol_list, n, length + 1, k_mer + symbol_list[i], string_list)

    return string_list


def process_file(input_file):
    file = open(input_file, 'r')
    symbols = file.readline().strip().replace(' ', '')
    symbol_list = [symbol for symbol in symbols]
    n = int(file.readline())

    solution = organise_strings(symbol_list, n)

    solution_file = open('solution_file.txt', 'w')
    for k_mer in solution:
        solution_file.write(k_mer + '\n')

    solution_file.close()
    return solution


print(process_file('rosalind_lexf.txt'))
# print(self_cartesion(['a', 'c', 'g', 't'], 2, 0, '', []))
