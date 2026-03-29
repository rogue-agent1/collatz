#!/usr/bin/env python3
"""collatz - Collatz sequence explorer."""
import sys, argparse, json

def collatz_seq(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq

def main():
    p = argparse.ArgumentParser(description="Collatz explorer")
    p.add_argument("n", type=int)
    p.add_argument("--range", type=int, help="Explore 1..N")
    p.add_argument("--longest", action="store_true")
    args = p.parse_args()
    if args.range:
        results = []
        for i in range(1, args.range + 1):
            seq = collatz_seq(i)
            results.append({"n": i, "steps": len(seq)-1, "max": max(seq)})
        if args.longest:
            results.sort(key=lambda x: x["steps"], reverse=True)
        print(json.dumps({"range": args.range, "results": results[:20]}, indent=2))
    else:
        seq = collatz_seq(args.n)
        print(json.dumps({"n": args.n, "steps": len(seq)-1, "max": max(seq), "sequence": seq}, indent=2))

if __name__ == "__main__": main()
