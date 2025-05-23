# sort dictionary in increase/decrease orders
import operator


d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# increase order
incr_d = dict(sorted(d.items(), key = operator.itemgetter(1)))
print(incr_d)

# decrease order
decr_d = dict(sorted(d.items(), key = operator.itemgetter(1), reverse=True)) 
print(decr_d)
