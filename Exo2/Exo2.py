data = [[int(y) for y in x.split(' ')] for x in open('C:\\Users\\AbdelBadi\\Desktop\\Avent_Calendar\\Avent_Calendar\\Exo2\\2.txt').read().split('\n')]

def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    return set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}

safe_count = sum([is_safe(row) for row in data])
print(safe_count)