#!/usr/bin/env python3
"""Collatz conjecture — sequences, stopping times, records."""
import sys
def collatz(n):
    seq=[n]
    while n!=1:
        n=n//2 if n%2==0 else 3*n+1; seq.append(n)
    return seq
def stopping_time(n):
    steps=0
    while n!=1: n=n//2 if n%2==0 else 3*n+1; steps+=1
    return steps
def records(limit):
    max_steps=0; max_n=1; records=[]
    for n in range(2,limit+1):
        s=stopping_time(n)
        if s>max_steps: max_steps=s; max_n=n; records.append((n,s))
    return records
def cli():
    n=int(sys.argv[1]) if len(sys.argv)>1 else 27
    if sys.argv[-1]=="--records":
        for num,steps in records(n): print(f"  {num:>8}: {steps} steps")
    else:
        seq=collatz(n)
        print(f"  n={n}: {len(seq)-1} steps, max={max(seq)}")
        if len(seq)<=50: print(f"  {seq}")
        else: print(f"  {seq[:10]} ... {seq[-5:]}")
if __name__=="__main__": cli()
