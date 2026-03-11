#!/usr/bin/env python3
"""Collatz conjecture — explore hailstone sequences."""
import sys
def collatz(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq
if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 27
    seq = collatz(n)
    print(f"Collatz({n}): {len(seq)} steps, max={max(seq)}")
    if len(seq) <= 50: print(f"Sequence: {seq}")
    else: print(f"Start: {seq[:10]}... End: ...{seq[-5:]}")
    # Find longest sequence in range
    if "--range" in sys.argv:
        hi = int(sys.argv[sys.argv.index("--range")+1]) if "--range" in sys.argv else 1000
        best = max(range(1, hi+1), key=lambda x: len(collatz(x)))
        print(f"\nLongest in 1..{hi}: {best} ({len(collatz(best))} steps)")
