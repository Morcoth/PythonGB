from heapq import heappush, heappop, heapify
from collections import defaultdict, Counter
 
def encode(symb2freq):
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
 
txt = input("InputText: ")
symb2freq = defaultdict(int)
for ch in txt:
    symb2freq = Counter(txt)
    
huff = encode(symb2freq)
for p in huff:
    print (f'{p[0]} {symb2freq[p[0]]} {p[1]}')
