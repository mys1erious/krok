'''
Здравствуйте, в условии задания сказано, что за реализацию программно будет автомат за курс,
    отпишите пожалуйста в комментариях к оцениванию достаточно ли этой работы для получения автомата?
'''

import numpy as np
import random as rnd
import math


class Individual:
    A = None

    def __init__(self):
        self.gene_values = np.empty(self.A.shape[0], 'int32')
        self.gene_names = np.empty(self.A.shape[0], 'int32')

    def create_random_individual_from_distance_matrix(self):
        ind_len = self.A.shape[0]
        randomized_route = np.random.choice(ind_len, ind_len, replace=False)

        for i in range(ind_len - 1):
            self[i] = (randomized_route[i], randomized_route[i+1])
        self[-1] = (randomized_route[-1], randomized_route[0])

    def create_single_distance(self, val1, val2, by_index=False):
        if by_index:
            return self.A[self.get_name(val1), self.get_name(val2)]
        return self.A[val1, val2]

    def sum(self):
        return self.gene_values.sum()

    def mutate(self, index1, index2):
        self.gene_names[index1], self.gene_names[index2] = self.gene_names[index2], self.gene_names[index1]

        index2_next = index2 + 1
        if index2 == len(self)-1:
            index2_next = 0

        self.gene_values[index2] = self.create_single_distance(index2, index2_next, by_index=True)
        self.gene_values[index2 - 1] = self.create_single_distance(index2 - 1, index2, by_index=True)

        self.gene_values[index1] = self.create_single_distance(index1, index1 + 1, by_index=True)
        self.gene_values[index1 - 1] = self.create_single_distance(index1 - 1, index1, by_index=True)

    def value_index(self, value):
        return np.where(self.gene_values == value)

    def name_index(self, value):
        return np.where(self.gene_names == value)

    def get_value(self, item):
        if isinstance(item, (int, np.integer)):
            return self.gene_values[item]

        elif isinstance(item, slice):
            start, stop, step = item.indices(len(self))
            values = np.array([self.get_value(i) for i in range(start, stop, step)])
            return values

    def copy(self, to_copy):
        ind = Individual()
        ind.gene_names = to_copy.gene_names.copy()
        ind.gene_values = to_copy.gene_values.copy()
        return ind

    def get_name(self, item):
        if isinstance(item, (int, np.integer)):
            return self.gene_names[item]

        elif isinstance(item, slice):
            start, stop, step = item.indices(len(self))
            names = np.array([self.get_name(i) for i in range(start, stop, step)])
            return names

    def __setitem__(self, key, value):
        index1 = value[0]
        index2 = value[1]

        self.gene_names[key] = index1
        self.gene_values[key] = self.create_single_distance(index1, index2)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.get_name(item), self.get_value(item)

        elif isinstance(item, slice):
            start, stop, step = item.indices(len(self))

            names = np.array([self.get_name(i) for i in range(start, stop, step)])
            values = np.array([self.get_value(i) for i in range(start, stop, step)])

            return names, values

    def __len__(self):
        return self.gene_names.shape[0]

    def __repr__(self):
        if hasattr(self, 'gene_names') and hasattr(self, 'gene_values'):
            names = f"[{'{:>4}' * len(self)}]"
            names = names.format(*[f'A{i}' for i in self.gene_names])

            values = f"[{'{:>4}' * len(self)}]"
            values = values.format(*self.gene_values)

            return f"{names}\n{values}"


def create_population(num_of_individuals):
    population = list()

    for i in range(num_of_individuals):
        ind = Individual()
        ind.create_random_individual_from_distance_matrix()
        population.append(ind)

    return population


def random_mutations(ind_len):
    rand = np.random.choice(ind_len, 2, replace=False)
    return np.sort(rand)


def create_single_distance_from_matrix(A, val1, val2):
    return A[val1, val2]


def init_M_and_L(A):
    M = []
    L = []

    for i in range(A.shape[0]-1):
        for j in range(1 + i, A.shape[0]):
            M.append((i, j))
            L.append(create_single_distance_from_matrix(A, i, j))

    return M, L


