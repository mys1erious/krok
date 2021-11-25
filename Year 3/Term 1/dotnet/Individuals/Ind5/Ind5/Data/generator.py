# triangle
# equilateral triangle;
# rectangle;
# square;
# rhombus;
# circle;
# ellipse;

import random as rnd
import json


def generate_figures_data():
    length = rnd.randint(2, 10)

    data = {}
    data['key'] = 'value'
    json_data = json.dumps(data)
    return json_data, length


def add_data(file_path, data, length):
    with open(file_path, 'w') as f:
        f.write(data)


if __name__ == '__main__':
    file_path = './data.json'
    d, length = generate_figures_data()
    add_data(file_path, d, length)

'''
file_path = './data.txt'
rows_num = 10
salaries, children = generate_salary_and_children(rows_num)

with open(file_path, 'w') as f:
    for i in range(rows_num):
        line = f"Name{i},Surname{i},Position{i},{salaries[i]},{children[i]}\n"

        f.write(line)
'''
