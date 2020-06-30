colour = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

print(list(i for i in colour if colour.index(i) not in (0, 4, 5)))
