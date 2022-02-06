hour = 0
div = 2
ameba = 1

while hour in range(0,24):
    hour += 3
    ameba = ameba*div
    print(f"In {hour} hours will e {ameba} ameba")