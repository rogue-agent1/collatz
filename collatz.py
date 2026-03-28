#!/usr/bin/env python3
"""collatz - Collatz conjecture (3n+1) sequence explorer."""
import sys
def sequence(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq
def stats(n):
    seq = sequence(n)
    return {"start": n, "steps": len(seq)-1, "max": max(seq), "sequence": seq}
if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: collatz <number> [--range N] [--top N]"); sys.exit(1)
    if "--range" in sys.argv:
        end = int(sys.argv[sys.argv.index("--range")+1]) if sys.argv.index("--range")+1 < len(sys.argv) else 100
        top = int(sys.argv[sys.argv.index("--top")+1]) if "--top" in sys.argv else 10
        results = [(n, len(sequence(n))-1) for n in range(1, end+1)]
        results.sort(key=lambda x: -x[1])
        print(f"Top {top} longest sequences (1-{end}):")
        for n, steps in results[:top]: print(f"  {n:6d}: {steps} steps")
    else:
        s = stats(int(sys.argv[1]))
        print(f"Start: {s['start']} | Steps: {s['steps']} | Max: {s['max']}")
        if len(s['sequence']) <= 50: print(" → ".join(str(x) for x in s['sequence']))
