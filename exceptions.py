jina = "Python Programming"

for i in jina:
    if i != 0:
        print(i)

x = ['Python', 'exceptions', 'try and except']
try:
    for i in range(5):
        print(f'The index and elements from list is {i, x[i]}')
except IndexError:
    print('Index out of range')
    