class Stack:
    def __init__(self): self.data = []
    def push(self, c): self.data.append(c)
    def pop(self): return self.data.pop()
    def is_empty(self): return len(self.data) == 0


class Queue:
    def __init__(self): self.data = []
    def enqueue(self, c): self.data.append(c)
    def dequeue(self): return self.data.pop(0)
    def is_empty(self): return len(self.data) == 0


def is_match(a, b):
    return (a == 'A' and b == 'T') or (a == 'T' and b == 'A') or \
           (a == 'C' and b == 'G') or (a == 'G' and b == 'C')


def analyze_dna(dna):
    dna = dna.upper().strip()
    if not dna:
        return {'error': 'Enter a DNA sequence!'}
    for c in dna:
        if c not in 'ATCG':
            return {'error': f"Invalid character '{c}'!"}
    if len(dna) % 2 != 0:
        return {'error': 'Length must be even!'}

    q, s = Queue(), Stack()
    for c in dna:
        q.enqueue(c)
    for _ in range(len(dna) // 2):
        s.push(q.dequeue())

    valid = True
    pairs = []
    while not q.is_empty():
        fq, fs = q.dequeue(), s.pop()
        match = is_match(fs, fq)
        if not match:
            valid = False
        pairs.append({'stack_char': fs, 'queue_char': fq, 'match': match})

    return {
        'error': None, 'sequence': dna, 'valid': valid, 'pairs': pairs,
        'count_a': dna.count('A'), 'count_t': dna.count('T'),
        'count_c': dna.count('C'), 'count_g': dna.count('G'),
        'length': len(dna)
    }
