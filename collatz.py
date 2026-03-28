#!/usr/bin/env python3
"""Collatz conjecture explorer."""
import sys

def sequence(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq

def stats(start, end):
    longest, longest_n, highest, highest_n = 0, 0, 0, 0
    for n in range(start, end + 1):
        seq = sequence(n)
        if len(seq) > longest: longest, longest_n = len(seq), n
        mx = max(seq)
        if mx > highest: highest, highest_n = mx, n
    return {'longest_chain': longest, 'longest_n': longest_n, 'highest_value': highest, 'highest_n': highest_n}

if __name__ == '__main__':
    if len(sys.argv) < 2: print("Usage: collatz.py <number> | collatz.py range <start> <end>"); sys.exit(1)
    if sys.argv[1] == 'range':
        s = stats(int(sys.argv[2]), int(sys.argv[3]))
        for k, v in s.items(): print(f"{k}: {v}")
    else:
        seq = sequence(int(sys.argv[1]))
        print(f"Length: {len(seq)} | Max: {max(seq)}")
        if '--full' in sys.argv: print(' → '.join(map(str, seq)))
        else: print(' → '.join(map(str, seq[:20])) + ('...' if len(seq) > 20 else ''))
