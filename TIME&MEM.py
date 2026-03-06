import tracemalloc
import time

tracemalloc.start()
start = time.perf_counter()

#start of program
from collections import Counter
l = Counter('рубашка,футболка,футболка,брюки,футболка,сырный соус,рубашка,носки,рубашка'.split(','))
res = {k:l[k] for k in sorted(l)}
mx = len(max(res, key=len))
for k, v in res.items():
    s = sum([ord(i) for i in k if i != ' '])
    print(f'{k:<{mx}}: {s} UC x {v} = {s*v} UC')


#end

current, peak = tracemalloc.get_traced_memory()
end = time.perf_counter()

print(f"Текущая память: {current / 1024 / 1024:.2f} MB")
print(f"Пиковая память: {peak / 1024 / 1024:.2f} MB")
print(f"Время выполнения: {end - start:.6f} секунд")

tracemalloc.stop()
#text for branch new
