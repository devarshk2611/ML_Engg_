"""
argparse_example.py
Reusable CLI template: python argparse_example.py --name Alice --times 3
"""

import argparse

def greet(name, times):
    for _ in range(times):
        print(f"Hello, {name}!")

def parse_args():
    p = argparse.ArgumentParser(description="Greet someone multiple times.")
    p.add_argument("--name", required=True, help="Name to greet")
    p.add_argument("--times", type=int, default=1, help="How many times")
    return p.parse_args()

if __name__ == "__main__":
    args = parse_args()
    greet(args.name, args.times)
