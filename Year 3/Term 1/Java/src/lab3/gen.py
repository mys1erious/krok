import random as rnd


def generate_salary_and_children(rows_num):
    salaries = list()
    children = list()

    for i in range(rows_num):
        salaries.append(rnd.randint(500, 3500))
        children.append(rnd.randint(1, 7))

    return sorted(salaries), sorted(children)


file_path = './data.txt'
rows_num = 10
salaries, children = generate_salary_and_children(rows_num)

with open(file_path, 'w') as f:
    for i in range(rows_num):
        line = f"Name{i},Surname{i},Position{i},{salaries[i]},{children[i]}\n"

        f.write(line)
