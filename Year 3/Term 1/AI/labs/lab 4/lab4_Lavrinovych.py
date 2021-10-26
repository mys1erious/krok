from itertools import groupby

import random as rnd
import numpy as np


class Individual:
    A = None

    def __init__(self, gene_names=None, gene_values=None):

        if gene_names is not None and gene_values is not None and len(gene_names) == len(gene_values):
            if isinstance(gene_names, list) and isinstance(gene_values, list):
                self.gene_names = np.array(gene_names)
                self.gene_values = np.array(gene_values)
            elif isinstance(gene_names, np.ndarray) and isinstance(gene_values, np.ndarray):
                self.gene_names = gene_names
                self.gene_values = gene_values
        else:
            self.gene_values = np.empty(self.A.shape[0], 'int32')
            self.gene_names = np.empty(self.A.shape[0], 'int32')
            self.create_random_individual_from_distance_matrix()

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

    def get_name(self, item):
        if isinstance(item, (int, np.integer)):
            return self.gene_names[item]

        elif isinstance(item, slice):
            start, stop, step = item.indices(len(self))
            names = np.array([self.get_name(i) for i in range(start, stop, step)])
            return names

    def append(self, index):
        self.gene_values[-1] = self.create_single_distance(self.gene_names[-1], index)

        self.gene_names = np.append(self.gene_names, index)
        self.gene_values = np.append(self.gene_values,
                                     self.create_single_distance(self.gene_names[-1], self.gene_names[0]))

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


def create_population(A, num_of_individuals):
    population = list()

    for i in range(num_of_individuals):
        population.append(Individual())

    return population


def random_parents(population, num_of_individuals):
    parents = np.random.choice(num_of_individuals, 2, replace=False)
    return [population[parents[0]], population[parents[1]]]


def random_mutations(ind_len):
    rand = np.random.choice(ind_len, 2, replace=False)
    return np.sort(rand)


def random_break_point(individual_len):
    return rnd.randint(1, individual_len - 2)


def crossover(parents, break_point, A):
    parents_len = len(parents)
    ind_len = len(parents[0].gene_values)

    breed = []
    to_crossover = []

    for i in range(parents_len):
        cur_child = parents[i][0:break_point]
        cur_to_crossover = parents[parents_len - 1 - i][break_point:]

        breed.append(Individual(cur_child[0], cur_child[1]))
        to_crossover.append(Individual(cur_to_crossover[0], cur_to_crossover[1]))

    for i in range(parents_len):
        cur_individual = breed[i]

        for j in range(ind_len - break_point):
            new_genes = to_crossover[i]
            if new_genes.gene_names[j] not in cur_individual.gene_names:
                cur_individual.append(new_genes.gene_names[j])
            if len(cur_individual) == ind_len:
                break

        for j in range(ind_len - break_point):
            new_genes = to_crossover[parents_len - 1 - i]
            if new_genes.gene_names[j] not in cur_individual.gene_names:
                cur_individual.append(new_genes.gene_names[j])
            if len(cur_individual) == ind_len:
                break

    return breed


def selection(population, num_to_remove):
    cur_sums = []
    for ind in population:
        cur_sums.append(ind.sum())
    max_sums = sorted(cur_sums, reverse=True)[:num_to_remove]

    i = 0
    remove_count = 0
    while remove_count < num_to_remove:
        for cur_sum in max_sums:
            if population[i].sum() == cur_sum:
                del population[i]
                i -= 1
                remove_count += 1
            if remove_count == num_to_remove:
                break
        i += 1

    return population


def average_of_population(array):
    tmp_sums = list()
    for ind in array:
        tmp_sums.append(ind.sum())

    return sum(tmp_sums) // len(tmp_sums)


# Checks 3 last distances for equality
def verify_distances(array):
    g = groupby(array)
    return next(g, True) and not next(g, False)


def genetic_algorithm(A, population, num_of_individuals):

    # 1. Случайным образом выбираем 2 родителя
    parents = random_parents(population, num_of_individuals)
    print("\nParents: ")
    for parent in parents:
        print(f"{parent}")

    # 2. Генерируем точку разрыва
    break_point = random_break_point(A.shape[0])
    print(f"\nBreakpoint: {break_point}")

    # 3. Скрещивание
    breed = crossover(parents, break_point, A)
    print("\nBreed: ")
    for child in breed:
        print(f"{child}")

    # 4. Мутация
    mutation_percent = np.random.randint(0, 100)
    if mutation_percent > 50:
        genes_to_mutate = random_mutations(len(breed[0]))
        print(f"\nGenes to mutate: {genes_to_mutate}")
        for child in breed:
            child.mutate(genes_to_mutate[0], genes_to_mutate[1])
        print("Mutation: ")
        for child in breed:
            print(f"{child}")

    # 5. Добавляем новых нащадков в population
    for child in breed:
        population.append(child)

    # 6. Иммитируем природный отбор, удаляем людей с макс. значением
    num_to_remove = len(breed)
    population = selection(population, num_to_remove)
    print("\nNew Population: ")
    for ind in population:
        print(f"{ind}")

    return population


def main():
    # Задание: Створити приклад вирішення задачі комівояжера використовуючи генетичний алгоритм

    # Изначальная матрица расстояний
    A = np.array([
        [0, 310, 250, 200, 400, 200],
        [310, 0, 500, 350, 600, 180],
        [250, 500, 0, 250, 200, 98],
        [200, 350, 250, 0, 250, 340],
        [400, 600, 200, 250, 0, 450],
        [200, 180, 98, 340, 450, 0]])
    Individual.A = A

    # Случайный образом создаем маршруты(генетические наборы)
    num_of_individuals = 5
    population = create_population(A, num_of_individuals)
    print("Initial Population: ")
    for ind in population:
        print(f"{ind} sum={ind.sum()}")

    distance_averages = [average_of_population(population)]
    print(f"Distance average: {distance_averages[0]}")

    # Используем генетический алгоритм
    max_iterations = 50

    for i in range(1, max_iterations+1):
        print(f"{'-'*100}\n"
              f"Iteration: {i}")

        population = genetic_algorithm(A, population, num_of_individuals)

        distance_averages.append(average_of_population(population))
        print(f"Distance average: {distance_averages[i]}")

        print(f"{'-' * 100}\n")

        if len(distance_averages) > 3 and verify_distances(distance_averages[-3:]):
            print(f"All distances: {distance_averages}")
            print(f"End result: {distance_averages[-1]}, Iterations taken: {len(distance_averages)-1}")
            break


if __name__ == '__main__':
    main()
