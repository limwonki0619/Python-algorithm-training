matrix = []
for i in range(1, 6):
    line = []
    for k in range(1, 6):
        line.append(str(i)+'/'+str(k))
    matrix.append(line)

from pprint import pprint
pprint(matrix, indent=4)

# TODO