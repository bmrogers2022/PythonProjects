# recursive program to check amount of possible android box passwords
# given the length of the password and the starting point

def pairs(x, y):
    return [(x, y), (y, x)]

def count_patterns_from(firstPoint, length):

    if length > 9:
        return 0
    elif length == 1:
        return 1
    elif length == 0:
        return 0

    def recursive_combos(firstPoint, length, used):
        if length == 1:
            return 1
        new_valids = {'B': pairs('A', 'C'), 'F': pairs('C', 'I'), 'H': pairs('G', 'I'), 'D':pairs('A', 'G'), 'E': pairs('B', 'H') + pairs('D', 'F') + pairs('A', 'I') + pairs('G', 'C')}
        possibles = {'A': 5, 'B': 7, 'C': 5, 'D': 7, 'E': 8, 'F': 7, 'G': 5, 'H': 7, 'I': 5}
        touching = {'A': 'BDEFH', 'B':'ACDEFGI', 'C': 'BEFDH', 'D': 'ABEHGCI', 'E': 'ABCDFGHI', 'F': 'CBEHIAG', 'G': 'DEHBF', 'H': 'GDAEIFC', 'I': 'EFHDB'}
        for x in used:
            if x in new_valids:
                for y in new_valids[x]:
                    possibles[y[0]] += 1
                    touching[y[0]] += y[1]
        for x in used:
            for l in touching:
                if x in touching[l]:
                    temp = list(touching[l])
                    temp.remove(x)
                    touching[l] = ''.join(temp)
                    possibles[l] -= 1
        total = 0
        for x in touching[firstPoint]:
            paths_along_path = recursive_combos(x, length-1, used + [x])
            total += paths_along_path
        return total

    return recursive_combos(firstPoint, length, [firstPoint])


print(count_patterns_from('E',5))
print(pairs("C", "E"))
