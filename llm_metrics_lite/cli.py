import argparse
from .eval import evaluate_output

def main():
    p=argparse.ArgumentParser()
    p.add_argument("output")
    p.add_argument("--context")
    A=p.parse_args()
    o=open(A.output).read()
    c=open(A.context).read() if A.context else None
    r=evaluate_output(o,c)
    print(r)
