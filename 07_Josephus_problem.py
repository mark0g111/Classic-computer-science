n, k = int(input()), int(input())
ps, cur_idx = [x for x in range(1, n + 1)], 0
while len(ps) > 1:
    cur_idx = (cur_idx + k - 1) % len(ps)
    del ps[cur_idx]

print(ps[0])