def distance(gene_set1, gene_set2):
    return gene_set1.sum() - gene_set2.sum()


def calc_P(T, distance):
    return 100 * math.exp(-distance/T)


def decrease_T(T, alpha):
    return int(alpha * T)


def simulated_annealing_algorithm(gene_set, T, alpha):
    # Создаем копию прошлого набора
    new_gene_set = gene_set.copy(gene_set)

    # Случайным образом выбираем 2 гена и мутируем их
    genes_to_mutate = random_mutations(len(gene_set))
    new_gene_set.mutate(genes_to_mutate[0], genes_to_mutate[1])

    print(f"Old set =\n"
          f"{gene_set} {gene_set.sum()}\n"
          f"Mutated set =\n"
          f"{new_gene_set} {new_gene_set.sum()}")

    # Считаем сумы двух наборов
    if new_gene_set.sum() < gene_set.sum():
        # Если новый набор меньше чем старый, возвращаем новый набор
        print(f"Set =\n"
              f"{new_gene_set} {new_gene_set.sum()}\n"
              f" T = {T}")
        return new_gene_set, decrease_T(T, alpha)
    else:
        # Если новый набор больше чем старый, считаем разницу между новым и старым набором
        ds = distance(new_gene_set, gene_set)
        print(f"Difference between mutated and old sets = {ds}")
        if ds > 0:
            # Если разница больше 0, считаем P и сравниваем его с случайным числом от 1 до 100,
            #   если P больше случайного числа, возвращаем новый набор
            P = calc_P(T, ds)
            boundary = rnd.randint(1, 100)
            print(f"P = {P:.2f}; Boundary = {boundary}")
            if P > boundary:
                print(f"Set =\n"
                      f"{new_gene_set} {new_gene_set.sum()}\n"
                      f" T = {T}")
                return new_gene_set, decrease_T(T, alpha)

        # Если разница меньше 0 или P меньше случайного числа, возвращаем старый набор
        print(f"Set =\n"
              f"{gene_set} {gene_set.sum()}\n"
              f" T = {T}")
        return gene_set, decrease_T(T, alpha)


def main():

    # Задание : Вирішити задачу комівояжера із застосуванням алгоритму відпалу
    # PS : Использую пример с генами, тк половина кода была взята из 4 лабы и разницы особо нету, что брать за пример

    # Task matrix
    A = np.array([
        [0, 9, 117, 126, 87, 128],
        [9, 0, 38, 127, 125, 119],
        [117, 38, 0, 137, 68, 69],
        [126, 127, 137, 0, 89, 140],
        [87, 125, 68, 89, 0, 148],
        [128, 119, 69, 140, 148, 0],
    ])

    # # Example matrix
    # A = np.array([
    #     [0, 310, 250, 230, 175, 230],
    #     [310, 0, 400, 350, 300, 180],
    #     [250, 400, 0, 250, 200, 198],
    #     [230, 350, 250, 0, 250, 340],
    #     [175, 300, 200, 250, 0, 450],
    #     [230, 180, 198, 340, 450, 0]
    # ])

    Individual.A = A

    # Количество ген
    K = A.shape[0]

    # Создаем M, L
    M, L = init_M_and_L(A)
    print("M and L: ")
    for i in range(len(M)):
        print(f"m={M[i]} l={L[i]}")

    # Создаем случайную комбинацию генов
    gene_set = create_population(1)[0]
    initial_gene_set = gene_set.copy(gene_set)
    print("Arbitrary combination: ")
    print(f"{gene_set} {gene_set.sum()}")

    # Выбираем температуру T и параметр alpha
    T = 500
    alpha = 0.8

    # Используем алгоритм
    print(f"\nSimulated Annealing Algorithm:")

    iters = 0
    while T > 1:
        print(f"{'-' * 100}")
        gene_set, T = simulated_annealing_algorithm(gene_set, T, alpha)
        print(f"{'-' * 100}\n")
        iters += 1

    print(f"Initial set distance = {initial_gene_set.sum()}\n"
          f"Final set distance = {gene_set.sum()}\n"
          f"Iterations taken = {iters}")


if __name__ == "__main__":
    main()

