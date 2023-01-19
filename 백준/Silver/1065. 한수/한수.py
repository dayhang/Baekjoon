n = int(input())
h = 0

for i in range(1, n+1):
    if i <= 99:
        h += 1
    else:
        n_list = list(map(int, str(i)))
        if n_list[0] - n_list[1] == n_list[1] - n_list[2]:
            h += 1
print(h)