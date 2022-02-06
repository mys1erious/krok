import numpy as np


def list_of_all_initial_rooms(length, end_room):
    lst = np.random.choice(length, length, replace=False)
    lst = delete_already_used_initial_room(lst, end_room)
    return lst


def random_initial_room(lst):
    return np.random.choice(lst, 1)[0]


def choose_next_room(R, current_room_ind):
    current_room = R[current_room_ind]

    if np.max(current_room) == 100:
        return np.argmax(current_room)
    else:
        next_rooms = np.where(current_room >= 0)
        return np.random.choice(next_rooms[0], 1)[0]


def delete_already_used_initial_room(initial_rooms, room_to_delete):
    return np.delete(initial_rooms, np.where(initial_rooms == room_to_delete))


def update_Q(Q, R, current_room, next_room, gamma):

    max_index = np.where(Q[next_room] == np.max(Q[next_room]))

    if len(max_index) > 1:
        max_index = max_index[1]
    else:
        max_index = max_index[0]

    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size=1))
    else:
        max_index = max_index[0]

    Q[current_room, next_room] = R[current_room, next_room] + gamma * Q[next_room, max_index]


def Q_learning_algorithm(Q, R, gamma, end_room):
    # Все комнаты из которых можно начать
    initial_rooms = list_of_all_initial_rooms(Q.shape[0], end_room)

    while len(initial_rooms) > 0:
        # Повторяем цикл, пока не пройдем все начальные комнаты

        # Случайным образом выбираем первую комнату
        current_room = random_initial_room(initial_rooms)
        initial_rooms = delete_already_used_initial_room(initial_rooms, current_room)
        print(f"Initial room: {current_room}")

        while current_room != end_room:
            # Повторяем цикл пока не дойдем до последней комнаты

            # Выбираем следующую комнату
            next_room = choose_next_room(R, current_room)
            print(f"Next room: {next_room}")

            # Обновляем матрицу
            update_Q(Q, R, current_room, next_room, gamma)

            current_room = next_room

        print(f"Current Q:\n{np.around(Q, decimals=2)}")


def main():
    # Вариант 2

    R = np.array([
            [-1, 0, -1, -1, 0, -1, -1, 0],
            [0, -1, 0, 0, -1, -1, -1, 0],
            [-1, 0, -1, 0, -1, 0, -1, 0],
            [-1, 0, 0, -1, 0, 0, -1, -1],
            [0, -1, -1, 0, -1, -1, -1, -1],
            [-1, -1, 0, 0, -1, -1, 100, -1],
            [-1, -1, -1, -1, -1, 0, -1, -1],
            [0, 0, 0, -1, -1, -1, -1, -1],
        ])

    Q = np.array(np.zeros([8, 8]))

    g = 0.8

    # Комната выхода
    end_room = 6

    # Количество итерацияй
    iters = 10

    # Использум Q-learning algorithm
    for i in range(iters):
        print('-----------------------------------')
        Q_learning_algorithm(Q, R, g, end_room)
        print('-----------------------------------')


    # Задание 2 варианта:
    # Самый быстрый путь с 7комнаты(мыши) до 6комнаты(сыра)
    current_room = 7
    cur_weight = 0
    path = []
    while cur_weight != 100:
        path.append(current_room)
        cur_weight = np.max(Q[current_room])
        current_room = np.argmax(Q[current_room])
    else:
        path.append(end_room)

    print(f"Shortest path from mouse to cheese: {path}")


if __name__ == '__main__':
    main()
