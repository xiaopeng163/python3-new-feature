import time

a = [1]*100000000

d = dict(zip(a, a))

t = time.time()
for k, v in d.items():
    pass
print(time.time() - t)