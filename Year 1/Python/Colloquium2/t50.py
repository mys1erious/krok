import numpy as np
import random

tickets = np.arange(100)
winTickets = np.array(random.sample(range(100), 10))
print(winTickets)

N = int(input("Enter ur ticket number: "))

if N in winTickets:
    print("U won")
else:
    print("Not this time")