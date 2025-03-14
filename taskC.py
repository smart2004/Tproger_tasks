# sort dictionary in increase/decrease values
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# increase order
d_keys = list(d.keys())
# print(d_keys)

d_keys.sort()
# print(d_keys)

d_incr = {}
for k in d_keys:
    d_incr[k] = d[k]

print(d_incr)

# decrease order
d_keys.reverse()

d_decr = {}
for r in d_keys:
    d_decr[r] = d[r]

print(d_decr)
