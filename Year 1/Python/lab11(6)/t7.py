import os


path = 'D:/+brain/KROK/Programming/Labs/Year1/lab11(6)/NewFolder'
filename = 'profile.txt'

try:
    os.mkdir(path)
except FileExistsError:
    pass


prof_inf = 'Name:\nAddress:\nNumber:\nEmail:\nOverview:'

if not os.path.isfile(path + '/' + filename):
    with open(os.path.join(path, filename), 'w+') as f:
        f.write(prof_inf)
        print(f.read())
else:
    with open(path + '/' + filename, 'r') as f:
        print(f.read())